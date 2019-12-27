import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry! I didn't get it")
        except sr.RequestError:
            print("Sorry! the speech service is down")
        return voice_data


def speak():
    pass


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Rod')
    if 'what time is it' in voice_data:
        print(time.ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = f'https://google.com/search?q={search}'
        webbrowser.get().open(url)
        print(f'Results for {search}')
    if 'location' in voice_data:
        loc = record_audio('What location do you need?')
        url = f'https://google.com/maps/place/{loc}/&amp;'
        webbrowser.get().open(url)
        print(f'Location of {loc}')
    if 'exit' in voice_data:
        exit()


# time.sleep(1)
print('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
