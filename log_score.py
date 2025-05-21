import os
import cv2
import csv
import numpy as np
from datetime import datetime

# Pick the latest screenshot
tile_dir = "data/tiles"
latest_tile = sorted(os.listdir(tile_dir))[-1]
tile_path = os.path.join(tile_dir, latest_tile)

img = cv2.imread(tile_path)
if img is None:
    raise ValueError("Image load failed")

# Color masks
red = cv2.inRange(img, (0, 0, 150), (100, 100, 255))
orange = cv2.inRange(img, (0, 150, 150), (100, 255, 255))
green = cv2.inRange(img, (0, 100, 0), (100, 255, 100))

total = img.shape[0] * img.shape[1]
score = (3 * np.sum(red > 0) + 2 * np.sum(orange > 0) + 1 * np.sum(green > 0)) / total
score = round(score, 4)

# Log score
log_path = "data/traffic_scores.csv"
is_new = not os.path.exists(log_path)

with open(log_path, "a", newline="") as f:
    writer = csv.writer(f)
    if is_new:
        writer.writerow(["timestamp", "image", "score"])
    writer.writerow([datetime.now().isoformat(), latest_tile, score])

print(f"[📊] Logged: {latest_tile} → {score}")
