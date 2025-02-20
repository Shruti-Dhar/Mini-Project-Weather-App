import streamlit as st
import base64
from modules.api_handler import get_weather_data
from modules.ui_components import display_weather_info, city_input

st.title("Weather App")

# Function to Set Background Image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

city = city_input()

if city:
    weather_data = get_weather_data(city)
    display_weather_info(weather_data)

if 'broken clouds' in weather_data['condition'].lower():
    set_background("assets/cloudy.jpg")
elif 'overcast clouds' in weather_data['condition'].lower():
    set_background("assets/cloudy.jpg")
elif 'clear sky' in weather_data['condition'].lower():
    set_background("assets/sun.jpg")
elif 'haze' in weather_data['condition'].lower():
    set_background("assets/rain.jpg")
elif 'snowy' in weather_data['condition'].lower():
    set_background("assets/snow.jpg")
elif 'few clouds' in weather_data['condition'].lower():
    set_background("assets/sun.jpg")