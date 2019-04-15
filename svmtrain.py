# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:30:07 2019

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
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from PIL import Image
import h5py

with h5py.File('X.hdf5', 'r') as hf1:
    X = hf1['X'][10000:40000]
with h5py.File('Ybin.hdf5', 'r') as hf2:
    Y = hf2['Y'][10000:40000]


model = SVC(class_weight='balanced')
print("start training")
scores = cross_validate(model, X, Y, cv=3, return_train_score=True)
print(scores)