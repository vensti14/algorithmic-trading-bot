import pandas as pd
import matplotlib.pyplot as plt

def backtest_strategy(data, model, features):
    data['Predicted_Signal'] = model.predict(features)
    data['Position'] = data['Predicted_Signal'].shift()
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Position'] * data['Daily_Return']
    data['Portfolio'] = (1 + data['Strategy_Return']).cumprod()
    data['Benchmark'] = (1 + data['Daily_Return']).cumprod()
    
    plt.figure(figsize=(14, 7))
    plt.plot(data['Portfolio'], label='Strategy Portfolio')
    plt.plot(data['Benchmark'], label='Benchmark Portfolio')
    plt.title('Strategy vs Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.show()
