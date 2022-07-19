import datetime

import pyttsx3

assname = "Seer o"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 12:
        speak("Good morning, Ryan")
    elif 12 <= hour < 5:
        speak("Good afternoon, Ryan")
    else:
        speak("Good evening, Ryan")

    speak("I am your assistant slash slave")
    speak(assname)
