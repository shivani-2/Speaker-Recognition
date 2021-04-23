# 200 files per speaker, 112 correct, 8 incorrect (120 test data, 20 per speaker) 93.3%
# 100 files per speaker, 114 correct, 6 incorrect (120 test data, 20 per speaker) 95%
# 100 files per speaker, 58 correct, 2 incorrect (60 test data, 10 per speaker) 96.6%
# 50 files per speaker, 58 correct, 2 incorrect (60 test data, 10 per speaker) 96.6%
# 30 files per speaker, 55 correct, 5 incorrect (60 test data, 10 per speaker) 91.667%
# 30 files per speaker, 28 correct, 2 incorrect (30 test data, 5 per speaker) 93.33%

import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

def check_speaker():
    #path to training data
    source   = "dataset_test\\"   

    modelpath = "speaker_models\\"

    test_file = "testing_file.txt"        

    file_paths = open(test_file,'r')


    gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

    #Load the Gaussian gender Models
    models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]

    # correct = 0
    # incorrect = 0

    # Read the test directory and get the list of test audio files 
    for path in file_paths:   
        path = path.strip()   
        # print (path)
        sr,audio = read(source + path)
        vector   = extract_features(audio,sr)
    
        log_likelihood = np.zeros(len(models)) 
    
        for i in range(len(models)):
            gmm    = models[i]         #checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()
    
        winner = np.argmax(log_likelihood)
        detected_speaker = speakers[winner]
        # return detected_speaker
        # print(detected_speaker)
        # print(log_likelihood)
        # print(path.split("_")[1])

        if(path.split("_")[1] == detected_speaker):
            return detected_speaker
    
if __name__ == "__main__":
    print ("Speaker testing")
    # check_speaker()
# print("correct:", correct)
# print("incorrect:", incorrect)