import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "CLIENT_ID_HERE"
CLIENT_SECRET = "CLIENT_SECRET_HERE"
# Your fixed ngrok URL
REDIRECT_URI = "https://realizable-expeditiously-sariah.ngrok-free.dev/callback"

SCOPE = "user-read-currently-playing user-read-playback-state"

class MusicService:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope=SCOPE,
                open_browser=True,  # will open browser to log in
                cache_path=".spotifycache"
            )
        )

    def get_now_playing(self):
        try:
            result = self.sp.current_user_playing_track()

            if not result or not result.get("item"):
                return {
                    "track": "Nothing Playing",
                    "artist": "",
                    "album": "",
                    "image": None,
                    "is_playing": False
                }

            item = result["item"]

            return {
                "track": item["name"],
                "artist": ", ".join(a["name"] for a in item["artists"]),
                "album": item["album"]["name"],
                "image": item["album"]["images"][0]["url"] if item["album"]["images"] else None,
                "is_playing": result["is_playing"]
            }

        except Exception as e:
            print("Spotify error:", e)
            return {
                "track": "Spotify Error",
                "artist": "",
                "album": "",
                "image": None,
                "is_playing": False
            }
