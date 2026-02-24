from flask import Flask, request, jsonify
import yfinance as yf
from feature_engineering import add_features
from predictor import predict_signal

app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():

    symbol = request.args.get("symbol")

    # checks missing symbol
    if not symbol:
        return jsonify({"error": "Symbol parameter is required"}), 400

    try:
        # downloads data directly
        df = yf.download(symbol, start="2023-01-01", end="2024-01-01")

        # check for invalid data or missing data
        if df.empty:
            return jsonify({"error": "Invalid symbol or no data found"}), 404

        # add features
        df = add_features(df)

        # generate prediction
        result = predict_signal(df)

        return jsonify(result), 200

    except Exception:
        # catch unexpected error
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)

# prototype for a flask API endpoint that recieves a stock symbol, processes historical data, generates a BUY, SELL, HOLD prediction, and returns result with bsic error handling
# This is just a blueprint 
