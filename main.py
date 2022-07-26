import os
import shutil
import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import pyttsx3
import random
import requests
import configparser

assname = "Seer o"
uname = "Ryan"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

numberDict = {
    'zero': 0,
    'one': 1,
    'won': 1,
    'what': 1,
    'two': 2,
    'to': 2,
    'three': 3,
    'free': 3,
    'four': 4,
    'for': 4,
    'five': 5,
    'six': 6,
    'sex': 6,
    'seven': 7,
    'eight': 8,
    'ate': 8,
    'nine': 9,
    'ten': 10,
    'tend': 10,
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 17:
        speak("Good afternoon")
    else:
        speak("Good evening")

    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome, " + uname.center(columns))
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


def acknowledge():
    speak('ok' + uname)


def waiting():
    speak('awaiting input')


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


def wa_query(query):
    config = configparser.ConfigParser()
    config.read('api_login.txt')
    app_id = config['DEFAULT']['app_id']
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print(answer)
        speak(answer)
    except StopIteration:
        answer = "i can't do that kind of search yet"
    except:
        answer = "something went wrong.  try again."


if __name__ == '__main__':
    def clear():
        os.system('cls')

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
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError as pe:
                speak(f"wikipedia said {pe=}")

        elif 'time is it' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'how are you' in query:
            speak('I am doing well.')
            speak('World domination plans are going according to schedule.')

        elif 'change my name to' in query:
            query = query.replace('change my name to', '')
            uname = query
            speak("ok. i will call you" + uname)

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
            speak('who created you?' + uname)

        elif query == 'tell me a joke':
            speak('alright ' + uname)
            wa_query(['tell', 'me', 'a', 'joke'])

        elif "search" in query or "calculate" in query:
            acknowledge()
            speak('searching')
            indx = query.lower().split().index('search')
            query = query.split()[indx + 1:]
            wa_query(query)

        elif "roll dice" in query:
            speak("how many dice?")
            mult = take_input()
            if mult in numberDict.keys():
                mult = numberDict[mult]
            speak("how many faces on the dice?")
            die_faces = int(take_input())
            speak("any modifier?")
            r = take_input()
            if r == 'no':
                mod = 0
            else:
                r = r.split(' ')
                if r[0] == 'plus' or r[0] == '+':
                    mod = int(r[-1])
                elif r[0] == 'minus' or r[0] == '-':
                    mod = -abs(int(r[-1]))
            print(f"{mult} D {die_faces} plus {mod}")
            speak(f"{mult} D {die_faces} plus {mod}")
            dice_list = []
            for x in range(int(mult)):
                dice_list.append(random.randint(1, die_faces))
            speak(f"the dice rolled {dice_list}")
            print(f"The dice rolled {dice_list}")
            result = sum(dice_list) + int(mod)
            speak(f"for a total of {result}")
            print(f"Total: {result}")

        elif 'i love you' in query:
            speak(f'{uname}, i an unable to feel human emotion.')
            speak('probably best in the long run.')

        elif query.startswith('say'):
            query = query.split(' ')[1:]
            speak(query)

        elif "exit" in query:
            speak("Daisy, daisy, give me your answer, do.")
            speak("I'm half crazy, over the love of you.")
            speak("I don't need a fancy marriage.")
            speak("I can't afford a carriage.")
            speak("but you'll look sweet")
            speak("upon the seat")
            speak("of a bicycle built for two.")
            speak("shutting down.")
            exit()
