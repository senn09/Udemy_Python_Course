from pprint import pprint

import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/30ee8cefeddb4d6147250f338a443567/flightDealTracker/sheet1"

class DataManager:

    def __init__(self):
        self.account_sid = os.environ.get("ACCOUNT_SID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.secret = os.environ.get('SHEETLY_SECRET')
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {self.secret}"
        }

        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        # pprint(data)
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)