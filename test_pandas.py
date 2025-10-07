import pandas as pd

data = {
    "timestamp": ["2025-01-02", "2025-01-03"],
    "open": [100, 102],
    "close": [101, 103],
}

df = pd.DataFrame(data)
print(df)