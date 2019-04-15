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






with open("ekg_fullbeats_data.json", 'r') as fp:
    data = json.load(fp)


path = os.path.dirname(os.path.abspath(__file__))

AAMIdata = {}
AAMImap = {}
AAMImap[0] = ['N', 'L', 'R', 'B']
AAMImap[1] = ['j','e','A','a','S','J','n']
AAMImap[2] = [ 'V', 'E', 'r']
AAMImap[3] = ['F']
AAMImap[4] = ['/', 'f', 'Q']

for key in AAMImap.keys():
    AAMIdata[key] = []
#
#for key in data.keys():
#    print(key)
#    print(len(data[key]))
#print("---------------------")

for classnum in AAMImap.keys():
    for beat in AAMImap[classnum]:
        AAMIdata[classnum].extend(data[beat])

with open('ekg_AAMI_beats.json', 'w') as fp:
    json.dump(AAMIdata, fp, sort_keys=True, indent=4)

#for classnum in AAMIdata.keys():
#    print(classnum)
#    print(AAMImap[classnum])
#    print(len(AAMIdata[classnum]))

