import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from time import sleep
from game_messages import GameOver, YouWin, YouLose
from status import Vaccine


def run_game():
    pygame.init()
    game_settings = Setting()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption('Corona Invasion')
    ship = Ship(game_settings, screen)
    bullets_group = Group()
    alien_group = Group()
    stats = GameStats(game_settings)
    game_over = GameOver(screen, game_settings)
    you_win = YouWin(screen, game_settings)
    you_lose = YouLose(screen, game_settings)
    vaccine_group = Group()
    gf.create_vaccine_rack(screen, vaccine_group, stats)
    gf.creat_alien_fleet(game_settings, screen, ship, alien_group)
    while True:
        gf.check_events(game_settings, screen, ship, bullets_group, stats, vaccine_group, alien_group)
        if stats.ships_left > 0 and stats.ships_left <=game_settings.ship_limit:
            ship.update()
            bullets_group.update()
            gf.update_aliens(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group)
            gf.update_screen(stats, game_settings, screen, ship, bullets_group, alien_group, game_over, you_win, vaccine_group)
        elif stats.ships_left == 0:
            print('Game Over..!!!')
            print('Bullets Fired: ' + str(stats.bullets_fired) + '   ' + 'Corona Killed: ' + str(stats.aliens_killed))
            game_over.blitme()
            stats.reset_stats()
            stats.ships_left = 10

run_game()