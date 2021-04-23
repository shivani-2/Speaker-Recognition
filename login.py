import pyaudio
import wave
import speech_recognition as sr
import random
from test_speaker import check_speaker
import os

name = input("Enter your Name: ")

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
 
audio = pyaudio.PyAudio()

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

OUTPUT_FILENAME="test_" + name + "_1.wav"
WAVE_OUTPUT_FILENAME=os.path.join("dataset_test",OUTPUT_FILENAME)

trainedfilelist = open("testing_file.txt", 'a')
trainedfilelist.write(OUTPUT_FILENAME+"\n")
trainedfilelist.close()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# Digit Recogniton
r = sr.Recognizer()
with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print("You said : {}".format(text))

number = str(number)

# Checking if said number was equal to the random number displayed
if (number == text):
    speaker = check_speaker()
    # print(speaker)
    if not speaker:
        print("Please try again")
    else:
        print("You have been detected as ", speaker)


#Clear the testing_file.txt
file_clean = open("testing_file.txt",'r+')
file_clean.truncate(0)
file_clean.close()

os.remove("dataset_test\\" + OUTPUT_FILENAME)