import pandas as pd
import os

curr_dir = os.getcwd()

file_path = os.path.join(curr_dir, "quant-week3\\day3-4\\NVDA_historical_data.csv")
df = pd.read_csv(
    file_path,
    parse_dates=["Date"],   
    index_col="Date"        
)


# print(df.head())      # First 5 rows
# print(df.tail())      # Last 5 rows
# print(df.shape)       # (number_of_rows, number_of_columns)
# print(df.columns)     # Names of all columns
# print(df.dtypes)      # Data type of each column
# print(df.index)
# print(df.isna().sum())
# df = df.dropna(how="all")


print(df.info())
print(df.describe())


volume = df['Volume']
close_volume = df[["Close", "Volume"]]
single_day = df.loc["2020-01-02"]
date_range = df["2020-01-02" : "2020-02-01"]
one_year = df.loc["2020"]        # all data from 2020
one_month = df.loc["2020-03"]     # March 2020 only
last_close_price = df['Close'].iloc[-1]
first_opening_price = df['Open'].iloc[0]
max_volume = df['Volume'].max()
min_closing_price = df['Close'].min()
when_min_volume_happen = df['Volume'].idxmin()
when_max_price_happen = df["Close"].idxmax()

print(volume)
print(close_volume)
print(single_day)
print(date_range)
print(one_year)
print(one_month)
print(last_close_price)
print(first_opening_price)
print(max_volume)
print(min_closing_price)
print(when_min_volume_happen)
print(when_max_price_happen)
print(df["Volume"].describe())
print(df[df["Close"] > 100])

print(df[df["Volume"] > 300_000_000])
print(df[df["Close"] > df["Open"]])
print(df[(df["High"] - df["Low"]) > 0.5])