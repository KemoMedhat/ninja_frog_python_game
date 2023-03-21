import time
import os
import pygame
import math
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Ninja Frog")

WIDTH, HEIGHT = 900, 700
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))
def get_background(name):
    image = pygame.image.load(join("assets","background",name))
    _, _, width,height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width , j * height)
            tiles.append(pos)
    return tiles,image
def draw(window,backgrond,bg_image):
    for tile in backgrond:
        window.blit(bg_image,tile)
    pygame.display.update()

def main(window):
    run = True
    backgroud, bg_image = get_background("Green.png")
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window,backgroud,bg_image)
    pygame.quit()  
    quit()

if __name__ == "__main__":
    main(window)
    