import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    
    speak('I am your assistant sir. Please tell me how may I help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        # print(e)

        print('Say that again pleage...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', '********')
    server.sendmail('abc@gmail.com', to, content)
    server.close()
   


if __name__ == "__main__":
    # speak('Gautam is god boy')
    wishMe()
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'update my job' in query:
            webbrowser.open('naukri.com/myapply/historypage')

        # elif 'play dil ko maine di kasam song':
        #     webbrowser.open('youtube.com/watch?v=w6plBXjxtxw')
        elif 'play music' in query:
            music_dir = 'G:\\Music\\Naina song'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\imgau\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to raj' in query:
            try:
                speak('Wthat should I say ?')
                content = takeCommand()
                to = 'bdjkdh@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry Sir, I am not able to send this email')

    














# import pyttsx3
# engine = pyttsx3.init()
# engine.say('Sally sells seashells by the seashore.')
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
