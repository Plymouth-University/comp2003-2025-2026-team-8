import os
import json
import pandas as pd
import yfinance as yf
import feedparser
from datetime import datetime, timezone
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def run_model():
    print("MODEL STARTED")

    tickers = [
        "AAPL", "MSFT", "TSLA", "GOOGL", "AMZN",
        "BTC-USD", "ETH-USD", "SOL-USD", "ADA-USD", "DOGE-USD"
    ]

    startdate = "2021-01-01"
    buythresh = 0.60
    sellthresh = 0.40
    trainratio = 0.80

    file_path = os.path.join(os.path.dirname(__file__), "marketData.json")

    rssurl = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL,MSFT,TSLA,GOOGL,AMZN&region=US&lang=en-US"

    # Price data
    print("Fetching price data...")

    raw = yf.download(tickers, start=startdate, group_by="ticker", threads=False)

    rows = []

    for tkr in tickers:
        try:
            temp = raw[tkr].reset_index()
            temp["ticker"] = tkr
            temp = temp.rename(columns={"Date": "dt"})
            rows.append(temp[["dt", "ticker", "Close"]])
        except Exception as e:
            print(f"Skipping {tkr}: {e}")

    df = pd.concat(rows, ignore_index=True)
    df["dt"] = pd.to_datetime(df["dt"])
    df = df.sort_values(["ticker", "dt"])

    # Price features
    df["returnday1"] = df.groupby("ticker")["Close"].pct_change(1)
    df["returnday5"] = df.groupby("ticker")["Close"].pct_change(5)

    df["fwdret"] = df.groupby("ticker")["Close"].shift(-1) / df["Close"] - 1
    df["yup"] = (df["fwdret"] > 0).astype(int)

    # Sentiment
    print("Fetching sentiment...")

    analyzer = SentimentIntensityAnalyzer()
    feed = feedparser.parse(rssurl)

    newsrows = []

    for entry in feed.entries:
        title = entry.title.lower()

        dt = datetime.now(timezone.utc).date()
        sent = analyzer.polarity_scores(title)["compound"]

        matched = []

        if "apple" in title or "aapl" in title:
            matched.append("AAPL")
        if "microsoft" in title or "msft" in title:
            matched.append("MSFT")
        if "tesla" in title or "tsla" in title:
            matched.append("TSLA")
        if "google" in title or "alphabet" in title or "googl" in title:
            matched.append("GOOGL")
        if "amazon" in title or "amzn" in title:
            matched.append("AMZN")

        for tkr in matched:
            newsrows.append({
                "dt": dt,
                "ticker": tkr,
                "sentiment": sent
            })

    news = pd.DataFrame(newsrows)

    if news.empty:
        agg = pd.DataFrame(columns=["dt", "ticker", "newscount", "newssent"])
    else:
        agg = news.groupby(["dt", "ticker"], as_index=False).agg(
            newscount=("sentiment", "count"),
            newssent=("sentiment", "mean")
        )

    df["dtdate"] = df["dt"].dt.date

    df = df.merge(agg, left_on=["dtdate", "ticker"], right_on=["dt", "ticker"], how="left")

    df["newscount"] = df["newscount"].fillna(0)
    df["newssent"] = df["newssent"].fillna(0)

    df = df.dropna(subset=["returnday1", "returnday5"])

    # Model
    print("Training model...")

    features = ["returnday1", "returnday5", "newscount", "newssent"]

    X = df[features]
    y = df["yup"]

    split = int(len(df) * trainratio)

    model = LogisticRegression(max_iter=500)
    model.fit(X[:split], y[:split])

    preds = model.predict(X[split:])
    acc = accuracy_score(y[split:], preds)

    print(f"Model accuracy: {acc:.2f}")

    # Predictions
    latest = df.groupby("ticker").tail(1)

    latest["probup"] = model.predict_proba(latest[features])[:, 1]

    def getsignal(p):
        if p >= buythresh:
            return "BUY"
        elif p <= sellthresh:
            return "SELL"
        return "HOLD"

    latest["signal"] = latest["probup"].apply(getsignal)

    # Export
    export = {}

    for tkr in tickers:
        sub = df[df["ticker"] == tkr].tail(15)

        if sub.empty:
            continue

        row = latest[latest["ticker"] == tkr].iloc[0]

        last_price = sub["Close"].iloc[-1]

        if row["signal"] == "BUY":
            predicted = last_price * 1.02
        elif row["signal"] == "SELL":
            predicted = last_price * 0.98
        else:
            predicted = last_price

        export[tkr.replace("-USD", "")] = {
            "labels": sub["dt"].dt.strftime("%b %d").tolist(),
            "historical": sub["Close"].round(2).tolist(),
            "predicted": round(predicted, 2),
            "signal": row["signal"],
            "confidence": round(row["probup"] * 100, 1),
            "sentiment": "Positive" if row["newssent"] > 0 else "Neutral/Negative",
            "accuracy": round(acc, 2)
        }

    with open(file_path, "w") as f:
        json.dump(export, f, indent=2)

    print("Updated marketData.json")

if __name__ == "__main__":
    run_model()
