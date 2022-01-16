import sys
import pygame

from setting import Settings
from ship import ship
from bullet import bullet
from alien import Alien

class AlienInvasion:
    """Class to manage the game"""

    def __init__(self) -> None:
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_height,self.setting.screen_width))

        pygame.display.set_caption("Alien Invasion")

        """Setting the bg setting"""
        self.bg_color = self.setting.bg_color

        #creating the ship
        #so pass the ai game as argument as self.
        #so ship is also an attribute of the class AI.(action)
        self.ship = ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main game"""
        """Setting the va"""
        while True:

            #this will keep checking for the keystrokes          
            self._check_event()

            #this will keep updating the ship position
            self.ship.update()
            
            #update the bullet group
            #this calls -- sprite -> each bullet in the list --> bullet.update()
            #sprite is special function which groups the bullet.
            self._update_bullets()

            #update the aliens
            self._update_aliens()

            #based on the ship position update and display the latest screen.
            self._update_screen()
            
            
    
    #helper method.
    #cannot be called from the instance of the class.
    #but adds value to help refactor code within other
    #methods of the class.

    #this helper method checks the events pushed by the user.
    #these are internal methods which are not called by the instance of the class.

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.K_q:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_event_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_event_keyup_events(event)
                          
                
    def _check_event_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_event_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

    #helper method 2
    #to help update the screen.

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()

    #fire bullet helper function
    #create a new bullet and add it to the list(group)
    def _fire_bullet(self):

        new_bullet = bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

        #identify the collision
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
    
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _update_aliens(self):

        self._check_edges()

        self.aliens.update()

    def _check_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_direction()
            break

    def _change_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

if __name__ == "__main__":
    #Make a game instance and run it.
    ai = AlienInvasion()
    ai.run_game()

