import os
import alpaca_trade_api as tradeapi

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

account = api.get_account()
print(f"[✓] Connected to Alpaca Paper Account: ${account.cash} available")

# Optional: check market status
clock = api.get_clock()
print(f"[🕒] Market open: {clock.is_open}, Time: {clock.timestamp}")
