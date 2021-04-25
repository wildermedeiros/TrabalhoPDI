import glob
import cv2
import numpy as np
import pandas as pd

from skimage.feature import greycomatrix, greycoprops

images = [cv2.imread(file) for file in glob.glob(
    "C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/*.png")]

len(images)

def GetArea(image):
    height = image.shape[0]
    width = image.shape[1]
    area = height * width

    return area


def ContournPerimeter(image):
    ret, thresh = cv2.threshold(image, 127, 255, 0)

    contours, hierarchy = cv2.findContours(
        image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    #M = cv2.moments(cnt)

    perimeter = cv2.arcLength(cnt, True)

    return perimeter


def GetEnergy(cooccurrenceMatrix, maxValue):
    energy = greycoprops(cooccurrenceMatrix, 'energy')
    return energy
    # energy = 0.0

    # for i in range(maxValue):
    #     for j in range(maxValue):
    #             energy += cooccurrenceMatrix[i][j] * cooccurrenceMatrix[i][j]

    # return energy
    


def GetHomogeneity(cooccurrenceMatrix):
    homogeneity = greycoprops(cooccurrenceMatrix, 'homogeneity')
    return homogeneity


def GetCorrelation(cooccurrenceMatrix):
    correlation = greycoprops(cooccurrenceMatrix, 'correlation')
    return correlation


def GetContrast(cooccurrenceMatrix):
    contrast = greycoprops(cooccurrenceMatrix, 'contrast')
    return contrast


def GetASM(cooccurrenceMatrix):
    asm = greycoprops(cooccurrenceMatrix, 'ASM')
    return asm


def GetDissimilarity(cooccurrenceMatrix):
    dissimilarity = greycoprops(cooccurrenceMatrix, 'dissimilarity')
    return dissimilarity



dictionaryList = []
for image in images:

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = image / image.max()

    maxValue = image.max() + 1
    cooccurrenceMatrix = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=maxValue)

    area = GetArea(image)
    perimeter = ContournPerimeter(image)
    energy = GetEnergy(cooccurrenceMatrix, maxValue)
    homogeneity = GetHomogeneity(cooccurrenceMatrix)
    correlation = GetCorrelation(cooccurrenceMatrix)
    contrast = GetContrast(cooccurrenceMatrix)
    asm = GetASM(cooccurrenceMatrix)
    dissimilarity = GetDissimilarity(cooccurrenceMatrix)
    cat = 1

    dictionary = {
        "Area": area,
        "Perimetro": perimeter,
        "Energy": energy,
        "Homogeneity": homogeneity,
        "Correlation": correlation,
        "Contrast": contrast,
        "ASM": asm,
        "Dissimilarity": dissimilarity,
        "Categoria": cat
    }

    # get input row in dictionary format
    # key = col_name
    #dict1.update(blah..)

    dictionaryList.append(dictionary)


df = pd.DataFrame(dictionaryList)

df.to_csv("C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/dataframe.txt",
          header=False, sep=",", index=False)
