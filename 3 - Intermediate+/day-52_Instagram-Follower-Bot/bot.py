import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException

class InstagramBot:
    load_dotenv()

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        # Open URL
        url = "https://www.instagram.com/"
        self.driver.get(url)

        self.login()
        self.saveLoginInfo()

    def login(self):
        self.driver.implicitly_wait(3)
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(os.getenv("INSTA_USER"))
        pw = self.driver.find_element(By.NAME, 'password')
        pw.send_keys(os.getenv("INSTA_PASS"))
        signin = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        signin.click()

    def saveLoginInfo(self):
        try:
            notNow = self.driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
            notNow.click()
        except:
            pass



bot = InstagramBot()

