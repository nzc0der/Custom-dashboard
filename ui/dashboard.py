import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime
from services.weather_service import WeatherService
from services.music_service import MusicService
from services.quote_service import QuoteService

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Premium Python Dashboard")
        self.geometry("1200x800")
        ctk.set_appearance_mode("dark")

        # Colors - using a deep navy/purple palette to match the target design
        self.bg_color = "#0f0f1b"
        self.card_color = "#1e1e2e"
        self.accent_color = "#3b82f6"
        self.text_dim = "#888888"

        self.configure(fg_color=self.bg_color)

        self.weather_service = WeatherService()
        self.music_service = MusicService()
        self.quote_service = QuoteService()

        self.setup_ui()
        self.update_clock()
        self.update_weather()
        self.update_music()
        self.update_quote()

    def setup_ui(self):
        # Configure Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Header
        self.grid_rowconfigure(1, weight=1) # Main Content
        self.grid_rowconfigure(2, weight=0) # Footer

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=(60, 40), padx=40, sticky="nsew")

        self.greeting_label = ctk.CTkLabel(self.header_frame, text="GOOD MORNING",
                                          font=ctk.CTkFont(family="Inter", size=24, weight="bold"),
                                          text_color=self.text_dim)
        self.greeting_label.pack()

        # Clock Container to handle AM/PM layout
        self.clock_container = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.clock_container.pack()

        self.clock_label = ctk.CTkLabel(self.clock_container, text="07:20:14",
                                       font=ctk.CTkFont(family="Inter", size=100, weight="bold"))
        self.clock_label.pack(side="left")

        self.ampm_label = ctk.CTkLabel(self.clock_container, text="AM",
                                      font=ctk.CTkFont(family="Inter", size=32, weight="bold"))
        self.ampm_label.pack(side="left", padx=(10, 0), pady=(40, 0))

        self.date_label = ctk.CTkLabel(self.header_frame, text="Sunday, February 15, 2026",
                                      font=ctk.CTkFont(family="Inter", size=20),
                                      text_color=self.text_dim)
        self.date_label.pack(pady=(10, 0))

        # --- Main Content Area ---
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=1, column=0, padx=40, pady=(0, 40), sticky="nsew")
        self.content_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # 1. Weather Card
        self.weather_card = self.create_card(self.content_frame, "Weather", 0)
        self.temp_label = ctk.CTkLabel(self.weather_card, text="22°C", font=ctk.CTkFont(size=54, weight="bold"))
        self.temp_label.pack(pady=(10, 0))
        self.weather_desc = ctk.CTkLabel(self.weather_card, text="Cloudy", font=ctk.CTkFont(size=18), text_color=self.text_dim)
        self.weather_desc.pack()

        # Weather Stats (Wind/Humidity)
        self.weather_stats = ctk.CTkFrame(self.weather_card, fg_color="transparent")
        self.weather_stats.pack(fill="x", side="bottom", pady=20)
        self.wind_label = ctk.CTkLabel(self.weather_stats, text="12 km/h", font=ctk.CTkFont(size=14))
        self.wind_label.pack(side="left", expand=True)
        self.humid_label = ctk.CTkLabel(self.weather_stats, text="45%", font=ctk.CTkFont(size=14))
        self.humid_label.pack(side="left", expand=True)

        # 2. Music Card
        self.music_card = self.create_card(self.content_frame, "Currently Playing", 1)
        self.album_art_label = ctk.CTkLabel(self.music_card, text="", width=140, height=140)
        self.album_art_label.pack(pady=10)
        self.track_label = ctk.CTkLabel(self.music_card, text="Starboy", font=ctk.CTkFont(size=20, weight="bold"))
        self.track_label.pack()
        self.artist_label = ctk.CTkLabel(self.music_card, text="The Weeknd", font=ctk.CTkFont(size=14), text_color=self.text_dim)
        self.artist_label.pack()

        # 3. Daily Inspiration Card
        self.quote_card = self.create_card(self.content_frame, "Daily Inspiration", 2)
        self.quote_text = ctk.CTkLabel(self.quote_card, text='"..."', font=ctk.CTkFont(size=18, slant="italic"), wraplength=250)
        self.quote_text.pack(pady=(20, 10), padx=20)
        self.quote_author = ctk.CTkLabel(self.quote_card, text="— STEVE JOBS", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.accent_color)
        self.quote_author.pack(side="bottom", pady=20)

        # --- Footer ---
        self.footer_frame = ctk.CTkFrame(self, fg_color="#252538", height=40, corner_radius=10)
        self.footer_frame.grid(row=2, column=0, padx=80, pady=(0, 40), sticky="ew")
        self.footer_frame.grid_propagate(False)

        self.status_label = ctk.CTkLabel(self.footer_frame, text="SYSTEM OPERATIONAL", font=ctk.CTkFont(size=12, weight="bold"), text_color="#aaaaaa")
        self.status_label.pack(side="left", padx=20)

        self.version_label = ctk.CTkLabel(self.footer_frame, text="V1.0.0 ●", font=ctk.CTkFont(size=12), text_color="#10b981")
        self.version_label.pack(side="right", padx=20)

    def create_card(self, parent, title, column):
        card = ctk.CTkFrame(parent, corner_radius=25, fg_color=self.card_color, border_width=1, border_color="#333344")
        card.grid(row=0, column=column, padx=15, pady=20, sticky="nsew")

        title_label = ctk.CTkLabel(card, text=title.upper(), font=ctk.CTkFont(size=14, weight="bold"), text_color=self.accent_color)
        title_label.pack(pady=(20, 5))

        return card

    def update_clock(self):
        now = datetime.now()
        self.clock_label.configure(text=now.strftime("%I:%M:%S"))
        self.ampm_label.configure(text=now.strftime("%p"))
        self.date_label.configure(text=now.strftime("%A, %B %d, %Y"))

        hour = now.hour
        if hour < 12: greeting = "GOOD MORNING"
        elif hour < 18: greeting = "GOOD AFTERNOON"
        else: greeting = "GOOD EVENING"
        self.greeting_label.configure(text=greeting)

        self.after(1000, self.update_clock)

    def update_weather(self):
        data = self.weather_service.get_weather()
        self.temp_label.configure(text=f"{data['temp']}°C")
        self.weather_desc.configure(text=data['description'])
        self.wind_label.configure(text=f"༄  {data['wind_speed']} km/h")
        self.humid_label.configure(text=f"💧  {data['humidity']}%")
        self.after(600000, self.update_weather)

    def update_music(self):
        data = self.music_service.get_now_playing()
        self.track_label.configure(text=data['track'])
        self.artist_label.configure(text=data['artist'])

        if data.get('image'):
            try:
                response = requests.get(data['image'])
                img = Image.open(BytesIO(response.content))
                img = img.resize((140, 140), Image.Resampling.LANCZOS)
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(140, 140))
                self.album_art_label.configure(image=ctk_img, text="")
            except Exception: pass

        self.after(15000, self.update_music)

    def update_quote(self):
        quote = self.quote_service.get_random_quote()
        self.quote_text.configure(text=f'"{quote["text"]}"')
        self.quote_author.configure(text=f"— {quote['author'].upper()}")
        self.after(3600000, self.update_quote) # Update hourly

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
