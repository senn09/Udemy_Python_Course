import pprint

import requests
import os
from dotenv import load_dotenv

load_dotenv()

class MovieSearch():
    def __init__(self):
        self.base_poster_url = "https://image.tmdb.org/t/p/original"


    def title_search(self, title):
        url = 'https://api.themoviedb.org/3/search/movie'
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('MOVIE_API_KEY')}"
        }

        params = {
            'query': title
        }
        response = requests.get(url, headers=headers, params=params)

        data = response.json()
        pprint.pp(len(data['results']))

        return data['results']

    def id_search(self, id):
        url = f'https://api.themoviedb.org/3/movie/{id}'
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('MOVIE_API_KEY')}"
        }
        response = requests.get(url, headers=headers)

        data = response.json()
        pprint.pp(data)

        return data
