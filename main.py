# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.time import Clock
from constants import *
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # make the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # make a black screen
        screen.fill("black")
        pygame.display.flip()

        # limit framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
