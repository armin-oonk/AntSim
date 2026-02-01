import pygame
import random

from Ant import Ant
from World import World

# Initialize Pygame
pygame.init()

# Constants
world = World(800, 600)

# Set up the display
world.screen = pygame.display.set_mode((world.width, world.height))
pygame.display.set_caption("Ant Colony Simulation")


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    world.render()

    # Draw the ants
    for _ in range(50):
        ant = Ant(world=world)
        ant.render()

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
