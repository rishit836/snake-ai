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

fruit_x,fruit_y = random.randrange(0, WIDTH, head_size),random.randrange(0, HEIGHT, head_size)
velx,vely=0,0
score=0
snake = [((WIDTH-head_size)//2,(HEIGHT-head_size)//2)]
move_delay = 6
frame_count = 0

def draw_snake(screen,snake):
    for idx,body in enumerate(snake):
        rect_obj = pygame.Rect((body[0],body[1]),(head_size,head_size))
        pygame.draw.rect(screen,"green",rect_obj)
        if idx == 0:
            head = rect_obj

    return head
def move_snake(snake,velx,vely,grow=False):
    head_x,head_y=snake[0]
    head_x+=velx
    head_y+=vely
    snake.insert(0,(head_x,head_y))
    if not grow:
        snake.pop()
    return snake
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velx == 0:
                velx = head_size
                vely = 0

            elif event.key == pygame.K_LEFT and velx == 0:
                velx = -head_size
                vely = 0

            elif event.key == pygame.K_UP and vely == 0:
                velx = 0
                vely = -head_size

            elif event.key == pygame.K_DOWN and vely == 0:
                velx = 0
                vely = head_size
            

    screen.fill("black")
    head = draw_snake(screen,snake)
    frame_count += 1

    # draw fruit
    fruit = pygame.Rect((fruit_x,fruit_y),(head_size,head_size))
    pygame.draw.rect(screen,"red",fruit)

    if frame_count >= move_delay:

        snake = move_snake(snake, velx, vely, grow=False)

        head_x, head_y = snake[0]

        if fruit.colliderect(head):
            snake.append(snake[-1])   # grow
            fruit_x = random.randrange(0, WIDTH, head_size)
            fruit_y = random.randrange(0, HEIGHT, head_size)
            score += 1

        frame_count = 0
    


    pygame.display.flip()
    clock.tick(60)
    # game over
    if not 0<=snake[0][0]<WIDTH:
        print("game over bitch!")
        break
    if not 0<=snake[0][1]<=HEIGHT:
        print("game over bitch!")
        break
