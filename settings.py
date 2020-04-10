import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200                                                # Changed from 1200
        self.screen_height = 800                                                # Changed from 800
        self.bg_color = pygame.Color('#E6E6E6')                                 # Changed from (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        self.height_limit = self.screen_height * 0.75

        # Bullet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # Sound settings
        self.hit = pygame.mixer.Sound('sounds/boom.wav')
        self.shoot_sound = pygame.mixer.Sound('sounds/shoot_sound.wav')
        self.haha = pygame.mixer.Sound('sounds/haha.wav')
        self.ship_explode = pygame.mixer.Sound('sounds/ship_explode.wav')
        self.round_one = pygame.mixer.Sound('sounds/round_one.wav')
        self.round_two = pygame.mixer.Sound('sounds/round_two.wav')
        self.round_three = pygame.mixer.Sound('sounds/round_three.wav')
        self.welcome = pygame.mixer.Sound('sounds/welcome.wav')
        self.game_over = pygame.mixer.Sound('sounds/game_over.wav')

        # Difficulty settings
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_difficulty(self):
        """Increase speed settings and alien point values when board cleared."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
