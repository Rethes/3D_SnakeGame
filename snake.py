import pygame
from pygame import Vector2

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
BLUE = (17, 85, 204)

class Snake:

    def __init__(self, screen_size=400, lives=3):
        # Create the head with a rounded shape, eyes, and a mouth
        self.snake = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]

        # Dimensions for the head, body, and tail
        self.block_size = 20  # Adjust size for a larger, rounded head

        # Create a rounded head
        self.head = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)  # Enable transparency
        pygame.draw.circle(self.head, (0, 0, 255), (self.block_size // 2, self.block_size // 2),
                           self.block_size // 2)  # Blue rounded head

        # Add eyes to the rounded head
        pygame.draw.circle(self.head, (255, 255, 255), (self.block_size // 3, self.block_size // 3),
                           self.block_size // 6)  # Left eye (white)
        pygame.draw.circle(self.head, (255, 255, 255), ((self.block_size * 2) // 3, self.block_size // 3),
                           self.block_size // 6)  # Right eye (white)
        pygame.draw.circle(self.head, (0, 0, 0), (self.block_size // 3, self.block_size // 3),
                           self.block_size // 12)  # Left pupil (black)
        pygame.draw.circle(self.head, (0, 0, 0), ((self.block_size * 2) // 3, self.block_size // 3),
                           self.block_size // 12)  # Right pupil (black)

        # Add a mouth (a smiling arc) to the snake's head
        mouth_rect = pygame.Rect(self.block_size // 4, self.block_size // 2, self.block_size // 2, self.block_size // 4)
        pygame.draw.arc(self.head, (0, 0, 0), mouth_rect, 3.14, 0, 2)  # Black smile arc (smiling mouth)

        # Create the body as a rectangle for now (can also be rounded if needed)
        self.skin = pygame.Surface((self.block_size, self.block_size))
        self.skin.fill((0, 0, 255))  # Blue body

        # Create a rounded tail (same logic as the head)
        self.tail = pygame.Surface((self.block_size, self.block_size), pygame.SRCALPHA)  # Enable transparency
        pygame.draw.circle(self.tail, (0, 0, 255), (self.block_size // 2, self.block_size // 2),
                           self.block_size // 2)  # Blue rounded tail

        self.direction = Vector2(1, 0)  # Default direction
        self.screen_size = screen_size  # Save screen size for wrap-around effect
        self.lives = lives  # Initialize number of lives
        self.new_block = False

        # Load sound effects
        self.crunch_sound = pygame.mixer.Sound('sound/food.mp3')
        self.move_sound = pygame.mixer.Sound('sound/move.mp3')

    def draw(self, screen):
        """Draws the snake on the screen."""
        for snake_pos in self.snake[:-1]:
            screen.blit(self.skin, snake_pos)
            screen.blit(self.head, self.snake[-1])

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

        # Add new head position to the snake
        self.snake.append((x, y))

        # Check for self-collision (collision with its body)
        self.self_collision()

        # Check for wall collision
        self.wall_collision()

        # If no collision, remove the tail unless the snake has just eaten
        if not self.new_block:
            self.snake.pop(0)
        else:
            self.new_block = False  # Reset after the snake grows

    def wall_collision(self):
        """Check if the snake collides with the wall."""
        head_x, head_y = self.snake[-1]

        # Collision with boundaries (if the snake goes out of bounds and doesn't wrap)
        if head_x < 0 or head_y < 0 or head_x >= self.screen_size or head_y >= self.screen_size:
            self.lose_life()

    def self_collision(self):
        """Check if the snake collides with itself."""
        head_x, head_y = self.snake[-1]

        # Collision with snake's own body (excluding the head)
        if (head_x, head_y) in self.snake[:-1]:  # Head collides with body
            self.lose_life()

    def lose_life(self):
        """Reduce lives when the snake collides with itself."""
        self.lives -= 1
        if self.lives <= 0:
            print("Game Over!")
            self.reset_game()

    def reset_game(self):
        """Rest the game when all lives are lost."""
        print("Resetting game...")
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.direction = RIGHT
        self.lives = 3  # Reset lives

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

    def get_lives(self):
        """Return the number of lives remaining."""
        return self.lives

    def change_direction(self, new_direction):
        """Change the snake's direction with a sound effect."""
        if (
                (new_direction == UP and self.direction != DOWN) or
                (new_direction == DOWN and self.direction != UP) or
                (new_direction == LEFT and self.direction != RIGHT) or
                (new_direction == RIGHT and self.direction != LEFT)
        ):
            self.direction = new_direction
            self.move_sound.play()  # Play movement sound

    def reset_position(self, screen_size):
        """Resets the snake's position to the center of the screen."""
        initial_length = len(self.snake)  # Preserve the current length
        self.snake = [(screen_size // 2, screen_size // 2) for _ in range(initial_length)]
        self.direction = RIGHT  # Reset direction to default