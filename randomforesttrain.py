# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:01:47 2019

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
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import cross_validate
from PIL import Image
import h5py



with h5py.File('X.hdf5', 'r') as hf1:
    X = hf1['X'][:]
with h5py.File('Ybin.hdf5', 'r') as hf2:
    Y = hf2['Y'][:]


model = RandomForestClassifier(class_weight="balanced")
print("start training")
scores = cross_validate(model, X, Y, cv=3, return_train_score=True)
print(scores)


