import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import time
import requests
from google import genai
import sys
# activate virtual env using source .venv/bin/activate

recognizer=sr.Recognizer()
engine=pyttsx3.init()
DEV_MODE = True  # set to False to go full voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(c):
    client = genai.Client(api_key="AIzaSyAizhf6W1MNiXb_xM1cAHBCXnIwBAf329k")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=command)
    print(response.text)
    speak(response.text)
    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/TDS2K5")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        newsapi = '711e1acb230f488598cc19e3001b1558'
        url = (f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            
            for idx, article in enumerate(articles[:5], 1):  #top 5 to keep it short
                print(f"{idx}. {article['title']}")
                speak(f"{idx}. {article['title']}") # CRRL + C to skip articles, repeatedly to terminate program

        else:
            speak(f"[ERROR] Failed to fetch news: {response.status_code}")

    elif "stop program" in c.lower() or "exit" in c.lower() or "goodbye" in c.lower():
        print("Shutting down. Goodbye!")
        speak("Shutting down. Goodbye!")
        sys.exit() # This will terminate the entire script

    else:
        # let ai handle requests
        aiProcess(c)



if __name__=="__main__":
    speak("Initializing Fried Egg....")
    while True:

        # listen for the wake word Fried Egg
        # obtain audio from the mic

        r=sr.Recognizer()
    
        #recognize speech using google
        print("recognizing...")
        try:
            #no if else (for voice mode) :
            #  with sr.Microphone() as source:
            #     print("Listening...")
            #     audio=r.listen(source)
            # word= r.recognize_google(audio)
            if DEV_MODE:
                word = input(">> Wake word: ").lower()
            
            else:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                word = r.recognize_google(audio)

            # for voice mode :
            # if(word.lower()== "fried egg" ) :
            #     speak("ya?")
            #     #Listen for command
            #     with sr.Microphone() as source:
            #         print("Fried Egg active...")
            #         audio=r.listen(source)
            #         command= r.recognize_google(audio)
            if DEV_MODE:
                if(word.lower()== "fried egg" or word.lower() == "fried" or word.lower() == "egg") :
                    speak("yes sir?")
                    print("Fried Egg active...")
                    command = input(">> Command: ")
                    print(command)
                    processCommand(command)
            else:
                with sr.Microphone() as source:
                    print("Fried Egg active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    print(command)
                    processCommand(command)

        except Exception as e:
            print(f"[ERROR] {e}")
            speak("I'm sorry?")

        