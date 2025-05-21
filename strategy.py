import pandas as pd

def generate_trade_signal(csv_path="data/traffic_scores.csv"):
    df = pd.read_csv(csv_path)
    df = df.tail(10)
    mean = df["score"].mean()
    std = df["score"].std()
    latest = df.iloc[-1]["score"]
    z = (latest - mean) / std if std != 0 else 0

    if latest > 1.3 and z > 2:
        return "BUY", latest, z
    elif latest < 0.8 and z < -1:
        return "SELL", latest, z
    else:
        return "HOLD", latest, z
