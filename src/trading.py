import alpaca_trade_api as tradeapi
import logging

# Alpaca API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def place_order(symbol, qty, side, type='market'):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force='gtc'
    )
    logging.info(f"Trade: {side} {qty} of {symbol}")

# Example usage:
# place_order('AAPL', 1, 'buy')
