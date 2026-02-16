import requests
import os
import subprocess
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
            except Exception: pass

    def get_now_playing(self):
        """Fetches the currently playing track. Prioritizes AppleScript (macOS), then Spotify API, then Last.fm."""

        # 1. Try AppleScript (macOS Focus)
        apple_data = self._get_from_applescript()
        if apple_data:
            return apple_data

        # 2. Try Spotify API
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
                        "source": "Spotify API",
                        "is_mock": False
                    }
            except Exception: pass

        # 3. Try Last.fm
        if self.lastfm_api_key and self.lastfm_api_key != "YOUR_API_KEY":
            try:
                base_url = "http://ws.audioscrobbler.com/2.0/"
                params = {
                    "method": "user.getrecenttracks", "user": self.lastfm_username,
                    "api_key": self.lastfm_api_key, "format": "json", "limit": 1
                }
                response = requests.get(base_url, params=params, timeout=5)
                data = response.json()
                track = data["recenttracks"]["track"][0]
                return {
                    "track": track["name"], "artist": track["artist"]["#text"],
                    "album": track["album"]["#text"],
                    "image": track["image"][-1]["#text"] if track["image"] else None,
                    "is_playing": track.get("@attr", {}).get("nowplaying") == "true",
                    "source": "Last.fm", "is_mock": False
                }
            except Exception: pass

        return self._get_mock_data()

    def _get_from_applescript(self):
        """Executes AppleScript to get Spotify info (macOS only)."""
        script_path = os.path.join(os.path.dirname(__file__), "..", "scripts", "get_spotify_info.applescript")
        if not os.path.exists(script_path):
            return None

        try:
            # osascript is only available on macOS
            result = subprocess.run(["osascript", script_path], capture_output=True, text=True, timeout=2)
            if result.returncode == 0 and result.stdout.strip():
                parts = result.stdout.strip().split("|")
                if len(parts) >= 5 and parts[0] != "stopped":
                    return {
                        "track": parts[1], "artist": parts[2], "album": parts[3],
                        "image": parts[4] if parts[4] else None,
                        "is_playing": parts[0] == "playing",
                        "source": "AppleScript", "is_mock": False
                    }
        except Exception: pass
        return None

    def _get_mock_data(self):
        return {
            "track": "Starboy", "artist": "The Weeknd", "album": "Starboy",
            "image": "https://lastfm.freetls.fastly.net/i/u/300x300/e9d6d5669b32e01b446f7f1412e6b208.png",
            "is_playing": True, "source": "Mock", "is_mock": True
        }
