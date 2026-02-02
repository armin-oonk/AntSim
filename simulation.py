import pygame
import random

from Ant import Ant
from Nest import Nest
from World import World

# Initialize Pygame
pygame.init()

# Constants
width = 800
height = 600
world = World(width, height)

# Set up the display
world.screen = pygame.display.set_mode((world.width, world.height))
pygame.display.set_caption("Ant Colony Simulation")


running = True
clock = pygame.time.Clock()

nest = Nest(world=world, x=width/2, y=height/2, color=(255, 0, 0), size=10.0)
ants = list()
max_nr_ants = 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    world.render()

    if not nest.is_full():
        nest.create_ant()

    nest.render()
    # # Create a new ant if we have not reached the max
    # if len(ants) != max_nr_ants:
    #     ants.append(Ant(world=world, x=400.0, y=300.0, size=5.0))
    #
    # # Run the ants
    # for a in ants:
    #     a.run()
    #     a.render()


    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
