from sklearn.neural_network import MLPClassifier
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

mlp = MLPClassifier(hidden_layer_sizes=(42, 42),
                    activation='relu', solver='adam', max_iter=100, verbose=2)

mlp.fit(scaledXTrain, yTrain)

predictions = mlp.predict(scaledXTest)

print(confusion_matrix(yTest, predictions))

print(classification_report(yTest, predictions))
