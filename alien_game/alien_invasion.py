import sys
import pygame

from setting import Settings
from ship import ship


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

    def run_game(self):
        """Start the main game"""
        """Setting the va"""
        while True:

            #this will keep checking for the keystrokes          
            self._check_event()

            #this will keep updating the ship position
            self.ship.update()
            
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
        pygame.display.flip()

    

if __name__ == "__main__":
    #Make a game instance and run it.
    ai = AlienInvasion()
    ai.run_game()

