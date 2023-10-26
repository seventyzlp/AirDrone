import airsim
import time


class Drone():
    def __init__(self):
        # connect to the AirSim simulator
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def isLanded(self):
        landed = self.client.getMultirotorState().landed_state
        if landed == airsim.LandedState.Landed:
            print("taking off...")
            self.client.takeoffAsync().join()
        else:
            print("already flying...")
            self.client.hoverAsync().join()

    def forward(self):
        self.car_controls.throttle = 0.5
        self.car_controls.steering = 0

        print("Go Forward")
        time.sleep(3)  # let car drive a bit

    def