import pygame
import random

PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

class Banana:
    def __init__(self):
        self.banana = pygame.Surface((10, 10))  # Banana size
        self.banana.fill(YELLOW)  # Banana color
        self.position = (0, 0)  # Initial position

    def set_random_position(self, screen_size, walls):
        valid_positions = False
        while not valid_positions:
            self.position = (random.randrange(0, screen_size - 10, 10), random.randrange(0, screen_size - 10, 10))
            valid_positions = True
            for wall in walls:
                if self.position in wall.get_wall_positions():
                    valid_positions = False
                    break 

    def check_collision(self, wall):
        """Check if the banana's position collides with the wall."""
        px, py = self.position
        return wall.x <= px < wall.x + wall.width and wall.y <= py < wall.y + wall.height              
        
    def draw(self, screen):
        """Draw the banana on the screen."""
        screen.blit(self.banana, self.position)



class Grape:
    def __init__(self):
        self.grape = pygame.Surface((10, 10))  # Grape size
        self.grape.fill(PURPLE)  # Grape color
        self.position = (0, 0)  # Initial position

    def set_random_position(self, screen_size, walls):
        valid_positions = False
        while not valid_positions:
            self.position = (random.randrange(0, screen_size - 10, 10), random.randrange(0, screen_size - 10, 10))
            valid_positions = True

            for wall in walls:
                if self.position in wall.get_wall_positions():
                    valid_positions = False
                    break  

    def check_collision(self, wall):
        """Check if the grape's position collides with the wall."""
        px, py = self.position
        return wall.x <= px < wall.x + wall.width and wall.y <= py < wall.y + wall.height
        
    def draw(self, screen):
        """Draw the grape on the screen."""
        screen.blit(self.grape, self.position)
        