import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class MusicService:
    def __init__(self):
        # Spotify credentials
        self.spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI", "http://localhost:8888/callback")

        # Last.fm credentials
        self.lastfm_api_key = os.getenv("LASTFM_API_KEY")
        self.lastfm_username = os.getenv("LASTFM_USERNAME", "r_v_s_")

        self.sp = None
        if self.spotify_client_id and self.spotify_client_secret:
            try:
                auth_manager = SpotifyOAuth(
                    client_id=self.spotify_client_id,
                    client_secret=self.spotify_client_secret,
                    redirect_uri=self.spotify_redirect_uri,
                    scope="user-read-currently-playing"
                )
                self.sp = spotipy.Spotify(auth_manager=auth_manager)
            except Exception as e:
                print(f"Spotify Auth Error: {e}")

    def get_now_playing(self):
        """Fetches the currently playing track from Spotify, falling back to Last.fm or mock data."""

        # 1. Try Spotify
        if self.sp:
            try:
                current_track = self.sp.currently_playing()
                if current_track and current_track.get('item'):
                    item = current_track['item']
                    return {
                        "track": item['name'],
                        "artist": item['artists'][0]['name'],
                        "album": item['album']['name'],
                        "image": item['album']['images'][0]['url'] if item['album']['images'] else None,
                        "is_playing": current_track['is_playing'],
                        "source": "Spotify",
                        "is_mock": False
                    }
            except Exception as e:
                print(f"Spotify API Error: {e}")

        # 2. Try Last.fm
        if self.lastfm_api_key and self.lastfm_api_key != "YOUR_API_KEY":
            try:
                base_url = "http://ws.audioscrobbler.com/2.0/"
                params = {
                    "method": "user.getrecenttracks",
                    "user": self.lastfm_username,
                    "api_key": self.lastfm_api_key,
                    "format": "json",
                    "limit": 1
                }
                response = requests.get(base_url, params=params, timeout=5)
                response.raise_for_status()
                data = response.json()

                track = data["recenttracks"]["track"][0]
                is_playing = track.get("@attr", {}).get("nowplaying") == "true"

                return {
                    "track": track["name"],
                    "artist": track["artist"]["#text"],
                    "album": track["album"]["#text"],
                    "image": track["image"][-1]["#text"] if track["image"] else None,
                    "is_playing": is_playing,
                    "source": "Last.fm",
                    "is_mock": False
                }
            except Exception as e:
                print(f"Last.fm API Error: {e}")

        # 3. Fallback to Mock
        return self._get_mock_data()

    def _get_mock_data(self):
        """Returns mock track data."""
        return {
            "track": "Starboy",
            "artist": "The Weeknd",
            "album": "Starboy",
            "image": "https://lastfm.freetls.fastly.net/i/u/300x300/e9d6d5669b32e01b446f7f1412e6b208.png",
            "is_playing": True,
            "source": "Mock",
            "is_mock": True
        }

if __name__ == "__main__":
    service = MusicService()
    print(service.get_now_playing())
