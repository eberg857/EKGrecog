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
#import scipy.signal as sig
#import pywt
#import sklearn as sk
#from PIL import Image

path = os.path.dirname(os.path.abspath(__file__))





with open("ekg_AAMI_beats.json", 'r') as fp:
    data = json.load(fp)


# bad data to remove in class 0 :
baddata = [43118, 79630, 79684, 79689, 81081, 86802, 88868]

classes = ['4', '3', '2', '1', '0']
classesstr = ['N', 'S', 'V', 'F', 'Q']
minlen = 10000
maxlen = 0
counter = 0
total = 0
plt.ioff()
for i in classes:
    os.mkdir(classesstr[int(i)])
    dirpath = path +'\\'+ classesstr[int(i)]
    for j in range(len(data[i])):
        if i != '0' or j not in baddata:
            fig = plt.figure()
            plt.axis('off')
            x = np.array(data[i][j]).astype(np.uint16)
            x = 500*((x - np.min(x))/(np.max(x)-np.min(x))) + 500
            freq = abs(np.fft.fft(x - np.mean(x))).astype(np.uint16)
            freq = 500*(freq/np.max(freq))
            plt.plot(x, 'b')
            plt.plot(freq[0:int(len(freq)/4)].repeat(4, axis=0), 'r')
            fig.savefig(dirpath+'\\'+str(j)+".png",  bbox_inches='tight', pad_inches=0)
            plt.close(fig)


            
            
            