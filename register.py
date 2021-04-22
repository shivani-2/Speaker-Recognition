import pyaudio
import wave
import os
from train_models import check_speaker

name = input("Enter your name:")
for count in range(10):
    print("Say the number ", count)
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3

    # WAVE_OUTPUT_FILENAME = "9_mau_1.wav"
 
    audio = pyaudio.PyAudio()

    #path where training speakers will be saved
    # dest = "dataset\\mau\\"
 
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
    # print (isdir)

    if not isdir:
        # Parent Directory path
        parent_dir = "dataset_train\\"
  
        # Path
        path = os.path.join(parent_dir, name)
  
        os.makedirs(path)

    OUTPUT_FILENAME = str(count) + "_" + name + "_1.wav"
    WAVE_OUTPUT_FILENAME=os.path.join(dest,OUTPUT_FILENAME)

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()