from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf
import requests
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# CORS(app, origins=["http://localhost:3000"]) # allow requests only from localhost:3000

@app.route('/data')
def fetch_data():
    # Use the `requests` library to get data from an API
    response = requests.get("https://api.example.com/data")
    data = response.json()
    
    # Use `pandas` to work with the data
    df = pd.DataFrame(data)
    summary = df.describe().to_dict()  # Simple data summary
    
    return jsonify(summary)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Lior's Flask test</h1>"

@app.route('/stock', methods=['GET'])  
def get_stock_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(period="1d")
        current_price = stock_info['Close'][0]

        return jsonify({
            "symbol": symbol,
            "price": current_price
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
