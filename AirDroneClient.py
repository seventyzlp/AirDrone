from lib2to3.fixes.fix_urllib import build_pattern
from turtle import forward
import typing
from PyQt5 import QtCore, QtGui
import airsim
from PyQt5.QtWidgets import QBoxLayout, QHBoxLayout, QPushButton, QWidget, QApplication
from PyQt5.QtCore import *
import sys



# form application # 
app = QApplication(sys.argv)

class AirDroneClientWindow(QWidget):
    
    def initUI(self):
        self.resize(1280, 720)
        self.setWindowTitle("AirDrone-Client")
        
        # button
        button_f = QPushButton(self)
        button_b = QPushButton(self)
        button_l = QPushButton(self)
        button_r = QPushButton(self)
        
        button_f.setText("Move Forward")
        button_b.setText("Move Backward")
        button_l.setText("Move Left")
        button_r.setText("Move Right")
        
        layout = QHBoxLayout()
        layout.addWidget(button_f)
        layout.addWidget(button_b)
        layout.addWidget(button_l)
        layout.addWidget(button_r)
        layout.setSpacing(40)
        
        button_f.clicked.connect(self.forward)
        button_b.clicked.connect(self.backward)
        button_l.clicked.connect(self.left)
        button_r.clicked.connect(self.right)
        # button

        self.setLayout(layout)
        self.show()
    

# move function
    def forward(self):
        print("FF")
    def backward(self):
        pass
    def left(self):
        pass
    def right(self):
        pass


window = AirDroneClientWindow()
window.initUI()
sys.exit(app.exec())