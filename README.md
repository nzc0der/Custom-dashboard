# Premium Python Dashboard

A modern, "nice" dashboard built with Python and CustomTkinter.

## Features
- **Real-time Clock:** Displays current time, date, and greeting.
- **Weather Widget:** Integrates with OpenWeatherMap API (with mock fallback).
- **Music Widget:** Supports **Spotify API** (via `spotipy`) and falls back to **Last.fm** or mock data.
- **Inspiration Widget:** Displays daily quotes.
- **Modern UI:** Built with CustomTkinter for a sleek, dark appearance.

## Codebase Diversity
This project includes 10 different types of code/files:
1. Python (.py)
2. Bash (.sh)
3. JSON (.json)
4. YAML (.yml)
5. SQL (.sql)
6. Markdown (.md)
7. TOML (.toml)
8. Makefile
9. ENV (.env)
10. XML (.xml)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables in `.env`:
   - `OPENWEATHER_API_KEY`: Get from [OpenWeatherMap](https://openweathermap.org/api).
   - `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`: Get from [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
   - `LASTFM_API_KEY`: (Optional fallback) Get from [Last.fm API](https://www.last.fm/api).
3. Run the dashboard:
   ```bash
   python3 main.py
   ```
