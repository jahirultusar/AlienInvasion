import pygame
#import os #To find the image path


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

<<<<<<< HEAD
        # Load the ship image and get its rect
        self.image = pygame.image.load("AlienInvasion/images/ship.bmp")
            #print(os.getcwd())
=======
        # Load the ship image and get its rectz
        self.image = pygame.image.load(
            '/home/meda/PycharmProjects/PythonCrashCourse/CrashCourseProjects/AlienInvasion/images/ship.bmp')
>>>>>>> 9f7670db87974916431bc74d0f0ea5acbb2318be
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
<<<<<<< HEAD
                
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ Update the ships position based on the movement flag"""
        # Update the ships x value, not the rect 
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
=======

        # Movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """ Update the ships position based on movement flag"""
        # Update the ships x value not the rect()

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
>>>>>>> 9f7670db87974916431bc74d0f0ea5acbb2318be
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x

<<<<<<< HEAD
=======

>>>>>>> 9f7670db87974916431bc74d0f0ea5acbb2318be
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)