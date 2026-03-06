import pygame 
import random
import numpy as np

pygame.init()

# init variables
grid = np.zeros((20,20))
grid_size = 20
WIDTH,HEIGHT = grid.shape[0]*grid_size, grid.shape[1]*grid_size
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake ai goes brr")

while 