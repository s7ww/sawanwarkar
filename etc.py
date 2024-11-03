# etc.py
import requests


def get_weather():
    api_key = "ec5ddfcfd7431a3062ff72a8113b5d8c"  # Replace with your actual OpenWeather API key
    city = "gulbarga"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error: {err}")

    # Return None values in case of an error
    return None, None


get_weather()