import pandas as pd
import matplotlib.pyplot as plt

def backtest_strategy(data, model, features):
    # Predict signals
    data = data.copy()  # Ensure you work on a copy to avoid SettingWithCopyWarning
    data['Predicted_Signal'] = model.predict(features)
    
    # Create trading signals
    data['Position'] = data['Predicted_Signal'].shift()
    
    # Calculate daily returns and strategy returns
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Position'] * data['Daily_Return']
    
    # Calculate cumulative returns
    data['Portfolio'] = (1 + data['Strategy_Return']).cumprod()
    data['Benchmark'] = (1 + data['Daily_Return']).cumprod()

    # Plot results
    plt.figure(figsize=(14, 7))
    plt.plot(data['Portfolio'], label='Strategy Portfolio')
    plt.plot(data['Benchmark'], label='Benchmark Portfolio')
    plt.title('Strategy vs Benchmark Performance')
    plt.legend()
    plt.show()
