from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import sys
import MenuWindow
import webbrowser

class DevelopersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI(self)
    def setupUI(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1600, 900)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"QLabel{\n"
"    background-color: rgb(255,255,255,0);\n"
"}\n"
"QPushButton{\n"
"    border:1px solid rgb(84, 84, 85);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 12px;\n"
"    border-radius: 8px;\n"
"    border-bottom: 4px solid grey;\n"
"    \n"
"    color: rgb(0, 0, 0)\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 50, 301, 290))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/dev_choi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(250, 250))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 50, 301, 290))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/dev_lee.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(250, 250))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 50, 301, 290))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/dev_shin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(250, 250))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1100, 50, 301, 290))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/dev_park1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(250, 250))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 370, 301, 51))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 370, 301, 51))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(780, 370, 301, 51))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(1100, 370, 301, 51))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 450, 301, 291))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(460, 450, 301, 291))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(780, 450, 301, 291))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(1100, 450, 301, 291))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 770, 301, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(460, 770, 301, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(780, 770, 301, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(1100, 770, 301, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(1440, 800, 131, 71))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")

        self.retranslateUi(Form)
        self.pushButton_17.clicked.connect(self.BTN_return)
        self.pushButton_13.clicked.connect(self.git_choi)
        self.pushButton_14.clicked.connect(self.git_lee)
        self.pushButton_15.clicked.connect(self.git_shin)
        self.pushButton_16.clicked.connect(self.git_park)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "최준호"))
        self.pushButton_6.setText(_translate("Form", "이다윤"))
        self.pushButton_7.setText(_translate("Form", "신효섭"))
        self.pushButton_8.setText(_translate("Form", "박민형"))
        self.pushButton_9.setText(_translate("Form", "19970422\n"
"\n"
"고려대학교 세종캠퍼스\n"
"컴퓨터융합소프트웨어학과\n"
"\n"
"역할: 개발 총괄, 모듈화\n"
"데이터 수집 및 분석\n"
"\n"
" Git: junhochoi-dev"))
        self.pushButton_10.setText(_translate("Form", "19990417\n"
"\n"
"홍익대학교 세종캠퍼스\n"
"소프트웨어융합학과\n"
"\n"
"역할: 데이터 수집, 발표 자료\n"
"\n"
"Git: dayun4444"))
        self.pushButton_11.setText(_translate("Form", "19960222\n"
"\n"
"충북대학교\n"
"정보통계학과\n"
"\n"
"역할: 데이터 수집, 분석, 자문\n"
"\n"
"Git: sms291"))
        self.pushButton_12.setText(_translate("Form", "19980607\n"
"\n"
"광운대학교\n"
"컴퓨터정보공학과\n"
"\n"
"역할: 데이터 수집, GUI\n"
"\n"
"Git: duncan1409"))
        self.pushButton_13.setText(_translate("Form", "GitHub"))
        self.pushButton_14.setText(_translate("Form", "GitHub"))
        self.pushButton_15.setText(_translate("Form", "GitHub"))
        self.pushButton_16.setText(_translate("Form", "GitHub"))
        self.pushButton_17.setText(_translate("Form", "돌아가기"))
    def BTN_return(self):
        self.close()
        os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')
        self.mw = MenuWindow.menuwindow()
        self.mw.show()

    def git_choi(self):
        webbrowser.open('https://github.com/junhochoi-dev')
    def git_lee(self):
        webbrowser.open('https://github.com/dayun4444')
    def git_shin(self):
        webbrowser.open('https://github.com/sms291')
    def git_park(self):
        webbrowser.open('https://github.com/duncan1409')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DevelopersWindow()
    ui.show()
    sys.exit(app.exec_())