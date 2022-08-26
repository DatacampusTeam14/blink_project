# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

from rppg import *
import ResultWindow
import os
import sys
import glob
import makeGraph
import DevelopersWindow
import ProductWindow

path_result = "C:/Users/choi/PycharmProjects/yolo7/blinkResult/"
class menuwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"QLabel{\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton{\n"
"    border:1px solid rgb(84, 84, 85);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 12px;\n"
"    border-radius: 30px;\n"
"    border-bottom: 4px solid grey;\n"
"    \n"
"    color: rgb(0, 0, 0)\n"
"}")
        self.BTN_quit = QtWidgets.QPushButton(Form)
        self.BTN_quit.setGeometry(QtCore.QRect(1350, 690, 150, 150))
        self.BTN_quit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/icon_Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_quit.setIcon(icon)
        self.BTN_quit.setIconSize(QtCore.QSize(100, 100))
        self.BTN_quit.setObjectName("BTN_quit")
        self.BTN_HealthcareWindow = QtWidgets.QPushButton(Form)
        self.BTN_HealthcareWindow.setGeometry(QtCore.QRect(350, 690, 150, 150))
        self.BTN_HealthcareWindow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/icon_Eye_Stretching.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_HealthcareWindow.setIcon(icon1)
        self.BTN_HealthcareWindow.setIconSize(QtCore.QSize(100, 100))
        self.BTN_HealthcareWindow.setObjectName("BTN_HealthcareWindow")
        self.BTN_cvWindow = QtWidgets.QPushButton(Form)
        self.BTN_cvWindow.setGeometry(QtCore.QRect(100, 690, 150, 150))
        self.BTN_cvWindow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/icon_Eye_Fatigue_Detecting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_cvWindow.setIcon(icon2)
        self.BTN_cvWindow.setIconSize(QtCore.QSize(100, 100))
        self.BTN_cvWindow.setObjectName("BTN_cvWindow")
        self.BTN_ResultWindow = QtWidgets.QPushButton(Form)
        self.BTN_ResultWindow.setGeometry(QtCore.QRect(600, 690, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_ResultWindow.sizePolicy().hasHeightForWidth())
        self.BTN_ResultWindow.setSizePolicy(sizePolicy)
        self.BTN_ResultWindow.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/icon_Statistical_Analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_ResultWindow.setIcon(icon3)
        self.BTN_ResultWindow.setIconSize(QtCore.QSize(80, 80))
        self.BTN_ResultWindow.setObjectName("BTN_ResultWindow")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 660, 1601, 291))
        self.label.setStyleSheet("border:1px solid rgb(84, 84, 85);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 12px;\n"
"border-radius: 50px;\n"
"border-bottom: 4px solid grey;\n"
"    \n"
"color: rgb(0, 0, 0)")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.BTN_ProductWindow = QtWidgets.QPushButton(Form)
        self.BTN_ProductWindow.setGeometry(QtCore.QRect(850, 690, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_ProductWindow.sizePolicy().hasHeightForWidth())
        self.BTN_ProductWindow.setSizePolicy(sizePolicy)
        self.BTN_ProductWindow.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/icon_Recommended_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_ProductWindow.setIcon(icon4)
        self.BTN_ProductWindow.setIconSize(QtCore.QSize(100, 100))
        self.BTN_ProductWindow.setObjectName("BTN_ProductWindow")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 850, 101, 41))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 850, 101, 41))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(620, 850, 111, 41))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(860, 850, 121, 41))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(1410, 860, 41, 21))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.BTN_Developers = QtWidgets.QPushButton(Form)
        self.BTN_Developers.setGeometry(QtCore.QRect(1100, 690, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Developers.sizePolicy().hasHeightForWidth())
        self.BTN_Developers.setSizePolicy(sizePolicy)
        self.BTN_Developers.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/icon_Developers.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Developers.setIcon(icon5)
        self.BTN_Developers.setIconSize(QtCore.QSize(100, 100))
        self.BTN_Developers.setObjectName("BTN_Developers")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(1130, 860, 101, 21))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.Board = QtWidgets.QLabel(Form)
        self.Board.setGeometry(QtCore.QRect(40, 20, 1521, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Board.sizePolicy().hasHeightForWidth())
        self.Board.setSizePolicy(sizePolicy)
        self.Board.setStyleSheet("border:1px solid rgb(84, 84, 85);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 12px;\n"
"border-radius: 50px;\n"
"border-bottom: 4px solid grey;\n"
"    \n"
"color: rgb(0, 0, 0)")
        self.Board.setText("")
        self.Board.setObjectName("Board")
        self.doctor = QtWidgets.QLabel(Form)
        self.doctor.setGeometry(QtCore.QRect(890, 330, 361, 291))
        self.doctor.setText("")
        self.doctor.setPixmap(QtGui.QPixmap("images/doctor.png"))
        self.doctor.setObjectName("doctor")
        self.quote = QtWidgets.QLabel(Form)
        self.quote.setGeometry(QtCore.QRect(620, 80, 921, 251))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(29)
        self.quote.setFont(font)
        self.quote.setAlignment(QtCore.Qt.AlignCenter)
        self.quote.setObjectName("quote")
        self.solution = QtWidgets.QPushButton(Form)
        self.solution.setGeometry(QtCore.QRect(160, 40, 441, 581))
        self.solution.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/eyecare.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solution.setIcon(icon6)
        self.solution.setIconSize(QtCore.QSize(550, 550))
        self.solution.setObjectName("solution")

        self.label.raise_()
        self.BTN_quit.raise_()
        self.BTN_HealthcareWindow.raise_()
        self.BTN_cvWindow.raise_()
        self.BTN_ResultWindow.raise_()
        self.BTN_ProductWindow.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.BTN_Developers.raise_()
        self.label_8.raise_()
        self.Board.raise_()
        self.doctor.raise_()
        self.quote.raise_()
        self.solution.raise_()

        self.retranslateUi(self)
        self.BTN_quit.clicked.connect(self.Quit)
        self.BTN_cvWindow.clicked.connect(self.Go_to_cvWindow)
        self.BTN_HealthcareWindow.clicked.connect(self.Go_to_HealthcareWindow)
        self.BTN_Developers.clicked.connect(self.Go_to_DevelopersWindow)
        self.BTN_ResultWindow.clicked.connect(self.Go_to_ResultWindow)
        self.BTN_ProductWindow.clicked.connect(self.Go_to_ProductWindow)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Eye Fatigue\n"
"Detecting"))
        self.label_4.setText(_translate("Form", "Eye\n"
"Stretching"))
        self.label_5.setText(_translate("Form", "Statistical\n"
"Analysis"))
        self.label_6.setText(_translate("Form", "Recommended\n"
"Item"))
        self.label_7.setText(_translate("Form", "Quit"))
        self.label_8.setText(_translate("Form", "Developers"))
        self.quote.setText(_translate("MenuWIndow", "In the blink of an eye, everything can change.\n"
"So forgive often and love with all your heart.\n"
"You may never know when you may not have that chance again."))

    def Go_to_cvWindow(self):
        self.close()
        os.system('python ../yolov7/detect.py --weights ../yolov7/test.pt --conf 0.5 --img-size 480 --source 0 --nosave --no-trace')
        os.chdir(path_result)
        makeGraph.makeGraph()
        condition = 'bi*_*.csv'
        csvfiles = glob.glob(condition)
        filename = csvfiles[-1]
        filename = filename[2:17]
        self.ui = ResultWindow.graph(filename)
        self.ui.show()

    def Go_to_HealthcareWindow(self):
        self.close()
        os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')
        os.system('python ../stretching/main.py')
        self.mw = menuwindow()
        self.mw.show()

    def Go_to_DevelopersWindow(self):
        self.close()
        self.dw = DevelopersWindow.DevelopersWindow()
        self.dw.show()

    def Go_to_ResultWindow(self):
        self.close()                     
        self.rs = ResultWindow.ResultWindow()
        self.rs.show()

    def Go_to_ProductWindow(self):
        self.close()
        self.rs = ProductWindow.Ui_Form()
        self.rs.show()

    def Quit(self):
        exit()

if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)
    ui = menuwindow()
    ui.show()
    sys.exit(App.exec_())
