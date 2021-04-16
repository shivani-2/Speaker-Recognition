import speech_recognition as sr
import random


number = random.randint(1000,9999)
print(number)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")


text = int(text)

if (number == text):
    print("You have been detected")
else:
    print("Please try again")
