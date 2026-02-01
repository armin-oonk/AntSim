import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 5  # Size of each pixel/cell in screen pixels
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BG_COLOR = (0, 0, 0)
ANT_COLOR = (255, 0, 0)  # Red ants

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Colony Simulation")

def draw_ants(surface):
    # Example: Set some random pixels to the ant color
    # In a real simulation, you would iterate over your ant objects
    # Here we just demonstrate setting a color at a grid coordinate
    
    # Let's place 50 random ants
    for _ in range(50):
        grid_x = random.randint(0, GRID_WIDTH - 1)
        grid_y = random.randint(0, GRID_HEIGHT - 1)
        
        # Calculate screen coordinates
        screen_x = grid_x * GRID_SIZE
        screen_y = grid_y * GRID_SIZE
        
        # Draw a rectangle representing the pixel
        rect = pygame.Rect(screen_x, screen_y, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, ANT_COLOR, rect)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BG_COLOR)

    # Draw the ants
    draw_ants(screen)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
