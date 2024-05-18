from datetime import datetime

import requests

USERNAME = "steve12345"
TOKEN = "zxczxczcasdasdasd1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)
# print(response.text)


graph_config = {
    "id": "graph12",
    "name": "GRAPH",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime(year=2023, month=5, day=19)
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_pixel_config = {
    "quantity": "100",
}

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config["date"]}"
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
#
# print(response.text)
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{pixel_config["date"]}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)

print(response.text)
