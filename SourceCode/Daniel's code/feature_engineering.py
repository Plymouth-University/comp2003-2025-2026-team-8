import pandas as pd

def add_features(df):
    df["returns"] = df["Close"].pct_change()
    df["ma_5"] = df["Close"].rolling(5).mean()
    df["ma_20"] = df["Close"].rolling(20).mean()
    df = df.dropna()
    return df

# this file should help with adding features and keep the prediction logic stable
