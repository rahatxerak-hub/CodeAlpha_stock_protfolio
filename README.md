# Ink & Ticker — Stock Portfolio Tracker

A simple command-line tool for building a mock stock portfolio using a fixed,
hardcoded set of ticker prices. Built as CodeAlpha Task 2.

There is no live market data — prices are defined in a Python dictionary — so
the tool is meant for practicing basic Python concepts like dictionaries,
input validation, formatted output, and file I/O, not for real trading or
investment decisions.

## Features

- View a table of available tickers, company names, and fixed prices
- Interactively enter tickers and quantities to build a portfolio
- Automatic input validation (unknown tickers, non-numeric or non-positive
  quantities are rejected with a helpful message)
- Repeated entries for the same ticker are combined into a running total
- A formatted ledger showing per-position value and total investment
- Optional export of the ledger to a timestamped `.csv` or `.txt` file

## Requirements

- Python 3.9+ (no external dependencies — only the standard library is used)

## Usage

Run the script from a terminal:

```bash
python portfolio.py
```

(Replace `portfolio.py` with whatever you've named the file.)

You'll be shown a table of available stocks, then prompted to enter holdings:

```
Ticker: AAPL
  Quantity of AAPL: 10
  Added 10 x AAPL. Running total: 10
Ticker: TSLA
  Quantity of TSLA: 5
  Added 5 x TSLA. Running total: 5
Ticker: DONE
```

Type `DONE` (or `Q`, `QUIT`, or just press Enter) to finish entering holdings.

Once finished, a ledger is printed showing each position's value and the
total investment. You'll then be asked whether to save the ledger:

```
Save the ledger? [csv / txt / skip]: csv
  Wrote /path/to/portfolio_20260909-142530.csv
```

Choosing `csv` or `txt` writes a timestamped file (e.g.
`portfolio_20260909-142530.csv`) to the current working directory; any other
input skips saving.

## Available Tickers

| Ticker | Name      | Price      |
|--------|-----------|------------|
| AAPL   | Apple     | $180.00    |
| TSLA   | Tesla     | $250.00    |
| GOOGL  | Alphabet  | $140.00    |
| AMZN   | Amazon    | $175.00    |
| MSFT   | Microsoft | $380.00    |
| NVDA   | NVIDIA    | $875.00    |
| META   | Meta      | $490.00    |
| NFLX   | Netflix   | $620.00    |

To change or extend the available stocks, edit the `PRICES` and `NAMES`
dictionaries at the top of the script (both must have matching ticker keys).

## Output File Formats

**CSV** (`portfolio_<timestamp>.csv`): columns `ticker, name, quantity, price,
value`, with a final `TOTAL` row summing the investment.

**TXT** (`portfolio_<timestamp>.txt`): a human-readable summary with a
generation timestamp and an aligned table of holdings, followed by the total
investment.

## Project Structure

The script is organized into small, single-purpose functions:

| Function            | Purpose                                             |
|----------------------|------------------------------------------------------|
| `show_market()`       | Prints the table of available tickers and prices     |
| `read_holdings()`     | Prompts the user for tickers/quantities, with validation |
| `position_value()`    | Computes the value of a single holding                |
| `total_investment()`  | Sums the value of all holdings                        |
| `print_ledger()`      | Prints the formatted portfolio summary                |
| `save_csv()`          | Writes the ledger to a CSV file                       |
| `save_txt()`          | Writes the ledger to a plain-text file                |
| `maybe_save()`        | Prompts to save and dispatches to the right writer    |
| `main()`              | Orchestrates the overall flow                         |

## Notes & Limitations

- Prices are static and do not reflect real market values.
- Holdings are not persisted between runs unless explicitly saved.
- Only one portfolio can be built per run of the script.
