import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import MenuWindow
import webbrowser

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form_intro = resource_path('IntroWindow.ui')
form_IntroWindow = uic.loadUiType(form_intro)[0]

os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')
class IntroWindow(QMainWindow, form_IntroWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        os.chdir('C:/Users/choi/PycharmProjects/yolo7/UI_v13')

    def btn_go_to_menu(self): 
        self.close()
        self.mn = MenuWindow.menuwindow()
        self.mn.show()

    def btn_github(self):
        webbrowser.open('https://github.com/orgs/DatacampusTeam14/repositories')

    def Quit(self):
        exit()

if __name__ == '__main__':
    
    App = QApplication(sys.argv)
    myWindow = IntroWindow()
    myWindow.show()
    App.exec_()