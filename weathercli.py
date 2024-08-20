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
        # This would be a good example of leveraging the .get() notation for referencing dot structures. 
        # It provides a good way to error handle and prevent index issues
        # For Example you could do something like this, the .get property provides you a way to specify a specific data type
        # I.e. [] or {} if left blank its None so you could do if not blah: then do x
        # weather_data = data.get('weather', [])
        # if len(weather_data) > 0:
        #     weather_data = weather_data[0]
        #     weather = weather_data.get('description', "No Description")
        #     temperature = weather_data.get('main',{}).get('temp')
        #     humidity = weather_data.get('main', {}).get('humidity')
            
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        # You could experiment with triple quotes for more flexibility in your text outputs i.e.
        # f"""
        # Weather: {weather}
        # Temperature: {temperature}°C
        # Humidity: {humidity}%
        #"""
    else:
        # Its always good to be specific on the error return i.e.
        # return f"Error fetching weather data with error: {response.status_code}"
        return "Error fetching weather data."

if __name__ == "__main__":
    # I would also suggest you take a look at argparse
    #     # Create the argument parser
    # parser = argparse.ArgumentParser(
    #     description="""
    #         CHANGE THIS
    #         """
    #     )

    # parser.add_argument("-u", "--users", required=True, help="A single user, or a comma dileniated list of users, given in the form: whatever.form.your.script.needs")
    # parser.add_argument("-d", "--dry_run", action="store_true", help="Pass this to see what the script will do without actually changing anything")
    
    # args = parser.parse_args()
    # dry_run = args.dry_run

    if len(sys.argv) < 2:
        print("Usage: python weathercli.py <city name>")
    else:
        city = ' '.join(sys.argv[1:])
        print(get_weather(city))
