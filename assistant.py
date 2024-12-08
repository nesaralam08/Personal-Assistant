import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import pyaudio

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understand")

sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

speechtx("Hello Guys")

if __name__ == '__main__':
    try:
        data1 = sptext().lower()
        # print(data1)
        if "your name" in data1:
            name = "my name is Zara"
            speechtx(name)
        elif "who are you" in data1:
            speak = '''Hello, I am Zara. Your personal Assistant.
                I am here to make your life easier. You can command me to perform
                various tasks such as calculating sums or opening applications etcetera'''
            speechtx(speak)
        elif "who made you" in data1:
            speak = "I have been created by Nesar Alam."
            speechtx(speak)    
        elif "old are you" in data1:
            age = "I am 20 years old "
            speechtx(age)
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke1)
            speechtx(joke1)
        elif 'open google' in data1:
            speechtx('Opening Google')
            webbrowser.open('google.com')
        elif 'open facebook' in data1:
            speechtx('Opening Facebook')
            webbrowser.open('facebook.com')
        elif 'open linkedin' in data1:
            speechtx('Opening Linkedin')
            webbrowser.open('linkedin.com')
        elif 'open gmail' in data1:
            speechtx('Opening Gmail')
            webbrowser.open('gmail.com')
        elif 'shutdown' in data1:
            speechtx('I am shutting down')
            self.close_window() 
        elif "chrome" in data1:
            speechtx("opening google chrome")
            webbrowser.open('chrome.com')
        else:
            speechtx('I did not understand, can you repeat again')
    except:
        speechtx('Waiting for your response')
