import requests
from transformers import pipeline
import spacy
import configparser

config = configparser.ConfigParser()

config.read('cred.txt')

# Weather functionality
def get_weather(city_name):
    api_key = config.get('DEFAULT','WEATHER_API_KEY')
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] != "404":
            weather_data = data["main"]
            temperature = weather_data["temp"]
            humidity = weather_data["humidity"]
            weather_desc = data["weather"][0]["description"]
            return f"The temperature is {temperature}°C with {weather_desc} and humidity of {humidity}%"
        else:
            return "City Not Found"
    except:
        return "Unable to retrieve weather data at the moment"