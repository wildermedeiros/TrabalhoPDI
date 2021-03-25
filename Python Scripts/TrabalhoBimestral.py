# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterfaceTrabBimestral.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import cv2
import numpy as np


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1395, 715)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 251, 381))
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 20, 711, 91))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 130, 711, 471))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../snow.JPG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(1000, 130, 251, 471))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1000, 80, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(1180, 610, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.removeButton.setFont(font)
        self.removeButton.setAcceptDrops(True)
        self.removeButton.setObjectName("removeButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(1090, 610, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.displayButtonTemp = QtWidgets.QPushButton(self.centralwidget)
        self.displayButtonTemp.setGeometry(QtCore.QRect(1000, 610, 75, 23))
        self.displayButtonTemp.setObjectName("displayButtonTemp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browseFileButton.clicked.connect(self.BrowseFile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Tools"))
        self.convertRGB2HSLButton.setText(_translate("MainWindow", "Convert RGB To HSL"))
        self.applyThresholdButton.setText(_translate("MainWindow", "Apply Binary Threshold"))
        self.applyGaussianButton.setText(_translate("MainWindow", "Apply Gaussian Blur"))
        self.applyMorphGradButton.setText(_translate("MainWindow", "Apply Gradient Morph"))
        self.applyBorderDetection.setText(_translate("MainWindow", "Apply Border Detection"))
        self.displayButton.setText(_translate("MainWindow", "Display"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search "))
        self.browseFileButton.setText(_translate("MainWindow", "Browse File"))
        self.label_2.setText(_translate("MainWindow", "History"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.displayButtonTemp.setText(_translate("MainWindow", "Display"))

    def BrowseFile(self):
        filePath = QFileDialog.getOpenFileName(self, 'Open File')
        self.lineEdit.setText(filePath[0])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
