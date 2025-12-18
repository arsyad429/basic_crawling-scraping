from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

# Bikin list buat nyimpen dictionary product
list_products = []

# For loop untuk halaman
for page in range(1, 3):
	print(f"\nBuka halaman {page}")
	driver.get(f"https://www.tokopedia.com/p/rumah-tangga/kebutuhan-rumah/baterai?page={page}")
	time.sleep(3)

	# Scroll sampe kebawah halaman dulu buat tau ada produk atau objek apa aja
	last_height = driver.execute_script("return document.body.scrollHeight") #<- nyimpen tinggi halaman keseluruhan
	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #<- ngescroll halaman web ampe bawah
		time.sleep(2)
		new_height = driver.execute_script("return document.body.scrollHeight") #<- nyimpen tinggi halaman sekarang
		if new_height == last_height: # Kalo ada object di bawah yg baru, maka new_height > last_height nanti bakal terus scroll ke bawah
			break # kalo udah mentok, break
		last_height = new_height # nge-update tinggi baru
	
	# Ambil semua link produk
	products = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="lstCL3ProductList"] a[href]')
	links = [p.get_attribute('href') for p in products] # List list comprehension ngakses semua object products

	# Ngeloop setiap link produk
	for i, link in enumerate(links, start=1):
		
		print(f"Buka produk ke-{i}, halaman {page}: {link}")
		driver.get(link)
		time.sleep(3)

		last_height = driver.execute_script("return document.body.scrollHeight")
		while True:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #<- ngescroll halaman web ampe bawah
			time.sleep(2)
			new_height = driver.execute_script("return document.body.scrollHeight") #<- nyimpen tinggi halaman sekarang
			if new_height == last_height: # Kalo ada object di bawah yg baru, maka new_height > last_height nanti bakal terus scroll ke bawah
				break # kalo udah mentok, break
			last_height = new_height # nge-update tinggi baru

		# Ngambil elemen produk
		try:
			try:
				name = driver.find_element(By.CSS_SELECTOR, ".css-j63za0").text
			except:
				try:
					name = driver.find_element(By.CSS_SELECTOR, ".css-14yroid").text
				except:
					name = None
			
			product_data = {
				'name': name,
				'url': link
			}
			list_products.append(product_data)
		except Exception as e:
			print(e)

		#stop kalo udah produk ke 5
		if i == 5:
			break

		
		
driver.quit()
# Masukin hasil scraping ke dataframe
products_df = pd.DataFrame(list_products)
print(products_df.head(10))