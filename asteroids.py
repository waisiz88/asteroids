from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, *type(self).containers)
        # Asteroid-specific initialization can go here