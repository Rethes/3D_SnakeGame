import pygame
from pygame.locals import *
import random

class Apple:

    APPLE_LIFETIME = 5000  # Apple disappears after 5 seconds (5000 milliseconds)

    def __init__(self):
        self.radius = 5  # Set the radius for the apple (circle)
        self.color = (0, 0, 255)  # Blue color for the apple
        self.position = (0, 0)  # Initial position
        self.last_appeared = pygame.time.get_ticks()  # Record the time when the apple first appears

    def set_random_position(self, screen_size):
        # Ensure that the position is random but within bounds considering the radius of the apple
        self.position = (random.randrange(self.radius, screen_size - self.radius, 10),
                         random.randrange(self.radius, screen_size - self.radius, 10))
        self.last_appeared = pygame.time.get_ticks()  # Reset the time when the apple appears
        print(self.position)  # For debugging purposes, prints the new position of the apple

    def draw(self, screen):
        current_time = pygame.time.get_ticks()  # Get the current time
        # Check if the apple has been on screen for less than 5 seconds
        if current_time - self.last_appeared < self.APPLE_LIFETIME:
            # Draw the apple as a circle if it hasn't expired
            pygame.draw.circle(screen, self.color, self.position, self.radius)
        else:
            # If 5 seconds have passed, reposition the apple
            self.set_random_position(400)  # Assuming screen size is 400x400
