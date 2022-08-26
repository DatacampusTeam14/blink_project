from importlib.resources import path
import string
import sys, os, glob
from tkinter import Widget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import main
import MenuWindow
import makeGraph

path_result = "C:/Users/choi/PycharmProjects/yolo7/blinkResult/"
class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi_ui(self)
        os.chdir(path_result)
        for filename in os.listdir("."): #현재 디렉토리의 모든 파일을 iterate
            if filename.startswith("bf"):
                self.listWidget.addItem(filename[2:6]+'년 '+filename[6:8]+'월 '+filename[8:10]+'일 '+filename[11:13]+'시 '+filename[13:15]+'분 '+filename[15:17]+'초')

    def setupUi_ui(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(600, 645)
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
        "    border-radius: 8px;\n"
        "    border-bottom: 4px solid grey;\n"
        "    \n"
        "    color: rgb(0, 0, 0)\n"
        "}\n"
        "QPushButton{\n"
        "}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 561, 611))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setAlternatingRowColors(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(256, 0))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.BTN_go = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BTN_go.setFont(font)
        self.BTN_go.setObjectName("BTN_go")
        self.verticalLayout.addWidget(self.BTN_go)
        self.BTN_go.clicked.connect(self.show_result)
        self.BTN_Cancel = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BTN_Cancel.setFont(font)
        self.BTN_Cancel.setObjectName("BTN_Cancel")
        self.verticalLayout.addWidget(self.BTN_Cancel)
        self.BTN_Cancel.clicked.connect(self.click_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BTN_go.setText(_translate("Form", "보기"))
        self.BTN_Cancel.setText(_translate("Form", "닫기"))
    def show_result(self):
        resultFileName=self.listWidget.currentItem().text()
        self.close()
        os.chdir(path_result)
        self.ui = graph(resultFileName[0:4] + resultFileName[6:8] + resultFileName[10:12] + '_' + resultFileName[14:16]  + resultFileName[18:20] + resultFileName[22:24])
        self.ui.show()
    def click_cancel(self):
        self.close()
        os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')
        self.mw = MenuWindow.menuwindow()
        self.mw.show()
    
        
class graph(QWidget):
    def __init__(self, resultFileName):
        super().__init__()
        self.resultFileName=resultFileName
        self.setupUi_ui(self)
        os.chdir(path_result)

    def setupUi_ui(self, Form):
        Form.setObjectName("MainWindow")
        Form.setFixedSize(1600, 900)
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255)\n"
"}\n"
"QLabel{\n"
"border:1px solid rgb(84, 84, 85);\n"
"background-color: rgb(255,255,255,0);\n"
"border-radius: 20px;\n"
"border-bottom: 4px solid grey;\n"
"}\n"
"QPushButton{\n"
"border:1px solid rgb(84, 84, 85);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 12px;\n"
"border-radius: 8px;\n"
"border-bottom: 4px solid grey;\n"
"color: rgb(0, 0, 0)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.time_measuring = QtWidgets.QLabel(self.centralwidget)
        self.time_measuring.setGeometry(QtCore.QRect(1200, 360, 351, 101))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setBold(True)
        font.setWeight(75)
        self.time_closing = QtWidgets.QLabel(self.centralwidget)
        self.time_closing.setGeometry(QtCore.QRect(1200, 20, 351, 101))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setBold(True)
        font.setWeight(75)
        self.time_closing.setFont(font)
        self.time_closing.setStyleSheet("")
        self.time_closing.setObjectName("time_closing")
        self.time_measuring.setFont(font)
        self.time_measuring.setStyleSheet("")
        self.time_measuring.setObjectName("time_measuring")
        self.FPS = QtWidgets.QLabel(self.centralwidget)
        self.FPS.setGeometry(QtCore.QRect(1200, 250, 351, 91))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setBold(True)
        font.setWeight(75)
        self.FPS.setFont(font)
        self.FPS.setStyleSheet("")
        self.FPS.setObjectName("FPS")
        self.number_blinking = QtWidgets.QLabel(self.centralwidget)
        self.number_blinking.setGeometry(QtCore.QRect(1200, 140, 351, 91))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setBold(True)
        font.setWeight(75)
        self.number_blinking.setFont(font)
        self.number_blinking.setStyleSheet("")
        self.number_blinking.setObjectName("number_blinking")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 20, 1081, 811))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graph_blink_count_bf = QtWidgets.QLabel(self.widget)
        self.graph_blink_count_bf.setText("")
        self.graph_blink_count_bf.setPixmap(QtGui.QPixmap('blink_count_bf'+str(self.resultFileName)+'.png'))
        self.graph_blink_count_bf.setScaledContents(True)
        self.graph_blink_count_bf.setObjectName("graph_blink_count_bf")
        self.gridLayout.addWidget(self.graph_blink_count_bf, 0, 0, 1, 1)
        self.graph_blink_count_bi = QtWidgets.QLabel(self.widget)
        self.graph_blink_count_bi.setText("")
        self.graph_blink_count_bi.setPixmap(QtGui.QPixmap('blink_count_bi'+str(self.resultFileName)+'.png'))
        self.graph_blink_count_bi.setScaledContents(True)
        self.graph_blink_count_bi.setObjectName("graph_blink_count_bi")
        self.gridLayout.addWidget(self.graph_blink_count_bi, 0, 1, 1, 1)
        self.graph_blink_total_count_bi = QtWidgets.QLabel(self.widget)
        self.graph_blink_total_count_bi.setText("")
        self.graph_blink_total_count_bi.setPixmap(QtGui.QPixmap('blink_total_count_bi'+str(self.resultFileName)+'.png'))
        self.graph_blink_total_count_bi.setScaledContents(True)
        self.graph_blink_total_count_bi.setObjectName("graph_blink_total_count_bi")
        self.gridLayout.addWidget(self.graph_blink_total_count_bi, 1, 0, 1, 1)
        self.graph_clt_bf = QtWidgets.QLabel(self.widget)
        self.graph_clt_bf.setText("")
        self.graph_clt_bf.setPixmap(QtGui.QPixmap('clt_bf'+str(self.resultFileName)+'.png'))
        self.graph_clt_bf.setScaledContents(True)
        self.graph_clt_bf.setObjectName("graph_clt_bf")
        self.gridLayout.addWidget(self.graph_clt_bf, 1, 1, 1, 1)
        self.graph_interval_bf = QtWidgets.QLabel(self.widget)
        self.graph_interval_bf.setText("")
        self.graph_interval_bf.setPixmap(QtGui.QPixmap('interval_bf'+str(self.resultFileName)+'.png'))
        self.graph_interval_bf.setScaledContents(True)
        self.graph_interval_bf.setObjectName("graph_interval_bf")
        self.gridLayout.addWidget(self.graph_interval_bf, 2, 0, 1, 1)
        self.graph_total_interval_bf = QtWidgets.QLabel(self.widget)
        self.graph_total_interval_bf.setText("")
        self.graph_total_interval_bf.setPixmap(QtGui.QPixmap('total_interval_bf'+str(self.resultFileName)+'.png'))
        self.graph_total_interval_bf.setScaledContents(True)
        self.graph_total_interval_bf.setObjectName("graph_ total_interval_bf")
        self.gridLayout.addWidget(self.graph_total_interval_bf, 2, 1, 1, 1)


        self.statusBTN = QtWidgets.QPushButton(self.centralwidget)
        self.statusBTN.setGeometry(QtCore.QRect(1200, 500, 351, 191))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusBTN.setFont(font)
        if makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<6:
            self.statusBTN.setStyleSheet("font: 48pt \"Bahnschrift\";\nbackground: rgb(255, 0, 0)")
        elif 6<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<10:
            self.statusBTN.setStyleSheet("font: 48pt \"Bahnschrift\";\nbackground: rgb(255, 142, 61)")
        elif 10<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<14:
            self.statusBTN.setStyleSheet("font: 48pt \"Bahnschrift\";\nbackground: rgb(255, 255, 0)")
        elif 14<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<18:
            self.statusBTN.setStyleSheet("font: 48pt \"Bahnschrift\";\nbackground: rgb(197, 255, 121)")
        else:
            self.statusBTN.setStyleSheet("font: 48pt \"Bahnschrift\";\nbackground: rgb(0, 255, 0)")
        self.statusBTN.setIconSize(QtCore.QSize(16, 16))
        self.statusBTN.setObjectName("statusBTN")
        self.closebtn = QtWidgets.QPushButton(self.centralwidget)
        self.closebtn.setGeometry(QtCore.QRect(1200, 750, 351, 79))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.closebtn.setFont(font)
        self.closebtn.setObjectName("closebtn")
        self.closebtn.clicked.connect(self.click_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closebtn.setText(_translate("MainWindow", "나가기"))
        self.time_closing.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">눈 감은 시간:%.2f초"%makeGraph.SAVE[3]+"</span></p></body></html>"))
        self.time_measuring.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p><span style=\" font-size:18pt;\">측정시간:%.2f초"%makeGraph.SAVE[0]+"</span></p><p><br/></p></body></html>"))
        self.FPS.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p><span style=\" font-size:18pt;\">평균 프레임:%.2f초"%makeGraph.SAVE[1]+"</span></p><p><br/></p></body></html>"))
        self.number_blinking.setText(_translate("MainWindow", "<html><head/><body><p><br/></p><p><span style=\" font-size:18pt;\">깜빡임 횟수:%d초"%makeGraph.SAVE[2]+"</span></p><p><br/></p></body></html>"))
        if makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<6:
            self.statusBTN.setText(_translate("MainWindow", "심각"))
        elif 6<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<10:
            self.statusBTN.setText(_translate("MainWindow", "경계"))
        elif 10<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<14:
            self.statusBTN.setText(_translate("MainWindow", "주의"))
        elif 14<=makeGraph.SAVE[2]*60/makeGraph.SAVE[0]<18:
            self.statusBTN.setText(_translate("MainWindow", "관심"))
        else:
            self.statusBTN.setText(_translate("MainWindow", "양호"))

    def click_cancel(self):
        self.close()
        os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')
        self.mw = MenuWindow.menuwindow()
        self.mw.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ResultWindow()
    ui.show()
    sys.exit(app.exec_())
