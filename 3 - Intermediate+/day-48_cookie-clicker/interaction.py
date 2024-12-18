from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # articlecount = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # articlecount.click()
# # print(articlecount.text)
#
# searchbar = driver.find_element(By.CLASS_NAME, value="search-toggle")
# searchbar.click()
#
# searchbar = driver.find_element(By.NAME, value="search")
# searchbar.send_keys("python")
# searchbar.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
lName = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CLASS_NAME, value="btn-block")

fname.send_keys("Steve")
lName.send_keys("N")
email.send_keys("steveN@gg")
submit.click()




