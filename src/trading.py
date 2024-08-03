import alpaca_trade_api as tradeapi
import logging
import os

import os
print("API Key:", os.getenv('APCA_API_KEY_ID'))
print("API Secret:", os.getenv('APCA_API_SECRET_KEY'))

# Alpaca API credentials
API_KEY = os.getenv('APCA_API_KEY_ID')
API_SECRET = os.getenv('APCA_API_SECRET_KEY')
BASE_URL = 'https://paper-api.alpaca.markets'

if not API_KEY or not API_SECRET:
    raise ValueError("API_KEY and API_SECRET must be set in environment variables")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def place_order(symbol, qty, side, type='market'):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force='gtc'
        )
        logging.info(f"Trade: {side} {qty} of {symbol}")
    except Exception as e:
        logging.error(f"Error placing order: {e}")

# Example usage:
# place_order('AAPL', 1, 'buy')
