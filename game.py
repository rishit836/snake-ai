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
next_velx, next_vely = 0, 0
score=0
snake = [((WIDTH // (2 * head_size)) * head_size, (HEIGHT // (2 * head_size)) * head_size)]
move_delay = 6
frame_count = 0
show_grid = False
game_over = False

# fonts
score_font = pygame.font.SysFont("consolas", 22, bold=True)
game_over_font = pygame.font.SysFont("consolas", 36, bold=True)
subtitle_font = pygame.font.SysFont("consolas", 18)
grid_font = pygame.font.SysFont("consolas", 14)

# numpy : 0=empty, 1=snake, 2=fruit
grid_rows, grid_cols = HEIGHT // head_size, WIDTH // head_size
grid = np.zeros((grid_rows, grid_cols), dtype=np.int8)

def update_grid(snake, fruit_x, fruit_y):
    grid[:] = 0
    for (sx, sy) in snake:
        grid[sy // head_size, sx // head_size] = 1
    grid[fruit_y // head_size, fruit_x // head_size] = 2
    return grid

def draw_snake(screen, snake):
    for idx, body in enumerate(snake):
        rect_obj = pygame.Rect(body[0], body[1], head_size, head_size)
        color = (0, 200, 0) if idx == 0 else (0, 160, 0)
        pygame.draw.rect(screen, color, rect_obj)
        pygame.draw.rect(screen, (0, 100, 0), rect_obj, 1)
    return pygame.Rect(snake[0][0], snake[0][1], head_size, head_size)
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
            if game_over:
                if event.key == pygame.K_r:
                    # restart
                    snake = [((WIDTH // (2 * head_size)) * head_size, (HEIGHT // (2 * head_size)) * head_size)]
                    velx, vely = 0, 0
                    next_velx, next_vely = 0, 0
                    score = 0
                    fruit_x = random.randrange(0, WIDTH, head_size)
                    fruit_y = random.randrange(0, HEIGHT, head_size)
                    game_over = False
                continue

            if event.key == pygame.K_RIGHT and velx == 0:
                next_velx = head_size
                next_vely = 0

            elif event.key == pygame.K_LEFT and velx == 0:
                next_velx = -head_size
                next_vely = 0

            elif event.key == pygame.K_UP and vely == 0:
                next_velx = 0
                next_vely = -head_size

            elif event.key == pygame.K_DOWN and vely == 0:
                next_velx = 0
                next_vely = head_size

            elif event.key == pygame.K_g:
                show_grid = not show_grid

    screen.fill((20, 20, 20))

    if game_over:
        # game over screen
        go_text = game_over_font.render("GAME OVER", True, (220, 50, 50))
        score_text = subtitle_font.render(f"Score: {score}", True, "white")
        restart_text = subtitle_font.render("Press R to restart", True, (180, 180, 180))
        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2 - 60))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))
        pygame.display.flip()
        clock.tick(60)
        continue

    # movement tick
    frame_count += 1
    if frame_count >= move_delay:
        velx, vely = next_velx, next_vely
        grow = False

        # check if we'll eat fruit before moving
        future_x = snake[0][0] + velx
        future_y = snake[0][1] + vely
        if future_x == fruit_x and future_y == fruit_y:
            grow = True
            score += 1
            fruit_x = random.randrange(0, WIDTH, head_size)
            fruit_y = random.randrange(0, HEIGHT, head_size)
            # make sure fruit doesn't spawn on snake
            while (fruit_x, fruit_y) in snake:
                fruit_x = random.randrange(0, WIDTH, head_size)
                fruit_y = random.randrange(0, HEIGHT, head_size)

        snake = move_snake(snake, velx, vely, grow=grow)
        frame_count = 0

        # wall collision
        hx, hy = snake[0]
        if not (0 <= hx < WIDTH and 0 <= hy < HEIGHT):
            game_over = True
            continue

        # self collision
        if snake[0] in snake[1:]:
            game_over = True
            continue

    # draw everything
    head = draw_snake(screen, snake)

    # draw fruit
    fruit_rect = pygame.Rect(fruit_x, fruit_y, head_size, head_size)
    pygame.draw.rect(screen, (220, 30, 30), fruit_rect)
    pygame.draw.rect(screen, (180, 20, 20), fruit_rect, 1)

    # update numpy grid
    update_grid(snake, fruit_x, fruit_y)

    # draw grid overlay (toggle with G)
    if show_grid:
        for r in range(grid_rows):
            for c in range(grid_cols):
                val = grid[r, c]
                if val != 0:
                    label = grid_font.render(str(val), True, "white")
                    screen.blit(label, (c * head_size + 7, r * head_size + 4))
                pygame.draw.rect(screen, (40, 40, 40),
                    pygame.Rect(c * head_size, r * head_size, head_size, head_size), 1)

    # score display
    score_surface = score_font.render(f"Score: {score}", True, "white")
    screen.blit(score_surface, (10, 8))

    pygame.display.flip()
    clock.tick(60)
