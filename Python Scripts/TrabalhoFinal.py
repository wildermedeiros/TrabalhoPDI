import glob
import cv2
import numpy as np
import pandas as pd

images = [cv2.imread(file) for file in glob.glob(
    "C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/*.png")]

len(images)

#dataFrame = pd.DataFrame()

def GetArea(image):
    height, width, _ = image.shape
    area = height * width
    return area


dictionaryList = []
for image in images:
    area = GetArea(image)

    var = 4

    corr = 3

    cat = 1

    dictionary = { 
        "Area": area,
        "Var": var,
        "Corr": corr,
        "Categoria" : cat
    }
    # get input row in dictionary format
    # key = col_name
    
    #dict1.update(blah..)

    dictionaryList.append(dictionary)


df = pd.DataFrame(dictionaryList)

df.to_csv("C:/Users/Usuario/Downloads/PDI Exercicios/Python Scripts/datasetTest/dataframe.txt",
          header=False, sep=",", index=False)
