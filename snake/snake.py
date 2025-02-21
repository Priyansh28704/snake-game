import pygame
import time
import random

pygame.init()

# Colors
blue = (51, 153, 255)
red = (255, 0, 0)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (255, 255, 0)

# Window settings
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

# Snake properties
snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

def user_score(score):
    score_text = score_font.render(f"Score: {score}", True, red)
    window.blit(score_text, [10, 10])

def game_snake(snake_size, snake_list):
    for pos in snake_list:
        pygame.draw.rect(window, green, [pos[0], pos[1], snake_size, snake_size])

def message(msg):
    msg_surface = font_style.render(msg, True, red)
    window.blit(msg_surface, [win_width / 6, win_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(grey)
            message("You Lost! Press P to Play Again or Q to Quit")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False  # Exit game
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = snake_size

        # Check if the snake hits the wall
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        
        # Draw food
        pygame.draw.rect(window, yellow, [foodx, foody, snake_size, snake_size])

        # Update snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        game_snake(snake_size, snake_list)
        user_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
