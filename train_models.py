import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM 
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")

def train_model(name):

    #path to training data
    source   = "dataset_train\\" + name + "\\"

    #path where training speakers will be saved
    dest = "speaker_models\\"

    train_file = "training_file.txt"        

    file_paths = open(train_file,'r')

    count = 1

    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for path in file_paths:    
        path = path.strip()   
        print (path)
    
        # read the audio
        sr,audio = read(source + path)
    
        # extract 40 dimensional MFCC & delta MFCC features
        vector = extract_features(audio,sr)
    
        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))
        # when features of 50 files of speaker are concatenated, then do model training
        if count == 10:    
            gmm = GMM(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
            gmm.fit(features)
        
            # dumping the trained gaussian model
            picklefile = path.split("_")[1]+".gmm"
            cPickle.dump(gmm,open(dest + picklefile,'wb'))
            print ("+ modeling completed for speaker:",picklefile," with data point = ",features.shape)
            features = np.asarray(())
            count = 0
        count = count + 1   