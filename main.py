import pygame
from pygame.time import Clock
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        # make the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # make a black screen and draw the player
        screen.fill("black")
        # update to check movement
        player.update(dt)
        # draw the triangle
        player.draw(screen)
        #refresh the dispaly
        pygame.display.flip()

        # limit framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
