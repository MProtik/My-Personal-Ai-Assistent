import pyttsx3
import speech_recognition as sr
import datetime
import requests
import webbrowser

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[14].id) #14 is good, 38 is usable

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

#TEXT TO SPEECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 1, phrase_time_limit=5)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said, {query}")
    except:
        speak('say that again please')
        return 'none'
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=5 and hour <=12:
        speak('Good Morning')
    elif hour>12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    #get_weather("Narsingdi")
    speak('THIS IS JARVIS')
    speak("At your service. Tell me how can i help you")
    


# def get_weather(city):
#     api = 'Api key'
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
#     response = requests.get(url)
#     data = response.json()

#     weather_descriptions = {
#     "Clear Conditions": ["Clear sky"],
#     "Cloudy Conditions": ["Few clouds", "Scattered clouds", "Broken clouds", "Overcast clouds"],
#     "Atmospheric Conditions": ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand, dust whirls", 
#                                "Dust, low visibility", "Sand"],
#     "Poor Visibility Conditions": ["Haze", "Dust, low visibility"],
#     "Windy Conditions": ["Squalls", "Tornado"],
#     "Rain Conditions": ["Light rain showers", "Moderate rain showers", "Heavy rain showers",
#                         "Light rain", "Moderate rain", "Heavy rain", "Thunderstorm with light rain",
#                         "Thunderstorm with moderate rain", "Thunderstorm with heavy rain",
#                         "Thunderstorm with light drizzle", "Thunderstorm with drizzle",
#                         "Thunderstorm with heavy drizzle", "Thunderstorm with Hail",
#                         "Light shower sleet", "Shower sleet", "Light rain and snow", "Rain and snow",
#                         "Light shower snow", "Shower snow", "Heavy shower snow"],
#     "Snow Conditions": ["Light snow showers", "Moderate snow showers", "Heavy snow showers",
#                         "Light snow", "Moderate snow", "Heavy snow", "Sleet", "Shower sleet",
#                         "Light shower snow", "Shower snow", "Heavy shower snow"]
# }


#     if response.status_code == 200:
#         weather = data['weather'][0]['description']
#         speak(f'It is {weather} outside')
    
#     else:
#         speak("Couldn't get the weather information sir")

if __name__ == "__main__":
    wish()
    takecommand()
    while True:
        query = takecommand().lower()
        sites = [['youtube', 'https://www.youtube.com/'], ['google', 'https://www.youtube.com/]']]
        for site in sites:
            if f"open {'youtube'}" in query:
                webbrowser.open("https://www.youtube.com/")
                speak('Opening YouTube')
        

        #logic buildind or task
