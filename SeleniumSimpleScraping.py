from selenium import webdriver
from selenium.webdriver.common.by import By

# Inisialisasi objek chrome driver
driver = webdriver.Chrome()

# Kunjungi situs 
driver.get("https://www.tokopedia.com/jabrick/lego-30685-star-wars-tie-interceptor-polybag-build-and-display?extParam=ivf%3Dfalse%26keyword%3Dlego+star+wars%26search_id%3D2025121602523689F0FD5C927D46144ULC%26src%3Dsearch&t_id=1765853567759&t_st=1&t_pp=search_result&t_efo=search_pure_goods_card&t_ef=goods_search&t_sm=&t_spt=search_result")

# Dapatkan elemen elemen yang ingin diambil
product = {
    'image': driver.find_element(By.CSS_SELECTOR, ".css-pefdcn").get_attribute("src"),
    'name': driver.find_element(By.CSS_SELECTOR, ".css-j63za0").text,
    'price': driver.find_element(By.CSS_SELECTOR, ".price").text
}

driver.quit()
print(product)