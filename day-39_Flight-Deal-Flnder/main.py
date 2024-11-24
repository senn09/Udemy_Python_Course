import requests
import datetime

AMADUES_API_KEY = ""
AMADUES_API_SECRET = ""

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
    print(result)
    if response.status_code == 200:

        return result["access_token"]
    else:
        print("ERROR")
        return ""


def get_flight_deals(
        originLocationCode="YTO",
        destinationLocationCode="NYC",
        departureDate="2024-12-29",
        returnDate="2025-01-05",
        adults="2"):
    flight_offer_enpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    date6months = (datetime.date.today() + datetime.timedelta(days=180)).strftime('%Y-%m-%d')
    print(tomorrow)
    print(date6months)


    params = {
        "originLocationCode": originLocationCode,
        "destinationLocationCode": destinationLocationCode,
        "departureDate": tomorrow,
        "returnDate": date6months,
        "adults": adults
    }

    response = requests.get(flight_offer_enpoint, headers=headers, params=params)
    result = response.json()
    lowestprice = 900
    cheapflights = [flight for flight in result["data"] if float(flight["price"]["total"]) <= lowestprice]
    print(cheapflights)

#     todo
#     connect to google sheets
#     send sms

token = request_token()
print(token)

print(get_flight_deals())
