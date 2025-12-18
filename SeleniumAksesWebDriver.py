from selenium import webdriver

# Inisialisasi objek chrome driver
driver = webdriver.Chrome()

# Kunjungi situs 
driver.get("https://www.tokopedia.com/search?st=&q=lego%20star%20wars&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=")

# Tampilkan semua html halaman
print(driver.page_source)

driver.quit()