import pygame
import random

class Fruit:
    def __init__(self, image_path, size=(40, 40)):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)  # Resize to specified size
        self.size = size
        self.position = (0, 0)  # Initial position

    def set_random_position(self, screen_size, walls):
        """Sets a random position for the fruit, ensuring it is not within the outline area or on the walls."""
        global x,y
        valid_position = False
        while not valid_position:
            # Generate random position within the screen area minus the border (100px)
            x = random.randint(100, screen_size - 100)
            y = random.randint(100, screen_size - 100)

            # Check if the position is within any wall or the outline area
            valid_position = True
            for wall in walls:
                if wall.x <= x <= wall.x + wall.width and wall.y <= y <= wall.y + wall.height:
                    valid_position = False
                    break  # Position is on a wall, try again
        self.position = (x, y)

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
        Fruit.__init__(self, 'graphics/banana.png', size=(40, 40))

# Grape class inherits from Fruit
class Grape(Fruit):
    def __init__(self):
        # Pass specific details to the Fruit base class
        Fruit.__init__(self, 'graphics/grape.png', size=(40, 40))

# Apple class inherits from Fruit
class Apple(Fruit):
    def __init__(self):
        # Pass specific details to the Fruit base class
        Fruit.__init__(self, 'graphics/apple.png', size=(40, 40))
