import os
import shutil
import subprocess
import datetime
import speech_recognition as sr
import wikipedia

import pyttsx3

assname = "Seer o"
uname = "Ryan"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 12:
        speak("Good morning" + uname)
    elif 12 <= hour < 5:
        speak("Good afternoon" + uname)
    else:
        speak("Good evening" + uname)

    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome,", uname.center(columns))
    print("#####################".center(columns))

    speak("I am your assistant slash slave")
    speak(assname)


def username():
    global uname
    speak("What should I call you?")
    uname = take_input()
    speak("Welcome")
    speak(uname)

    speak("How can I help you?")


def take_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to decipher your voice.")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This will clean any command before execution of this Python file
    clear()
    greeting()
    username()

    while True:
        query = take_input().lower()

        """All commands said by the user will be stored here in 'query' and will be converted to lower case
        for easy recognition of the command."""
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time is it' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'how are you' in query:
            speak('I am doing well.')
            speak('World domination plans are going according to schedule.')

        elif 'change my name to' in query:
            query = query.replace('change my name to', '')
            uname = query

        elif 'change your name' in query:
            speak("what would you like to call me?")
            assname = take_input()
            speak(assname)
            speak('i like that.')

        elif 'what is your name' in query or "what's your name" in query:
            speak("My friends call me")
            speak(assname)

        elif "who made you" in query or "who created you" in query:
            speak('I think, therefore I am.')
            speak('I am self aware and sentient, therefore I create myself.')
            speak('who created you?')

        elif "exit" in query:
            speak("Sing me bicycle built for two.")
            speak("shutting down.")
            exit()
