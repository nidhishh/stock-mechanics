# Stock Market Simulator (Python)

A Python-based **agent-based stock market simulator** that models the **core mechanics of real-world financial markets**, including order flow, price formation, and liquidity.

This project focuses on **market microstructure**, not price prediction.

---

## 🚀 Features

- Limit Order Book (LOB)
- Order matching engine (price–time priority)
- Bid–ask spread formation
- Noise traders and market makers
- Partial order fills
- Price discovery via order flow
- Simulated price time series

---

## 🧠 Core Concepts Modeled

- Order-driven markets
- Supply–demand interaction
- Liquidity and spreads
- Aggressive vs passive orders
- Mid-price vs last traded price
- Market impact (basic)

---

## 🏗️ Project Structure

```text
.
├── order_book.py      # Order book and matching engine
├── traders.py         # Trader behavior (noise trader, market maker)
├── simulation.py      # Market loop and execution
├── main.py            # Entry point
└── README.md
````

---

## ⚙️ How the Market Works (High Level)

1. Traders observe the market (mid-price)
2. Traders submit limit orders to the order book
3. The matching engine matches compatible buy and sell orders
4. Trades update prices and liquidity
5. The process repeats over time

Price is **not assumed** — it **emerges** from order interactions.

---

## ▶️ How to Run

### Requirements

* Python 3.8+
* matplotlib

### Install dependencies

```bash
pip install matplotlib
```

### Run the simulation

```bash
python main.py
```

This will generate a simulated price series.

---

## 📈 Example Output

* Time series of prices generated from order flow
* Volatility emerging from trader interactions
* Bid–ask spread dynamics

---

## 🔍 Design Philosophy

This simulator intentionally avoids:

* Random walk price assumptions
* Black-box ML prediction
* Indicator-based trading logic

Instead, it focuses on **first-principles market mechanics**, similar to how real exchanges operate.

---

## 🧪 Future Improvements

* Market orders
* Order cancellations
* Trader inventory & PnL tracking
* Informed and momentum traders
* Multi-asset markets
* Volatility clustering analysis
* Correlation and spillover modeling

---

## 🎯 Motivation

Built to deeply understand **how prices are actually formed in financial markets**, rather than treating prices as exogenous data.

This project serves as a foundation for:

* Quantitative finance research
* Agent-based modeling
* Market microstructure studies

--
