class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # 28, 56, 33
        self.ship_speed_factor = 1.5

        self.bullet_speeed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (245, 114, 66)
        self.bullets_allowed = 3

        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 15
        self.fleet_direction = 1

        self.ship_limit = 5
