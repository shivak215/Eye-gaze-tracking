# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:15:48 2019

@author: Shiva
"""
import pandas as pd
df = pd.read_csv('mm.csv', header=None)

ds = df.sample(frac=1)

ds.to_csv('newfile.csv')
