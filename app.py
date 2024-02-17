# importing reqquired libraries
from dotenv import load_dotenv
from flask import Flask, request, render_template
import requests
import os

# Loading the environment variables
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.route('/', methods=['GET', 'POST'])

# Rendering the index.html file
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html')

# Getting the weather data from the API
def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
