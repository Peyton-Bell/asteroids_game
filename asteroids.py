import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):

    # constructor
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    # override draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # update position of asteroid
    def update(self, dt):
        self.position += self.velocity * dt