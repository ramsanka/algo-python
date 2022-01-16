import pygame


class ship:
    """Class for managing the ship"""

    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('alien_game\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left  = False

             

    def blitme(self):
        """draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        elif self.moving_left == True and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        self.rect.x = self.x

