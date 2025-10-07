# 🧠 Mini Backtester — Step 01: Data Loader

> First milestone of building a lightweight event-driven backtesting engine in Python.

---

## 🚀 Overview
This step sets up the foundation of the backtester — a **data ingestion module** that reads OHLCV bars from CSV files and streams them as Python dataclasses.  
Everything that follows (engine, broker, portfolio, strategy) will consume this data.

---

## 🧩 Features
- ✅ `Bar` dataclass (`timestamp`, `open`, `high`, `low`, `close`, `volume`)
- ✅ `load_bars_from_csv()` — generator that yields `Bar` objects
- ✅ Automatic column validation
- ✅ Sample CSV generator (`create_sample_csv()`)
- ✅ Built-in `_test()` for quick validation

---

## 🧰 Requirements
- Python 3.9+
- Dependencies:
  ```bash
  pip install pandas
  pip install yfinance
  pip install cctx
