import speech_recognition as sr
recognizer = sr.Recognizer() # crrated an recogniser instance

run = True
while run:                                              

    try:
        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio).lower()
            print(f'Recognized --> {text}')
            if 'false' in text or 'exit' in text:
                run = False

    except sr.UnknownValueError:
        print("Voice not recogniced")
        print('Try again sir')
        recognizer = sr.Recognizer()
        continue





