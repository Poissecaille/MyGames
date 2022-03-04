from re import I
import pygame
from pygame.locals import *
import sys
from player import Player
from window import GameSettings

# OBJECTS INITIALIZATION
game_settings = GameSettings('Shoot them all!', (800, 600))
player = Player(game_settings.window_center)

# MAIN LOOP
while True:
    print(game_settings.clock.get_time())
    if game_settings.clock.get_time() >500:
        player.missile.missile_rect=None
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                player.shoot_missile()
                game_settings.clock.tick()

    if player.player_rect.right >= game_settings.width:
        player.player_rect.right = game_settings.width
    if player.player_rect.left <= 0:
        player.player_rect.left = 0
    if player.player_rect.top <= 0:
        player.player_rect.top = 0
    if player.player_rect.bottom >= game_settings.height:
        player.player_rect.bottom = game_settings.height
    player.handle_keys()

    # ANIMATION
    # for i in range(len(game_settings.animated_background)):
    #     game_settings.clock.tick(100)
    #     game_settings.window.blit(game_settings.animated_background[i], (0, 0))

    game_settings.window.blit(game_settings.animated_background[0], (0, 0))
    game_settings.window.blit(player.player_img, player.player_rect)
    
    try:
        game_settings.window.blit(
            player.missile.missile_img, player.missile.missile_rect)
        game_settings.window.blit(
            player.missile.fire_img, player.missile.fire_rect
         )
        # pygame.draw.rect(game_settings.window, (255, 0, 0),
        #                  player.missile.missile_rect, 1)
        player.missile.missile_rect.move_ip(0, -player.missile.missile_speed)
    except AttributeError:
        pass

    pygame.draw.rect(game_settings.window, (255, 0, 0),
                     player.player_rect, 1)
    pygame.display.update()
