from ui.dashboard import Dashboard
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env if present
    load_dotenv()

    # Initialize and run the dashboard
    app = Dashboard()

    # In a headless environment, mainloop might fail if display is not found.
    # But for implementation, this is the standard way.
    try:
        app.mainloop()
    except Exception as e:
        print(f"Application terminated: {e}")

if __name__ == "__main__":
    main()
