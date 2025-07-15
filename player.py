import pygame # this allows us to use code from the open-source pygame library throughout this file
from circleshape import CircleShape
from constants import *

class Player(CircleShape): # this is the player class that inherits from the CircleShape class
    def __init__(self, x, y, *groups): # updated constructor to accept groups
        super().__init__(x, y, PLAYER_RADIUS, *groups) # pass groups to parent
        self.rotation = 0 # this is the rotation of the player

    # in the player class
    def triangle(self): # this is the method that draws the player on the screen
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # this is the forward vector of the player
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # this is the right vector of the player
        a = self.position + forward * self.radius # this is the top point of the player
        b = self.position - forward * self.radius - right # this is the left point of the player
        c = self.position - forward * self.radius + right # this is the right point of the player
        return [a, b, c] # this is the return value of the triangle method

    def draw(self, screen): # this is the method that draws the player on the screen
        pygame.draw.polygon( # this is the method that draws the player on the screen
            screen, # this is the screen to draw on
            (255, 255, 255), # this is the color of the player
            self.triangle(), # this is the triangle to draw
            2 # this is the thickness of the line
        )
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a]:
            self.rotate(-dt)
    
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.position.x = max(0, min(SCREEN_WIDTH, self.position.x))
        self.position.y = max(0, min(SCREEN_HEIGHT, self.position.y))

