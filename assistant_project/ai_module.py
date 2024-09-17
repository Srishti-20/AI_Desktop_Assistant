# ai_module.py

import requests
from transformers import pipeline
import spacy
import configparser

# Create a config parser object
config = configparser.ConfigParser()

# Read the credentials from the file
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

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def sentiment_analysis(text):
    result = sentiment_analyzer(text)
    return result[0]['label']

# Load question-answering pipeline
question_answerer = pipeline("question-answering")

def advanced_question_answering(question, context):
    result = question_answerer(question=question, context=context)
    return result['answer']

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
