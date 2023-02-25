import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0

# Set up the food
food_block = 10
food_x = round(random.randrange(0, width - food_block) / 10.0) * 10.0
food_y = round(random.randrange(0, height - food_block) / 10.0) * 10.0

# Define the function to display the score
def display_score(score):
    text = font.render("Score: " + str(score), True, black)
    window.blit(text, [0, 0])

# Define the function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Define the main game loop
def game_loop():
    # Set up the variables
    game_over = False
    game_close = False
    score = 0

    # Start the game
    while not game_over:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Move the snake
        x1 += x1_change
        y1 += y1_change

        # Check for collisions with the walls
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the snake list
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and the food
        window.fill(white)
        draw_snake(snake_block, snake_list)
        pygame.draw.rect(window, red, [food_x, food_y, food_block, food_block])

        # Update the score
        display_score(score)

        # Check for collisions with the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width,food_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - food_block) / 10.0) * 10.0
            snake_length += 1
            score += 10
