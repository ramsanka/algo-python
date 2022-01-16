from socket import AI_ADDRCONFIG
import pygame
from pygame.sprite import Sprite

#this is inheritance 
#bullet is inheirting some attributes from Sprite super class.
class bullet(Sprite):
    """ this is the class to define the bullet"""

    def __init__(self, ai):
        
        super().__init__()
        
        self.screen = ai.screen
        self.setting = ai.setting
        self.color  = self.setting.bullet_color

        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)





