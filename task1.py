import speech_recognition as sr
import requests
import nltk
import pyttsx3
from nltk.tokenize import  word_tokenize


def speak(yourtext):
    engine=pyttsx3.init()
    engine.say(yourtext)
    engine.runAndWait()
x="hello iam your voice assistant.how can i help you"
speak(x)

audio_text="Speak Clearly"
def listen():
    r = sr.Recognizer()
   
    with sr.Microphone() as source: 
       global audio_text
       audio_text = r.listen(source)
       try:
            audio_text=r.recognize_google(audio_text)
       except:
           audio_text="Sorry, I did not get that"
listen()
tokens=""
def token(audio_text):
    global tokens 
    tokens=word_tokenize(audio_text)
token(audio_text)
def get_weather(location):
    api_key = 'a4966fd48dc501c8b10601f2ab192271'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        z=f"Current weather in {location}: {description}, Temperature: {temperature} kelvins"
        print(z)
        speak(z)
    else:
       speak("weather details not found") 

if  "weather" in tokens:
    speak("tell your city name for weather details")
    listen()
    city=audio_text
    get_weather(city)
elif audio_text=="Sorry, I did not get that":
    speak("Sorry ,I did not get that")
else:
    speak("I can only help to find out weather deatails")
    


