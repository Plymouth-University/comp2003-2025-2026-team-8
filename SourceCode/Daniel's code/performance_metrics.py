def calculate_performance(initial_capital, final_value, trade_results=None):

    # total profit or loss
    total_return = final_value - initial_capital

    # percentage return
    percent_return = (total_return / initial_capital) * 100

    # optional win rate calculation
    win_rate = None
    if trade_results:
        wins = sum(1 for trade in trade_results if trade > 0)
        win_rate = (wins / len(trade_results)) * 100

    return {
        "initial_capital": initial_capital,
        "final_value": final_value,
        "total_return": total_return,
        "percent_return": percent_return,
        "win_rate": win_rate
    }

# this file calculates basic performance metrics for evaluating trding strategy results
