def backtest(df):
    cash = 10000
    position = 0
    
    for i in range(20, len(df)):
        row = df.iloc[i]
        
        if row["ma_5"] > row["ma_20"] and cash > 0:
            position = cash / row["Close"]
            cash = 0
        
        elif row["ma_5"] < row["ma_20"] and position > 0:
            cash = position * row["Close"]
            position = 0
    
    final_value = cash + position * df.iloc[-1]["Close"]
    return final_value

# measures how much money we would have if we followed the AI signal rule through history
