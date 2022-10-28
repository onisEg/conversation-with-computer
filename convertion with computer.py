
import sys
import speech_recognition as sr
rec  = sr.Recognizer()

with sr.Microphone() as src:
    while True:
        print("say something.....")
        audio = rec.listen(src)
        text = rec.recognize_google(audio)
        
        if text in ["hello", "hi"]:
            print("hi, who are you ?")
        elif text in ["i am fine", "i am good", "good", "fine"]:
            print("nice to meet you")
        elif text in "close":
            sys.exit()
        else:
            print("i don't understand you")
