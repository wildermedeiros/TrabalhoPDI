# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITrabalhoBimestral.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QListWidgetItem
from PyQt5.uic import loadUi
import cv2
import numpy as np

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1267, 705)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(990, 120, 251, 471))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.removeButton = QtWidgets.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(1170, 600, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.removeButton.setFont(font)
        self.removeButton.setAcceptDrops(True)
        self.removeButton.setObjectName("removeButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 120, 711, 471))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../snow.JPG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.displayButtonTemp = QtWidgets.QPushButton(Dialog)
        self.displayButtonTemp.setGeometry(QtCore.QRect(990, 600, 75, 23))
        self.displayButtonTemp.setObjectName("displayButtonTemp")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 10, 711, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.browseFileButton = QtWidgets.QPushButton(self.groupBox_2)
        self.browseFileButton.setGeometry(QtCore.QRect(310, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browseFileButton.setFont(font)
        self.browseFileButton.setObjectName("browseFileButton")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(1080, 600, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(990, 70, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 251, 381))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.convertRGB2HSLButton = QtWidgets.QPushButton(self.groupBox)
        self.convertRGB2HSLButton.setGeometry(QtCore.QRect(10, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.convertRGB2HSLButton.setFont(font)
        self.convertRGB2HSLButton.setObjectName("convertRGB2HSLButton")
        self.applyThresholdButton = QtWidgets.QPushButton(self.groupBox)
        self.applyThresholdButton.setGeometry(QtCore.QRect(10, 90, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.applyThresholdButton.setFont(font)
        self.applyThresholdButton.setObjectName("applyThresholdButton")
        self.applyGaussianButton = QtWidgets.QPushButton(self.groupBox)
        self.applyGaussianButton.setGeometry(QtCore.QRect(10, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.applyGaussianButton.setFont(font)
        self.applyGaussianButton.setObjectName("applyGaussianButton")
        self.applyMorphGradButton = QtWidgets.QPushButton(self.groupBox)
        self.applyMorphGradButton.setGeometry(QtCore.QRect(10, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.applyMorphGradButton.setFont(font)
        self.applyMorphGradButton.setObjectName("applyMorphGradButton")
        self.applyBorderDetection = QtWidgets.QPushButton(self.groupBox)
        self.applyBorderDetection.setGeometry(QtCore.QRect(10, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.applyBorderDetection.setFont(font)
        self.applyBorderDetection.setObjectName("applyBorderDetection")
        self.displayButton = QtWidgets.QPushButton(self.groupBox)
        self.displayButton.setGeometry(QtCore.QRect(10, 330, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.displayButton.setFont(font)
        self.displayButton.setObjectName("displayButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.browseFileButton.clicked.connect(self.BrowseFile)
        self.convertRGB2HSLButton.clicked.connect(self.ConvertBGR2HSL)
        self.applyThresholdButton.clicked.connect(self.ApplyBinaryThreshold)
        self.applyGaussianButton.clicked.connect(self.ApplyGaussianBlur)
        self.applyMorphGradButton.clicked.connect(self.ApplyGradientMorph)
        self.listWidget.doubleClicked.connect(self.DisplayItemFromList)
        self.removeButton.clicked.connect(self.RemoveFromList)
        self.clearButton.clicked.connect(self.ClearList)
        self.applyBorderDetection.clicked.connect(self.ApplyBorderDetection)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.removeButton.setText(_translate("Dialog", "Remove"))
        self.displayButtonTemp.setText(_translate("Dialog", "Display"))
        self.groupBox_2.setTitle(_translate("Dialog", "Search "))
        self.browseFileButton.setText(_translate("Dialog", "Browse File"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.label_2.setText(_translate("Dialog", "History"))
        self.groupBox.setTitle(_translate("Dialog", "Tools"))
        self.convertRGB2HSLButton.setText(_translate("Dialog", "Convert RGB To HSL"))
        self.applyThresholdButton.setText(_translate("Dialog", "Apply Binary Threshold"))
        self.applyGaussianButton.setText(_translate("Dialog", "Apply Gaussian Blur"))
        self.applyMorphGradButton.setText(_translate("Dialog", "Apply Gradient Morph"))
        self.applyBorderDetection.setText(_translate("Dialog", "Apply Border Detection"))
        self.displayButton.setText(_translate("Dialog", "Display"))

    img = 0 

    #TODO Tide up na interface ? 

    def DisplayItemFromList(self):
        print("oi")
        index = self.listWidget.currentIndex().row()
        print(index)
        cv2.imshow("From History", listOfActions[index])


    def RemoveFromList(self):
        index = self.listWidget.currentIndex().row()
        self.listWidget.takeItem(index)
        listOfActions.pop(index)

    def ClearList(self):
        global img, imgSourceCopy

        self.listWidget.clear()
        listOfActions.clear()
        cv2.destroyAllWindows()
        img = imgSourceCopy.copy()
        

    def BrowseFile(self):
        global img, imgSourceCopy

        filePath = QFileDialog.getOpenFileName(self, 'Open File')

        #TODO Fazer uma verifica????o para imagem vazia 

        self.lineEdit.setText(filePath[0])
        img = cv2.imread(filePath[0])
        imgSourceCopy = img.copy()
        self.label.setPixmap(QtGui.QPixmap(filePath[0]))
        self.listWidget.addItem(filePath[0])
        listOfActions.append(img)
    

    def ConvertBGR2HSL(self):
        global img, hslCount

        if (len(img.shape) == 2):
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

        hslCount += 1

        self.listWidget.addItem("HSL Conversion Applied: " + str(hslCount))
        listOfActions.append(img)
        cv2.imshow("HSL Conversion", img)
        

    def ApplyBinaryThreshold(self):
        global img, thresCount

        if (len(img.shape) == 3):
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    

        thresholdValue, img = cv2.threshold(
            img, 127, 255, cv2.THRESH_BINARY)

        thresCount += 1

        self.listWidget.addItem("Threshold Binary Applied: " + str(thresCount))
        listOfActions.append(img)
        cv2.imshow("Threshold Binary Applied", img)


    def ApplyGaussianBlur(self):
        global img, blurCount

        img = cv2.GaussianBlur(img, (5, 5), 10)

        blurCount += 1

        self.listWidget.addItem("Gaussian Blur Applied: " + str(blurCount))
        listOfActions.append(img)
        cv2.imshow("Gaussian Blur Applied", img)
        


    def ApplyGradientMorph(self):
        global img, gradientCount

        if (len(img.shape) == 3):
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    

        sobelx = cv2.Sobel(img, cv2.CV_8UC1, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_8UC1, 0, 1, ksize=5)
        img = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

        gradientCount += 1

        self.listWidget.addItem(
            "Gradient Morphological Applied: " + str(gradientCount))
        listOfActions.append(img)
        cv2.imshow("Gradient Morphological Applied", img)


    def ApplyBorderDetection(self):
        global img, borderCount

        if (len(img.shape) == 3):
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)    

        externalContours = np.zeros(img.shape)

        contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        for i in range(len(contours)):

            if hierarchy[0][i][3] == -1:

                cv2.drawContours(externalContours, contours, i, 255, 2)


        borderCount += 1

        self.listWidget.addItem("Contour Detection Applied: " + str(borderCount))
        listOfActions.append(externalContours)
        cv2.imshow("Contour Detection Applied", externalContours)


listOfActions = []
hslCount = 0
thresCount = 0
blurCount = 0 
gradientCount = 0
borderCount = 0 
imgSourceCopy = 0


# def ConvertOpenCvImageToQImage(img, self):
#     height, width, channel = img.shape
#     bytesPerLine = 3 * width
#     qImg = QtGui.QImage(img.data, width, height,
#                         bytesPerLine, QtGui.QImage.Format_RGB888)

#     self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))


def ConvertOpenCvImageGrayToQImage(img, self):
    height = img.shape[0]
    width = img.shape[1]

    bytesPerLine = 1 * width

    qImg = QtGui.QImage(img.data, width, height,
                        bytesPerLine, QtGui.QImage.Format_Grayscale8).rgbSwapped()

    self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



