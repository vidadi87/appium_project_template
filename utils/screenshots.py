import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    driver.save_screenshot(filename)
