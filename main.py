import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    # initializing pygame
    pygame.init()

    # Startup message
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create new clock object
    clock = pygame.time.Clock()
    dt = 0.0 # delta time

    # create empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add groups to Player class
    Player.containers = (updatable, drawable)

    # add groups to Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # add groups to AsteroidField class
    AsteroidField.containers = (updatable)

    # Insanitiate AsteroidField Object
    asteroidfield = AsteroidField()

    # Insanitiate Player Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # infinite game loop
    while True:

        # calling log state()
        log_state()

        # processing events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # make screen black
        screen.fill("black")

        # calling update on updatable group
        updatable.update(dt)

        # .draw() each item in the drawable group
        for drawing in drawable:
            drawing.draw(screen)

        # calculate delta time and restrict game to 60fps
        dt = clock.tick(60) / 1000

        # update the display
        pygame.display.flip()



if __name__ == "__main__":
    main()
