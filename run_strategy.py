import subprocess
from strategy import generate_trade_signal
from trade_executor import execute_trade
from alpaca_trader import place_order

# Step 1: Scrape
subprocess.run(["python", "live_tile_scraper.py"])

# Step 2: Score
subprocess.run(["python", "log_score.py"])

# Step 3: Signal
signal, score, z = generate_trade_signal()

# Step 4: Log it
execute_trade(signal, score, z)

# Step 5: Send order
place_order(signal, symbol="XRT", qty=1)
