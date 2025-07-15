import pygame # this allows us to use code from the open-source pygame library throughout this file
from constants import * # this imports all the constants from the constants.py file
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # this creates a window that is the size of the screen

def main(): # this is the main function that runs the game
    pygame.init() # this initializes the pygame library
    print("Starting Asteroids!") # this prints a message to the console
    print(f"Screen width: {SCREEN_WIDTH}") # this prints the screen width to the console
    print(f"Screen height: {SCREEN_HEIGHT}") # this prints the screen height to the console

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, updatable, drawable)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock() # this creates a clock object that we can use to control the frame rate of the game
    dt = 0 # this is the time since the last frame

    while True: # this is the main game loop
        screen.fill((0, 0, 0)) # this fills the screen with black

        for event in pygame.event.get(): # this is the event loop that checks for events
            if event.type == pygame.QUIT: # this is the event that happens when the user clicks the close button
                return

        dt = clock.tick(60) / 1000.0 # this is the time since the last frame
        # print(f"Frame time: {dt}") # this prints the frame time to the console

        updatable.update(dt)

        # Collision detection: check if player collides with any asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                exit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

if __name__ == "__main__": # this is the main function that runs the game
    main() # this is the main function that runs the game
