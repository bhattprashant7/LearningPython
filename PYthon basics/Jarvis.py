
from datetime import datetime
import webbrowser
import os 
import pyttsx3
import speech_recognition as sr
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
        print("Jarvis:",text)
        engine.say(text)
        engine.runAndWait()
def listen():
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source,
            timeout=5,phrase_time_limit=5)     #add time limit i.e timeout=5 means wait at most 5 seconds for you to start speaking 
                                                #phrase time limit=5 means record for at most 5 seconds
        try:
            command=recognizer.recognize_google(audio)
            print("YOU:",command)
            return command.lower()
        except:
            print("Jarvis:sorry,I din't understand.")
            return " "
def jarvis():
    speak("Hello! Iam Jarvis")
    while True:
        command=listen()
        if "hello" in command:
              speak("Hello there")
        elif "how are you" in command:
              speak("Iam functioning perfectly")
        elif command.startswith("search"):
            query=command.replace("search","").strip()
            if query:
                 speak(f"searching for {query}")
                 webbrowser.open(f"http://www.google.com/search?q={query}")
            else:
                 speak("what would you like to search for?")
        elif command.startswith("play"):
            query=command.replace("play","").strip()
            if query:
                 speak(f"playing {query}")
                 webbrowser.open(f"http://www.youtube.com/search?search_query={query}")
            else:
                 speak("what would you like to search for?")         

        elif "google" in command:
            speak("Opening Google Wait..")
            webbrowser.open("http://www.google.com")
        elif "youtube" in command:
             speak("opening youtube wait...")
             webbrowser.open("http://www.youtube.com")
        elif "calculator" in command:
            speak("Opening calculator wait...")
            os.system("calc ") 
        elif "time" in command:
            current_time=datetime.now().strftime("%H:%M:%S")  #M=minute
            speak(f"The time is {current_time}")
        elif "date" in command:
            current_date=datetime.now().strftime("%Y-%m-%d")  #m=month 
            speak(f"Today's date is {current_date}") 
        elif "bye" in command:
            speak("good bye")
            break
        else:
             speak("invalid command")
             
jarvis()
    
    
    
   