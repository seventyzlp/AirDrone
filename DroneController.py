import airsim
import time


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

    def DroneMoveByTime(self, vx, vy, vz, duration=0):
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

        return State
    def Hover(self):
        landed = self.client.getMultirotorState()

    def MoveToPosition(self,x,y,z,duration=3):
        self.client.moveToPositionAsync(x, y, z, duration).join()

    def Reset(self):
        self.client.reset()




if __name__ == '__main__':
    myDrone = Drone()
    # myDrone.TakeOff()
    # time.sleep(1)
    # print(myDrone.GetState())
    print(myDrone.client.getMultirotorState().landed_state)
    # myDrone.Hover()
    # myDrone.DroneMoveByTime(3,3,-5,2)
    # myDrone.Landed()
    # print(myDrone.client.getMultirotorState().landed_state)
