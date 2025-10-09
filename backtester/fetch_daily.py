import pandas as pd 
import yfinance as yf
from events import BarEvent, OrderEvent, FillEvent
from queue import Queue


event_q = Queue()

# Simulate incoming market bar
event_q.put(BarEvent("AAPL", "2020-01-02", 75, 76, 74, 75.5, 120000))

# Strategy reacts → places order
event_q.put(OrderEvent("AAPL", "MARKET", 10, "BUY"))

# Broker executes order → fill event
event_q.put(FillEvent("AAPL", 10, "BUY", 755.0, "2020-01-02 10:05"))

# Engine loop: process events in order
while not event_q.empty():
    event = event_q.get()
    if isinstance(event, BarEvent):
        print(f"[BAR]  {event.symbol} {event.time} Close={event.close}")
    elif isinstance(event, OrderEvent):
        print(f"[ORDER] {event.direction} {event.quantity} {event.symbol}")
    elif isinstance(event, FillEvent):
        print(f"[FILL]  {event.quantity} {event.symbol} @ {event.fill_cost}")



df = pd.read_csv('data/AAPL_1d.csv')

print(df.head()) 
print("\nColumns:", df.columns.tolist())