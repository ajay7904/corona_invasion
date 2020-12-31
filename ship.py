import pygame

class Ship:
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/vaccine.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.game_settings = game_settings
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        elif self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx