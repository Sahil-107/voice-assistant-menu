import pyttsx3
aud = pyttsx3.init()
voices = aud.getProperty('voices')
aud.setProperty('voice', voices[1].id)

rate = aud.getProperty('rate')
aud.setProperty('rate', 120)

def speak(text):
    aud.say(text)
    aud.runAndWait()