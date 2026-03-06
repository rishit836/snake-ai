import numpy as np
import random
import sys
import pygame

pygame.init()

# variables
head_size = 25
WIDTH,HEIGHT = 500,500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake ai goess brr")
clock = pygame.time.Clock()
head_x,head_y = (WIDTH-head_size)/2,(HEIGHT-head_size)/2
fruit_x,fruit_y = random.randint(0,WIDTH-head_size),random.randint(0,HEIGHT-head_size)
velx,vely=0,0


def draw_snake(screen,head_x,head_y):
    rect_obj = pygame.Rect((head_x,head_y),(head_size,head_size))
    pygame.draw.rect(screen,"green",rect_obj)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velx=5
                vely=0
            if event.key == pygame.K_LEFT:
                velx=-5
                vely=0
            if event.key == pygame.K_UP:
                velx=0
                vely=-5
            if event.key == pygame.K_DOWN:
                velx=0
                vely=5
            

    screen.fill("black")
    draw_snake(screen,head_x,head_y)
    head_x+=velx
    head_y+=vely
    pygame.display.flip()
    clock.tick(60)
    # game over
    if not 0<=head_x<=WIDTH:
        print("game over bitch!")
        break
    if not 0<=head_y<=HEIGHT:
        print("game over bitch!")
        break
