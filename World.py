import random

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = None
        self.BG_COLOR = (0, 0, 0)

    def render(self):
        # Start of the render
        self.screen.fill(self.BG_COLOR)


    def random_position(self) -> tuple[float, float]:
        return random.uniform(0, self.width), random.uniform(0, self.height)