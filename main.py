import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from AppOpener import open
from pynput.keyboard import Key, Controller

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning!")
    elif hour >= 12 and hour < 18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    
    assname = "Baki"
    
    say("Hi")
    say("I am your assistant")
    say(assname)

def takeCommand(t = 1, d = 0.5):
    r = sr.Recognizer()
    
    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise with a longer duration
        print("Calibrated for ambient noise")
        r.pause_threshold = t  # Shorten pause threshold to reduce waiting time after speech
        r.non_speaking_duration = d  # Reduce the duration considered as non-speaking
        
        audio = r.listen(source)
        print("Stopped listening...")
        
    try:
        print("Recognizing with Google Web Speech API...")
        query = r.recognize_google(audio, language='en-US')
        print(f"Google Web Speech API recognized: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
def username():
    say("What should I call you sir")
    uname = takeCommand(0.5, 0.3)
    say(f"Welcome {uname}")
    columns = shutil.get_terminal_size().columns
    try:
        print("#####################".center(columns))
        print("Welcome Mr.", uname.center(columns))
        print("#####################".center(columns))
    except:
        print("NONE")
    say(f"How can i Help you {uname}")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    
    clear()
    wishMe()
    username()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            say('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            SearchResults = wikipedia.summary(query, sentences = 3)
            say("According to Wikipedia")
            print(SearchResults)
            say(SearchResults)
            
        elif 'open youtube' in query:
            say("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'play music' in query or 'play song' in query:
            say("Playing some music")
            open('spotify')
            time.sleep(5)
            keyboard = Controller()
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            say(f"The time now is {strTime}")
        elif 'open chrome' in query:
            open("google chrome")
        elif 'how are you' in query:
            say("I am fine, Thank you for asking")
            say("How are you doing")
        elif "Change your name to" in query:
            query = query.replace("Change your name to", "")
            assname = query
        elif "what is your name" in query:
            say("My name is")
            say(assname)
        elif 'exit' in query:
            say(assname)
            say("OUT")
            say("BYE")
        elif "joke" in query:
            say(pyjokes.get_joke())
        elif "calculate" in query: 
             
            app_id = "KJLTKY-4KH2LUU3K5"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            say("The answer is " + answer) 
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query)
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query)
        elif 'is love' in query:
            say("It is 7th sense that destroy all other senses")
        elif 'lock window' in query:
                say("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                say("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            say("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            say("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            say("User asked to Locate")
            say(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")  
        