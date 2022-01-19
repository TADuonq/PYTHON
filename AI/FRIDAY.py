import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
import datetime

Friday = pyttsx3.init()
voice = Friday.getProperty('voices')
Friday.setProperty('voice', voice[2].id)

def speak(audio):
    print("F.R.I.D.A.Y. : " + audio)
    Friday.say(audio)
    Friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour 
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening Sir")  
    speak("How can i help you?") 
 
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language= 'en')
        print("T.O.N.Y S.T.A.R.K: " + query)
    except sr.UnknownValueError:
        print("Please repeat or tying the command")
        query = str(input('Your oder is:'))
    return query
if __name__ == "__main__":
    welcome() 
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak("Here is your {search} on Google")
        if "youtube" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak("Here is your {search} on Youtube")
        elif "audio" in query:
            meme = r"D:\Video\meme.mp4"
            os.startfile(meme)
        elif "zalo" in query:
            Zalo = r"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zalo"
            os.startfile(Zalo)
        elif "music" in query:
            music = r"D:\Music\lạ lùng.mp3"
            os.startfile(music)
        elif "quit" in query:
            speak("Friday is quitting sir. Goodbye Boss")
            quit()
            