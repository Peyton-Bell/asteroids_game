import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player

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

        # draw the player
        player.draw(screen)

        # update position of player(WASD)
        player.update(dt)

        # restrict game to 60fps
        clock.tick(60)

        # calculate delta time
        dt = clock.tick(60) / 1000

        # update the display
        pygame.display.flip()



if __name__ == "__main__":
    main()
