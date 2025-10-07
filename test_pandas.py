# fetch_daily.py
import yfinance as yf
import pandas as pd

symbol = "AAPL"               # single symbol for MVP
df = yf.download(symbol, start="2018-01-01", end="2025-01-01", progress=False)
df = df.rename_axis("timestamp").reset_index()  # timestamp column
df = df[["timestamp", "Open", "High", "Low", "Close", "Volume"]]
df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
df.to_csv("data/AAPL_1d.csv", index=False)
print("Saved data/AAPL_1d.csv", len(df), "rows")
