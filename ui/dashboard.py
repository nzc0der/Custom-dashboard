import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime
from services.weather_service import WeatherService
from services.music_service import MusicService
from services.quote_service import QuoteService
from ui.background import create_gradient

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Premium Music Dashboard")
        self.geometry("1280x800")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")

        self.weather_service = WeatherService()
        self.music_service = MusicService()
        self.quote_service = QuoteService()

        self.setup_ui()
        self.update_clock()
        self.update_weather()
        self.update_music()

    def setup_ui(self):
        # Apply Gradient Background
        self.bg_image_pil = create_gradient(1280, 800, (15, 15, 27), (40, 40, 70))
        self.bg_image = ctk.CTkImage(light_image=self.bg_image_pil,
                                     dark_image=self.bg_image_pil,
                                     size=(1280, 800))

        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Use a single main frame to hold everything
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=40, pady=40)

        # --- Top Right: Clock ---
        self.clock_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.clock_frame.place(relx=1.0, rely=0.0, anchor="ne")

        self.clock_label = ctk.CTkLabel(self.clock_frame, text="00:00:00",
                                       font=ctk.CTkFont(family="Inter", size=48, weight="bold"))
        self.clock_label.pack(anchor="e")

        self.date_label = ctk.CTkLabel(self.clock_frame, text="Date",
                                      font=ctk.CTkFont(size=16), text_color="#888888")
        self.date_label.pack(anchor="e")

        # --- Center: Music Focus ---
        self.music_focus = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.music_focus.place(relx=0.5, rely=0.45, anchor="center")

        # Large Album Art
        self.album_art_label = ctk.CTkLabel(self.music_focus, text="", width=400, height=400)
        self.album_art_label.pack(pady=20)

        # Track Info
        self.track_label = ctk.CTkLabel(self.music_focus, text="Track Title",
                                       font=ctk.CTkFont(size=36, weight="bold"))
        self.track_label.pack()

        self.artist_label = ctk.CTkLabel(self.music_focus, text="Artist Name",
                                        font=ctk.CTkFont(size=20), text_color="#3b82f6")
        self.artist_label.pack(pady=(5, 0))

        self.album_label = ctk.CTkLabel(self.music_focus, text="Album Name",
                                       font=ctk.CTkFont(size=14), text_color="#888888")
        self.album_label.pack()

        # Visualizer-like spacer
        self.viz_frame = ctk.CTkFrame(self.music_focus, height=4, width=300, fg_color="#3b82f6", corner_radius=2)
        self.viz_frame.pack(pady=30)

        # --- Bottom Left: Weather ---
        self.weather_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.weather_frame.place(relx=0.0, rely=1.0, anchor="sw")

        self.temp_label = ctk.CTkLabel(self.weather_frame, text="22°C", font=ctk.CTkFont(size=32, weight="bold"))
        self.temp_label.pack(side="left", padx=(0, 10))

        self.weather_info = ctk.CTkFrame(self.weather_frame, fg_color="transparent")
        self.weather_info.pack(side="left")

        self.weather_desc = ctk.CTkLabel(self.weather_info, text="Cloudy", font=ctk.CTkFont(size=14))
        self.weather_desc.pack(anchor="w")

        self.city_label = ctk.CTkLabel(self.weather_info, text="MOCK CITY", font=ctk.CTkFont(size=12, weight="bold"), text_color="#888888")
        self.city_label.pack(anchor="w")

    def update_clock(self):
        now = datetime.now()
        self.clock_label.configure(text=now.strftime("%I:%M %p"))
        self.date_label.configure(text=now.strftime("%A, %b %d"))
        self.after(1000, self.update_clock)

    def update_weather(self):
        data = self.weather_service.get_weather()
        self.temp_label.configure(text=f"{data['temp']}°C")
        self.weather_desc.configure(text=data['description'])
        self.city_label.configure(text=data['city'].upper())
        self.after(600000, self.update_weather)

    def update_music(self):
        data = self.music_service.get_now_playing()
        self.track_label.configure(text=data['track'])
        self.artist_label.configure(text=data['artist'])
        self.album_label.configure(text=data['album'])

        if data.get('image'):
            try:
                response = requests.get(data['image'])
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 400), Image.Resampling.LANCZOS)
                ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 400))
                self.album_art_label.configure(image=ctk_img, text="")
            except Exception: pass

        self.after(5000, self.update_music)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
