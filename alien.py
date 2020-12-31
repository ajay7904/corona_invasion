import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game_settings, screen):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/corona.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
