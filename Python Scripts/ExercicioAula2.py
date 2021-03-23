import cv2
import numpy as np
import time

def nothing(x):
    pass

def MedianBlur(frame):
    global dest 

    medianBlurKernel = cv2.getTrackbarPos('Median Blur', 'Aula2')

    dest = frame.copy()

    cv2.medianBlur(frame, medianBlurKernel, dest)

    time.sleep(1/180)
    cv2.imshow('Aula2', dest)


def GaussianBlur(frame):
    global dest

    gaussianBlurKernel = cv2.getTrackbarPos('Gaussian Blur', 'Aula2')

    dest = frame.copy()

    cv2.GaussianBlur(frame, (gaussianBlurKernel, gaussianBlurKernel), 10, dest)

    time.sleep(1/180)
    cv2.imshow('Aula2', dest)

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

cv2.createTrackbar("Median Blur", 'Aula2', 1, 11, nothing)
cv2.createTrackbar("Gaussian Blur", 'Aula2', 1, 11, nothing)
switch = "0 : Median Blur \n1 : Gaussian Blur"
cv2.createTrackbar(switch, 'Aula2', 0, 1, nothing)

cap = cv2.VideoCapture('c:/video.mp4')

if cap.isOpened() == False:
    print("ERROR: FILE NOT FOUND OR WRONG CODEC USED")


while cap.isOpened:
    ret, frame = cap.read()
    dest = np.copy(frame)

    if ret:

        medianBlurKernel = cv2.getTrackbarPos("Median Blur", 'Aula2')
        gaussianBlurKernel = cv2.getTrackbarPos("Gaussian Blur", 'Aula2')
        switchTrackBar = cv2.getTrackbarPos(switch, 'Aula2')

        if switchTrackBar == 0:
            blurredFrame = cv2.medianBlur(frame, medianBlurKernel)
        else:
            blurredFrame = cv2.GaussianBlur(
                frame, (gaussianBlurKernel, gaussianBlurKernel), 10)

        grayFrame = cv2.cvtColor(blurredFrame, cv2.COLOR_RGB2GRAY)

        sobelx = cv2.Sobel(grayFrame, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(grayFrame, cv2.CV_64F, 0, 1, ksize=5)
        blended = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

        thresholdValue, frameThresholded = cv2.threshold(
            blended, 70, 255, cv2.THRESH_BINARY)

        time.sleep(1/180)
        cv2.imshow('Aula2', frameThresholded)

        
        if cv2.waitKey(1) & 0xFF == 27:
           break

    else:
        break
 

cap.release()
cv2.destroyAllWindows()
