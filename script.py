from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option(name="detach", value=True)

service = Service(executable_path="/home/yacine/.local/chromedriver-142/chromedriver") # Because their is two version 
driver = webdriver.Chrome(service=service, options=chromeoptions)




driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(3)
language = driver.find_element(By.ID, 'langSelect-EN')

print(language.text)
language.click()
time.sleep(3)
Game = True
checking_interval = 5
game_interval = 300
game_launch_time= int(time.time())
last_check = int(time.time())
products_data = {}

time_in_seconds = int(time.time())

while Game:
    now = int(time.time())

    if now - last_check >= checking_interval :
        products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        if products :
            for product in products :
                    product_id = product.get_attribute("id")
                    product_price = int(product.find_element(By.CLASS_NAME,"price").text.replace(",", ""))
                    products_data[product_id] = product_price 
            product_max = max(products_data,  key=products_data.get)
            choosen_product = driver.find_element(By.ID, product_max)
            choosen_product.click()

        last_check = now
    bigCookie = driver.find_element(By.ID, "bigCookie")
    bigCookie.click()
    if now - game_launch_time >= game_interval : 
         Game = False
         cookies_per_seconds = driver.find_element(By.ID, "cookiesPerSecond")
         print(f"Cookie/second: {cookies_per_seconds}")

driver.quit()