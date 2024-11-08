class Apple:
    def __init__(self):
        self.apple = pygame.Surface((10, 10))  # Size of the apple
        self.apple.fill((0, 0, 255))  # Fill with blue color for visibility
        self.position = (0, 0)  # Initial position

    def set_random_position(self, screen_size, walls):
        # Ensure the apple is positioned within the bounds of the screen and on a grid
        valid_position = False
        while not valid_position:
            self.position = (random.randrange(0, screen_size - 10, 10), random.randrange(0, screen_size - 10, 10))
            if not is_apple_in_wall(self.position, walls):
                valid_position = True
        print("Apple position:", self.position)  # Debugging output

    def draw(self, screen):
        # Draw the apple at its current position
        screen.blit(self.apple, self.position)

# Helper function to check if apple collides with walls
def is_apple_in_wall(apple_position, walls):
    for wall in walls:
        wall_rect = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
        apple_rect = pygame.Rect(apple_position[0], apple_position[1], 10, 10)  # Assuming apple size is 10x10
        if wall_rect.colliderect(apple_rect):
            return True
    return False
