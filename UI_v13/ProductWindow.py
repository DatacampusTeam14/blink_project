# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import MenuWindow
import sys

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1600, 900)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
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
"    border-radius: 20px;\n"
"    border-bottom: 4px solid grey;\n"
"    \n"
"    color: rgb(0, 0, 0)\n"
"}")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 800, 201, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.carrot = QtWidgets.QPushButton(Form)
        self.carrot.setGeometry(QtCore.QRect(1270, 310, 241, 231))
        self.carrot.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Documents/카카오톡 받은 파일/UI_last_version/images/carrot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carrot.setIcon(icon)
        self.carrot.setIconSize(QtCore.QSize(200, 200))
        self.carrot.setObjectName("carrot")
        self.cheese = QtWidgets.QPushButton(Form)
        self.cheese.setGeometry(QtCore.QRect(90, 640, 231, 211))
        self.cheese.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Documents/카카오톡 받은 파일/UI_last_version/images/cheese.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cheese.setIcon(icon1)
        self.cheese.setIconSize(QtCore.QSize(200, 200))
        self.cheese.setObjectName("cheese")
        self.blueberry = QtWidgets.QPushButton(Form)
        self.blueberry.setGeometry(QtCore.QRect(90, 40, 231, 211))
        self.blueberry.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Documents/카카오톡 받은 파일/UI_last_version/images/blueberry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blueberry.setIcon(icon2)
        self.blueberry.setIconSize(QtCore.QSize(200, 200))
        self.blueberry.setObjectName("blueberry")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(450, 110, 691, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(self.coupang1)
        self.pushButton_3.clicked.connect(self.coupang2)
        self.pushButton_5.clicked.connect(self.coupang3)
        self.pushButton.clicked.connect(self.coupang4)
        self.pushButton_2.clicked.connect(self.coupang5)
        self.pushButton_6.clicked.connect(self.return_menu)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_6.setText(_translate("Form", "돌아가기"))
        self.pushButton_4.setText(_translate("Form", "눈에 좋은 차"))
        self.pushButton_3.setText(_translate("Form", "눈에 좋은 약"))
        self.pushButton_5.setText(_translate("Form", "눈에 좋은 야채"))
        self.pushButton.setText(_translate("Form", "눈에 좋은 과일"))
        self.pushButton_2.setText(_translate("Form", "눈에 좋은 음식"))

    def coupang1(self):
        webbrowser.open('https://www.coupang.com/np/search?component=&q=%EB%88%88%EC%97%90+%EC%A2%8B%EC%9D%80+%EC%B0%A8&channel=user')
    def coupang2(self):
        webbrowser.open('https://www.coupang.com/np/search?component=&q=%EB%88%88%EC%97%90+%EC%A2%8B%EC%9D%80+%EC%95%BD&channel=user')
    def coupang3(self):
        webbrowser.open('https://www.coupang.com/np/search?component=&q=%EB%88%88%EC%97%90+%EC%A2%8B%EC%9D%80+%EC%95%BC%EC%B1%84&channel=user')
    def coupang4(self):
        webbrowser.open('https://www.coupang.com/np/search?component=&q=%EB%88%88%EC%97%90+%EC%A2%8B%EC%9D%80+%EA%B3%BC%EC%9D%BC&channel=user')
    def coupang5(self):
        webbrowser.open('https://www.coupang.com/np/search?component=&q=%EB%88%88%EC%97%90+%EC%A2%8B%EC%9D%80+%EC%9D%8C%EC%8B%9D&channel=user')
    def return_menu(self):
        self.close()                     
        self.mw = MenuWindow.menuwindow()
        self.mw.show()
if __name__ == "__main__":
    App = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(App.exec_())