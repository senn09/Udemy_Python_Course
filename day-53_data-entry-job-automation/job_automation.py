from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

class Job_Automation:
    load_dotenv()
    def __init__(self):
        self.scrap_data()
        self.populate_form()

    def scrap_data(self):
        zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
        response = requests.get(zillow_url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get data from zillow
        self.link_list = [link['href'] for link in soup.select('a[class="property-card-link"]')]
        self.price_list = [price.getText().split("+")[0].split("/")[0] for price in soup.select('span[data-test="property-card-price"]')]
        self.address_list = [price.getText().strip().split("|")[-1].strip() for price in soup.find_all('address')]

    def populate_form(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(os.getenv("GOOGLEFORM"))

        # todo find element for the 3 inputs
        # todo submit and repeat with next input

        for n in range(len(self.link_list)):
            address_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.address_list[n])
            price_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.address_list[n])
            address_input = self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(self.address_list[n])

            print(f"{self.link_list[n]} {self.price_list[n]} {self.address_list[n]}")


auto = Job_Automation()