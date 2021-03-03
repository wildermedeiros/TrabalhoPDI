import numpy as np
import matplotlib.pyplot as plt
import cv2

def Menu():
    print('Press [1] To Show The Selected Image')
    print('Press [2] To Go To HSL Menu options')
    print('Press [3] To Nothing')
    print('Press [0] To CLose')
    print()
    print('Press Esc To Close The Images')

def MenuHSLInfo():
    print('Press [1] To Show The HSL Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms of Each Channel and Save')
    print('Press [4] To Back')
    print()
    print('Press Esc To Close The Images')
    
def MenuHSL():
    MenuHSLInfo()
    option = int(input('Choose a option: '))
        
    while option != 4:
    
        if option == 1:
            ShowImg(hslImg)
            CloseAllWindows()
            print()
        
        elif option == 2:
            SplitAndShow(hslImg)
            CloseAllWindows()
            print()
            
        else:
            print('Invalid option')

        print()
        MenuHSLInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()
         
def ShowImg(img):
    while True:
        cv2.imshow('Geovaninha', img)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

def ShowChannels(channelOne, channelTwo, channelThree):
    while True:
        cv2.imshow('Channel One', channelOne)
        cv2.imshow('Channel Two', channelTwo)
        cv2.imshow('Channel Three', channelThree)

        if cv2.waitKey(1) & 0xFF == 27:
            break
            
def CloseAllWindows():
    cv2.destroyAllWindows()

def SplitAndShow(imgToSplit):
    r, g, b = cv2.split(imgToSplit)    
    ShowChannels(r, g, b)
    
# Start

imgPath = input('Enter the imagem path: ')

rgbImg = cv2.imread(imgPath)

hslImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HLS)
hsvImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HSV)
grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2GRAY)

# Prompt the Menu 

Menu()
option = int(input('Choose a option: '))

while option != 0:
    
    if option == 1:
        ShowImg(rgbImg)
        CloseAllWindows()
        print()
        
    elif option == 2:
        MenuHSL()
        
    elif option == 3:
        ShowImg(hsvImg)
        CloseAllWindows()
        
    elif option == 4:
        ShowImg(grayImg)
        CloseAllWindows()
 
    else:
        print('Invalid option')
    
    print()
    Menu()
    print()
    option = int(input('Choose a option: '))

cv2.destroyAllWindows()