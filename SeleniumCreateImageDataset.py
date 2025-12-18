from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
import pandas as pd

# Dictionary isi link web
url_dict = {
    'Blacktip reef (Carcharhinus melanopterus)': 'https://www.inaturalist.org/taxa/67964-Carcharhinus-melanopterus/browse_photos',
    'Whitetip reef (Triaenodon obesus)': 'https://www.inaturalist.org/taxa/52314-Triaenodon-obesus/browse_photos',
    'Oceanic whitetip (Carcharhinus longimanus)': 'https://www.inaturalist.org/taxa/96760-Carcharhinus-longimanus/browse_photos',
    'Bull shark (Carcharhinus leucas)': 'https://www.inaturalist.org/taxa/84996-Carcharhinus-leucas/browse_photos',
    'Whale shark (Rhincodon typus)': 'https://www.inaturalist.org/taxa/52188-Rhincodon-typus/browse_photos'

}
# List buat nanti bikkin dataframe
image_list = []

# Index image buat nama file image nya
image_index = 1

# Buat mastiin url nya unik (ga ada gambar duplikat)
downloaded_urls = set()

driver = webdriver.Chrome()

# For loop dictionary-nya buat bikin dataframe
for key, value in url_dict.items():
    image_count = 0
    driver.get(value)
    time.sleep(5)

    # Bikin folder kalo belom ada
    folder = "sharkImages"
    os.makedirs(folder, exist_ok=True)

    # Nge scroll ampe gambar yg di download 200
    while image_count <200:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        images = driver.find_elements(By.CSS_SELECTOR, "div[id^='cover-image']")

        # Looping buat akses objek gambar
        for img in images:
            if image_count >= 200:
                break
            
            try:
                # Ambil link gambar
                style = img.get_attribute("style")
                if "background-image" not in style:
                    continue

                src = style.split('url("')[1].split('")')[0] # split format html nya biar dapet link
            
                # Kalo image gak ada atau ga bisa di download
                if not src or not src.startswith("http"):
                    continue

                # Kalo url nya udah ada, skip
                if src in downloaded_urls:
                    continue

                downloaded_urls.add(src)

                # Proses download nya
                response = requests.get(src, timeout=10)
                if response.status_code == 200:
                    print(f"Download label {key} ke-{image_count}: {src}")
                    filename = f"image_{image_index}.jpg"
                    path = os.path.join(folder, filename)

                    with open(path, "wb") as f: # pake wb krn buat akses gambar 
                        f.write(response.content)
                
                    # Data dictionary buat ngisi dataframe
                    data = {
                        'image': f"{folder}/{filename}",
                        'label': key
                    }

                    image_list.append(data)
                    image_index+=1
                    image_count+=1
           
            except Exception as e:
                print("Error:", e)

driver.quit()
# Ubah list ke dataframe
image_df = pd.DataFrame(image_list)
print(image_df.head(5))

# Export dataframe nya ke lokal csv 
image_df.to_csv('shark_dataset.csv', index=False)