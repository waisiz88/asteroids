from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS, *type(self).containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)