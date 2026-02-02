import pygame

class Food:
    def __init__(self, world, x: float, y: float, amount: int):
        self.world = world
        self.x = x
        self.y = y
        self.amount = amount
        self.color = (0, 255, 0)
        self.size = 4

    def take(self, amount: int) -> int:
        taken = min(self.amount, amount)
        self.amount -= taken
        return taken

    def render(self):
        if self.amount > 0:
            pygame.draw.circle(self.world.screen, self.color, (int(self.x), int(self.y)), self.size)
