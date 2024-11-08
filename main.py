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
score  = 0

# Render and display the apple count
def show_score():
    """Displays the score board."""
    font= pygame.font.Font(None,35)
    score_text= font.render("Score:" +str(score), True, WHITE)
    screen.blit(score_text, (10,10)) #display score in the top left corner

def game_over_screen():
    """Displays the game-over screen."""
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, RED)
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(game_over_text, text_rect)  # Display text
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

while GAME_ON:
    # Clear screen
    screen.fill((0, 0, 0))
    clock.tick(SPEED)

    snake.crawl()  # Update snake position
    # print("Game loop running")

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

    # display the apple count
    show_score()

    pygame.display.update()

pygame.quit()
