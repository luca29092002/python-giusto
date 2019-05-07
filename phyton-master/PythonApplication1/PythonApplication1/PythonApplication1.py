import webbrowser 
import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("parla")
    audio = r.listen(source)
    testo = r.recognize_google(audio, language="it-IT")
    print("trascrizione: " + testo)
    if( testo =="Apri Google"):
        webbrowser.open("https://google.com")
