-- Database schema for dashboard persistence
CREATE TABLE IF NOT EXISTS weather_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    city TEXT,
    temp REAL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS music_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    track TEXT,
    artist TEXT,
    album TEXT
);

CREATE INDEX idx_weather_time ON weather_history(timestamp);
CREATE INDEX idx_music_time ON music_history(timestamp);
