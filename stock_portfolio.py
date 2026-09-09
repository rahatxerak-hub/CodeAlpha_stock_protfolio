from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

PRICES: dict[str, float] = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "AMZN": 175.0,
    "MSFT": 380.0,
    "NVDA": 875.0,
    "META": 490.0,
    "NFLX": 620.0,
}

NAMES: dict[str, str] = {
    "AAPL": "Apple",
    "TSLA": "Tesla",
    "GOOGL": "Alphabet",
    "AMZN": "Amazon",
    "MSFT": "Microsoft",
    "NVDA": "NVIDIA",
    "META": "Meta",
    "NFLX": "Netflix",
}


def show_market() -> None:
    print()
    print("Available stocks (hardcoded prices)")
    print("%-8s%-14s%10s" % ("Ticker", "Name", "Price"))
    print("-" * 32)
    for ticker, price in PRICES.items():
        print("%-8s%-14s%10s" % (ticker, NAMES[ticker], "$" + format(price, ",.2f")))


def read_holdings() -> dict[str, int]:
    holdings: dict[str, int] = {}
    print()
    print("Enter ticker and quantity. Type DONE when finished.")
    while True:
        raw = input("Ticker: ").strip().upper()
        if raw in {"DONE", "Q", "QUIT", ""}:
            break
        if raw not in PRICES:
            print("  Unknown ticker '%s'. Choose from: %s" % (raw, ", ".join(PRICES)))
            continue
        qty_raw = input("  Quantity of %s: " % raw).strip()
        try:
            qty = int(qty_raw)
        except ValueError:
            print("  Quantity must be a whole number.")
            continue
        if qty <= 0:
            print("  Quantity must be positive.")
            continue
        holdings[raw] = holdings.get(raw, 0) + qty
        print("  Added %d x %s. Running total: %d" % (qty, raw, holdings[raw]))
    return holdings


def position_value(ticker: str, quantity: int) -> float:
    return PRICES[ticker] * quantity


def total_investment(holdings: dict[str, int]) -> float:
    return sum(position_value(t, q) for t, q in holdings.items())


def print_ledger(holdings: dict[str, int]) -> None:
    if not holdings:
        print()
        print("The ledger is empty.")
        return
    print()
    print("PORTFOLIO")
    print("%-8s%-14s%6s%12s%14s" % ("Ticker", "Name", "Qty", "Price", "Value"))
    print("-" * 54)
    for ticker, qty in holdings.items():
        value = position_value(ticker, qty)
        print(
            "%-8s%-14s%6d%12s%14s"
            % (
                ticker,
                NAMES[ticker],
                qty,
                "$" + format(PRICES[ticker], ",.2f"),
                "$" + format(value, ",.2f"),
            )
        )
    print("-" * 54)
    print(
        "%-28s%26s"
        % ("TOTAL INVESTMENT", "$" + format(total_investment(holdings), ",.2f"))
    )


def save_csv(holdings: dict[str, int], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["ticker", "name", "quantity", "price", "value"])
        for ticker, qty in holdings.items():
            writer.writerow(
                [
                    ticker,
                    NAMES[ticker],
                    qty,
                    "%.2f" % PRICES[ticker],
                    "%.2f" % position_value(ticker, qty),
                ]
            )
        writer.writerow(["TOTAL", "", "", "", "%.2f" % total_investment(holdings)])


def save_txt(holdings: dict[str, int], path: Path) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "INK & TICKER — PORTFOLIO SUMMARY",
        "Generated: %s" % stamp,
        "Hardcoded prices (CodeAlpha Task 2)",
        "--------------------------------",
        "",
    ]
    for ticker, qty in holdings.items():
        value = position_value(ticker, qty)
        lines.append(
            "%-6s %-12s  x %4d  @ %10.2f  =  %12.2f"
            % (ticker, NAMES[ticker], qty, PRICES[ticker], value)
        )
    lines.append("")
    lines.append("TOTAL INVESTMENT: %.2f" % total_investment(holdings))
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def maybe_save(holdings: dict[str, int]) -> None:
    if not holdings:
        return
    choice = input("\nSave the ledger? [csv / txt / skip]: ").strip().lower()
    if choice not in {"csv", "txt"}:
        print("  Skipped.")
        return
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = Path("portfolio_%s.%s" % (stamp, choice))
    if choice == "csv":
        save_csv(holdings, path)
    else:
        save_txt(holdings, path)
    print("  Wrote %s" % path.resolve())


def main() -> None:
    print("INK & TICKER — Stock Portfolio Tracker")
    print("Prices are fixed in a dictionary. No market feed.")
    show_market()
    holdings = read_holdings()
    print_ledger(holdings)
    maybe_save(holdings)


if __name__ == "__main__":
    main()
