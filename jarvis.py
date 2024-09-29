import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary  # Ensure this module is properly defined or imported
import requests
from openai import OpenAI  # Make sure you have the OpenAI library installed and configured

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "50df137402c2432fb680e7541bca98b9"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # Fixed the method call with parentheses
        link = musiclibrary[song]  # Ensure musiclibrary is a dictionary or adjust as needed
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")  # Use f-string for API key
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("Initializing Jarvis.........")
    while True:
        # r = sr.recognizers()  # This line was incorrect; removed it
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)  # Fixed the method name
            if word.lower() == "jarvis":
                speak("Yes")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active ...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)  # Fixed the method name

                    processcommand(command)

        except Exception as e:
            print("Error: {0}".format(e))
