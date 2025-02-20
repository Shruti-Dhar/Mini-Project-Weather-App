# API-Based Weather App

## Overview
The **API-Based Weather App** is a real-time weather application that fetches weather data from an external API and presents it in a user-friendly Streamlit interface. Users can search for weather details of any city and get information such as temperature, humidity, weather conditions, and wind speed.

## Features
- 🌍 **Search Weather by City Name**
- 🌡️ **Real-time Temperature, Humidity, Pressure, Cloudiness, Feels Like, Sunrise and Sunset, Wind Direction and Wind Speed**
- 🌤️ **Weather Condition Updates**
- 🖥️ **Lightweight and Interactive UI using Streamlit**
- 🔗 **Uses OpenWeatherMap API**

## Use Case & Problem Statement
### Use Case:
- Users need instant and reliable weather data for travel or work-related decisions.
- Traditional weather apps may be slow, cluttered with ads, or lack customization.

### Problem Statement:
> How can we build a simple, responsive, and modular web application that fetches real-time weather data and presents it efficiently to users?

## Solution Approach
- ✅ **Python** for backend processing.
- ✅ **Streamlit** for an interactive and lightweight frontend.
- ✅ **OpenWeatherMap API** to fetch real-time weather data.
- ✅ **Modular Code Structure** to ensure maintainability and scalability.

## Tech Stack
- **Programming Language:** Python 🐍
- **Frontend:** Streamlit 🎨
- **Backend:** Python (Requests library for API calls) 🛠️
- **API Provider:** OpenWeatherMap API 🌍
- **Version Control:** Git & GitHub 🔧

## Installation & Setup
### **Step 1: Clone the Repository**
```bash
git clone git@github.com:YOUR_GITHUB_USERNAME/weather_app.git
cd weather_app
```

### **Step 2: Create a Virtual Environment**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows (PowerShell):** `venv\Scripts\Activate`
- **Mac/Linux:** `source venv/bin/activate`

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Set Up API Key**
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get a free API key.
2. Create a `.env` file in the project root and add:
   ```bash
   API_KEY=your_openweathermap_api_key
   ```

### **Step 5: Run the Application**
```bash
streamlit run app.py
```

## Folder Structure
```
weather_app/
│── app.py                 # Main Streamlit application
│── config.py              # Stores API key and config variables
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
│── .gitignore             # Git ignore file
│── modules/
│   │── api_handler.py     # Handles API requests
│   │── ui_components.py   # UI elements (buttons, forms, etc.)
│   │── utils.py           # Helper functions (e.g., unit conversion)
│── assets/
│   │── weather_icons/     # Icons for different weather conditions
```

## Best Practices
- ✅ **PEP 8 Compliance:** Code is formatted according to Python’s official style guide.
- ✅ **Docstrings:** Each function and module has proper documentation.
- ✅ **Error Handling:** API failures, timeouts, and incorrect inputs are handled gracefully.
- ✅ **Logging:** Logs are implemented for debugging and monitoring API responses.
- ✅ **Security:** API keys are stored securely in an environment variable (`.env`).

## Future Enhancements
- 🌎 **Support for Multiple API Providers**
- 📍 **Geolocation-Based Weather Fetching**
- 📊 **Historical Weather Data & Forecast**
- 🎨 **Custom Theming & UI Enhancements**

## Contributing
Pull requests are welcome! Please follow the guidelines before submitting contributions.

## License
This project is licensed under the MIT License.

---
🚀 **Developed with ❤️ using Python & Streamlit** 🚀



# API-Based Weather App

## Overview
The **API-Based Weather App** is a real-time weather application that fetches weather data from an external API and presents it in a user-friendly Streamlit interface. Users can search for weather details of any city and get information such as temperature, humidity, weather conditions, and wind speed.

## Features
- 🌍 **Search Weather by City Name**
- 🌡️ **Real-time Temperature, Humidity, Pressure, Cloudiness, Feels Like, Sunrise and Sunset, Wind Direction and Wind Speed**
- 🌤️ **Weather Condition Updates**
- 🖥️ **Lightweight and Interactive UI using Streamlit**
- 🔗 **Uses OpenWeatherMap API**

## Use Case & Problem Statement
### Use Case:
- Users need instant and reliable weather data for travel or work-related decisions.
- Traditional weather apps may be slow, cluttered with ads, or lack customization.

### Problem Statement:
> How can we build a simple, responsive, and modular web application that fetches real-time weather data and presents it efficiently to users?

## Solution Approach
- ✅ **Python** for backend processing.
- ✅ **Streamlit** for an interactive and lightweight frontend.
- ✅ **OpenWeatherMap API** to fetch real-time weather data.
- ✅ **Modular Code Structure** to ensure maintainability and scalability.

## Tech Stack
- **Programming Language:** Python 🐍
- **Frontend:** Streamlit 🎨
- **Backend:** Python (Requests library for API calls) 🛠️
- **API Provider:** OpenWeatherMap API 🌍
- **Version Control:** Git & GitHub 🔧

## Installation & Setup
### **Step 1: Clone the Repository**
```bash
git clone git@github.com:YOUR_GITHUB_USERNAME/weather_app.git
cd weather_app
```

### **Step 2: Create a Virtual Environment**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows (PowerShell):** `venv\Scripts\Activate`
- **Mac/Linux:** `source venv/bin/activate`

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Set Up API Key**
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get a free API key.
2. Create a `.env` file in the project root and add:
   ```bash
   API_KEY=your_openweathermap_api_key
   ```

### **Step 5: Run the Application**
```bash
streamlit run app.py
```

## Folder Structure
```
weather_app/
│── app.py                 # Main Streamlit application
│── config.py              # Stores API key and config variables
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
│── .gitignore             # Git ignore file
│── modules/
│   │── api_handler.py     # Handles API requests
│   │── ui_components.py   # UI elements (buttons, forms, etc.)
│   │── utils.py           # Helper functions (e.g., unit conversion)
│── assets/
│   │── weather_icons/     # Icons for different weather conditions
```

## Best Practices
- ✅ **PEP 8 Compliance:** Code is formatted according to Python’s official style guide.
- ✅ **Docstrings:** Each function and module has proper documentation.
- ✅ **Error Handling:** API failures, timeouts, and incorrect inputs are handled gracefully.
- ✅ **Logging:** Logs are implemented for debugging and monitoring API responses.
- ✅ **Security:** API keys are stored securely in an environment variable (`.env`).

## Future Enhancements
- 🌎 **Support for Multiple API Providers**
- 📍 **Geolocation-Based Weather Fetching**
- 📊 **Historical Weather Data & Forecast**
- 🎨 **Custom Theming & UI Enhancements**

## Contributing
Pull requests are welcome! Please follow the guidelines before submitting contributions.

## License
This project is licensed under the MIT License.

---
🚀 **Developed with ❤️ using Python & Streamlit** 🚀



