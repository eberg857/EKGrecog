# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 05:20:42 2019

@author: Eduardo Berg
"""

import wfdb
import os

anno = wfdb.rdann('/mitdb/100', 'atr', return_label_elements=['symbol',
        'label_store', 'description'])

print(anno)