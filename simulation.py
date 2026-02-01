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

ants = list()
max_nr_ants = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    world.render()

    # Create a new ant if we have not reached the max
    if len(ants) != max_nr_ants:
        ants.append(Ant(world=world))

    # Run the ants
    for a in ants:
        a.run()
        a.render()


    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
