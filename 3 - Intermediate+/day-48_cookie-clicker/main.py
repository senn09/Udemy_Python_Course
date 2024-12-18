from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")

time_start = time.time()



while(True):
    time_check = time.time()
    time_elapsed = time_check - time_start
    if(time_elapsed > 5):
        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        time_start = time.time()
        for upgrade in upgrades[::-1]:
            if(upgrade.get_attribute("class") != "grayed"):
                print(upgrade.text)
                print(f"Purchased: {upgrade.get_attribute("id")}")
                upgrade.click()
                break

    cookie.click()
