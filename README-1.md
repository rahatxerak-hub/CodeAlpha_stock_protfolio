# CodeAlpha_StockPortfolioTracker

A simple command-line stock portfolio tracker built in Python, created as
Task 2 for the CodeAlpha Python Programming Internship.

## How It Works

- Stock prices are hardcoded in a dictionary (e.g. `{"AAPL": 180, "TSLA": 250}`).
- The user enters stock symbols and quantities until typing `done`.
- The program calculates the value of each holding and the total
  investment.
- The user can optionally save a summary to `portfolio_summary.txt`.

## Concepts Used

- Dictionaries for storing stock prices and the user's portfolio
- Basic arithmetic for calculating investment value
- Input validation (checking for valid symbols and positive whole numbers)
- File handling (`open()`/`write()`) for saving the summary

## How to Run

```bash
python stock_tracker.py
```

Enter a stock symbol (from the available list shown), then its quantity.
Type `done` when finished to see your portfolio breakdown and total
investment.

## Example

```
Stock symbol (or 'done'): AAPL
Quantity of AAPL: 10
Added 10 share(s) of AAPL.

Stock symbol (or 'done'): done

--- Portfolio Breakdown ---
AAPL: 10 share(s) = $1800

Total Investment: $1800
```
