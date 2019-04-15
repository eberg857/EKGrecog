# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 05:20:42 2019

@author: Eduardo Berg
"""

#import wfdb
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import scipy.io
import os
import json
import scipy.signal as sig
#import pywt
#import sklearn as sk
#from PIL import Image
import h5py



path = os.path.dirname(os.path.abspath(__file__))





with open("ekg_AAMI_beats.json", 'r') as fp:
    data = json.load(fp)


# bad data to remove in class 0 :
baddata = [43118, 79630, 79684, 79689, 81081, 86802, 88868]


#total samples = 109446 - 7 = 109439
#sample length = 1501
X = np.empty((109439, 1501), dtype=np.uint16)
Y = np.empty((109439,), dtype=np.uint8)
classes = ['4', '3', '2', '1', '0']
classesstr = ['N', 'S', 'V', 'F', 'Q']


totalind = 0
for i in classes:
    for j in range(len(data[i])):
        if i != '0' or j not in baddata:
            x = np.array(data[i][j])
            newx = sig.resample(x, 500)
            freq = np.fft.fft(x - np.mean(x))
            newfreq = sig.resample(abs(freq[:int(len(freq)/2)]), 250)
            newfreq2 = sig.resample(np.angle(freq[:int(len(freq)/2)]), 250)
            convy = sig.resample(np.convolve(x, [1, -1], 'valid'), 500)
            stddev = [np.std(x)]
            featurized = np.concatenate((newx, newfreq, newfreq2, convy, stddev))
            plt.plot(featurized)
            plt.figure()
            X[totalind, :] = featurized.astype(np.float32)
            Y[totalind] = int(i)
            totalind += 1
            break
    break
#f = h5py.File('X.hdf5', 'w')
#f.create_dataset('X', data=X)
#f.close()
#f2 = h5py.File('Y.hdf5', 'w')
#f2.create_dataset('Y', data=Y)
#f2.close()
            
            