import pygame
pygame.init
from constants import *


def main():
    print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    pygame.Surface.fill(screen, (0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
    main()
