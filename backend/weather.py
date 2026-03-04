import requests

# Your secret key
api_key = "ad7559ec9a4073dfa98c6502409e2d8a"

city = input("Enter city name: ")

# The URL to ask for weather
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Fetching the data
response = requests.get(url)
data = response.json()

# Checking if the city exists
if data["cod"] != "404":
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"In {city}, it is currently {temp}°C with {desc}.")
    
    # Wardrobe Logic in Python
    if temp > 25:
        print("Suggestion: Wear a T-shirt!")
    elif temp > 15:
        print("Suggestion: A light hoodie is fine.")
    else:
        print("Suggestion: Wear a heavy coat!")
else:
    print("City not found!")