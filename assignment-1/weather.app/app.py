import random

city = input("Enter the name of a city to check the weather: ")

weather_list = ["Sunny", "Rainy", "Cloudy", "Windy", "Stormy", "Clear sky"]


temperature_list = [22, 28, 31, 34, 26, 19, 37]

weather = random.choice(weather_list)
temp = random.choice(temperature_list)

print("\n📍 City:", city.title())
print(f"🌤️ Weather: {weather}")
print(f"🌡️ Temperature: {temp}°C")
