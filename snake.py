import pygame

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
BLUE = (17, 85, 204)

class Snake:

    def __init__(self, screen_size=400, lives=3):
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.skin = pygame.Surface((10, 10))
        self.skin.fill(BLUE)
        self.head = pygame.Surface((10, 10))
        self.head.fill(BLUE)
        self.direction = RIGHT
        self.screen_size = screen_size  # Save screen size for wrap-around effect
        self.lives = lives  # Initialize number of lives

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

        # Check for collision with itself or boundary
        self.check_collisions()

    def check_collisions(self):
        """Check if the snake collides with itself or the wall."""
        head_x, head_y = self.snake[-1]

        # Collision with snake's own body
        if (head_x, head_y) in self.snake[:-1]:
            self.lose_life()

        # Collision with boundaries (if the snake goes out of bounds and doesn't wrap)
        if head_x < 0 or head_y < 0 or head_x >= self.screen_size or head_y >= self.screen_size:
            self.lose_life()

    def lose_life(self):
        """Reduce lives when the snake collides."""
        self.lives -= 1
        if self.lives <= 0:
            print("Game Over!")
            self.reset_game()

    def reset_game(self):
        """Reset the game when all lives are lost."""
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

    def check_self_collision(self):
        """Check if the snake collides with itself."""
        head = self.snake[-1]  # The head is the last element in the snake's body
        # Check if the head's position matches any of the body parts
        for segment in self.snake[:-1]:  # Skip checking the head
            if head == segment:
                return True  # Collision with itself
        return False
