import rerun as rr

from robot import Robot


class Visualizer:
    def __init__(self, robot: Robot):
        self.robot = robot
        rr.init("SLAM Gym", spawn=True)

    def show(self):
        for pose in self.robot.history:
            rr.set_time_seconds("robot_clock", pose["clock"])
            rr.log_point("simple", position=[pose["x"], pose["y"]])
            rr.log_arrow("simple", origin=[pose["x"], pose["y"], 0], vector=[1, 0, 0])
