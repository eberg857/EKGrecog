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
dirnames = ["1 NSR", "2 APB", "3 AFL", "4 AFIB", "5 SVTA", "6 WPW", "7 PVC", "8 Bigeminy", "9 Trigeminy", "10 VT", 
           "11 IVR", "12 VFL", "13 Fusion", "14 LBBBB", "15 RBBBB", "16 SDHB", "17 PR"]


oldmax = 0
index = 0
#for i in range(len(data['1'])):
#    print(len(data['1'][i]))
#    if len(data['1'][i]) > oldmax:
#
#        index = i
#        oldmax = len(data['1'][i])
#
#test = []   
#print(oldmax)
#print(len(data['1']))
#for i in range(198, 202):
#    test = np.concaten

# MAX height 1000

def ekgtoimage(x, maxamp):
    x = np.array(x)
    output = np.zeros((len(x), maxamp + 1, 3), dtype=np.uint8)
    xtemp = (maxamp*(x / maxamp)).astype(np.uint16)
    freq = abs(np.fft.fft(x - np.mean(x)))
    freqres = (maxamp*(freq/np.max(freq))).astype(np.uint16)
    diff = abs(np.convolve(x, [-1, 1], 'valid'))
    diff = np.concatenate((diff, [np.mean(diff)]))
    diffres = (maxamp*(diff/np.max(diff))).astype(np.uint16)
    for i in range(len(x)):
        output[i, xtemp[i]-2:xtemp[i]+2, 0] = 255
        output[i, freqres[i], 1] = 255
        output[i, diffres[i], 2] = 255
    return output

def ekgtoimage(x):
    x = np.array(x)
    output = np.zeros((len(x), 2070, 3), dtype=np.uint8)
    xtemp = (2048*(x/2048)).astype(np.uint16)
    freq = abs(np.fft.fft(x - np.mean(x)))
    freqres = (2048*(freq/np.max(freq))).astype(np.uint16)
    diff = abs(np.convolve(x, [-1, 1], 'valid'))
    diff = np.concatenate((diff, [np.mean(diff)]))
    diffres = (2048*(diff/np.max(diff))).astype(np.uint16)
    for i in range(len(x)):
        output[i, xtemp[i]:xtemp[i]+20, 0] = 255
        output[i, freqres[i]:freqres[i]+20, 1] = 255
        output[i, diffres[i]:diffres[i]+20, 2] = 255
    return output




#maxamp = 0
dirchars = [str(j) for j in range(5)]
#    sample = data[i]
#    for k in sample:
#        if np.max(k) > maxamp:
#            maxamp = np.max(k)
#print(len(sample))
##plt.plot(test)
with open("ekg_AAMI_beats.json", 'r') as fp:
    data = json.load(fp)
    
path = os.path.dirname(os.path.abspath(__file__))

for i in range(len(dirchars)):
    newpath = []
    os.mkdir(dirnames[i])
    dirpath = path +'\\'+ dirnames[i]
    data2 = data[dirchars[i]]
    for i in range(len(data2)):
        image = Image.fromarray(ekgtoimage(data2[i], 1800))
        image.save(dirpath+'\\'+str(i)+".jpg")
#result = ekgtoimage(sample, 1800)
#print(type(result[0,0,0]))
#imageres = Image.fromarray(result)
#imageres.save("testfile.jpg")



#output = np.empty((400, 10))
##print(sample)
#diff = np.convolve(sample, [1 , -1], 'valid')
##plt.plot(sample)
##plt.figure()
##plt.plot(diff)
##plt.figure()
#testy = np.fft.fft(sample - np.mean(sample))
#plt.plot(abs(testy[:int(len(testy)/2)]))
##length = len(sample)
#if len(sample) != 400:
#    sample.extend(np.zeros(400 - len(sample)))
#    output[:, 0] = sample
#print(output[:, 0])

