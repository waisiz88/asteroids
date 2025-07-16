from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, *type(self).containers)
        # Asteroid-specific initialization can go here

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Otherwise, spawn two smaller asteroids
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        from asteroids import Asteroid  # local import to avoid circular import
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2