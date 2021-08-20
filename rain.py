import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to manage the rain"""

    def __init__(self, ai_game) -> None:
        """Create a single rain drop"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.rain_color

        # Create a rain rect at (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.rain_width,
            self.settings.rain_height)
        
        # Store the rains exact vertical postion
        self.y = float(self.rect.y)

    def update(self):
        """Move the rain down"""
        self.y += (self.settings.rain_speed)
        self.rect.y = self.y
    
    def draw_rain(self):
        """Draw the rain to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)