import speech_recognition as sr
from bot_function import *
import time

r = sr.Recognizer()
m = sr.Microphone()

print("initialize...")
with m as source: r.adjust_for_ambient_noise(source)

while True:
    time.sleep(1)
    try:
        print("...")
        try:
            with m as source: audio = r.listen(source)
            value = r.recognize_google(audio,language='fr-FR')
            print('Tu dit :',str(value))
            response_bot(value)
        except sr.UnknownValueError:
            print("Reessayer")
            time.sleep(2)
        except sr.RequestError as e:
            print("Erreur service {0}".format(e))
    except KeyboardInterrupt:
        break
