import datetime
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser as web
import keyboard as kb
import math
from selenium import webdriver as wb
from bs4 import BeautifulSoup
import requests
import pywhatkit as kit
from PyDictionary import PyDictionary as dictionary
import pandas as pd
import pprint
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 5 and hour < 12):
        speak('Good Morning sir')
        speak('My name is Jarvis and I am your personal AI assistant')

    elif (hour >= 12 and hour < 12):
        speak('Good Afternoon sir')
        speak('My name is Jarvis and I am your personal AI assistant')

    else:
        speak('Good Evening sir')
        speak('My name is Jarvis and I am your personal AI assistant.How may I help you')


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')
        speak('On it sir')
        print("User said: ", query)

    except Exception as e:
        print(e)

        # speak('Say that again please')
        return "None"
    return query


def dow(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayNumber = date.weekday()
    return days[dayNumber]



def send_whatsapp_message():
    speak('to whom shall I send this message')
    name = listen()
    x = name.title()
    print(x)


    #Add the path of your csv file of contacts which you can export from Google Contacts
    df = pd.read_csv(r"C:\Users\Souparna\PycharmProjects\Voice Controlled AI\contacts.csv")

    df2 = df[['Name', 'Phone 1 - Value']]

    # print(df2.head())

    df3 = df2[(df['Name']) == x]
    number = df3['Phone 1 - Value'].values[0]
    print(number)

    minutes = datetime.datetime.now().minute
    hour =  datetime.datetime.now().hour

    speak('What is your message')
    message1=listen()
    message=message1.capitalize()

    kit.sendwhatmsg(f'+91{number}', message, hour, minutes+2)


if __name__ == '__main__':
    # wishMe()

    while True:
        query = listen().lower()

        # Execute tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Finds the meaning

        elif 'meaning' in query:
            query = query.replace('meaning', " ")
            speak(f"Searching for {query} on Google")
            # web.open_new(f"https://www.google.com/search?q={query}+meaning")

            meaning = dictionary.meaning(f"{query}")
            print(meaning)
            speak(''.join(meaning['Noun'] or ''.join(meaning['Verb'] or ''.join(meaning['Adjective']))))


        elif 'google' in query:
            query = query.replace('google', " ")
            speak(f"Searching for {query} on Google")
            web.open_new(f"https://www.google.com/search?q={query}")

        elif 'youtube' in query:
            query = query.replace('youtube', " ")
            speak(f"Searching for {query} on Youtube")
            kit.playonyt(query)

        elif 'pause' in query:
            kb.press("space")

        elif 'play' in query:
            kb.press("space")

        elif 'time' in query:
            curr_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {curr_time}")

        elif "today's date" in query:
            date = datetime.datetime.now().date()
            speak(f"Today''s date is {date}")

        elif "what day is it today" in query:
            speak(f"It's {dow(datetime.datetime.now().date())} today")

        elif 'next' in query:
            kb.press("right")

        elif 'back' in query:
            kb.press("left");

        elif 'escape' in query:
            kb.press('escape')

        elif 'stop' in query:
            speak("I don't feel so good,Mr.Stark")
            break

        elif 'tan' in query:
            query = query.replace('tan', "")
            print("{0:.3f}".format((math.tan(math.radians(int(query))))))
            speak("{0:.3f}".format((math.tan(math.radians(int(query))))))

        elif 'message' in query:
            send_whatsapp_message()

        elif 'tell me a joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)

