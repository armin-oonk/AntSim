import math
from enum import Enum, auto
import random

import pygame

from World import World


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def limit(val: float, min_val: float, max_val: float) -> float:
    if val < min_val:
        return min_val
    elif val > max_val:
        return max_val
    else:
        return val

class Ant:
    def __init__(self, world: World, initial: dict=None):
        self.world = world
        self.ANT_COLOR = (255, 0, 0)  # Red ants
        self.step_size = 2.0

        if initial is None:
            self.x, self.y = self.world.random_position()
            self.direction = random.random()

            self.width = 5
            self.height = 5
        else:
            self.x = initial['x']
            self.y = initial['y']
            self.direction = initial['direction']
            self.width = initial['width']
            self.height = initial['height']

    def get_new_direction(self) -> float:
        # Generate a new random direction based on the old direction
        # Add a Gaussian random number to the current direction
        # Adjust the standard deviation (e.g., 0.1) to control how much the ant turns
        new_direction = self.direction + random.gauss(0, 0.1)
        return new_direction

    def run(self):
        self.direction = self.get_new_direction()
        self.x += self.step_size * math.sin(2.0 * math.pi * self.direction)
        self.y += self.step_size * math.cos(2.0 * math.pi * self.direction)

        self.x = limit(self.x, 0, self.world.width)
        self.y = limit(self.y, 0, self.world.height)


    def render(self):
        # Draw a rectangle in the world
        rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(self.world.screen, self.ANT_COLOR, rect)
