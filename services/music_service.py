import requests
import os

class MusicService:
    def __init__(self, api_key=None, username="r_v_s_"):
        self.api_key = api_key or os.getenv("LASTFM_API_KEY")
        self.username = username
        self.base_url = "http://ws.audioscrobbler.com/2.0/"

    def get_now_playing(self):
        """Fetches the currently playing track from Last.fm or returns mock data."""
        if not self.api_key or self.api_key == "YOUR_API_KEY":
            return self._get_mock_data()

        try:
            params = {
                "method": "user.getrecenttracks",
                "user": self.username,
                "api_key": self.api_key,
                "format": "json",
                "limit": 1
            }
            response = requests.get(self.base_url, params=params, timeout=5)
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
                "is_mock": False
            }
        except Exception as e:
            print(f"Last.fm API Error: {e}")
            return self._get_mock_data()

    def _get_mock_data(self):
        """Returns mock track data."""
        return {
            "track": "Starboy",
            "artist": "The Weeknd",
            "album": "Starboy",
            "image": "https://lastfm.freetls.fastly.net/i/u/300x300/e9d6d5669b32e01b446f7f1412e6b208.png",
            "is_playing": True,
            "is_mock": True
        }

if __name__ == "__main__":
    service = MusicService()
    print(service.get_now_playing())
