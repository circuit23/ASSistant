import configparser
import datetime
import pyttsx3
import shutil
import speech_recognition as sr
import wikipedia
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.PageError as pe:
        speak(f"wikipedia said {pe=}")


def greeting(assname, uname):
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
