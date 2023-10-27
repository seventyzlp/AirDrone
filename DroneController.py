import airsim
import time

class DroneInfo():
    speed_x = 0


class Drone():
    def __init__(self):
        # connect to the AirSim simulator
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def TakeOff(self):
        landed = self.client.getMultirotorState().landed_state
        if landed == airsim.LandedState.Landed:
            self.client.takeoffAsync().join()
            print("take off")
        else:
            self.client.hoverAsync().join()
            print("already flying")

    def Landed(self):
        landed = self.client.getMultirotorState().landed_state
        if landed == airsim.LandedState.Landed:
            print("already landed")
        else:
            self.client.landAsync().join()

    def DroneMove(self,vx,vy,vz):
        self.client.moveByVelocityAsync(vx,vy,vz)



if __name__ == '__main__':

    myDrone = Drone()
    myDrone.TakeOff()
