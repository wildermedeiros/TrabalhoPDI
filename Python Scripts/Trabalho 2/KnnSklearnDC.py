from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np 
from numpy import genfromtxt
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import MinMaxScaler

data = genfromtxt("C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/data.txt", delimiter=',')

labels = data[:, 12]
features = data[:, 0:12]

X = features
y = labels

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33, random_state=42)

scalerObject = MinMaxScaler()

scalerObject.fit(XTrain)

scaledXTrain = scalerObject.transform(XTrain)
scaledXTest = scalerObject.transform(XTest)

neighbors = np.arange(1, 9)
trainAccuracy = np.empty(len(neighbors))
testAccuracy = np.empty(len(neighbors))

# Loop over K values
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(scaledXTrain, yTrain)

    predictions = knn.predict(scaledXTest)
    confusion_matrix(yTest, predictions)

    print(classification_report(yTest, predictions))

    # Compute traning and test data accuracy
    trainAccuracy[i] = knn.score(scaledXTrain, yTrain)
    testAccuracy[i] = knn.score(scaledXTest, yTest)

# Generate plot
plt.plot(neighbors, trainAccuracy, label='Training dataset Accuracy')
plt.plot(neighbors, testAccuracy, label='Testing dataset Accuracy')

plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()
