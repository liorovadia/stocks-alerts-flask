from flask import Flask, jsonify, request
# import yfinance as yf

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_stock_data():
    return "<h1>Lior's Flask test</h1>"
    # symbol = request.args.get('symbol')
    # if not symbol:
    #     return jsonify({"error": "Stock symbol is required"}), 400

    # try:
    #     stock = yf.Ticker(symbol)
    #     stock_info = stock.history(period="1d")
    #     current_price = stock_info['Close'][0]

    #     return jsonify({
    #         "symbol": symbol,
    #         "price": current_price
    #     })
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
