import speech_recognition as sr
import pyaudio

def voice_rec():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=5)
        print("Listening... ")
        a = rec.listen(source)
        print("Processing...!")

    cmd = rec.recognize_google(a, language = 'en-IN')
    print(cmd)
    return cmd