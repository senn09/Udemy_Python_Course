import requests
import datetime
import os

GENDER = "female"
WEIGHT_KG = 70
HEIGHT_CM = 190
AGE = 40

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

# Input exercise to feed into NUTRITIONIX

# message = input("Tell me which exercises you did: ")
message = "run 30 mins and swim 20 mins"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Authentication
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

# Request Payload
nutritionix_data = {"query": message,
                    "gender": GENDER,
                    "weight_kg": WEIGHT_KG,
                    "height_cm": HEIGHT_CM,
                    "age": AGE
                    }

nutritionix_response = requests.post(nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_data)

if nutritionix_response.status_code == 200:
    # Successful request

    result = nutritionix_response.json()['exercises']
    date_now = datetime.date.today().strftime('%d/%m/%Y')
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    sheetlyEndPoint = "https://api.sheety.co/30ee8cefeddb4d6147250f338a443567/workoutTracking/workouts"
    sheetly_header = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    for exercise in result:
        sheetlyData = {
            "workout": {
                "date": date_now,
                "time": time_now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        nutritionix_response = requests.post(sheetlyEndPoint, headers=sheetly_header, json=sheetlyData)


        # Check if the request was successful
        if nutritionix_response.status_code == 200 or nutritionix_response.status_code == 201:
            # Parse the JSON response
            result = nutritionix_response.json()
            print(result)
        else:
            print("Request failed with status code:", nutritionix_response.status_code)
            print(nutritionix_response.json())  # Print the error message if available

else:
    # Handle errors
    print("Request failed with status code:", nutritionix_response.status_code)
    print(nutritionix_response.json())  # Print the error message from the API if available
