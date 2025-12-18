from selenium import webdriver

# Instansiasi chrome option ovject
option = webdriver.ChromeOptions()

# Mengatur pengaturan chorme biar make headless mode
option.add_argument("--headless=new")

# Inisialisasi objek chrome driver
driver = webdriver.Chrome(options=option)

# Kunjungi situs 
driver.get("https://www.tokopedia.com/search?st=&q=lego%20star%20wars&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=")

# Tampilkan semua html halaman
print(driver.page_source)

driver.quit()