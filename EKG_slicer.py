import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import os
import json





def findcutoffs(data, thresh):
    cutter = [360*i for i in range(11)]
#    index = 0
#    out = []
#    diff = abs(np.convolve(data, [-1, 1], 'valid'))
#    diff = diff / np.max(diff)
#    count = 0
#    while index < len(diff):
#        if diff[index] > thresh:
#            out.append(index)
#            index += 90
#            count = 0
#        elif count == 310:
#            out.append(index)
#            index += 90
#            count = 0
#        else:
#            index += 1
#            count += 1
    return cutter


def slicer(data, cutoffs):
    slices = []
    for i in range(len(cutoffs) - 1):
        slices.append(data[cutoffs[i]:cutoffs[i+1]])
    return slices

def extractor(data, thresh):
    cuts = findcutoffs(data, thresh)
    slices = slicer(data, cuts)
    return slices

dirnames = ["1 NSR", "2 APB", "3 AFL", "4 AFIB", "5 SVTA", "6 WPW", "7 PVC", "8 Bigeminy", "9 Trigeminy", "10 VT", 
           "11 IVR", "12 VFL", "13 Fusion", "14 LBBBB", "15 RBBBB", "16 SDHB", "17 PR"]


def convert(dirname, thresh):
    folder = os.fsencode(dirname)
    output = []
    for file in os.listdir(folder):
        filename = dirname +'\\'+ os.fsdecode(file)
        print(filename)
        datamat = scipy.io.loadmat(filename)
        data = datamat['val'][0].tolist()
        output.extend(extractor(data, thresh))
    return output


def extractdata(dirnames, thresh):
    outputdata = {}
    path = os.path.dirname(os.path.abspath(__file__))
    newdirs = []
    for i in dirnames:
        newdirs.append(path + "\MLII\\" + i)
    for i in range(len(newdirs)):
        outputdata[i+1] = convert(newdirs[i], thresh)
    return outputdata



#save data as JSON
data = extractdata(dirnames, 0.5)



with open('ekg_1s_data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)

#verification plots:
    #test = scipy.io.loadmat("MLII/10 VT/205m (0).mat")
#test = scipy.io.loadmat("MLII/1 NSR/100m (0).mat")
#test = scipy.io.loadmat("MLII/1 NSR/101m (1).mat")
#test = scipy.io.loadmat("MLII/12 VFL/207m (0).mat")
#test = test['val'][0]
#test = test- np.mean(test)
#print(len(test))
#plt.plot(test)
#plt.figure()
#diff = abs(np.convolve(test, [-1 ,1], 'valid'))
#diff = diff / np.max(diff)
#print(len(diff))
#plt.plot(diff + 900)
#for i in data[1]:
#    plt.plot(i)
#    plt.figure()