from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os

# Option untuk headlessmode
option = webdriver.ChromeOptions()
option.add_argument("--headless=new")
option.add_argument("--window-size=1920,1080") # <- Nentuin ukuran viewport browser
option.add_argument("--disable-blink-features=AutomationControlled") #<- Ngurangin deteksi bot
option.add_argument( #<- Mengubah identitas browser
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(options=option)
driver.get("https://unsplash.com/id/s/foto/shark")
time.sleep(5)

# Bikin folder kalo belom ada
folder = "imagesSharks"
os.makedirs(folder, exist_ok=True)

# Scroll ampe bawah
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, "div[class='container-CgvcQa'] img") # Nyari div container yg isinya images

# Looping buat akses objek gambar
for i, img in enumerate(images, start=1):
    try:
        # Ambil link gambar
        src = (
            img.get_attribute("src")
            or img.get_attribute("data-src")
            or img.get_attribute("srcset")
        )

        # Kalo image gak ada atau ga bisa di download
        if not src or not src.startswith("http"):
            continue

        print(f"Download gambar ke-{i}: {src}")

        # Proses download nya
        response = requests.get(src, timeout=10)
        if response.status_code == 200:
            filename = f"gambar_{i}.jpg"
            path = os.path.join(folder, filename)

            with open(path, "wb") as f: # pake wb krn buat akses gambar 
                f.write(response.content)

    except Exception as e:
        print("Error:", e)

driver.quit()
