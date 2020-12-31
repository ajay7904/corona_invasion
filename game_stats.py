class GameStats:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
        self.aliens_killed = 0
        self.bullets_fired = 0