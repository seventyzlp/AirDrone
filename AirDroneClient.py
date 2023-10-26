from dataclasses import dataclass
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import *
import sys

import CarController


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
    label_speed_l = QLabel()
    
    label_rot_x = QLabel()
    label_rot_y = QLabel()
    label_rot_z = QLabel()
    label_speed_a = QLabel()
    
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
        
        self.button_f.pressed.connect(self.forward)
        self.button_b.pressed.connect(self.backward)
        self.button_l.pressed.connect(self.left)
        self.button_r.pressed.connect(self.right)
        
        self.button_f.released.connect(self.stop)
        self.button_b.released.connect(self.stop)
        self.button_l.released.connect(self.stop)
        self.button_r.released.connect(self.stop)

        # display widgets
        layout_p = QVBoxLayout()
        layout_p.addWidget(self.label_pos_x)
        layout_p.addWidget(self.label_pos_y)
        layout_p.addWidget(self.label_pos_z)
        layout_p.addWidget(self.label_speed_l)
        
        layout_r = QVBoxLayout()
        layout_r.addWidget(self.label_rot_x)
        layout_r.addWidget(self.label_rot_y)
        layout_r.addWidget(self.label_rot_z)
        layout_r.addWidget(self.label_speed_a)
        
        widget_r = QWidget()
        widget_r.setLayout(layout_r)
        widget_p = QWidget()
        widget_p.setLayout(layout_p)
        
        layout_pr = QHBoxLayout()
        layout_pr.addWidget(widget_p)
        layout_pr.addWidget(widget_r)
        
        # total layout
        layout_t = QVBoxLayout()
        widget_b = QWidget()
        widget_b.setLayout(layout_b)
        widget_pr = QWidget()
        widget_pr.setLayout(layout_pr)
        
        layout_t.addWidget(widget_pr)
        layout_t.addWidget(widget_b)
        
        self.setLayout(layout_t)
        
        # auto refresh information
        self.refreshinfo.start(1000)
        self.refreshinfo.timeout.connect(self.setInfo)
        
        self.show()

# display & refresh information
    def setInfo(self):
        self.label_pos_x.setText("position x: " + str(CarController.carcontrol.GetCarPose().pos_x))
        self.label_pos_y.setText("position y: " + str(CarController.carcontrol.GetCarPose().pos_y))
        self.label_pos_z.setText("position z: " + str(CarController.carcontrol.GetCarPose().pos_z))
        
        self.label_rot_x.setText("Rotation x: " + str(CarController.carcontrol.GetCarPose().rot_x))
        self.label_rot_y.setText("Rotation y: " + str(CarController.carcontrol.GetCarPose().rot_y))
        self.label_rot_z.setText("Rotation z: " + str(CarController.carcontrol.GetCarPose().rot_z))
        
        self.label_speed_l.setText("Linear Speed: "+ str(CarController.carcontrol.GetCarPose().speed_l))
        self.label_speed_a.setText("Angle Speed: "+ str(CarController.carcontrol.GetCarPose().speed_a))
       

# move function
    def forward(self):
        CarController.carcontrol.GoForward(veh.acc)
    def backward(self):
        pass
    def left(self):
        CarController.carcontrol.Steer(veh.acc, -1)
    def right(self):
        CarController.carcontrol.Steer(veh.acc, 1)

    def stop(self):
        CarController.carcontrol.Stop()
        
window = AirDroneClientWindow()
window.initUI()
window.setInfo()
sys.exit(app.exec())