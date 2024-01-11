import requests
import json
import geocoder

API_KEY = "2d169e7f16ac893dfa038834efc222a3"

def get_current_weather(latitude, longitude):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        return data
    else:
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

def main():
    location = get_current_location()
    if location:
        weather_data = get_current_weather(location[0], location[1])
        if weather_data:
            current_temperature = weather_data["main"]["temp"]
            current_weather_description = weather_data["weather"][0]["description"]

            print(f"Current temperature in {location[0]}, {location[1]}: {current_temperature:.2f}°C")
            print(f"Current weather condition: {current_weather_description}")
        else:
            print("Error fetching weather data.")
    else:
        print("Unable to determine current location. Please check your internet connection.")

if __name__ == "__main__":
    main()
