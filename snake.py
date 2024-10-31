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

    def self_collision(self):
        return self.snake[-1] in self.snake[0:-1]

    def wall_collision(self, screen_size):
        return self.snake[len(self.snake) - 1][0] >= screen_size or self.snake[len(self.snake) - 1][0] < 0 or \
            self.snake[len(self.snake) - 1][1] >= screen_size or self.snake[len(self.snake) - 1][1] < 0

    def snake_eat_apple(self, apple_pos):
        # Check if the head of the snake is at the same position as the apple
        return self.snake[-1] == apple_pos

    def snake_bigger(self):
        self.snake.insert(0, (self.snake[0]))