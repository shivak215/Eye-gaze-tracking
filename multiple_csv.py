# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:44:21 2019

@author: Shiva
"""
import pandas as pd

import numpy as np
import keras
from keras import backend as k
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import *
from keras import backend as Ke
import numpy as np
from numpy import genfromtxt
import csv
import pandas as pd
"""
fout=open("out.csv","a")
# first file:
for line in open("1.csv"):
    fout.write(line)
# now the rest:    
for num in range(2,61):
    f = open(str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
"""
"""
csv_list = ["1.csv","2.csv"]
combined_csv = pd.concat([ pd.read_csv(f, header=None) for f in csv_list ], axis=1)
##   writer =csv.writer(f)
print(combined_csv[)
"""

fout=open("out.csv","a")
for num in range(1,3):
    print(num)
    for line in open(str(num)+".csv"):
         
         fout.write(line)    
fout.close()
