import pygame

class GameOver:
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.fill(self.game_settings.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

class YouWin:
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('images/you_win.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.fill(self.game_settings.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

class YouLose:
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load('images/you_lose.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.fill(self.game_settings.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()