'''This is the settings module for alien_invasion game'''

class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize games static settings'''
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 980
        self.bg_color = (230, 230, 230) #will change later
        #self.bg_color = (64, 61, 61) # Temporary color

        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 3
                
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3 #was 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) # Dark grey
        #self.bullet_color = (250, 249, 246) # Temporary bullet color # off white
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 3 #was 3
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 1

    def increase_speed(self):
        """Increase speed settings and aliens point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        

