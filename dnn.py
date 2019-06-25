# -*- coding: utf-8 -*-
"""
@author: Shiva
"""

from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
import pandas as pd


features = pd.read_csv("/content/drive/My Drive/winter/out.csv")
X_test=pd.read_csv("/content/drive/My Drive/winter/31ul.csv")

x=np.ones(36928)
x1=np.zeros(25100)
labels=[]
Y_test=[]
for i in range(1,36930):
    labels.append(0)
for i in range(1,25100):    
    labels.append(1)
for i in range(1,1473):
    Y_test.append(0)    
#print(labels)
print(features.shape)
labels=np.array(labels)
print(labels.shape[0])
Y_test=np.array(Y_test)
X_train=features
Y_train= labels
#print("asjsjjs")

model = Sequential()
model.add(Dense(500, input_dim=(2), activation='relu'))

model.add(Dense(200, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(100, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(50, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(1, activation='sigmoid'))

#Compile model
model.compile(loss='binary_crossentropy', optimizer='Adagrad', metrics=['accuracy'])#adagrad
#Fit the model
model.fit(X_train, Y_train, batch_size=25, nb_epoch=20, verbose=1)
print("\n")

#Evaluate model on test data
z=model.predict(X_test)
score = model.evaluate(X_test, Y_test, verbose=1)
print("TEST ACCURACY ON AUTISM PREDICTION IS ",score[1])



