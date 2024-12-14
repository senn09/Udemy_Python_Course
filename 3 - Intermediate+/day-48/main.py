from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# ------------ Exercise 1 ------------

# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# ------------- Challenge --------------------
# times = driver.find_elements(By.CSS_SELECTOR, value=".last .shrubbery .menu li time")
# names = driver.find_elements(By.CSS_SELECTOR, value=".last .shrubbery .menu li a")

# event_tags = driver.find_elements(By.CSS_SELECTOR, value="div div div ul.menu")
# print(len(event_tags))

# count = 5# the number of expected links on the page
# link_locator = (By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# WebDriverWait(driver, 10).until(lambda driver: len(driver.find_elements(link_locator)) == count)
# event_tags = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

python_events = {}
for n in range(len(event_names)):
    python_events[ngi] = {
        "time": event_times[n].get_attribute("datetime").split("T")[0],
        "name": event_names[n].text
    }
print(python_events)


driver.quit()