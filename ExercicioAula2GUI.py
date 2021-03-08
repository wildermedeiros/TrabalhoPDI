import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline


def ShowImg(img):
    while True:
        cv2.imshow('Aula2', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

# def PutTextOnScreen(event, x, y, flags, param):
#     if event == cv2.EVENT_MOUSEMOVE:


# cv2.namedWindow(winname = 'Aula2')
# cv2.setMouseCallback('Aula2', PutTextOnScreen)
img = cv2.imread('c:/snow.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX
text = "Oi"
img = cv2.putText(img, text, (10, 500), font, 4,
                  (255, 255, 255), 3, cv2.LINE_AA)
ShowImg(img)

cv2.destroyAllWindows()
