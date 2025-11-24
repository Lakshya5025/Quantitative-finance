import yfinance as yf
import os
ticker = "NVDA"
start_date = "2020-01-01"
end_date = "2025-11-24"
curr_dir = os.getcwd()
file_path = os.path.join(curr_dir, f"quant-week3\\day3-4\\{ticker}_historical_data.csv")
data = yf.download(ticker,start = start_date, end = end_date)
data.to_csv(file_path)
print(f"Historical data for {ticker} saved to {ticker}_historical_data.csv")
