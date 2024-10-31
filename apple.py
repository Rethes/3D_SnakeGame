import pygame
import random

class Apple:
    def __init__(self):
        self.apple = pygame.Surface((10, 10))  # Size of the apple
        self.apple.fill((0, 0, 255))  # Fill with blue color for visibility
        self.position = (0, 0) # Initial Position

    def set_random_position(self, screen_size):
        # Ensure the apple is positioned within the bounds of the screen and on a grid
        self.position = (random.randrange(0, screen_size - 10, 10), random.randrange(0, screen_size - 10, 10))
        print("Apple position:", self.position)  # Debugging output

    def draw(self, screen):
        # Draw the apple at its current position
        screen.blit(self.apple, self.position)  # Blit the apple surface onto the screen