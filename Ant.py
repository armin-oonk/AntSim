from enum import Enum, auto
import random

import pygame

from World import World


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def get_random_direction():
    return random.choice(list(Direction))


class Ant:
    def __init__(self, world: World, initial: dict=None):
        self.world = world
        self.ANT_COLOR = (255, 0, 0)  # Red ants
        self.step_size = 1

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

    def get_new_direction(self) -> Direction:
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST
        }

        choices = list()

        for d in Direction:
            if d != opposites.get(self.direction):
                new_x, new_y = self.get_next_position(d)
                if 0 <= new_x <= self.world.width and 0 <= new_y <= self.world.height:
                    choices.append(d)

        # Create a weighted list, favour the current direction
        weight = list()
        for c in choices:
            if c == self.direction:
                weight.append(25)
            else:
                weight.append(1)

        return random.choices(choices, weights=weight, k=1)[0]

        # return random.choice(choices)

    def get_next_position(self, direction: Direction) -> tuple[int, int]:
        new_x = self.x
        new_y = self.y
        if direction == Direction.NORTH:
            new_y -= self.step_size
        elif direction == Direction.SOUTH:
            new_y += self.step_size
        elif direction == Direction.EAST:
            new_x += self.step_size
        elif direction == Direction.WEST:
            new_x -= self.step_size
        return new_x, new_y

    def run(self):
        self.direction = self.get_new_direction()
        self.x, self.y = self.get_next_position(direction=self.direction)

    def render(self):
        # Draw a rectangle in the world
        rect = pygame.Rect(self.x, self.y, self.width, self.width)
        pygame.draw.rect(self.world.screen, self.ANT_COLOR, rect)
