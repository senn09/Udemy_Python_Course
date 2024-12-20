from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv
import os

def sign_in():
    # Autofill Sign in
    try:
        sign_in_open = driver.find_element(By.CSS_SELECTOR, value="[data-modal='base-sign-in-modal']")
        sign_in_open.click()
    except NoSuchElementException:
        sign_in_open = driver.find_element(By.CSS_SELECTOR, value="[data-modal='base-sign-in-modal']")
        sign_in_open.click()

    username_field = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
    password_field = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
    username_field.send_keys(os.getenv('LINKEDIN_EMAIL'))
    password_field.send_keys(os.getenv('LINKEDIN_PASSWORD'))

    sign_in_complete = driver.find_element(By.CSS_SELECTOR,
                                           value="#base-sign-in-modal > div > section > div > div > form > div.flex.justify-between.sign-in-form__footer--full-width > button")
    sign_in_complete.click()


def close_overlay():
    overlay = driver.find_element(By.ID, value="ember43")
    overlay.click()


load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open Linkedin Job Form
url = "https://www.linkedin.com/jobs/search/?currentJobId=4102565752&f_AL=true&f_E=2&geoId=90009551&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

sign_in()
close_overlay()

# Save Job
# Get Job Listing
job_listing = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
# Get first 4 as they are viewable
for n in range(4):
    try:
        print(job_listing[n].text)
        job_listing[n].click()
        save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
        save_button.click()
    except NoSuchElementException:
        continue
driver.quit()
