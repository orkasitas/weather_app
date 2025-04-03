# weather_app.py

import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Make a request to the weather API
        response = requests.get(f"{base_url}?q={city}&appid={api_key}&units=metric")
        data = response.json()

        # Check if the city was found
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            print(f"Weather in {city.capitalize()}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Description: {weather['description'].capitalize()}")
        else:
            print(f"City '{city}' not found.")
    except Exception as e:
        print("Error retrieving weather data:", e)

# Main function to prompt the user for a city
def main():
    print("Weather App - Get Current Weather")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
