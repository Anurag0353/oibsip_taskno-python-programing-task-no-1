import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter city or ZIP code: ")
    get_weather(api_key, location)
