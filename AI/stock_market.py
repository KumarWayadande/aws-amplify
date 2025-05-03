import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch historical stock data
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Simple Moving Average Crossover Strategy
def moving_average_crossover_strategy(data, short_window=40, long_window=100):
    # Compute the moving averages
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Create a signal when the short MA crosses above the long MA
    data['Signal'] = 0.0
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1.0, 0.0)

    # Create the positions by calculating the difference in signals
    data['Position'] = data['Signal'].diff()

    return data

# Plot the stock data with moving averages and buy/sell signals
def plot_stock_data(data, ticker):
    plt.figure(figsize=(10,6))

    plt.plot(data['Close'], label='Close Price', color='black', alpha=0.3)
    plt.plot(data['Short_MA'], label='40-Day Moving Average', color='blue')
    plt.plot(data['Long_MA'], label='100-Day Moving Average', color='red')

    # Plot Buy signals
    plt.plot(data[data['Position'] == 1].index, 
             data['Short_MA'][data['Position'] == 1], 
             '^', markersize=10, color='g', lw=0, label='Buy Signal')

    # Plot Sell signals
    plt.plot(data[data['Position'] == -1].index, 
             data['Short_MA'][data['Position'] == -1], 
             'v', markersize=10, color='r', lw=0, label='Sell Signal')

    plt.title(f'{ticker} - Moving Average Crossover Strategy')
    plt.legend(loc='best')
    plt.show()

# Backtesting the strategy
def backtest(data):
    # Initial balance
    initial_balance = 10000
    balance = initial_balance
    position = 0
    for i in range(1, len(data)):
        # Buy signal
        if data['Position'][i] == 1:
            position = balance / data['Close'][i]
            balance = 0
            print(f"Buying at {data['Close'][i]} on {data.index[i]}")
        
        # Sell signal
        elif data['Position'][i] == -1 and position > 0:
            balance = position * data['Close'][i]
            position = 0
            print(f"Selling at {data['Close'][i]} on {data.index[i]}")

    # Final balance
    final_balance = balance if position == 0 else position * data['Close'][-1]
    print(f"Initial Balance: {initial_balance}")
    print(f"Final Balance: {final_balance}")
    print(f"Profit/Loss: {final_balance - initial_balance}")

# Main function
def run_trading_bot(ticker, start_date, end_date):
    # Step 1: Fetch historical data
    data = fetch_stock_data(ticker, start_date, end_date)

    # Step 2: Apply Moving Average Crossover Strategy
    data = moving_average_crossover_strategy(data)

    # Step 3: Plot the stock data with signals
    plot_stock_data(data, ticker)

    # Step 4: Backtest the strategy
    backtest(data)

# Run the trading bot with a sample stock ticker (e.g., 'AAPL')
if __name__ == "__main__":
    run_trading_bot('AAPL', '2020-01-01', '2023-01-01')
