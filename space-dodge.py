import pygame
import time
import random
import sys

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.image.load("bg.jpeg")


def draw():
    WIN.blit(BG, (0, 0))


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
