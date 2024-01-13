from flask import Flask, jsonify, render_template
import requests
import geocoder

app = Flask(__name__)

API_KEY = "2d169e7f16ac893dfa038834efc222a3"

def get_current_weather(latitude, longitude):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    print(f"API Request URL: {url}")  
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"API Response: {response.content.decode()}")
        raise Exception(f"Error fetching weather data: {response.status_code}")

def get_current_location():
    try:
        location = geocoder.ip("me").latlng
        latitude = location[0]
        longitude = location[1]
        return latitude, longitude
    except Exception as e:
        print(f"Error determining current location: {e}")
        return None, None

@app.route('/current_weather')
def current_weather():
    try:
        location = get_current_location()
        if location:
            weather_data = get_current_weather(location[0], location[1])
            if weather_data:
                current_temperature = round(weather_data["main"]["temp"])
                current_weather_description = weather_data["weather"][0]["description"]

                return render_template('weather.html', temperature=current_temperature, weather_description=current_weather_description)
            else:
                error_message = "Error fetching weather data."
        else:
            error_message = "Unable to determine current location. Please check your internet connection."
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"

    return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)