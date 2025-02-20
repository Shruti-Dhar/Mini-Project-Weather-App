import requests
from config import API_KEY

def get_weather_data(city: str):
    """
    Fetch weather data for the given city from OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        if data["cod"] != 200:
            return None

        # Extracting data and organizing it into a dictionary
        weather_data = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],  # Atmospheric pressure
            "cloudiness": data["clouds"]["all"],  # Cloud cover percentage
            "sunrise": data["sys"]["sunrise"],  # Sunrise timestamp
            "sunset": data["sys"]["sunset"],  # Sunset timestamp
            "feels_like": data["main"]["feels_like"],  # "Feels like" temperature
            "wind_direction": data["wind"]["deg"],  # Wind direction in degrees
            "icon": data["weather"][0]["icon"],  # Weather icon ID
        }

        # Converting sunrise and sunset timestamps to human-readable format (optional)
        from datetime import datetime
        
        weather_data["sunrise"] = datetime.utcfromtimestamp(weather_data["sunrise"]).strftime('%H:%M:%S')
        weather_data["sunset"] = datetime.utcfromtimestamp(weather_data["sunset"]).strftime('%H:%M:%S')

        return weather_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
