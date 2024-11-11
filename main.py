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

# Initialize walls
walls = [
    Wall(100, 100, 200, 10),  # Horizontal inner wall
    Wall(150, 250, 10, 100)   # Vertical inner wall
]

apple.set_random_position(screen_size, walls)

# Apple count variable
score  = 0

high_score=0

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

def show_splash_screen():
    """Displays the splash screen with game title and instructions."""
    screen.fill((0, 0, 0))  
    font = pygame.font.Font(None, 50)
    snake_xenzia_text = font.render("Snake Xenzia", True, WHITE)
    text_rect = snake_xenzia_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    loading = True

    screen.blit(snake_xenzia_text, text_rect)
    pygame.display.flip() 
    pygame.time.delay(3000)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:  # Press 'Q' to quit
                loading = False
                pygame.quit()
                exit()
            


show_splash_screen()          

# Render and display the apple count
def show_score():
    """Displays the score board."""
    font= pygame.font.Font(None,35)
    score_text= font.render("Score:" +str(score), True, WHITE)
    screen.blit(score_text, (10,10)) #display score in the top left corner

def game_over_screen():
    """Displays the game-over screen and prompts for restart or exit with the score and the high score."""
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, RED)
    #text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    score_text = font.render(f"Score: {score}", True, WHITE)  # Display score
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)  # Display high score
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    high_score_rect = high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

    screen.fill((0, 0, 0))  # Clear screen
    #screen.blit(game_over_text, text_rect)  # Display text
    screen.blit(game_over_text, text_rect)  # Display "Game Over" text
    screen.blit(score_text, score_rect)  # Display score
    screen.blit(high_score_text, high_score_rect)  # Display high score

    #display prompt to restart or exit
    font_small = pygame.font.Font(None, 30)
    restart_text = font_small.render("Press 'R' to restart or 'Q' to quit", True, WHITE)
    screen.blit(restart_text, (screen.get_width() // 2 - 150, screen.get_height() // 2 + 50))

    pygame.display.flip()  # Update display

    # Wait for player to press 'R' to restart or 'Q' to quit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:  # Restart game
                    waiting_for_input = False
                    restart_game()
                    # return
                elif event.key == K_q:  # Quit game
                    pygame.quit()
                    exit()
   

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

    load_high_score()

def restart_game():
    """Restarts the game by reinitializing the game objects and variables."""
    global snake, score, SPEED
    snake = Snake(screen_size)  # Reset snake
    apple.set_random_position(400, walls)  # Reset apple position
    score = 0  # Reset score
    SPEED = 10  # Reset speed

def end_game():
    """Ends the game and exits the program."""
    font = pygame.font.Font(None, 30)
    end_gane_text = font.render("GAME ENDED!PRESS R TO RESTART", True, RED)
    text_rect = end_gane_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # screen.blit(end_gane_text, (screen.get_width() // 2 - 70, screen.get_height() // 2))
    # pygame.display.flip()  # Update display

    ended = True
    while ended:
        screen.fill((0, 0, 0))  # Clear screen
        screen.blit(end_gane_text, text_rect)  # Display paused text
        pygame.display.flip()  # Update display

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_r:  # Press 'P' to resume
                ended = False


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
            elif event.key == K_r: # Restart when 'R' is pressed
                restart_game()         
            elif event.key == K_q: # Restart when 'R' is pressed
                end_game()
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
        apple.set_random_position(400, walls)  # Set new random position for the apple
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

     # Check if new high score is achieved
    if score > high_score:
        high_score = score
        save_high_score()  # Save the new high score to the file


pygame.quit()



