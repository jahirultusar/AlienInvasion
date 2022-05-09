'''This is the settings module for alien_invasion game'''

class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        '''Initialize game settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (230, 230, 230) #will change later
        self.bg_color = (64, 61, 61) # Temporary color

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
                
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300 #was 3
        self.bullet_height = 15
        #self.bullet_color = (60, 60, 60) # Dark grey
        self.bullet_color = (250, 249, 246) # Temporary bullet color # off white
<<<<<<< HEAD
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = .30
        self.fleet_drop_speed = 30 #was 3
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
=======
        self.bullets_allowed = 3
>>>>>>> 5397ecb7d15596a997bcf3ba6517cd1f7c5a21f7
