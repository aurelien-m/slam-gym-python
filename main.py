from world import World
from robot import Robot
from visualizer import Visualizer

world = World()
robot = Robot(world)
visualizer = Visualizer(robot)

for step in range(10):
    robot.move()

visualizer.show()
