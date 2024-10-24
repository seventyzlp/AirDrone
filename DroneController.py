import airsim
import time
import math
import keyboard

class DroneInfo():
    gps_pos_altitude = 0
    gps_pos_latitude = 0
    gps_pos_longitude = 0

    ori_w = 0
    ori_x = 0
    ori_y = 0
    ori_z = 0

    # linear_velocity
    l_v_x = 0
    l_v_y = 0
    l_v_z = 0

    # angular_velocity
    a_v_x = 0
    a_v_y = 0
    a_v_z = 0

    roll = 0
    yaw = 0
    pitch = 0

    linear_speed = 0


class Drone():
    def __init__(self):
        # connect to the AirSim simulator
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def TakeOff(self):
        if airsim.LandedState.Landed == 0:
            self.client.takeoffAsync().join()
            print("take off")
        else:
            self.client.hoverAsync().join()
            print("already flying")

    def Landed(self):
        if airsim.LandedState.Landed == 1:
            print("already landed")
        else:
            self.client.landAsync().join()
            print("now landing")

    def DroneMoveByTime(self, vx, vy, vz, duration=3):
        print("now speed", vx, vy, vz)
        self.client.moveByVelocityAsync(vx, vy, vz, duration)
        time.sleep(duration)
        print("End Moving")

    def GetState(self):
        # State = self.client.getMultirotorState()
        State = DroneInfo()
        gps_pos = self.client.getMultirotorState().gps_location
        State.gps_pos_altitude = gps_pos.altitude
        State.gps_pos_longitude = gps_pos.longitude
        State.gps_pos_latitude = gps_pos.latitude

        orientation = self.client.getMultirotorState().kinematics_estimated.orientation
        State.ori_w = orientation.w_val
        State.ori_x = orientation.x_val
        State.ori_y = orientation.y_val
        State.ori_z = orientation.z_val

        a_velocity = self.client.getMultirotorState().kinematics_estimated.angular_velocity
        State.a_v_x = a_velocity.x_val
        State.a_v_y = a_velocity.y_val
        State.a_v_z = a_velocity.z_val

        l_velocity = self.client.getMultirotorState().kinematics_estimated.linear_velocity
        State.l_v_x = l_velocity.x_val
        State.l_v_y = l_velocity.y_val
        State.l_v_z = l_velocity.z_val

        State.roll = self.client.getMultirotorState().rc_data.roll
        State.yaw = self.client.getMultirotorState().rc_data.yaw
        State.pitch = self.client.getMultirotorState().rc_data.pitch

        State.linear_speed = math.sqrt(pow(State.l_v_x,2)+pow(State.l_v_y,2)+pow(State.l_v_z,2))

        return State
    def Hover(self):
        landed = self.client.getMultirotorState()

    def MoveToPosition(self,x,y,z,duration=3):
        self.client.moveToPositionAsync(x, y, z, duration).join()

    def Reset(self):
        self.client.reset()

    def SnowTeleport(self):
        position = airsim.Vector3r(9.87236677 , -279.41862836, -22.81082173) # snow
        # position = airsim.Vector3r(68.46729401 , 81.05318001, 60.85758088) # normal
        heading = airsim.utils.to_quaternion(0, 0, 0)
        pose = airsim.Pose(position, heading)
        self.client.simSetVehiclePose(pose, True)
    def CloseAPI(self):
        self.client.enableApiControl(False)

    def KeyboardControl(self,x):
        w = keyboard.KeyboardEvent('down', 28, 'w')             # 前进
        s = keyboard.KeyboardEvent('down', 28, 's')             # 后退
        a = keyboard.KeyboardEvent('down', 28, 'a')             # 左移
        d = keyboard.KeyboardEvent('down', 28, 'd')             # 右移
        up = keyboard.KeyboardEvent('down', 28, 'up')           # 上升
        down = keyboard.KeyboardEvent('down', 28, 'down')       # 下降
        left = keyboard.KeyboardEvent('down', 28, 'left')       # 左转
        right = keyboard.KeyboardEvent('down', 28, 'right')     # 右转
        k = keyboard.KeyboardEvent('down', 28, 'k')             # 获取控制
        l = keyboard.KeyboardEvent('down', 28, 'l')             # 释放控制
        if x.event_type == 'down' and x.name == w.name:
            # 前进
            self.client.moveByVelocityBodyFrameAsync(3, 0, 0, 0.5)
            print("forward")
        elif x.event_type == 'down' and x.name == s.name:
            # 后退
            self.client.moveByVelocityBodyFrameAsync(-3, 0, 0, 0.5)
            print("back")
        elif x.event_type == 'down' and x.name == a.name:
            # 左移
            self.client.moveByVelocityBodyFrameAsync(0, -2, 0, 0.5)
            print("left")
        elif x.event_type == 'down' and x.name == d.name:
            # 右移
            self.client.moveByVelocityBodyFrameAsync(0, 2, 0, 0.5)
            print("right")
        elif x.event_type == 'down' and x.name == up.name:
            # 上升
            self.client.moveByVelocityBodyFrameAsync(0, 0, -0.5, 0.5)
            print("up")
        elif x.event_type == 'down' and x.name == down.name:
            # 下降
            self.client.moveByVelocityBodyFrameAsync(0, 0, 0.5, 0.5)
            print("down")
        elif x.event_type == 'down' and x.name == left.name:
            # 左转
            self.client.rotateByYawRateAsync(-20, 0.5)
            print("turn left")
        elif x.event_type == 'down' and x.name == right.name:
            # 右转
            self.client.rotateByYawRateAsync(20, 0.5)
            print("turn right")
        elif x.event_type == 'down' and x.name == k.name:
            # 无人机起飞
            # get control
            self.client.enableApiControl(True)
            print("get control")
            # unlock
            self.client.armDisarm(True)
            print("unlock")
            # Async methods returns Future. Call join() to wait for task to complete.
            self.client.takeoffAsync().join()
            print("takeoff")
        elif x.event_type == 'down' and x.name == l.name:
            keyboard.wait("l")
            keyboard.unhook_all()
        else:
            # 没有按下按键
            self.client.moveByVelocityBodyFrameAsync(0, 0, 0, 0.5).join()
            self.client.hoverAsync().join()  # 第四阶段：悬停6秒钟
            print("hovering")




if __name__ == '__main__':
    myDrone = Drone()
    myDrone.SnowTeleport()

dronecontrol = Drone()

