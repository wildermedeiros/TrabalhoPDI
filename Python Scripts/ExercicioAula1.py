import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# DONE Verificar o savefile 
# DONE Verificar o savefile nos channels
# DONE Update menus infos about histograms
# DONE Verificar o savefile nos histogramas 
# MAYBE Verificar a ordem do split ?

def Menu():
    print('Press [1] To Show The Selected Image Menu Options')
    print('Press [2] To Go To HSL Menu Options')
    print('Press [3] To Go to HSV Menu Options')
    print('Press [4] To Go To Gray Menu Options')
    print()
    print('Press [0] To Close')
    print()
    print('Press Esc To Close The Images')


def MenuRGBInfo():
    print('Press [1] To Show The Selected Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms')
    print('Press [4] To Back')
    print()
    print('INFO: Press Esc To Close The Images')
    print('INFO: You Can Save and Manipulate The Histograms Direct From The Histogram Panel')
    print()


def MenuHSLInfo():
    print('Press [1] To Show The HSL Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms')
    print('Press [4] To Back')
    print()
    print('INFO: Press Esc To Close The Images')
    print('INFO: You Can Save and Manipulate The Histograms Direct From The Histogram Panel')
    print()


def MenuHSVInfo():
    print('Press [1] To Show The HSV Image and Save')
    print('Press [2] To Show The Channels and Save')
    print('Press [3] To Show The Histograms')
    print('Press [4] To Back')
    print()
    print('INFO: Press Esc To Close The Images')
    print('INFO: You Can Save and Manipulate The Histograms Direct From The Histogram Panel')
    print()


def MenuGRAYInfo():
    print('Press [1] To Show The GRAY Image and Save')
    print('Press [2] To Show The Histograms')
    print('Press [4] To Back')
    print()
    print('INFO: Press Esc To Close The Image')
    print('INFO: You Can Save and Manipulate The Histograms Direct From The Histogram Panel')
    print()


def MenuRGB():
    MenuRGBInfo()
    option = int(input('Choose a option: '))

    while option != 4:

        if option == 1:
            ShowImg(rgbImg)
            SaveImage('rgbImg.jpg', rgbImg)
            CloseAllWindows()
            print()

        elif option == 2:
            ChannelHandler(rgbImg, 'RGB-IMAGE')
            CloseAllWindows()
            print()

        elif option == 3:
            ShowHistrograms(rgbImg)

        else:
            print('Invalid option')

        print()
        MenuRGBInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()


def MenuHSL():
    MenuHSLInfo()
    option = int(input('Choose a option: '))

    while option != 4:

        if option == 1:
            ShowImg(hslImg)
            SaveImage('hslImg.jpg', hslImg)
            CloseAllWindows()
            print()

        elif option == 2:
            ChannelHandler(hslImg, 'HSL-IMAGE')
            CloseAllWindows()
            print()

        elif option == 3:
            ShowHistrograms(hslImg)

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
            SaveImage('hsvImg.jpg', hsvImg)
            CloseAllWindows()
            print()

        elif option == 2:
            ChannelHandler(hsvImg, 'HSV-IMAGE')
            CloseAllWindows()
            print()

        elif option == 3:
            ShowHistrograms(hsvImg)

        else:
            print('Invalid option')

        print()
        MenuHSVInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()


def MenuGray():
    MenuGRAYInfo()
    option = int(input('Choose a option: '))

    while option != 4:

        if option == 1:
            ShowImg(grayImg)
            SaveImage('grayImg.jpg', grayImg)
            CloseAllWindows()
            print()

        elif option == 2:
            ShowHistogram(grayImg)

        else:
            print('Invalid option')

        print()
        MenuGRAYInfo()
        print()
        option = int(input('Choose a option: '))

        cv2.destroyAllWindows()


def ShowImg(img):
    while True:
        cv2.imshow('Geovaninha', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break


def SaveImage(nameWithType, img):
    cv2.imwrite(nameWithType, img)

def SaveChannelsImages(channelName, img, channelName1, img1, channelName2, img2):
    cv2.imwrite(channelName, img)
    cv2.imwrite(channelName1, img1)
    cv2.imwrite(channelName2, img2)

def ChannelHandler(imgToSplit, imgMapColorName):
    r, g, b = cv2.split(imgToSplit)
    ShowChannels(r, g, b)

    channelRed = imgMapColorName + " Channel Red.jpg"
    channelGreen = imgMapColorName + " Channel Green.jpg"
    channelBlue = imgMapColorName + " Channel Blue.jpg"

    SaveChannelsImages(channelRed, r, channelGreen, g, channelBlue, b)

def ShowChannels(channelOne, channelTwo, channelThree):
    while True:
        cv2.imshow('Channel R', channelOne)
        cv2.imshow('Channel G', channelTwo)
        cv2.imshow('Channel B', channelThree)

        if cv2.waitKey(1) & 0xFF == 27:
            break

def ShowHistrograms(img):
    colors = ("r", "g", "b")
    channel_ids = (0, 1, 2)

    plt.xlim([0, 256])
    for channel_id, c in zip(channel_ids, colors):
        histogram, bin_edges = np.histogram(img[:, :, channel_id], bins=256, range=(0, 256))
        plt.plot(bin_edges[0:-1], histogram, color=c)

    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    plt.show()

def ShowHistogram(img):
    plt.xlim([0, 256])
    histogram, bin_edges = np.histogram(img, bins=256, range=(0, 256))
    plt.plot(bin_edges[0:-1], histogram)

    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    plt.show()

def CloseAllWindows():
    cv2.destroyAllWindows()


########################### Start ###########################


imgPath = input('Enter the imagem path: ')

rgbImg = cv2.imread(imgPath)

hslImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HLS)
hsvImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2HSV)
grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2GRAY)

print()
Menu()
print()
option = int(input('Choose a option: '))
print()

while option != 0:

    if option == 1:
        MenuRGB()

    elif option == 2:
        MenuHSL()

    elif option == 3:
        MenuHSV()

    elif option == 4:
        MenuGray()

    #elif option == 5:
    #    ShowHistrograms(rgbImg)

    else:
        print('Invalid option')

    print()
    Menu()
    print()
    option = int(input('Choose a option: '))

cv2.destroyAllWindows()
