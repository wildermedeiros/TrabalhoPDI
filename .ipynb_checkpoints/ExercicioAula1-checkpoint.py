import numpy as np
import matplotlib.pyplot as plt
import cv2

imgPath = input('Enter the imagem path: ')

rgbImg = cv2.imread(imgPath)

hslImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HLS)
hsvImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HSV)
grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2GRAY)

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
        # hsv menu

        ShowImg(hsvImg)
        CloseAllWindows()

    elif option == 4:
        # gray menu

        ShowImg(grayImg)
        CloseAllWindows()

    else:
        print('Invalid option')

    print()
    Menu()
    print()
    option = int(input('Choose a option: '))

cv2.destroyAllWindows()


def Menu():
    print('Press [1] To Show The Selected Image')
    print('Press [2] To Go To HSL Menu Options')
    print('Press [3] To Go to HSV Menu Options')
    print('Press [4] To Go To Gray Menu Options')
    print()
    print('Press [0] To Close')
    print()
    print('Press Esc To Close The Images')


def MenuHSLInfo():
    print('Press [1] To Show The HSL Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms of Each Channel and Save')
    print('Press [4] To Back')
    print()
    print('Press Esc To Close The Images')


def MenuHSVInfo():
    print('Press [1] To Show The HSV Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms of Each Channel and Save')
    print('Press [4] To Back')
    print()
    print('Press Esc To Close The Images')


def MenuGRAYInfo():
    print('Press [1] To Show The GRAY Image and Save')
    print('Press [2] To Show The Channel and Save')
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
            SplitAndShowChannels(hslImg)
            CloseAllWindows()
            print()

        elif option == 3:
            print()
            #ShowHistrograms()
            

        else:
            print('Invalid option')

        print()
        MenuHSLInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()


def MenuHSV():
    MenuHSVInfo()
    option = int(input('Choose a option: '))

    while option != 4:

        if option == 1:
            ShowImg(hsvImg)
            CloseAllWindows()
            print()

        elif option == 2:
            SplitAndShowChannels(hsvImg)
            CloseAllWindows()
            print()

        elif option == 3:
            print()
            #ShowHistrograms()

        else:
            print('Invalid option')

        print()
        MenuHSVInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()


def ShowImg(img):
    while True:
        cv2.imshow('Geovaninha', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break


def SplitAndShowChannels(imgToSplit):
    r, g, b = cv2.split(imgToSplit)
    ShowChannels(r, g, b)


def ShowChannels(channelOne, channelTwo, channelThree):
    while True:
        cv2.imshow('Channel One', channelOne)
        cv2.imshow('Channel Two', channelTwo)
        cv2.imshow('Channel Three', channelThree)

        if cv2.waitKey(1) & 0xFF == 27:
            break


def CloseAllWindows():
    cv2.destroyAllWindows()
