import pyaudio
import wave
import os

name = input("Enter your name: ")
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 4

if __name__ == "__main__":
    
    #create sub folder in test_dataset
    directory = name
    
    # Parent Directory path
    parent_dir = "dataset\\"
    # Path
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    #path where training speakers will be saved
    dest = "dataset\\" + name + "\\"

    for i in range(9):
        WAVE_OUTPUT_FILENAME = "test_" + name + "_" + i + ".wav"
        record(i)

    # call the training models function



def record(i):
    
    # WAVE_OUTPUT_FILENAME = "test_" + name + "_" + i + ".wav"
    print("Say the word: ", i)

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
 
    waveFile = wave.open(dest + WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()