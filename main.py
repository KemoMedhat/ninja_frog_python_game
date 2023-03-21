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
WIDTH, HEIGHT = 900, 700
PLAYER_VEL = 5


window = pygame.display.set_mode((WIDTH,HEIGHT))
#=========================================================================================================
class Player(pygame.sprite.Sprite):
    COLOR = (255,255,0)
    GRAVITY = 1
#====== initiation function ============================
    def __init__(self,x, y, width, heght):
        self.rect = pygame.Rect(x, y, width, heght)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left" 
        self.animation_count = 0
        self.fall_count = 0
#====== main moving function ============================
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
#====== moving to left function ============================
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction !="left":
            self.direction = "left"
            self.animation_count = 0 
#====== moving to right function ============================      
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction !="right":
            self.direction = "right"
            self.animation_count = 0
#====== looping and drawing (the player) funcks function ============================
    def loop(self,fps):
        self.y_vel +=min(1,self.fall_count / fps * self.GRAVITY )
        self.move(self.x_vel, self.y_vel)
        self.fall_count +=1
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,self.rect)
#===================================================================================
def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def draw(window,backgrond,bg_image,player):
    for tile in backgrond:
        window.blit(bg_image,tile)
    player.draw(window)
    pygame.display.update()

def get_background(name):
    image = pygame.image.load(join("assets","background",name))
    _, _, width,height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width + 1):    # الاحداثيات بتبدأ من اعلي اليسار
        for j in range(HEIGHT // height + 1):
            pos = (i * width , j * height)
            tiles.append(pos)
    return tiles,image
#===================================================================================
def main(window):
    run = True
    backgroud, bg_image = get_background("Green.png")
    player = Player(100,100,50,50)
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        player.loop(FPS)
        handle_move(player)
        draw(window,backgroud,bg_image,player)
    pygame.quit()  
    quit()

if __name__ == "__main__":
    main(window)
    