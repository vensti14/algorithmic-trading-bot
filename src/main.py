from data_collection import fetch_data
from feature_engineering import add_technical_indicators
from model_training import train_model
from backtesting import backtest_strategy
from trading import place_order

def main():
    # Prompt user for stock symbol and dates
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Fetch and prepare data
    data = fetch_data(symbol, start_date, end_date)
    
    if data.empty:
        print(f"No data found for symbol {symbol}. Please check the symbol and try again.")
        return
    
    data = add_technical_indicators(data)

    # Define features and target
    features = data[['MACD', 'MACD_signal', 'RSI']]
    target = (data['Close'].shift(-1) > data['Close']).astype(int)

    # Train model
    if features.empty or target.empty:
        print("Insufficient data for model training.")
        return
    
    model, accuracy = train_model(features, target)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Backtest strategy
    backtest_strategy(data, model, features)

    # Example trade (uncomment if you want to place a trade)
    # place_order(symbol, 1, 'buy')

if __name__ == "__main__":
    main()
