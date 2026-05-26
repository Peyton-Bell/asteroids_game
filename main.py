import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state

def main():
    # initializing pygame
    pygame.init()

    # Startup message
    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite loop
    while True:
        # processing events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # make screen black
        screen.fill("black")

        # update the display (must be called last)
        pygame.display.flip()

if __name__ == "__main__":
    main()
