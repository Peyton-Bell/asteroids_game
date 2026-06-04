import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH

class Shot(CircleShape):

    # constructor
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    # override draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # override update method
    def update(self, dt):
        self.position += self.velocity * dt