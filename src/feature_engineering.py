import pandas as pd
from ta.trend import MACD
from ta.momentum import RSIIndicator

def add_technical_indicators(data):
    data['MACD'] = MACD(data['Close']).macd()
    data['MACD_signal'] = MACD(data['Close']).macd_signal()
    data['RSI'] = RSIIndicator(data['Close']).rsi()
    return data.dropna()
s