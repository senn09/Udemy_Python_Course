import requests

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

    params = {
        "originLocationCode": originLocationCode,
        "destinationLocationCode": destinationLocationCode,
        "departureDate": departureDate,
        "returnDate": returnDate,
        "adults": adults
    }

    response = requests.get(flight_offer_enpoint, headers=headers, params=params)
    result = response.json()
    print(result)


# "PLQNe5wc3e8zv3cDwmf7IThf74Rs"
token = request_token()
print(token)

print(get_flight_deals())
