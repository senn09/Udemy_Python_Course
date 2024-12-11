import requests
from twilio.rest import Client

def check_if_rainy(data):
    rainy = False
    for day in data:
        if day["weather"][0]["id"] >= 700:
            rainy = True
            break
    if rainy:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="It will rain, bring an umbrella ☂️.",
            from_='+13436449066',
            to='+16475723596'
        )
        print(message.status)
    else:
        print("no umbrella needed")

parameters = {
    "lon": -78.680016,
    "lat": 33.816006,
    "appid": "",
    "cnt": 4,
}
account_sid = ""
auth_token = ""

OW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(OW_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()['list']
check_if_rainy(data)



