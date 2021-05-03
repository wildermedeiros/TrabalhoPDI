import glob
import cv2
import numpy as np
import pandas as pd

from skimage.feature import greycomatrix, greycoprops
from numpy import empty, mean

images = [cv2.imread(file) for file in glob.glob(
    "C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/*jpg")]

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
    energy = greycoprops(cooccurrenceMatrix, 'energy')[0][0]
    return energy


def GetHomogeneity(cooccurrenceMatrix):
    homogeneity = greycoprops(cooccurrenceMatrix, 'homogeneity')[0][0]
    return homogeneity


def GetCorrelation(cooccurrenceMatrix):
    correlation = greycoprops(cooccurrenceMatrix, 'correlation')[0][0]
    return correlation


def GetContrast(cooccurrenceMatrix):
    contrast = greycoprops(cooccurrenceMatrix, 'contrast')[0][0]
    return contrast


def GetASM(cooccurrenceMatrix):
    asm = greycoprops(cooccurrenceMatrix, 'ASM')[0][0]
    return asm


def GetDissimilarity(cooccurrenceMatrix):
    dissimilarity = greycoprops(cooccurrenceMatrix, 'dissimilarity')[0][0]
    return dissimilarity

def GetVariance(image):
    variance = np.var(image)
    return variance

def GetMean(image):
    myMean = mean(image)
    return myMean 

def GetMedian(image):
    median = np.median(image)
    return median 

def GetStandartDeviantion(image):
    standartDeviantion = np.std(image)
    return standartDeviantion

dictionaryList = []
for image in images:

    # try:
    #     if image is None:  # The variable
    #         print('It is None')
    # # except NameError:
    # #     print("This variable is not defined")
    # # else:
    # #     print("It is defined and has a value")
    if image is None: 
        pass

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = image / image.max()

    maxValue = image.max() + 1
    cooccurrenceMatrix = greycomatrix(image, [1], [0], levels = maxValue, symmetric = False, normed = True)

    area = GetArea(image)
    perimeter = ContournPerimeter(image)
    energy = GetEnergy(cooccurrenceMatrix, maxValue)
    homogeneity = GetHomogeneity(cooccurrenceMatrix)
    correlation = GetCorrelation(cooccurrenceMatrix)
    contrast = GetContrast(cooccurrenceMatrix)
    asm = GetASM(cooccurrenceMatrix)
    dissimilarity = GetDissimilarity(cooccurrenceMatrix)
    variance = GetVariance(image)
    myMean = GetMean(image)
    median = GetMedian(image)
    standartDeviantion = GetStandartDeviantion(image)

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
        "Variance": variance,
        "StandartDeviantion": standartDeviantion,
        "Mean": myMean,
        "Median": median,
        "Categoria": cat
    }

    # get input row in dictionary format
    # key = col_name
    #dict1.update(blah..)

    dictionaryList.append(dictionary)


df = pd.DataFrame(dictionaryList)

df.to_csv("C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/dataframe.txt",
          header=False, sep=",", index=False)
