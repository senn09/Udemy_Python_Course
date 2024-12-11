from pprint import pprint

import requests
from bs4 import BeautifulSoup


class BillboardScraper:
    def __init__(self, date):
        self.date = date
        self.endpoint = f"https://www.billboard.com/charts/hot-100/{self.date}"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.track_list = []

        self.scrapBillboard()

    def scrapBillboard(self):
        pprint(self.endpoint)

        response = requests.get(url=self.endpoint, headers=self.header)

        soup = BeautifulSoup(response.text, "html.parser")
        song_titles_tags = soup.select("li ul li h3")
        song_titles = [tag.getText().strip() for tag in song_titles_tags]
        artists_tag = soup.select("li ul li span")
        artists = [tag.getText().strip() for tag in artists_tag][::7]

        self.track_list = [(song_titles[i], artists[i]) for i in range(0, len(song_titles))]

    def getTrackList(self):
        return self.track_list
