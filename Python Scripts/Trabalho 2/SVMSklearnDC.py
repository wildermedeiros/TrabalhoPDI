from sklearn.model_selection import train_test_split
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

data = genfromtxt(
    "C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/data.txt", delimiter=',')

labels = data[:, 12]
features = data[:, 0:12]

X = features
y = labels

XTrain, XTest, yTrain, yTest = train_test_split(
    X, y, test_size=0.33, random_state=42)

scalerObject = MinMaxScaler()

scalerObject.fit(XTrain)

scaledXTrain = scalerObject.transform(XTrain)
scaledXTest = scalerObject.transform(XTest)

# 'linear' , 'rbf', 'poly', 'sigmoid'
svmModel = SVC(kernel='linear', verbose=2)
svmModel.fit(scaledXTrain, yTrain)

predictions = svmModel.predict(scaledXTest)

print(confusion_matrix(yTest, predictions))

print(classification_report(yTest, predictions))
