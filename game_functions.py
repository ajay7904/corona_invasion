import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from game_messages import GameOver
from game_stats import GameStats
from status import Vaccine

def check_keydown_events(event, game_settings, screen, ship, bullets_group, stats, vaccine_group, alien_group):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RETURN:
        if stats.ships_left == 10:
            stats.ships_left = game_settings.ship_limit
            create_vaccine_rack(screen, vaccine_group, stats)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        if len(bullets_group) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets_group.add(new_bullet)
            stats.bullets_fired += 1
            print('Bullets Fired: ' + str(stats.bullets_fired) + '   ' + 'Corona Killed: ' + str(stats.aliens_killed))


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets_group,stats, vaccine_group, alien_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets_group,stats, vaccine_group, alien_group)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(stats, game_settings, screen, ship, alien_group, bullets_group, you_win):
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()
        if bullet.rect.bottom <= 0:
            bullets_group.remove(bullet)
    check_bullet_alien_collisions(stats, game_settings, screen, ship, alien_group, bullets_group, you_win)

def check_bullet_alien_collisions(stats, game_settings, screen, ship, alien_group, bullets_group, you_win):
    collision = pygame.sprite.groupcollide(bullets_group, alien_group, True, True)
    if bool(collision) == True:
        stats.aliens_killed += 1
        print('Bullets Fired: ' + str(stats.bullets_fired) + '   ' + 'Corona Killed: ' + str(stats.aliens_killed))
    if len(alien_group) == 0:
        you_win.blitme()
        print('You Win..!!')
        print('Bullets Fired: ' + str(stats.bullets_fired) + '   ' + 'Corona Killed: ' + str(stats.aliens_killed))
        sleep(1)
        bullets_group.empty()
        # pygame.event.clear()
        creat_alien_fleet(game_settings, screen, ship, alien_group)
        ship.center_ship()


def update_screen(stats, game_settings,screen,ship, bullets_group, alien_group,game_over,you_win, vaccine_group):
    screen.fill(game_settings.bg_color)
    update_bullets(stats, game_settings, screen, ship, alien_group, bullets_group, you_win)
    ship.blitme()
    vaccine_group.draw(screen)
    alien_group.draw(screen)
    pygame.display.flip()

def get_number_aliens_x(game_settings,screen):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space_x / (2*alien_width))
    del alien
    return number_alien_x

def creat_alien(game_settings, screen, alien_group, aln_no, row_number):
    alien = Alien(game_settings, screen)
    alien_group.add(alien)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * aln_no
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 50

def create_vaccine(screen, vaccine_group, vac_no):
    vaccine = Vaccine(screen)
    vaccine_group.add(vaccine)
    vaccine.rect.x = 10 + 2 * vaccine.rect.width * vac_no

def create_vaccine_rack(screen, vaccine_group, stats):
    for vac_no in range(stats.ships_left):
        create_vaccine(screen, vaccine_group, vac_no)

def update_vaccine_rack(screen, vaccine_group, stats):
    vaccine_group.empty()
    create_vaccine_rack(screen, vaccine_group, stats)

def get_number_rows(game_settings, ship_height, alien_height):
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien_fleet(game_settings, screen, ship, alien_group):
    alien = Alien(game_settings, screen)
    number_alien_x = get_number_aliens_x(game_settings,screen)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_no in range(number_rows):
        for aln_no in range(number_alien_x):
            creat_alien(game_settings, screen, alien_group, aln_no, row_no)

def ship_hit(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group):
    stats.ships_left -= 1
    alien_group.empty()
    bullets_group.empty()
    print('You Lost..!!')
    print('Bullets Fired: ' + str(stats.bullets_fired) + '   ' + 'Corona Killed: ' + str(stats.aliens_killed))
    if stats.ships_left > 0:
        you_lose.blitme()
        sleep(1)
    creat_alien_fleet(game_settings, screen, ship, alien_group)
    update_vaccine_rack(screen, vaccine_group, stats)
    # pygame.event.clear()
    ship.center_ship()


def update_aliens(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group):
    check_fleet_edges(game_settings, alien_group)
    alien_group.update()
    if pygame.sprite.spritecollideany(ship, alien_group):
        ship_hit(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group)
    check_aliens_bottom(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group)

def check_fleet_edges(game_settings, alien_group):
    for alien in alien_group.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, alien_group)
            break

def change_fleet_direction(game_settings, alien_group):
    for alien in alien_group.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def check_aliens_bottom(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group):
    screen_rect = screen.get_rect()
    for alien in alien_group.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, alien_group, bullets_group, you_lose, vaccine_group)
            break