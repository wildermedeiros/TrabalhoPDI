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

knn = cv2.ml.KNearest_create()
knn.train(scaledXTrain, cv2.ml.ROW_SAMPLE, yTrain)
ret, result, neighbours, dist = knn.findNearest(scaledXTest, k=5)

matches = result == yTest
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print(accuracy)
