import os
import alpaca_trade_api as tradeapi

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

def place_order(signal, symbol="XRT", qty=1):
    if signal == "BUY":
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        print(f"[🟢] Placed BUY order for {qty} shares of {symbol}")
    elif signal == "SELL":
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side="sell",
            type="market",
            time_in_force="gtc"
        )
        print(f"[🔴] Placed SELL order for {qty} shares of {symbol}")
    else:
        print("[⏸️] HOLD — No order placed")
