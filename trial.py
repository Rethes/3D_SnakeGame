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
snake = Snake()
apple = Apple()
apple.set_random_position(400)

# Initialize walls
walls = [
    Wall(300, 150, 100, 10),   # Horizontal wall
    Wall(50, 250, 10, 100),    # Vertical wall
    Wall(200, 50, 150, 10)     # Another horizontal wall
]

def game_over_screen():
    """Displays the game-over screen."""
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, RED)
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(game_over_text, text_rect)  # Display text
    pygame.display.flip()  # Update display

    # Wait for a few seconds or until player closes the window
    pygame.time.delay(2000)

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
            elif event.type == KEYDOWN:
                if event.key == K_p:  # Press 'P' to resume
                    paused = False

paused = False  # Variable to track if the game is paused


while GAME_ON:

    # screen.fill((0, 0, 0))  # Clear screen at the start of each frame
    clock.tick(SPEED)

    snake.crawl()  # Update snake position

    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False
        if event.type == KEYDOWN:
            if event.type == KEYDOWN:
                if event.key == K_p:  # Pause when 'P' is pressed
                    pause_game()
            if event.key == K_UP and snake.direction != DOWN:
                print("UP")
                snake.direction = UP
            elif event.key == K_LEFT and snake.direction != RIGHT:
                print("LEFT")
                snake.direction = LEFT
            elif event.key == K_DOWN and snake.direction != UP:
                print("DOWN")
                snake.direction = DOWN
            elif event.key == K_RIGHT and snake.direction != LEFT:
                print("RIGHT")
                snake.direction = RIGHT

    # Draw walls
    for wall in walls:
        wall.draw(screen)  # Draw each wall

    if snake.wall_collision(400) or snake.self_collision():
        game_over_screen()
        GAME_ON = False

    if snake.snake_eat_apple(apple.position):
        apple.set_random_position(400)

        snake.snake_bigger()
        SPEED += 0.5

    screen.fill((0, 0, 0))
    for snake_pos in snake.snake[0:-1]:
        screen.blit(snake.skin, snake_pos)
    screen.blit(snake.head, snake.snake[-1])
    screen.blit(apple.apple, apple.position)

    pygame.display.update()

pygame.quit()