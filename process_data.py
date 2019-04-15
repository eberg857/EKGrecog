# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 05:20:42 2019

@author: Eduardo Berg
"""

import wfdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import os
import json
import scipy.signal as sig
import pywt
import sklearn as sk
from PIL import Image
import pandas as pd

labels = ['+', 'N', 'A', 'V', '~', '|', 'Q', '/', 'f', 'x', 'F', 'j', 'L', 'a', 'J', 'R', '[', '!', ']', 'E', 'S', '"', 'e']
output=  len(labels)*[0]

beatlabels = ['N', 'L', 'R', 'B', 'A', 'a', 'J', 'S', 'V', 'r', 'F', 'e', 'j', 'n', 'E', '/', 'f', 'Q', '?']
totalbeats = {}
for i in beatlabels:
    totalbeats[i] = []

counter = 0
# MAX IS 2047
maximum = 0
for i in [str(j) for j in range(100, 300)]:
    try:
        data = wfdb.rdrecord(i, channels=[0], physical=False, return_res=16).d_signal
        anno = wfdb.rdann(i, 'atr', return_label_elements=['symbol','label_store', 'description'])

        data = data.flatten()
        samples = []
        symbols = []
        for k in range(len(anno.sample)):
            if anno.symbol[k] in beatlabels:
                samples.append(anno.sample[k])
                symbols.append(anno.symbol[k])
        plt.plot(data[:1000])
        plt.savefig("heartbeats.png")
        plt.figure()
        plt.plot(np.convolve(data[:1000], [1, -1], mode='valid'))
        plt.savefig("diff.png")
#        for k in range(len(samples)-1):
#            totalbeats[symbols[k]].append((data[samples[k]:samples[k+1]]).tolist())
        break

    except:
        continue
#
#with open('ekg_fullbeats_data.json', 'w') as fp:
#    json.dump(totalbeats, fp, sort_keys=True, indent=4)

#print(totalbeats['A'])


#cuts= []
#for i in range(len(anno.symbol)):
#    cut1 = 0
#    cut2 = anno.labels
#    if anno.symbol[i] is in beatlabels:
#print(anno.sample[:10])
#print(len(anno.sample))
#print(anno.symbol[:10])
#print(len(anno.symbol))
#print(anno.fs)
#plt.plot(sig[:, 0])
#plt.figure()
#plt.plot(sig[:, 1])
#plt.figure()
#print(sig.shape)