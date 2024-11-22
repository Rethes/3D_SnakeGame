import pygame

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Snake:

    def __init__(self, screen_size=400):
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.skin = pygame.Surface((10, 10))
        self.skin.fill((255, 255, 255))
        self.head = pygame.Surface((10, 10))
        self.head.fill((200, 200, 200))
        self.direction = RIGHT
        self.screen_size = screen_size  # Save screen size for wrap-around effect

        # Load sound effects
        self.crunch_sound = pygame.mixer.Sound('sound/food.mp3')
        self.move_sound = pygame.mixer.Sound('sound/move.mp3')

    def crawl(self):
        x, y = self.snake[-1]  # Get current head position

        # Move head position based on the direction
        if self.direction == RIGHT:
            x += 10
        elif self.direction == UP:
            y -= 10
        elif self.direction == DOWN:
            y += 10
        elif self.direction == LEFT:
            x -= 10

        # Wrap around if the snake goes out of bounds
        x = x % self.screen_size
        y = y % self.screen_size

        # Add new head position to the snake and remove the tail
        self.snake.append((x, y))
        self.snake.pop(0)

    def snake_eat_apple(self, apple_pos, apple_size=40):
        """Check if the snake eats an apple."""
        head_x, head_y = self.snake[-1]
        apple_x, apple_y = apple_pos
        if (
            apple_x <= head_x < apple_x + apple_size and
            apple_y <= head_y < apple_y + apple_size
        ):
            self.crunch_sound.play()  # Play eating sound
            return True
        return False

    def snake_eat_banana(self, banana_pos, banana_size=40):
        """Check if the snake eats a banana."""
        head_x, head_y = self.snake[-1]
        banana_x, banana_y = banana_pos
        if (
            banana_x <= head_x < banana_x + banana_size and
            banana_y <= head_y < banana_y + banana_size
        ):
            self.crunch_sound.play()  # Play eating sound
            return True
        return False

    def snake_eat_grape(self, grape_pos, grape_size=40):
        """Check if the snake eats a grape."""
        head_x, head_y = self.snake[-1]
        grape_x, grape_y = grape_pos
        if (
            grape_x <= head_x < grape_x + grape_size and
            grape_y <= head_y < grape_y + grape_size
        ):
            self.crunch_sound.play()  # Play eating sound
            return True
        return False

    def snake_bigger(self):
        """Make the snake grow larger."""
        self.snake.insert(0, (self.snake[0]))