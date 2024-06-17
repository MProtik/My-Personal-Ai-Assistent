import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id) # index 1-> female voice and index 0-> male voice

rate = engine.getProperty('rate') # getting details of current rate
engine.setProperty('rate', 150) #set the speaking speed

engine.say('I am here at you service. Sir')
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak('I am pai')
    speak('At your service')
