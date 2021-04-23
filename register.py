import pyaudio
import wave
import os
from train_models import train_model
import time

name = input("Enter your name:")


for count in range(10):
    trainedfilelist = open("training_file.txt", 'a')
    OUTPUT_FILENAME = str(count) + "_" + name + "_1.wav"
    trainedfilelist.write(OUTPUT_FILENAME+"\n")
    trainedfilelist.close()

for count in range(10):
    print("Say the number ", count)
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3
 
    audio = pyaudio.PyAudio()
 
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
    
    # Path 
    dest = "dataset_train\\" + name

    # Check whether the specified path is an existing directory or not 
    isdir = os.path.isdir(dest) 

    if not isdir:
        # Parent Directory path
        parent_dir = "dataset_train\\"
  
        # Path
        path = os.path.join(parent_dir, name)
  
        os.makedirs(path)

    print(str(count))

    OUTPUT_FILENAME = str(count) + "_" + name + "_1.wav"
    WAVE_OUTPUT_FILENAME=os.path.join(dest,OUTPUT_FILENAME)

    # trainedfilelist = open("training_file.txt", 'a')
    # trainedfilelist.write(OUTPUT_FILENAME+"\n")

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

# time.sleep(5)

train_model(name)
print("User " + name + " succesfully registered")

file_clean = open("training_file.txt",'r+')
file_clean.truncate(0)
file_clean.close()