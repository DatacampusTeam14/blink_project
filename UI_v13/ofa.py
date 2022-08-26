import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

import time
import cv2
import webbrowser
import pyqtgraph as pg
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from collections import namedtuple

#sys.path.append('C:\\Users\dunca\\Workspace\\VS_Code\\Python\\Datacampus-Project-master\\Window\\py\\cvWindow.py')
#from . import cvWindow
#sys.path.append('C:\\Users\\dunca\\Workspace\\VS_Code\\Python\\Datacampus-Project-master\\Window\\py\\HealthcareWindow.py')
#from . import HealthcareWindow
#sys.path.append('C:\\Users\\dunca\\Workspace\\VS_Code\\Python\\Datacampus-Project-master\\Window\\py\\ResultWindow.py')
#from . import ResultWindow


App = QApplication(sys.argv)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
RppgResults = namedtuple("RppgResults", ["rawimg", "landmarks"])

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#form_intro = resource_path('IntroWindow.ui')
#form_IntroWindow = uic.loadUiType(form_intro)[0]

#form_menu = resource_path('MenuWindow.ui')
#form_MenuWindow = uic.loadUiType(form_menu)[0]

form_intro = resource_path('IntroWindow.ui')
form_IntroWindow = uic.loadUiType(form_intro)[0]

form_menu = resource_path('MenuWindow.ui')
form_MenuWindow = uic.loadUiType(form_menu)[0]

class IntroWindow(QMainWindow, form_IntroWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def btn_go_to_menu(self): 
        self.hide()                   
        self.change = MenuWindow()    
        self.change.show()    

    def btn_github(self):
        webbrowser.open('https://github.com/orgs/DatacampusTeam14/repositories')

class MenuWindow(QWidget,form_MenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def Go_to_cvWindow(self):
        self.close()   
        rppg = RPPG(video=0, parent=App)           
        self.cv = DetectWindow(rppg=rppg)
        self.cv.show()
        rppg.start()
        App.exec_()
    def Go_to_ResultWindow(self):
        self.close()                     
        self.rs = ResultWindow()
        self.rs.show()
    def Go_to_HealthcareWindow(self):
        self.close()
        rppg = RPPG(video=0, parent=App)                    
        self.hc = CareWindow(rppg=rppg)
        self.hc.show()
        rppg.start()
        App.exec_()

    def Quit(self):
        exit()

class DetectWindow(QWidget):
    def __init__(self, rppg):
        """MainWindow visualizing the output of the RPPG model.
        """
        super().__init__()

        rppg.rppg_updated.connect(self.on_rppg_updated)
        self.setupUi_ui(self)

    def setupUi_ui(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
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

        self.graphicsView = pg.GraphicsLayoutWidget(Form)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(490, 40, 601, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.img = pg.ImageItem(axisOrder="row-major")
        vb = self.graphicsView.addViewBox(invertX=True, invertY=True, lockAspect=True)
        vb.addItem(self.img)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 250, 70))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.CancelFeed)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 80, 481, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Datacampus-Project-master/image.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 550, 801, 81))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(1300, 10, 281, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QTimer(self)
        self.lcdNumber.setDigitCount(8)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.setWindowTitle('QTimer')
        self.timer.start()

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 679, 261, 81))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Return to Menu"))
        self.label_2.setText(_translate("Form", "얼굴을 윤곽선에 맞도록 인식시켜 주세요!"))
        self.pushButton_2.setText(_translate("Form", "Return to Menu"))

    def on_rppg_updated(self, output):
        """Update UI based on RppgResults.
        """
        img = output.rawimg.copy()
        draw_facemesh(img, output.landmarks, tesselate=True, contour=True)
        self.img.setImage(img)

    def timeout(self):
        sender = self.sender()
        currentTime = QTime.currentTime().toString("hh:mm:ss")
        if id(sender) == id(self.timer):
            self.lcdNumber.display(currentTime)
    
    def CancelFeed(self):
        self.hide()                     
        self.cv = MenuWindow()
        self.cv.show()
        RPPG.stop()
        Camera.stop()

class CareWindow(QMainWindow):
    def __init__(self, rppg):
        """MainWindow visualizing the output of the RPPG model.
        """
        super().__init__()

        rppg.rppg_updated.connect(self.on_rppg_updated)
        self.setupUi_ui(self)

    def setupUi_ui(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
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

        self.graphicsView = pg.GraphicsLayoutWidget(Form)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(490, 40, 601, 501))
        self.graphicsView.setObjectName("graphicsView")
        self.img = pg.ImageItem(axisOrder="row-major")
        vb = self.graphicsView.addViewBox(invertX=True, invertY=True, lockAspect=True)
        vb.addItem(self.img)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 250, 70))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.CancelFeed)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 80, 481, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Datacampus-Project-master/image.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(400, 550, 801, 81))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(1300, 10, 281, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.timer = QTimer(self)
        self.lcdNumber.setDigitCount(8)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
        self.setWindowTitle('QTimer')
        self.timer.start()

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 679, 261, 81))
        font = QtGui.QFont()
        font.setFamily("여기어때 잘난체 OTF")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Return to Menu"))
        self.label_2.setText(_translate("Form", "얼굴을 윤곽선에 맞도록 인식시켜 주세요!"))
        self.pushButton_2.setText(_translate("Form", "Return to Menu"))

    def on_rppg_updated(self, output):
        """Update UI based on RppgResults.
        """
        img = output.rawimg.copy()
        draw_facemesh(img, output.landmarks, tesselate=True, contour=True)
        self.img.setImage(img)

    def timeout(self):
        sender = self.sender()
        currentTime = QTime.currentTime().toString("hh:mm:ss")
        if id(sender) == id(self.timer):
            self.lcdNumber.display(currentTime)
    
    def CancelFeed(self):
        self.hide()                     
        self.cv = MenuWindow()
        self.cv.show() 
        RPPG.stop()
        Camera.stop()

class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.graphBTN = QPushButton("차트그리기")
        self.graphBTN.clicked.connect(self.click_graph)
        self.cancelBTN = QPushButton("취소")
        self.cancelBTN.clicked.connect(self.click_cancel)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.graphBTN)
        rightLayout.addWidget(self.cancelBTN)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def click_graph(self):
        print(self.lineEdit.text())
        
    def click_cancel(self):
        self.hide()                     
        self.cv = MenuWindow()
        self.cv.show()

class Camera(QThread):
    frame_received = pyqtSignal(np.ndarray)
    def __init__(self, video=0, parent=None):
        """Initialize Camera instance.

        Args:
            video (int or string): ID of camera or video filename
            parent (QObject): parent object in Qt context
        """
        super().__init__(parent=parent)

        self._cap = cv2.VideoCapture(video)
        self._running = False

    def run(self):
        """Start loop in thread capturing incoming frames.
        """
        self._running = True
        while self._running:
            ret, frame = self._cap.read()

            if not ret:
                self._running = False
                raise RuntimeError("No frame received")

            self.frame_received.emit(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def stop(self):
        """Stop loop and release camera.
        """
        
        #self._running = False
        time.sleep(0.1)
        self._cap.release()

class RPPG(QObject):

    rppg_updated = pyqtSignal(RppgResults)

    def __init__(self, parent=None, video=0):
        """rPPG model processing incoming frames and emitting calculation
        outputs.

        The signal RPPG.updated provides a named tuple RppgResults containing
          - rawimg: the raw frame from camera
          - landmarks: multiface_landmarks object returned by FaceMesh
        """
        super().__init__(parent=parent)

        self._cam = Camera(video=video, parent=parent)
        self._cam.frame_received.connect(self.on_frame_received)

        self.detector = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def on_frame_received(self, frame):
        """Process new frame - find face mesh and emit outputs.
        """
        rawimg = frame.copy()
        results = self.detector.process(frame)

        self.rppg_updated.emit(RppgResults(rawimg, results))

    def start(self):
        """Launch the camera thread.
        """
        self._cam.start()

    def stop(self):
        """Stop the camera thread and clean up the detector.
        """
        self._cam.stop()
        self.detector.close()


def draw_facemesh(img, results, tesselate=False,
                  contour=False, irises=False):
    """Draw all facemesh landmarks found in an image.

    Irises are only drawn if the corresponding landmarks are present,
    which requires FaceMesh to be initialized with refine=True.
    """
    if results is None or results.multi_face_landmarks is None:
        return

    for face_landmarks in results.multi_face_landmarks:
        if tesselate:
            mp.solutions.drawing_utils.draw_landmarks(
                image=img,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
        if contour:
            mp.solutions.drawing_utils.draw_landmarks(
                image=img,
                landmark_list=face_landmarks,
                connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp.solutions.drawing_styles
                .get_default_face_mesh_contours_style())
        if irises and len(face_landmarks) > 468:
            mp.solutions.drawing_utils.draw_landmarks(
                image=img,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_iris_connections_style())




if __name__ == '__main__':
    myWindow = IntroWindow()
    myWindow.show()
    App.exec_()