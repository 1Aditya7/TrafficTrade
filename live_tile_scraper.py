import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,800")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

maps_url = "https://www.google.com/maps/@40.7580,-73.9855,16z/data=!5m1!1e1"
driver.get(maps_url)
time.sleep(5)

timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
tile_path = f"data/tiles/traffic_{timestamp}.png"
os.makedirs("data/tiles", exist_ok=True)
driver.save_screenshot(tile_path)
driver.quit()

print(f"[✓] Screenshot saved: {tile_path}")
