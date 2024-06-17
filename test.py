weather_descriptions = {
    "Clear Conditions": ["Clear sky"],
    "Cloudy Conditions": ["Few clouds", "Scattered clouds", "Broken clouds", "Overcast clouds"],
    "Atmospheric Conditions": ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand, dust whirls", 
                               "Dust, low visibility", "Sand"],
    "Poor Visibility Conditions": ["Haze", "Dust, low visibility"],
    "Windy Conditions": ["Squalls", "Tornado"],
    "Rain Conditions": ["Light rain showers", "Moderate rain showers", "Heavy rain showers",
                        "Light rain", "Moderate rain", "Heavy rain", "Thunderstorm with light rain",
                        "Thunderstorm with moderate rain", "Thunderstorm with heavy rain",
                        "Thunderstorm with light drizzle", "Thunderstorm with drizzle",
                        "Thunderstorm with heavy drizzle", "Thunderstorm with Hail",
                        "Light shower sleet", "Shower sleet", "Light rain and snow", "Rain and snow",
                        "Light shower snow", "Shower snow", "Heavy shower snow"],
    "Snow Conditions": ["Light snow showers", "Moderate snow showers", "Heavy snow showers",
                        "Light snow", "Moderate snow", "Heavy snow", "Sleet", "Shower sleet",
                        "Light shower snow", "Shower snow", "Heavy shower snow"]
}

# Example usage:
print(weather_descriptions["Clear Conditions"])
#print(weather_descriptions["Rain Conditions"])

weather = "Light shower sleet"

for i in len(weather_descriptions):
    if weather in weather_descriptions[i]:
        print(i)

# Conditions = ["Few clouds", "Scattered clouds", "Broken clouds", "Overcast clouds"]
# print("Scattered clouds" in weather_descriptions["Cloudy Conditions"])