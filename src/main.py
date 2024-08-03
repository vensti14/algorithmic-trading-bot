from data_collection import fetch_data
from feature_engineering import add_technical_indicators
from model_training import train_model
from backtesting import backtest_strategy
from trading import place_order

# Fetch and prepare data
data = fetch_data('AAPL', '2020-01-01', '2024-01-01')
data = add_technical_indicators(data)

# Define features and target
features = data[['MACD', 'MACD_signal', 'RSI']]
target = (data['Close'].shift(-1) > data['Close']).astype(int)

# Train model
model, accuracy = train_model(features, target)
print(f"Model Accuracy: {accuracy:.2f}")

# Backtest strategy
backtest_strategy(data, model, features)

# Example trade
# place_order('AAPL', 1, 'buy')
