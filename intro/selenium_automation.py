print("Hello word")

import time
from selenium import webdriver

driver=webdriver.Chrome()


driver.get("Https://www.ecoders.in")

time.sleep(5)

print(driver.title)

print(driver.current_url)

print(driver.page_source)

driver.quit()