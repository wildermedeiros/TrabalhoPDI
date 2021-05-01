import cv2
import numpy as np
from numpy import genfromtxt

data = genfromtxt("C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/data.txt", delimiter = ',')

labels = data[:, 12]
features = data[:, 0:12]

X = features
y = labels

from sklearn.model_selection import train_test_split 

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.preprocessing import MinMaxScaler

scalerObject = MinMaxScaler()

scalerObject.fit(XTrain)

scaledXTrain = scalerObject.transform(XTrain)
scaledXTest = scalerObject.transform(XTest)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(12, input_dim = 12, activation = 'relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

model.fit(scaledXTrain, yTrain, epochs = 50 , verbose = 2)

from sklearn.metrics import confusion_matrix, classification_report

predictions = model.predict_classes(scaledXTest)
confusion_matrix(yTest, predictions)

print(classification_report(yTest, predictions))
