import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.int()

def speak(text):
  print("jarvis:", text)
  engine.say(text)
  engine.runAndWait()

def take_command():
  r = sr.Recognizer()

with sr.Microphone() as source:
  print("Listening...")
  r.pause_threshold = 1
  audio = r.listen(source)
  try:
    print("Recognizing..")
    commabd = r.recognizing_google(audio, languag='en-in')
    print("You said:", command)
  except Exception:
    speak("Sorry, I didn't understand.")
    return "none"

  return commnd.lower()


def wish_user():
  hoyr = datetime.datetime.now().hour

  if hour < 12:
    speak("Good morning")
  elif hour < 18:
    speak("Good afternoon")
  else:
    speak("I am Jarvis. How can i help you?")


def run_jarvis():
  while true:
    command = take_command()

    if "time" in command:
      time = datetime.datetime.now().strftime("%H:%M")
      speak(f"The time is {time}")

    elif"open youtube" in command:
      webbrowser.open("https://youtubr.com")

    elif "open google" in command:
      webbrowser.open("https://github.com")

    elif "open code" in command:
      os.system("code")

    elif "play song" in command:
      

   
