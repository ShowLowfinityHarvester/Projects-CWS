import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define display dimensions
WIDTH = 600
HEIGHT = 400

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define clock for controlling frame rate
clock = pygame.time.Clock()

# Define snake properties
snake_block = 10  # Size of one block of the snake (and grid size)
snake_speed = 15  # Speed of snake movement (higher = faster)

# Define font for displaying score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Function to display score
def display_score(score):
    value = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    # Initial snake body
    snake_list = []
    snake_length = 1

    # Generate initial food position
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Game over screen (if the player loses)
        while game_close:
            screen.fill(BLUE)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            display_score(snake_length - 1)
            pygame.display.update()

            # Handling game-over events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling movement input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Update the snake's position
        x += x_change
        y += y_change

        # Check for boundary collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update the screen
        screen.fill(BLUE)

        # Draw the food
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

        # Update the snake's body
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_block, snake_list)

        # Display the current score
        display_score(snake_length - 1)

        # Update the screen
        pygame.display.update()

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Control the frame rate
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

# Run the game loop
game_loop()
