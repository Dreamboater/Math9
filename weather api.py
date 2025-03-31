import requests


# Function to get weather data
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},ON,CA&appid={api_key}&units=metric"
    response = requests.get(url)

    # If the request was successful
    if True:
        data = response.json()
        #print(data)
        # Extract relevant data
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the weather information
        print(f"Weather for {city_name}, Ontario:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Sorry, couldn't fetch the weather. Please check the city name or try again later.")


# Main program
def main():
    # Your OpenWeatherMap API key
    api_key = '355fe9f6bca042f320bbbb9689a55be3'  # Replace with your own API key

    # Get city name from user
    city = input("Enter the city in Ontario, Canada to get the weather forecast: ").strip()

    # Fetch and display the weather
    get_weather(city, api_key)


# Run the program
if __name__ == "__main__":
    main()
