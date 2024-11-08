import pygame
from pygame.locals import *
from snake import *
from apple import *
from walls import *

GAME_ON = True
SPEED = 10
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Create game objects
screen_size = 400  # Adjust according to your game screen dimensions
snake = Snake(screen_size)
apple = Apple()
apple.set_random_position(400)

# Initialize walls
walls = [
    Wall(100, 100, 200, 10),  # Horizontal inner wall
    Wall(150, 250, 10, 100)   # Vertical inner wall
]

# Apple count variable
score = 0

# High score variable
high_score = 0

# Function to load high score from a file
def load_high_score():
    global high_score
    try:
        with open("high_score.txt", "r") as file:
            # Read the content of the file and try to convert it to an integer
            content = file.read().strip()  # Strip to remove any leading/trailing whitespace
            if content:  # Check if content is not empty
                high_score = int(content)  # Convert to integer
            else:
                high_score = 0  # Set high score to 0 if content is empty
    except FileNotFoundError:
        high_score = 0  # Set high score to 0 if the file doesn't exist
    except ValueError:
        high_score = 0  # Set high score to 0 if the file contains invalid data

# Function to save high score to a file
def save_high_score():
    global high_score
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

# Render and display the apple count
def show_score():
    """Displays the score board."""
    font = pygame.font.Font(None, 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))  # Display score in the top left corner

def game_over_screen():
    """Displays the game-over screen with the score and high score."""
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)  # Display score
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)  # Display high score

    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    high_score_rect = high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(game_over_text, text_rect)  # Display "Game Over" text
    screen.blit(score_text, score_rect)  # Display score
    screen.blit(high_score_text, high_score_rect)  # Display high score
    pygame.display.flip()  # Update display

    pygame.time.delay(2000)  # Wait for 2 seconds before quitting

def pause_game():
    """Pauses the game until the player presses 'P' to resume."""
    font = pygame.font.Font(None, 50)
    pause_text = font.render("Paused", True, WHITE)
    text_rect = pause_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    paused = True
    while paused:
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(pause_text, text_rect)  # Display paused text
        pygame.display.flip()  # Update display

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_p:  # Press 'P' to resume
                paused = False

# Load high score when the game starts
load_high_score()

while GAME_ON:
    # Clear screen
    screen.fill((0, 0, 0))
    clock.tick(SPEED)

    snake.crawl()  # Update snake position

    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False
        elif event.type == KEYDOWN:
            if event.key == K_p:  # Pause when 'P' is pressed
                pause_game()
            elif event.key == K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    # Check for wall collisions and self collision
    for wall in walls:
        wall.draw(screen)  # Draw each wall
        if snake.snake[-1][0] in range(wall.x, wall.x + wall.width) and snake.snake[-1][1] in range(wall.y,
                                                                                        wall.y + wall.height):
            game_over_screen()
            GAME_ON = False

    # Check if snake eats apple
    if snake.snake_eat_apple(apple.position):
        apple.set_random_position(400)  # Set new random position for the apple
        snake.snake_bigger()  # Make the snake grow
        SPEED += 0.5  # Increase speed
        score += 1  # Increment score

    # Draw snake and apple
    for snake_pos in snake.snake[:-1]:
        screen.blit(snake.skin, snake_pos)
    screen.blit(snake.head, snake.snake[-1])

    # Draw the apple
    apple.draw(screen)  # Call the draw method for the apple

    # Display the apple count
    show_score()

    pygame.display.update()

    # Check if new high score is achieved
    if score > high_score:
        high_score = score
        save_high_score()  # Save the new high score to the file

pygame.quit()
