import curses
import math
import time
import pygame


def move_sphere(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        stdscr.clear()
        run_sphere_animation()
        stdscr.refresh()


def run_sphere_animation():

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set window size
    clock = pygame.time.Clock()  # Frame rate control
    radius = 30  # Sphere radius

    # Create a pygame.Rect object representing the player (as a bounding box for the sphere)
    player = pygame.Rect(400, 300, radius * 2, radius * 2)  # (x, y, width, height)

    # Set up initial velocity
    vx, vy = 5, 3  # Velocity in x and y directions
    friction = 0.99  # Friction for smooth movement
    gravity = 9.8
    velocity_x, velocity_y = 1.0, 0.5
    x, y = curses.COLS // 2, curses.LINES // 2
    direction_x, direction_y = 1, 1

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black color


        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        velocity_y += gravity
        # key = pygame.key.get_pressed()
        # if event.type == KEYDOWN:
        #     if key == K_UP and snake.direction != DOWN:
        #         print("UP")
        #         move_sphere.direction = UP
                # elif event.key == K_LEFT and snake.direction != RIGHT:
                #     print("LEFT")
                #     snake.direction = LEFT
                # elif event.key == K_DOWN and snake.direction != UP:
                #     print("DOWN")
                #     snake.direction = DOWN
                # elif event.key == K_RIGHT and snake.direction != LEFT:
                #     print("RIGHT")
                #     snake.direction = RIGHT


       # Update position
        player.x += vx
        player.y += vy

        # Boundary collision detection and realistic bouncing
        if player.right >= screen.get_width() or player.left <= 0:
            vx = -vx * friction  # Reverse velocity and apply friction
        if player.bottom >= screen.get_height() or player.top <= 0:
            vy = -vy * friction

        if x + radius >= curses.COLS - 1 or x - radius <= 0:
            direction_x *= -1
            velocity_x *= friction
        if y + radius >= curses.LINES - 1 or y - radius <= 0:
            direction_y *= -1
            velocity_y *= friction

        x += direction_x * velocity_x
        y += direction_y * velocity_y

        # Draw the sphere as a circle inside the player's rectangle
        pygame.draw.circle(screen, (255, 0, 0), player.center, radius)

        # Update the display and maintain frame rate
        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    curses.wrapper(move_sphere)
