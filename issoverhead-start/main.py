import requests
from datetime import datetime
from config import Config
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude



#Your position is within +5 or -5 degrees of the ISS position.
def iss_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        print("ISS is above")
        return True
    else:
        print("ISS isn't above")
        return False
def is_night():
    time_now = datetime.now()

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = time_now.hour


    if hour_now >= sunset:
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
config = Config()
while True:
    time.sleep(60)
    if iss_within_range() and is_night():
        config.send_email()
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



