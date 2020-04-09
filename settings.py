import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200                                                # Changed from 1200
        self.screen_height = 800                                                # Changed from 800
        self.bg_color = pygame.Color('#E6E6E6')                                 # Changed from (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.height_limit = self.screen_height * 0.75

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
