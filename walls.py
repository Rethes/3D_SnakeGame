import pygame

class Wall:
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def get_wall_positions (self):
        positions = []
        for x in range (self.x, self.x + self.width, 10):
            for y in range (self.y, self.y + self.height, 10):
                positions.append((x, y))
            return positions
