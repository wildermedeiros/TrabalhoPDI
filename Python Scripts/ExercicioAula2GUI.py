import cv2
import numpy as np
#import matplotlib.pyplot as plt

newX = 0
newY = 0
fontType = cv2.FONT_HERSHEY_SIMPLEX

def nothing(x):
    pass

def PutTextOnScreen(event, x, y, flags, param):
    global newX, newY
    
    if event == cv2.EVENT_MOUSEMOVE:
        newX = x
        newY = y        

cv2.namedWindow(winname = 'Aula2')
cv2.setMouseCallback('Aula2', PutTextOnScreen)

cv2.createTrackbar('Blue', 'Aula2', 0, 256, nothing)
cv2.createTrackbar('Green', 'Aula2', 0, 256, nothing)
cv2.createTrackbar('Red', 'Aula2', 0, 256, nothing)

while True:
    img = cv2.imread('c:/snow.jpg')

    red = cv2.getTrackbarPos('Blue', 'Aula2')
    blue = cv2.getTrackbarPos('Green', 'Aula2')
    green = cv2.getTrackbarPos('Red', 'Aula2')
    
    textToDisplay = "X: " + str(newX) + "Y: " + str(newY)
    cv2.putText(img, textToDisplay, (10,500), fontType, 2, (red,blue,green), 3, cv2.LINE_AA)
    
    cv2.imshow('Aula2', img)
    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
