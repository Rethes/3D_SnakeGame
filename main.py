import pygame
from pygame.locals import *
from powerups import Banana, Grape
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
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# Create game objects
screen_size = 600  # Adjust according to your game screen dimensions
snake = Snake(screen_size)
apple = Apple()
banana = Banana()
grape = Grape()

# Initialize walls
walls = [
    Wall(100, 100, 400, 10),  # Horizontal inner wall
    Wall(150, 250, 10, 300)   # Vertical inner wall
]

apple.set_random_position(screen_size, walls)


# Apple count variable
score  = 0
banana_counter = 0
grape_counter = 0
apple_counter = 0
banana_active = False
grape_active = False
banana_timer = 0
grape_timer = 0

high_score=0
banana_lifespan = 5000
grape_lifespan = 4000

# def show_splash_screen():
#     """Displays the splash screen with the game title and instructions."""
#     font_large = pygame.font.Font(None, 70)
#     title_text = font_large.render("Snake Game", True, WHITE)
#     title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))
#
#     font_small = pygame.font.Font(None, 30)
#     instructions_text1 = font_small.render("Arrow Keys: Control the direction of the snake.", True, WHITE)
#     instructions_text2 = font_small.render("P Key: Pause the game. Press 'P' again to resume.", True, WHITE)
#     instructions_text3 = font_small.render("R Key: Restart the game if it’s over.", True, WHITE)
#     instructions_text4 = font_small.render("Q Key: Quit the game", True, WHITE)
#     font_small = pygame.font.Font(None, 40)
#     instructions_text5 = font_small.render("Press any key to start", True, WHITE)
#
#     instructions_rect1 = instructions_text1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 60))
#     instructions_rect2 = instructions_text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))
#     instructions_rect3 = instructions_text3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
#     instructions_rect4 = instructions_text4.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
#     instructions_rect5 = instructions_text5.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))  # Fifth instruction
#
#     screen.fill((0, 0, 0))  # Clear screen
#     screen.blit(title_text, title_rect)
#     screen.blit(instructions_text1, instructions_rect1)
#     screen.blit(instructions_text2, instructions_rect2)
#     screen.blit(instructions_text3, instructions_rect3)
#     screen.blit(instructions_text4, instructions_rect4)
#     screen.blit(instructions_text5, instructions_rect5)
#
#     pygame.display.flip()  # Update display
#
#     # Wait for player to press any key to start the game
#     waiting_for_input = True
#     while waiting_for_input:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 exit()
#             elif event.type == KEYDOWN:
#                 waiting_for_input = False  # Start the game once any key is pressed

def show_splash_screen():
    """Displays the splash screen with the game title and instructions."""
    font_large = pygame.font.Font(None, 70)
    title_text = font_large.render("Snake Game", True, WHITE)
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))

    font_small = pygame.font.Font(None, 30)
    instructions_text1 = font_small.render("Arrow Keys: Control the direction of the snake.", True, WHITE)
    instructions_text2 = font_small.render("P Key: Pause the game. Press 'P' again to resume.", True, WHITE)
    instructions_text3 = font_small.render("R Key: Restart the game if it’s over.", True, WHITE)
    instructions_text4 = font_small.render("Q Key: Quit the game", True, WHITE)
    instructions_text5 = pygame.font.Font(None, 40).render("Press any key to start", True, WHITE)

    instructions_rect1 = instructions_text1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 60))
    instructions_rect2 = instructions_text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))
    instructions_rect3 = instructions_text3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    instructions_rect4 = instructions_text4.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
    instructions_rect5 = instructions_text5.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))

    screen.fill((0, 0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(instructions_text1, instructions_rect1)
    screen.blit(instructions_text2, instructions_rect2)
    screen.blit(instructions_text3, instructions_rect3)
    screen.blit(instructions_text4, instructions_rect4)
    screen.blit(instructions_text5, instructions_rect5)
    pygame.display.flip()

    waiting_for_input = True
    clock = pygame.time.Clock()
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                waiting_for_input = False
        clock.tick(30)  # Ensure this loop runs at a reasonable frame rate

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

def show_score():
    """Displays the score board."""
    font= pygame.font.Font(None,35)
    score_text= font.render("Score:" +str(score), True, WHITE)
    screen.blit(score_text, (10,10)) #display score in the top left corner

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

def quit_screen():
    """Displays the quit confirmation screen and waits for user input to confirm or cancel quitting."""
    font = pygame.font.Font(None, 30)
    quit_text = font.render("Are you sure you want to quit?", True, RED)
    text_rect = quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    # Display instructions for the user
    font_small = pygame.font.Font(None, 30)
    confirm_text = font_small.render("Press 'Y' to confirm or 'N' to cancel", True, WHITE)
    confirm_rect = confirm_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(quit_text, text_rect)
    screen.blit(confirm_text, confirm_rect)

    pygame.display.flip()  # Update display

    # Wait for player input to confirm or cancel quitting
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_y:  # Confirm quit
                    pygame.quit()
                    exit()
                elif event.key == K_n:  # Cancel quit
                    waiting_for_input = False  # Exit the quit screen and return to the game

def restart_game():
    """Reinitializes the entire game, resetting pygame and restarting from scratch."""
    global snake, apple, score, GAME_ON, SPEED
    pygame.quit()
    pygame.init()  # Reinitialize pygame

    # Re-create the screen and clock
    global screen, clock
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()

    # Reset game state variables
    screen_size = 600
    snake = Snake(screen_size)
    apple = Apple()
    apple.set_random_position(screen_size, walls)
    score = 0
    SPEED = 10
    GAME_ON = True

    # Re-run the main game loop
    game_loop()

def game_over_screen():
    """Displays the game-over screen and prompts for restart or exit with the score and the high score."""
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    text_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    high_score_rect = high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    # Display prompt to restart or exit
    font_small = pygame.font.Font(None, 30)
    restart_text = font_small.render("Press 'R' to restart or 'Q' to quit", True, WHITE)
    restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

    screen.fill((0, 0, 0))
    screen.blit(game_over_text, text_rect)
    screen.blit(score_text, score_rect)
    screen.blit(high_score_text, high_score_rect)
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_r:  # Restart game
                    waiting_for_input = False
                    restart_game()  # Restart the game
                    return  # Exit the function after restarting
                elif event.key == K_q:  # Quit game
                    pygame.quit()
                    exit()
        pygame.time.delay(1000)  # Delay for 1 second to keep the game over screen visible before restart

def game_loop():
    global GAME_ON, score, high_score, SPEED
    global banana_active, banana_counter, grape_active, grape_counter, banana_timer, grape_timer, apple_counter

    # Show the splash screen at the start
    show_splash_screen()

    # Rest of your code...


    # Show the splash screen at the start
    show_splash_screen()

    # Rest of your code...


    # Show the splash screen at the start
    show_splash_screen()

    while GAME_ON:
        # Clear screen
        screen.fill((0, 0, 0))
        clock.tick(SPEED)

        # Update snake position
        snake.crawl()

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                GAME_ON = False
            elif event.type == KEYDOWN:
                if event.key == K_p:  # Pause when 'P' is pressed
                    pause_game()
                elif event.key == K_q:  # Press 'Q' to trigger quit screen
                    quit_screen()
                elif event.key == K_r:  # Press 'R' to restart the game
                    if not GAME_ON:  # Only allow restart if the game is over
                        restart_game()
                elif event.key == K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        # Check for wall collisions and self-collision
        for wall in walls:
            wall.draw(screen)  # Draw each wall
            if snake.snake[-1][0] in range(wall.x, wall.x + wall.width) and \
               snake.snake[-1][1] in range(wall.y, wall.y + wall.height):
                game_over_screen()
                GAME_ON = False

        # Check if snake eats apple
        if snake.snake_eat_apple(apple.position):
            apple.set_random_position(400, walls)  # Set new random position for the apple
            snake.snake_bigger()  # Make the snake grow
            SPEED += 0.5  # Increase speed
            score += 1  # Increment score
            apple_counter += 1
            banana_counter += 1
            grape_counter += 1

            # Check if the banana power-up should be activated
            # if apple_counter == 3:
            if banana_counter >= 3 and not banana_active:
                banana.set_random_position(400, walls)
                banana_active = True
                banana_timer = pygame.time.get_ticks()  # Start the timer
                banana_counter = 0  # Reset banana counter

            # Check if the grape power-up should be activated
            # if apple_counter == 5:
            if grape_counter >= 5 and not grape_active:
                grape.set_random_position(400, walls)
                grape_active = True
                grape_timer = pygame.time.get_ticks()  # Start the timer
                grape_counter = 0  # Reset grape counter

        # Check if snake eats banana
        if banana_active and snake.snake_eat_banana(banana.position):
            banana_active = False
            score += 3  # Increment score
            SPEED += 1

        # Check if the banana power-up timer has expired
        if banana_active and pygame.time.get_ticks() - banana_timer >= banana_lifespan:
            banana_active = False

        # Check if the grape power-up timer has expired
        if grape_active and pygame.time.get_ticks() - grape_timer >= grape_lifespan:
            grape_active = False

        # Check if snake eats grape
        if grape_active and snake.snake_eat_grape(grape.position):
            grape_active = False
            score += 5  # Increment score
            SPEED += 1.5

        # Draw snake, banana, grape and apple
        for snake_pos in snake.snake[:-1]:
            screen.blit(snake.skin, snake_pos)
        screen.blit(snake.head, snake.snake[-1])

        # Draw the apple
        apple.draw(screen)

        if banana_active:
            banana.draw(screen)  # Draw the banana

        if grape_active:
            grape.draw(screen)  # Draw the grape

        # Draw snake and apple
        for snake_pos in snake.snake[:-1]:
            screen.blit(snake.skin, snake_pos)
        screen.blit(snake.head, snake.snake[-1])

        # Draw the apple
        apple.draw(screen)

        # Display the apple count (score)
        show_score()

        pygame.display.update()

        # Check if new high score is achieved
        if score > high_score:
            high_score = score
            save_high_score()  # Save the new high score to the file

    pygame.quit()


# Call the game loop
game_loop()

