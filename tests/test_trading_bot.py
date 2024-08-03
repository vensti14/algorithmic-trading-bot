import unittest
from src.data_collection import fetch_data
from src.feature_engineering import add_technical_indicators

class TestTradingBot(unittest.TestCase):
    
    def test_fetch_data(self):
        data = fetch_data('AAPL', '2020-01-01', '2024-01-01')
        self.assertFalse(data.empty)
    
    def test_add_technical_indicators(self):
        data = fetch_data('AAPL', '2020-01-01', '2024-01-01')
        data = add_technical_indicators(data)
        self.assertTrue('MACD' in data.columns)
        self.assertTrue('RSI' in data.columns)

if __name__ == '__main__':
    unittest.main()
