import requests
import os
import sys

def get_weather(city):
    # Use environment variable for API key
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: OPENWEATHER_API_KEY environment variable not set."
    
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        return "Error fetching weather data."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weathercli.py <city name>")
    else:
        city = ' '.join(sys.argv[1:])
        print(get_weather(city))
