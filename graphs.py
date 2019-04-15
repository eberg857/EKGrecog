# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:15:37 2019

@author: Eduardo Berg
"""

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
            plt.plot()
            totalind += 1
