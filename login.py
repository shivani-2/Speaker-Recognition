import pyaudio
import wave
import speech_recognition as sr
import random
from test_speaker import check_speaker

name = input("Enter your Name: ")
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "test_" + name + "_7.wav"
 
audio = pyaudio.PyAudio()

#path where training speakers will be saved
dest = "dataset_test\\"

import random
number = random.randint(1000,9999)
print(number)

 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(dest + WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Can we hear it once more:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")


text = int(text)

# print(check_speaker())

if (number == text):
    speaker = check_speaker()
    print("You have been detected as ", speaker)
else:
    print("Please try again")