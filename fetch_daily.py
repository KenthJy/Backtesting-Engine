import pandas as pd 
import yfinance as yf
from dataclasses import dataclass

class BarEvent:
    symbol : str
    time : str
    open : float
    high : float
    low: float
    close : float
    close : float
    volume : int

    
df = pd.read_csv('data/AAPL_1d.csv')

print(df.head()) 
print("\nColumns:", df.columns.tolist())