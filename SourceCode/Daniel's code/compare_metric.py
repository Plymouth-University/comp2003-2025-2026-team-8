def buy_and_hold(df):
    start_price = df.iloc[0]["Close"]
    end_price = df.iloc[-1]["Close"]
    
    shares = 10000 / start_price
    final_value = shares * end_price
    
    return final_value

# this is the benchmark strategy
