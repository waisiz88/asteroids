import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, *groups):
        super().__init__(*groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(
            screen,
            (255, 255, 255), # white color
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2 # line width
        )

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def collides_with(self, other):
        return self.position.distance_to(other.position) < (self.radius + other.radius)