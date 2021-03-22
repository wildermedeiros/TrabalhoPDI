import cv2
import numpy as np
import time


def nothing(x):
    pass

def GetRBGFromInput(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:  # checks mouse left button down condition
        colorsB = frame[y, x, 0]
        colorsG = frame[y, x, 1]
        colorsR = frame[y, x, 2]
        colors = frame[y, x]
        print("Red: ", colorsR)
        print("Green: ", colorsG)
        print("Blue: ", colorsB)
        print("BRG Format: ", colors)
        print("Coordinates of pixel: X: ", x, "Y: ", y)


def clamp(value, smallest, largest): 
    return max(smallest, min(value, largest))

cv2.namedWindow('Aula2')
cv2.setMouseCallback('Aula2', GetRBGFromInput)

cv2.createTrackbar('Median Blur', 'Aula2', 3, 11, nothing)
cv2.createTrackbar('Gaussian Blur', 'Aula2', 1, 20, nothing)

cap = cv2.VideoCapture('c:/video.mp4')

if cap.isOpened() == False:
    print("ERROR: FILE NOT FOUND OR WRONG CODEC USED")




while cap.isOpened:
    ret, frame = cap.read()

    if ret:

        medianBlurKernel = cv2.getTrackbarPos('Median Blur', 'Aula2')
        gaussianBlur = cv2.getTrackbarPos('Gaussian Blur', 'Aula2')

        bluredFrame = cv2.medianBlur(frame, medianBlurKernel)

        # efeito é o kernel que será aplicado no blur e outros efeitos  

        grayFrame = cv2.cvtColor(bluredFrame, cv2.COLOR_RGB2GRAY)

        thresholdValue, frameThresholded = cv2.threshold(
            grayFrame, 70, 255, cv2.THRESH_BINARY)

        

        time.sleep(1/180)
        cv2.imshow('Aula2', frameThresholded)

        if cv2.waitKey(1) & 0xFF == 27:
           break

    else:
        break
 

cap.release()
cv2.destroyAllWindows()
