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
        self.ship_speed = 3
        self.height_limit = self.screen_height * 0.75

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Sound settings
        self.hit = pygame.mixer.Sound('sounds/boom.wav')
        self.shoot_sound = pygame.mixer.Sound('sounds/shoot_sound.wav')
        self.haha = pygame.mixer.Sound('sounds/haha.wav')
        self.ship_explode = pygame.mixer.Sound('sounds/ship_explode.wav')
        self.round_one = pygame.mixer.Sound('sounds/round_one.wav')
        self.round_two = pygame.mixer.Sound('sounds/round_two.wav')
        self.round_three = pygame.mixer.Sound('sounds/round_three.wav')
