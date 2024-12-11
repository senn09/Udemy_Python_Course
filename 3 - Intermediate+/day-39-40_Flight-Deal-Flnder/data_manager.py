from pprint import pprint

import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self.account_sid = os.environ.get("ACCOUNT_SID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.secret = os.environ.get('SHEETLY_SECRET')
        self.sheety_prices_endpoint = os.environ.get('SHEETY_PRICES_ENDPOINT')
        self.sheety_users_endpoint = os.environ.get('SHEETY_USERS_ENDPOINT')
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {self.secret}"
        }

        response = requests.get(self.sheety_prices_endpoint, headers=headers)
        data = response.json()
        # pprint(data)
        self.destination_data = data["sheet1"]
        return self.destination_data

    def get_customer_emails(self):
        headers = {
            "Authorization": f"Bearer {self.secret}"
        }

        response = requests.get(self.sheety_users_endpoint, headers=headers)
        data = response.json()
        # pprint(data)
        self.user_data = data["users"]
        return self.user_data

    def update_destination_codes(self):
        headers = {
            "Authorization": f"Bearer {self.secret}"
        }

        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                headers=headers,
                url=f"{self.sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)


dataManager = DataManager()
dataManager.get_customer_emails()