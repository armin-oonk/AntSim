import pygame

from Ant import Ant
from World import World


class Nest:
    def __init__(self, world: World, x: float, y: float, color: tuple[int, int, int], size: float):
        self.world = world
        self.x = x
        self.y = y
        self.color = color
        self.size = size

        self.ants = list()
        self.max_nr_ants = 50

    def is_full(self):
        return len(self.ants) >= self.max_nr_ants

    def create_ant(self):
        self.ants.append(Ant(world=self.world, x=self.x, y=self.y, size=5.0, color=self.color))

    def render(self):
        for a in self.ants:
            a.run()
            a.render()

        pygame.draw.circle(self.world.screen, self.color, (int(self.x), int(self.y)), int(self.size))
