import pyttsx3 #install this module for AI voices
import datetime
import speech_recognition as sr# install pyaudio first for installing py audio 1. pip install pipwin ,2. pip install pyaudio than pip install speechRecognition
import wikipedia#install
import webbrowser
import os
import random
import smtplib# install this module helps in automating emails

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """greeting function for greating for morning , evening ,afternoon"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("Please tell me how may I aid you?")

def takeCommand():
    """It takes microphone input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    """sending email to a particular mail address. It takes the mail address of receiver and content """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # login details take email which you are using to send the mail from and password
    server.login('harshitkun9@gmail.com', 'xrhpvgwruqenvfzw')
    server.sendmail('harshitkun9@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:#music
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            index = []
            for m in range(len(songs)):
                if songs[m][-3:] == 'mp3':
                    index.append(m)
            r = random.randint(0, len(index))
            os.startfile(os.path.join(music_dir, songs[index[r]]))
            print(songs[index[r]])

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\us\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening VScode ")
            os.startfile(codePath)

        elif 'open battle.net' in query:
            wowPath = "G:\\wow\\World of Warcraft\\World of Warcraft Launcher.exe"
            speak("opening battle.net")
            os.startfile(wowPath)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "harsharma543@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry sir I am not able to send the email")

        elif 'who are you' in query:
            speak('Hello, I am Jim, a voice assistant, programmed by Harshit Sharma')

        elif 'hello jim' in query:
            speak('yes sir')

        elif 'goodbye' in query:
            speak("If you need me call me again")
            quit()