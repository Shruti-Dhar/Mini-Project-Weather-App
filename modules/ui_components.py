import streamlit as st
from datetime import datetime
from modules.api_handler import get_weather_data

def display_weather_info(weather_data):
    """
    Display weather data on Streamlit with built-in icons beside the information.
    """
    if weather_data:
        # Show weather condition with an icon beside it
        condition = weather_data['condition'].capitalize()
        icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
        
        if "clear" in condition.lower():
            st.markdown(f"**Weather Condition**: 🌞 {condition}")
        elif "cloud" in condition.lower():
            st.markdown(f"**Weather Condition**: ☁️ {condition}")
        elif "rain" in condition.lower():
            st.markdown(f"**Weather Condition**: 🌧️ {condition}")
        elif "snow" in condition.lower():
            st.markdown(f"**Weather Condition**: ❄️ {condition}")
        else:
            st.markdown(f"**Weather Condition**: 🌥️ {condition}")
        
        # Display weather icon
        st.image(icon_url, width=50)
        
        # Show temperature with icon beside it
        st.markdown(f"**Temperature**: 🌡️ {weather_data['temperature']}°C")
        
        # Show humidity with icon beside it
        st.markdown(f"**Humidity**: 💧 {weather_data['humidity']}%")
        
        # Show wind speed with icon beside it
        st.markdown(f"**Wind Speed**: 🌬️ {weather_data['wind_speed']} m/s")
        
        # Show pressure with icon beside it
        st.markdown(f"**Pressure**: 🏋️‍♂️ {weather_data['pressure']} hPa")
        
        # Show cloudiness with icon beside it
        st.markdown(f"**Cloudiness**: ☁️ {weather_data['cloudiness']}%")
        
        # Show feels-like temperature with icon beside it
        st.markdown(f"**Feels Like**: 🥶 {weather_data['feels_like']}°C")
        
        # Show wind direction (if available) with icon beside it
        st.markdown(f"**Wind Direction**: 🧭 {weather_data['wind_direction']}°")
        
        # Show sunrise and sunset times
        st.markdown(f"**Sunrise**: 🌅 {weather_data['sunrise']}")
        st.markdown(f"**Sunset**: 🌇 {weather_data['sunset']}")
        
    else:
        st.error("City not found or invalid input.")


def city_input():
    """
    Create a text input for the user to enter a city name.
    """
    city = st.text_input("Enter a city name:", key="city_input")
    return city

st.title("Weather App")

city = city_input()

if city:
    weather_data = get_weather_data(city)
    display_weather_info(weather_data)