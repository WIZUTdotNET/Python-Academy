import speech_recognition as sr

def callback(recognizer, audio):                          # this is called from the background thread
    try:
        print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)                         # we're still listening even though the main thread is blocked

# 
# while True: 
#     if str(type(audio)) == "audio_data":
#         tresc = r.recognize_google(audio)
#         print(tresc)
        
        
"""
listen version

while True: 
    try:
        with mic as source:
            print("b1 - start")
#             audio = r.listen(source)
            print("b1 - koniec")
            
        tresc = r.recognize_google(audio)
        
    except sr.UnknownValueError as sc:
        print ("No input so far.")
"""


"""
r = sr.Recognizer()
source = sr.AudioFile("eng_m1.wav")
with source as kissmyass: 
    audio = r.record(kissmyass)
    

tresc = r.recognize_google(audio)
print(tresc)
# print(type(audio))
"""

