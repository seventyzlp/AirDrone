import airsim
import time

class CarController():
    def __init__(self):
        # connect to the AirSim simulator
        self.client = airsim.CarClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        print("API Control enabled: %s" % self.client.isApiControlEnabled())
        self.car_controls = airsim.CarControls()
        # self.ConnectionState = True
        self.car_state = airsim.CarState()

    """
    def ConformConnection(self):
        if self.ping():
            print("Connected!")
        else:
            print("Ping returned false!")
"""

    def GoForward(self, v):
        self.car_controls.throttle = v
        self.car_controls.steering = 0
        self.client.setCarControls(self.car_controls)
        print("Go Forward")
        time.sleep(3)

    def Steer(self, v, steering):
        self.car_controls.throttle = v
        self.car_controls.steering = steering
        self.client.setCarControls(self.car_controls)
        print("Steer")

    def GetCarPose(self):
        # print(self.car_state)
        print(airsim.CarState)


if __name__ == "__main__":
    Car = CarController()
    Car.Steer(0.5,-1)
    time.sleep(5)
    Car.GetCarPose()