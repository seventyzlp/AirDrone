from dataclasses import dataclass
from tkinter import SE
from PyQt5 import QtCore, QtGui
import airsim
from PyQt5.QtWidgets import QBoxLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import *
import sys


# mobile configuration
@dataclass
class vehicle():
    acc = 1;
veh = vehicle()


# form application # 
app = QApplication(sys.argv)

class AirDroneClientWindow(QWidget):

    button_f = QPushButton()
    button_b = QPushButton()
    button_l = QPushButton()
    button_r = QPushButton()
    
    label_pos_x = QLabel()
    label_pos_y = QLabel()
    label_pos_z = QLabel()
    
    refreshinfo = QTimer()
    
    def initUI(self):
         
        self.resize(1280, 720)
        self.setWindowTitle("AirDrone-Client")
        
        # button
        self.button_f.setText("Move Forward")
        self.button_b.setText("Move Backward")
        self.button_l.setText("Move Left")
        self.button_r.setText("Move Right")
        
        layout_b = QHBoxLayout()
        layout_b.addWidget(self.button_f)
        layout_b.addWidget(self.button_b)
        layout_b.addWidget(self.button_l)
        layout_b.addWidget(self.button_r)
        layout_b.setSpacing(40)
        
        self.button_f.clicked.connect(self.forward)
        self.button_b.clicked.connect(self.backward)
        self.button_l.clicked.connect(self.left)
        self.button_r.clicked.connect(self.right)

        # display widgets
        layout_w = QVBoxLayout()
        layout_w.addWidget(self.label_pos_x)
        layout_w.addWidget(self.label_pos_y)
        layout_w.addWidget(self.label_pos_z)
        
        # total layout
        layout_t = QVBoxLayout()
        widget_w = QWidget()
        widget_w.setLayout(layout_w)
        widget_b = QWidget()
        widget_b.setLayout(layout_b)
        layout_t.addWidget(widget_w)
        layout_t.addWidget(widget_b)
        self.setLayout(layout_t)
        
        # auto refresh information
        self.refreshinfo.start(1000)
        self.refreshinfo.timeout.connect(self.setInfo)
        
        self.show()

# display & refresh information
    def setInfo(self):
        self.label_pos_x.setText("position x: ")
        self.label_pos_y.setText("position y: ")
        self.label_pos_z.setText("position z: ")

# move function
    def forward(self):
        print(veh.acc)
    def backward(self):
        print(veh.acc)
    def left(self):
        print(veh.acc)
    def right(self):
        print(veh.acc)
        
window = AirDroneClientWindow()
window.initUI()
window.setInfo()
sys.exit(app.exec())