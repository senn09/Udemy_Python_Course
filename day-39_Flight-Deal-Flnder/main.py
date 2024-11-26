import requests
import datetime
import os
from twilio.rest import Client

AMADUES_API_KEY = os.environ.get('AMADUES_API_KEY')
AMADUES_API_SECRET = os.environ.get('AMADUES_API_SECRET')
SHEETLY_SECRET = os.environ.get('SHEETLY_SECRET')

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


amadues_enpoint_base = "test.api.amadeus.com/v2"


def request_token():
    auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADUES_API_KEY,
        "client_secret": AMADUES_API_SECRET,
    }

    response = requests.post(auth_endpoint, headers=headers, data=data)
    result = response.json()
    # print(result)
    if response.status_code == 200:

        return result["access_token"]
    else:
        print("ERROR")
        return ""


def get_flight_deals(token, destinationLocationCode="NYC", lowestprice=850):
    flight_offer_enpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    date6months = (datetime.date.today() + datetime.timedelta(days=180)).strftime('%Y-%m-%d')

    params = {
        "originLocationCode": "YTO",
        "destinationLocationCode": destinationLocationCode,
        "departureDate": tomorrow,
        "returnDate": date6months,
        "adults": 1,
        "max": 10,
        "currencyCode": "CAD"
    }

    response = requests.get(flight_offer_enpoint, headers=headers, params=params)

    result = response.json()

    if response.status_code == 200:
        cheapflights = [flight for flight in result["data"] if float(flight["price"]["total"]) <= lowestprice]
    else:
        print("ERROR")
        return ""

    return cheapflights

def getSheetData(token):
    sheetly_endpoint = "https://api.sheety.co/30ee8cefeddb4d6147250f338a443567/flightDealTracker/sheet1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(sheetly_endpoint, headers=headers)
    return response.json()

def sendSMS(startIATA, destinationIATA, flightPrice, startDate, endDate):
        #     IATA code, destination airport IATA code, flight price and flight dates
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    body = f""" Only ${flightPrice} to fly from {startIATA} to {destinationIATA},
    on {startDate} to {endDate}.
        """

    message = client.messages \
        .create(
        body=body,
        from_='+',
        to='+'
    )
    print(message.status)

amadues_token = request_token()
userSheetData = getSheetData(SHEETLY_SECRET)["sheet1"]


for tracker in userSheetData:
    destinationLocationCode = tracker["iataCode"]
    lowestprice = tracker["priceLow"]
    flightDeals = get_flight_deals(amadues_token, destinationLocationCode, lowestprice)
    if flightDeals:
        prices = [flight["price"]["total"] for flight in flightDeals]
        cheapFlightIndex = prices.index(min(prices))
        cheapFlight = flightDeals[cheapFlightIndex]
        startIATA = cheapFlight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destinationIATA = cheapFlight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
        flightPrice = cheapFlight["price"]["total"]
        startDate = datetime.datetime.fromisoformat(cheapFlight["itineraries"][0]["segments"][0]["departure"]["at"]).date()
        endDate = datetime.datetime.fromisoformat(cheapFlight["itineraries"][-1]["segments"][-1]["departure"]["at"]).date()

        sendSMS(startIATA, destinationIATA, flightPrice, startDate, endDate)
