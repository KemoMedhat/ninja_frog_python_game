import time
import os
import pygame
import math
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Ninja Frog")

BG_COLOR = (255,255,255)
WIDTH, HEIGHT = 400, 600
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))

def main(window):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()  
    quit()

if __name__ == "__main__":
    main(window)
    