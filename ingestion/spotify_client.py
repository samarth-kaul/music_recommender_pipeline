"""
# What this will do ??

- Authenticate using Client Credentials Flow
- Provide helper methods to search for:
        a) Artists
        b) Tracks
        c) Genres (via artists)
"""

import os
from dotenv import load_dotenv
import requests
from typing import Dict, List

load_dotenv()

class SpotifyClient:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.token_url = "https://accounts.spotify.com/api/token"
        self.api_url = "https://api.spotify.com/v1"
        self.token = self.get_access_token()

    def get_access_token(self) -> str:
        response = requests.post(
            self.token_url,
            data={"grant_type": "client_credentials"},
            auth=(self.client_id, self.client_secret),
        )
        if response.status_code != 200:
            print("Error Response:", response.status_code)
            print("Response Body:", response.text)
            raise Exception("Failed to get Spotify access token")
        return response.json()["access_token"]
    
    def get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}"
        }

    def search_artist(self, name: str) -> Dict:
        url = f"{self.api_url}/search"
        params = {"q": name, "type": "artist", "limit": 1}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json().get("artists", {}).get("items", [None])[0]

    def get_artist_top_tracks(self, artist_id: str, market="US") -> List[Dict]:
        url = f"{self.api_url}/artists/{artist_id}/top-tracks"
        params = {"market": market}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json().get("tracks", [])

    def get_track_info(self, track_id: str) -> Dict:
        url = f"{self.api_url}/tracks/{track_id}"
        response = requests.get(url, headers=self.get_headers())
        return response.json()

    def get_artist_genres(self, artist_id: str) -> List[str]:
        url = f"{self.api_url}/artists/{artist_id}"
        response = requests.get(url, headers=self.get_headers())
        return response.json().get("genres", [])