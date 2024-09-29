import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI

r=sr.Recognizer()
engine=pyttsx3.init()
newsapi="50df137402c2432fb680e7541bca98b9"

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
    elif(c.lower().startswith("play")):
        song=c.lower.split(" ")[1]
        link=musiclibrary[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            #Pare the JSON Response
            data=r.json()

            #Extract the Articles
            articles=data.get('articles',[])

            #Print the headlines
            for article in articles:
                speak(article['title'])



if __name__ == "__main__":
    speak("Intialsing Jarvis.........")
    while(True):
        r=sr.recognizer()
  
           #recognise speech using Sphinx
        print("recognising....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognise_google(audio) 
            if(word.lower()=="jarvis") :
                speak("Yes")

                #listen for command

                with sr.Microphone() as source:
                    print("Jarvis Active ...")
                    audio = r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognise_google (audio) 

                    processcommand(command)


        except Exception as e:
            print("Error;{0}".format(e))
