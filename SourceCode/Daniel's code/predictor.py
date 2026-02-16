def predict_signal(df):
    last_row = df.iloc[-1]
    
    if last_row["ma_5"] > last_row["ma_20"]:
        return {"signal": "BUY", "confidence": 0.75}
    elif last_row["ma_5"] < last_row["ma_20"]:
        return {"signal": "SELL", "confidence": 0.70}
    else:
        return {"signal": "HOLD", "confidence": 0.50}

# separates prediction logic from data logic to help with testing
