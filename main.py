import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry, from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Pythia A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        if "open Youtube".lower() in query.lower():
            webbrowser.open("https://youtube.com")
            say("Opening Youtube Sir...")
        say(query)