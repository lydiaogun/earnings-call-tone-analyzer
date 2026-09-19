from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf


def get_earnings_reaction(ticker, call_date, hold_days=1):
    """Fetch how the stock moved in the `hold_days` trading days after an
    earnings call.

    call_date: "YYYY-MM-DD" string, the calendar date of the call.
    NVIDIA reports after market close, so the call-day close is the
    pre-announcement price and the move shows up in the trading days
    that follow it.

    Returns a dict with the call-day close, the close `hold_days` trading
    days later, and the percentage return between them, or None if there
    isn't enough price history around that date (e.g. call date not yet
    reflected in available data).
    """
    call_ts = pd.Timestamp(call_date)
    start = call_ts - timedelta(days=7)
    end = call_ts + timedelta(days=hold_days * 3 + 14)

    history = yf.download(ticker, start=start, end=end, progress=False)
    if history.empty:
        return None

    closes = history["Close"]
    if hasattr(closes, "columns"):  # yfinance can return a 1-column frame
        closes = closes.iloc[:, 0]

    on_or_after = closes.index[closes.index >= call_ts]
    if on_or_after.empty:
        return None
    call_day = on_or_after[0]

    later_days = closes.index[closes.index > call_day]
    if len(later_days) < hold_days:
        return None
    target_day = later_days[hold_days - 1]

    call_close = float(closes.loc[call_day])
    target_close = float(closes.loc[target_day])

    return {
        "call_day": call_day.strftime("%Y-%m-%d"),
        "call_close": call_close,
        "target_day": target_day.strftime("%Y-%m-%d"),
        "target_close": target_close,
        "return": (target_close - call_close) / call_close,
    }
