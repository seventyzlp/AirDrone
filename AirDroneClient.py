import sys
from dataclasses import dataclass

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QApplication

import CarController
import DroneController


# mobile configuration
@dataclass
class Vehicle():
    acc = 1
    vehicle_type = ''


veh = Vehicle()

# form application #
app = QApplication(sys.argv)


class AirDroneClientWindow(QWidget):
    button_f = QPushButton()
    button_b = QPushButton()
    button_l = QPushButton()
    button_r = QPushButton()

    button_takeoff = QPushButton()
    button_land = QPushButton()
    button_up = QPushButton()
    button_down = QPushButton()

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
        # region
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
        self.button_b.released.connect(self.backwardend)
        self.button_l.released.connect(self.stop)
        self.button_r.released.connect(self.stop)

        # drone only
        layout_d = QHBoxLayout()
        self.button_takeoff.setText("Takeoff")
        self.button_land.setText("Land")
        self.button_up.setText("UP")
        self.button_down.setText("Down")

        layout_d.addWidget(self.button_takeoff)
        layout_d.addWidget(self.button_land)
        layout_d.addWidget(self.button_up)
        layout_d.addWidget(self.button_down)
        layout_d.setSpacing(40)

        self.button_takeoff.clicked.connect(DroneController.dronecontrol.TakeOff)
        self.button_land.clicked.connect(DroneController.dronecontrol.Landed)
        self.button_up.clicked.connect(self.up)
        self.button_down.clicked.connect(self.down)

        # endregion

        # display widgets
        # region
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
        widget_d = QWidget()
        widget_d.setLayout(layout_d)

        layout_t.addWidget(widget_pr)
        layout_t.addStretch(1)
        layout_t.addWidget(widget_d)
        layout_t.addWidget(widget_b)

        self.setLayout(layout_t)
        # endregion

        # auto refresh information
        self.refreshinfo.start(1000)
        self.refreshinfo.timeout.connect(self.setInfo)

        self.show()

    # display & refresh information
    def setInfo(self):
        if veh.vehicle_type == 'car':
            self.label_pos_x.setText("position x: " + str(CarController.carcontrol.GetCarPose().pos_x))
            self.label_pos_y.setText("position y: " + str(CarController.carcontrol.GetCarPose().pos_y))
            self.label_pos_z.setText("position z: " + str(CarController.carcontrol.GetCarPose().pos_z))

            self.label_rot_x.setText("Rotation x: " + str(CarController.carcontrol.GetCarPose().rot_x))
            self.label_rot_y.setText("Rotation y: " + str(CarController.carcontrol.GetCarPose().rot_y))
            self.label_rot_z.setText("Rotation z: " + str(CarController.carcontrol.GetCarPose().rot_z))

            self.label_speed_l.setText("Linear Speed: " + str(CarController.carcontrol.GetCarPose().speed_l))
            self.label_speed_a.setText("Angle Speed: " + str(CarController.carcontrol.GetCarPose().speed_a))
        else:
            self.label_pos_x.setText("GPS Altitude: " + str(DroneController.dronecontrol.GetState().gps_pos_altitude))
            self.label_pos_y.setText("GPS Latitude: " + str(DroneController.dronecontrol.GetState().gps_pos_latitude))
            self.label_pos_z.setText("GPS Longitude: " + str(DroneController.dronecontrol.GetState().gps_pos_longitude))

            self.label_rot_x.setText("Rotation W: " + str(DroneController.dronecontrol.GetState().ori_x))
            self.label_rot_y.setText("Rotation y: " + str(DroneController.dronecontrol.GetState().ori_y))
            self.label_rot_z.setText("Rotation z: " + str(DroneController.dronecontrol.GetState().ori_z))

            self.label_speed_l.setText("Linear Speed: " + str(DroneController.dronecontrol.GetState().linear_speed))
            self.label_speed_a.setText("Angle Speed: " + str(DroneController.dronecontrol.GetState().a_v_x))

    # move function
    def forward(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.GoForward(veh.acc)
        else:
            DroneController.dronecontrol.DroneMoveByTime(veh.acc, 0, 0)

    def backward(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.GoBackwardStart(veh.acc)
        else:
            DroneController.dronecontrol.DroneMoveByTime(-veh.acc, 0, 0)

    def left(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.Steer(veh.acc, -1)
        else:
            DroneController.dronecontrol.DroneMoveByTime(0, -veh.acc, 0)

    def right(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.Steer(veh.acc, 1)
        else:
            DroneController.dronecontrol.DroneMoveByTime(0, veh.acc, 0)

    def stop(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.Stop()
        else:
            pass

    def backwardend(self):
        if veh.vehicle_type == 'car':
            CarController.carcontrol.GoBackwardEnd()
        else:
            pass

    def up(self):
        DroneController.dronecontrol.DroneMoveByTime(0, 0, -veh.acc)

    def down(self):
        DroneController.dronecontrol.DroneMoveByTime(0, 0, veh.acc)


window = AirDroneClientWindow()
window.initUI()
window.setInfo()
sys.exit(app.exec())
