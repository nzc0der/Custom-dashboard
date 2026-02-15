import requests
import os
from datetime import datetime

class WeatherService:
    def __init__(self, api_key=None, city="London"):
        self.api_key = api_key or os.getenv("OPENWEATHER_API_KEY")
        self.city = city
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self):
        """Fetches weather data or returns mock data if API key is missing or request fails."""
        if not self.api_key or self.api_key == "YOUR_API_KEY":
            return self._get_mock_data()

        try:
            params = {
                "q": self.city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            return {
                "temp": round(data["main"]["temp"]),
                "description": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "city": data["name"],
                "is_mock": False
            }
        except Exception as e:
            print(f"Weather API Error: {e}")
            return self._get_mock_data()

    def _get_mock_data(self):
        """Returns realistic mock weather data."""
        return {
            "temp": 22,
            "description": "Partly Cloudy",
            "icon": "02d",
            "humidity": 45,
            "wind_speed": 12,
            "city": "Mock City",
            "is_mock": True
        }

if __name__ == "__main__":
    service = WeatherService()
    print(service.get_weather())
