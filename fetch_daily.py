import pandas as pd 
import yfinance as yf
from dataclasses import dataclass

@dataclass
class BarEvent:
    symbol : str
    time : str
    open : float
    high : float
    low: float
    close : float
    close : float
    volume : int

@dataclass
class OrderEvent:
    symbol : str
    order_type : str
    quantity : int
    direction : str
    
@dataclass
class fillEvent:
    symbol: str
    quantity : int
    direction : str
    fill_cost : float
    time : str


df = pd.read_csv('data/AAPL_1d.csv')

print(df.head()) 
print("\nColumns:", df.columns.tolist())