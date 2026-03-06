import pygame 
import random
import numpy as np
import sys

pygame.init()

# init variables
grid = np.zeros((20,20))
grid_size = 20
WIDTH,HEIGHT = grid.shape[0]*grid_size+3, grid.shape[1]*grid_size+3
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake ai goes brr")
clock = pygame.time.Clock()
grid[(9,9)]=1 # snake head
grid[(random.randint(0,len(grid)-1),random.randint(0,len(grid[1])-1))]=2

def draw_board(grid,screen):
    for r in range(len(grid)):
        for c,col in enumerate(grid[r]):
            if col == 0:
                rect_obj = pygame.Rect((grid_size*c+3,grid_size*r+3),(grid_size-3,grid_size-3))
                pygame.draw.rect(screen,"black",rect_obj)
            if col ==1:
                rect_obj = pygame.Rect((grid_size*c+3,grid_size*r+3),(grid_size-3,grid_size-3))
                pygame.draw.rect(screen,"green",rect_obj)
            if col == 2:
                rect_obj = pygame.Rect((grid_size*c+3,grid_size*r+3),(grid_size-3,grid_size-3))
                pygame.draw.rect(screen,"red",rect_obj)


def move_snake(grid,vel_x,vel_y=0):
    
    indices = np.where(grid==1)
    if vel_x>0:
        x = min(indices[1]+1,len(grid[1])-1)
        grid[indices]=0
        grid[(indices[0],x)]=1

    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
    screen.fill("white")
    draw_board(grid,screen)
    move_snake(grid)
    pygame.display.update()
    clock.tick(60)
