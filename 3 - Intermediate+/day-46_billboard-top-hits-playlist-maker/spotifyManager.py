from pprint import pprint

from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import urlencode
import spotipy.util as util

load_dotenv()


class SpotifyManager:
    def __init__(self, track_list, date="2000-08-12"):
        self.scope = "playlist-modify-private"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.playlist_id = ""
        self.track_list = track_list
        self.track_ids = []
        self.date = date

        self.create_playlist()
        self.compile_track_ids()
        self.add_tracks_to_playlist()

    def create_playlist(self):
        playlist_name = f"Top Tracks of the Week of  {self.date}"
        USER_ID = os.getenv("USER_ID")
        results = self.sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False, collaborative=False)

        # get playlist id from newly created playlist
        self.playlist_id = results['href'].split('/')[-1]
        pprint(f"Playlist ID:{self.playlist_id}\n\n")

    def compile_track_ids(self):
        pprint(self.track_list)
        for track in self.track_list:
            params = {
                'query': f'track:"{track[0]}" artist:"{track[1]}"',
                'type': 'track',
            }

            # Encode the query
            encoded_params = urlencode(params)
            url = f'https://api.spotify.com/v1/search?{encoded_params}'

            track_results = self.sp.search(url, 1)
            pprint(f"Added Track ID:{track_results["tracks"]["items"][0]["uri"]}\n\n")
            self.track_ids.append(track_results["tracks"]["items"][0]["uri"])



    def add_tracks_to_playlist(self):
        self.sp.playlist_add_items(self.playlist_id, self.track_ids)

# spotipy = SpotifyManager()
# spotipy.create_playlist()
