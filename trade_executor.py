import csv
from datetime import datetime
import os

def execute_trade(signal, price=None, z=None):
    log_file = "data/trade_log.csv"
    is_new = not os.path.exists(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["timestamp", "signal", "price", "z_score"])
        writer.writerow([datetime.now().isoformat(), signal, price, z])
    print(f"[🪙] Trade signal: {signal} (Score={price}, Z={z})")
