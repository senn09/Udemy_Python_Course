import requests
from bs4 import BeautifulSoup

# date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD:")
date = "2000-08-12"

endpoint = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=endpoint, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_titles = [song_title.getText().strip() for song_title in soup.select("li ul li h3")]
artists = [artist.getText().strip() for artist in soup.select("li ul li span")]

print(len(artists[::7]))

# for song in song_titles:
#     print(song)

for artist in artists[::7]:
    print(artist)
