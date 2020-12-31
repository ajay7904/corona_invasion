import pygame
from pygame.sprite import Sprite

class Vaccine(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/vaccine_bottle.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def blitme(self):
        self.screen.blit(self.image, self.rect)