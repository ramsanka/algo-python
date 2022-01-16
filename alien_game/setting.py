class Settings:
    """init the setting of the game in one class object"""

    def __init__(self):
        """Init the setting"""

        #Screen setting
        #we are setting the parameters of the class
    
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship setting
        self.ship_speed = 1.5

        #bullet setting
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        #alien setting
        self.alien_speed = 1.0

        self.fleet_drop_speed = 10

        self.fleet_direction = 1



