from world import World


class Robot:
    def __init__(self, world: World, move_clock_step: float = 1.0):
        self.move_clock_step = move_clock_step
        self.world = world
        self.history = []
        self.clock = 0

        self.theta = 0
        self.x = 0
        self.y = 0

    def __update_history(self):
        self.history.append(
            {"x": self.x, "y": self.y, "theta": self.theta, "clock": self.clock}
        )

    def move(self):
        self.x += 1
        self.clock += self.move_clock_step
        self.__update_history()
