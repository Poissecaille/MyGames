import pygame
from pygame.locals import *
import sys
from missile import Missile
from player import Player
from system import System

# OBJECTS INITIALIZATION
game_system = System('Shoot them all!', (800, 600))
player = Player(game_system.window_center)

# MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE and not game_system.missile_shot:
                missile = Missile(player.player_rect.center)
                game_system.shoot_event()
                missile_flame_countdown_start = pygame.time.get_ticks()

    player.handle_keys()
    player.handle_borders(game_system)

    # TODO ANIMATION
    # for i in range(len(game_system.animated_background)):
    #     game_system.clock.tick(100)
    #     game_system.window.blit(game_system.animated_background[i], (0, 0))

    game_system.window.blit(game_system.animated_background[0], (0, 0))

    game_system.window.blit(player.player_img, player.player_rect)
    pygame.draw.rect(game_system.window, (255, 0, 0),
                     player.player_rect, 1)

    if game_system.missile_shot:
        game_system.window.blit(
            missile.missile_img, missile.missile_rect)
        pygame.draw.rect(game_system.window, (255, 0, 0),
                         missile.missile_rect, 1)

        if pygame.time.get_ticks()-missile_flame_countdown_start < Missile.FLAME_DURATION:
            game_system.window.blit(
                missile.fire_img, missile.fire_rect
            )
        missile.move()
        missile.handle_range(game_system)

    pygame.display.update()
