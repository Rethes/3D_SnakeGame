import pygame
import random

class Fruit:
    def __init__(self, image_path, size=(40, 40)):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)  # Resize to specified size
        self.size = size
        self.position = (0, 0)  # Initial position

    def set_random_position(self, screen_size, walls):
        """Set a random position for the fruit, ensuring it doesn't overlap with walls."""
        width, height = self.size  # Unpack the fruit's size tuple into width and height

        while True:
            # Generate random x and y coordinates for the top-left corner of the fruit
            self.x = random.randint(0, screen_size - width)
            self.y = random.randint(0, screen_size - height)

            # Check for overlap with any walls
            overlaps_wall = False
            for wall in walls:
                if (
                        self.x + width > wall.x and self.x < wall.x + wall.width and
                        self.y + height > wall.y and self.y < wall.y + wall.height
                ):
                    overlaps_wall = True
                    break

            # If it doesn't overlap with any wall, break the loop
            if not overlaps_wall:
                break

        # Update the position tuple
        self.position = (self.x, self.y)

    def check_collision(self, wall):
        """Check if the fruit's position collides with the wall."""
        px, py = self.position
        return wall.x <= px < wall.x + wall.width and wall.y <= py < wall.y + wall.height

    def draw(self, screen):
        """Draw the fruit on the screen."""
        screen.blit(self.image, self.position)

# Banana class inherits from Fruit
class Banana(Fruit):
    def __init__(self):
        # Pass specific details to the Fruit base class
        Fruit.__init__(self, 'Graphics/banana.png', size=(40, 40))

# Grape class inherits from Fruit
class Grape(Fruit):
    def __init__(self):
        # Pass specific details to the Fruit base class
        Fruit.__init__(self, 'Graphics/grape.png', size=(40, 40))

# Apple class inherits from Fruit
class Apple(Fruit):
    def __init__(self):
        # Pass specific details to the Fruit base class
        Fruit.__init__(self, 'Graphics/apple.png', size=(40, 40))
