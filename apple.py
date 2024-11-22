import pygame
import random


class Apple:
    def __init__(self):
        # Load the apple image and scale it to 40x40 pixels
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (40, 40))  # Resize to 40x40 pixels
        self.position = (0, 0)  # Initial Position

    def set_random_position(self, screen_size, walls):
        valid_positions = False
        while not valid_positions:
            # Generate a random position aligned with a 40-pixel grid
            self.position = (
                random.randrange(0, screen_size - 40, 40),
                random.randrange(0, screen_size - 40, 40)
            )
            valid_positions = True

            # Ensure the apple doesn't overlap with any wall positions
            for wall in walls:
                if self.position in wall.get_wall_positions():
                    valid_positions = False
                    break

    def draw(self, screen):
        # Draw the apple at its current position
        screen.blit(self.apple, self.position)
