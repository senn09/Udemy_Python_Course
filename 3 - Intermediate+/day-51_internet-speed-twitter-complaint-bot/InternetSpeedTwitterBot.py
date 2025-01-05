from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from dotenv import load_dotenv
import os


class InternetSpeedTwitterBot:
    load_dotenv()

    def __init__(self):
        # create web browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.tweet_at_provider(self.get_internet_speed())

    def get_internet_speed(self):
        # Open URL
        url = "https://www.speedtest.net/"
        self.driver.get(url)

        # Start Test
        start_speed_test_button = self.driver.find_element(By.CSS_SELECTOR, "span.start-text")
        start_speed_test_button.click()
        time.sleep(40)

        # Collect Information
        down = self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text
        up = self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text
        isp = self.driver.find_element(By.CSS_SELECTOR, "div.js-data-isp").text
        return f"My current internet speed with {isp} is: {down}Mbps Down, {up}Mbps Up\n.\n.\n This message was automated in python"

    def tweet_at_provider(self, msg):
        # Open URL
        url = "https://x.com/i/flow/login"
        self.driver.get(url)
        self.driver.implicitly_wait(5)

        # Close Overlay
        # close_overlay = self.driver.find_element(By.XPATH, 'button[data-testid="xMigrationBottomBar"]')
        # close_overlay.click()

        # Sign in
        signin_methods = [self.twitter_signin1, self.twitter_signin2]
        for method in signin_methods:
            if method():
                print("Signed in")
                break

        # Close Overlay
        self.closeOverlay()

        # Tweet Internet Speed
        self.sendTweet(msg)

    def twitter_signin1(self):
        try:
            print("Trying Method 1 ...")
            open_sign_in = self.driver.find_element(By.LINK_TEXT, "Sign in")
            open_sign_in.click()
            enter_email = self.driver.find_element(By.NAME, "text")
            enter_email.send_keys(os.getenv("TWITTER_EMAIL"))
            click_next = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
            click_next.click()
            # for unusual login activity
            self.unusualActivity()

            enter_pass = self.driver.find_element(By.NAME, "password")
            enter_pass.send_keys(os.getenv("TWITTER_PASSWORD"))
            click_log_in = self.driver.find_element(By.XPATH,
                                                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
            click_log_in.click()
            return True
        except NoSuchElementException:
            return False
        return False

    def twitter_signin2(self):
        try:
            print("Trying Method 2 ...")
            enter_email = self.driver.find_element(By.XPATH,
                                                   '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
            enter_email.send_keys(os.getenv("TWITTER_EMAIL"))
            click_next = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
            click_next.click()

            # for unusual login activity
            self.unusualActivity()

            enter_pass = self.driver.find_element(By.NAME, "password")
            enter_pass.send_keys(os.getenv("TWITTER_PASSWORD"))
            click_log_in = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]')
            click_log_in.click()

            return True
        except NoSuchElementException:
            return False

    def unusualActivity(self):
        try:
            enter_username = self.driver.find_element(By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]')
            enter_username.send_keys(os.getenv("TWITTER_USER"))
            click_next = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="ocfEnterTextNextButton"]')
            click_next.click()
        except:
            pass

    def closeOverlay(self):
        try:
            overlay = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Close"]')
            overlay.click()
        except:
            pass

    def sendTweet(self, msg="Hello World"):
        textbox = self.driver.find_element(By.CSS_SELECTOR,
                                           'div[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
        textbox.click()
        textbox.send_keys(msg)

        post_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        post_button.click()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
# bot.tweet_at_provider()
# bot.driver.implicitly_wait(5)
# bot.driver.quit()
