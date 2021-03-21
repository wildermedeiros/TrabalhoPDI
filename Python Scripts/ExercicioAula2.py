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


cv2.namedWindow('Aula2')
cv2.setMouseCallback('Aula2', GetRBGFromInput)

cv2.createTrackbar('Efeito 1', 'Aula2', 0, 256, nothing)
cv2.createTrackbar('Efeito 2', 'Aula2', 0, 256, nothing)

cap = cv2.VideoCapture('c:/video.mp4')

if cap.isOpened() == False:
    print("ERROR: FILE NOT FOUND OR WRONG CODEC USED")




while cap.isOpened:
    ret, frame = cap.read()

    if ret:

        efeito1 = cv2.getTrackbarPos('Blue', 'Aula2')
        efeito2 = cv2.getTrackbarPos('Green', 'Aula2')

        #aplica o efeito aqui ? 

        time.sleep(1/180)
        cv2.imshow('Aula2', frame)

        if cv2.waitKey(1) & 0xFF == 27:
           break

    else:
        break
 

cap.release()
cv2.destroyAllWindows()
