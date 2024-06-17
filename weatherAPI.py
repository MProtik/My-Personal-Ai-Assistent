import requests
import json

def get_current_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        print(weather)
    else:
        print("Failed")

if __name__ == "__main__":
    get_current_weather("Narsingdi", 'aa25dfa89b8526f5bdeffc46c6492a32')