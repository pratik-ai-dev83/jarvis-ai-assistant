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
