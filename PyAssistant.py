import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
vocal = engine.getProperty('voices')
#print(vocal[1].id)
engine.setProperty('voice', vocal[1].id)


def startspeak(audio):
    engine.say(audio)
    engine.runAndWait()

def salutation():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        startspeak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        startspeak("Good Afternoon!!")
    else:
        startspeak("Good Evening!!")
    startspeak("I am your Personal Assistant, How May I help You?")

def takespeech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing Your Speech......")
        query = recognizer.recognize_google(audio, language = 'en-in')
        print(f"User Said:  {query}\n")

    except Exception as e:
        print(e)
        print("Say That Again Please.....")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderemailaddress", "senderaccountpassword")
    server.sendmail("receiveremailaddress", to, content)
    server.close()

if __name__ == "__main__":
    salutation()
    while True:
        query = takespeech().lower()
        
        if "wikipedia" in query:
            startspeak("Searching Wikipedia......")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            startspeak("According to the information provided by wikipedia")
            print(results)
            startspeak(results)

        elif "open youtube" in query:
            startspeak("Opening YouTube!!")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            startspeak("Opening Google!!")
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            startspeak("Opening Stackoverflow!!")
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music = "C:\\Users\\Pankaj Sharma\\Music\\My Card\\My Music"
            listing = os.listdir(music)
            print(listing)
            startspeak("Playing Music!!")
            os.startfile(os.path.join(music, listing[0]))

        elif "time" in query:
            presenttime = datetime.datetime.now().strftime("%H:%M:%S")
            startspeak(f"The Time is {presenttime}")

        elif "open code" in query:
            path = "C:\\Users\\Pankaj Sharma\\Anaconda3\\Scripts\\spyder-script.py"
            os.startfile(path)

        elif "send email" in query:
            try:
                startspeak("What should I send in email")
                content = takespeech()
                to = "receiveremailaddress"
                sendEmail(to, content)
                startspeak("Email has been sent!!")

            except Exception as e:
                print(e)
                startspeak("Sorry!! The E-mail can't be send")

        elif "quit" in query:
            exit()
