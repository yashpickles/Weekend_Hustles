import requests
import os
import json  

# (patch == v1.6)
def get_weather(city: str) -> str:
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Printing raw JSON
        # print("\n--- RAW API RESPONSE ---")
        # print(json.dumps(data, indent=2))  # Raw Data from the API

        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'City not found')}"
        
        # Extracting all the important data fields
        coord = data["coord"]
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]

        return (
            f"\n--- Weather Summary for {city.title()} ---\n"
            f" Coordinates: {coord}"
            f" Condition: {weather}"
            f" Temperature: {temperature}°C"
            f" Humidity: {humidity}%"
            f" Feels Like: {feels_like} °C"
            f" Wind Speed: {wind_speed} m/s"
        )

    except Exception as e:
        return f"Error: {e}"
