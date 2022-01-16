from re import T
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to define alien"""

    def __init__(self,ai):
        """Init code to initialize the alien"""

        super().__init__()

        self.screen = ai.screen

        self.setting = ai.setting

        self.image = pygame.image.load('alien_game\images\hamilton.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):

        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):

        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



