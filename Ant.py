from enum import Enum, auto
import random

import pygame

from World import World


class Direction(Enum):
    NORTH = auto
    EAST = auto
    SOUTH = auto
    WEST = auto


def get_random_direction():
    return random.choice(list(Direction))


class Ant:
    def __init__(self, world: World, initial: dict=None):
        self.world = world
        self.ANT_COLOR = (255, 0, 0)  # Red ants

        if initial is None:
            self.x, self.y = self.world.random_position()
            self.direction = get_random_direction()
            self.width = 5
            self.height = 5
        else:
            self.x = initial['x']
            self.y = initial['y']
            self.direction = initial['direction']
            self.width = initial['width']
            self.height = initial['height']

    def run(self):
        pass

    def render(self):
        # Draw a rectangle in the world
        rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(self.world.screen, self.ANT_COLOR, rect)



