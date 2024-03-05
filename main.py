import speech_recognition as sr
import os
import webbrowser
import datetime
import openai

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry, from Pythia"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Pythia A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],
                 ["wikipedia", "https://www.wikipedia.com"],
                 ["Google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "/Users/aashifansari/PycharmProjects/PythiaAI/holding-on-136343.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            musicPath = "/Users/aashifansari/PycharmProjects/PythiaAI/holding-on-136343.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"sir the time is {strfTime}")

        if "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")



        # say(query)