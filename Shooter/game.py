import pygame
from pygame.locals import *
import sys
from player import Player
from window import GameSettings


game_settings = GameSettings('Shoot them all!')
player_ship = Player((game_settings.window_width, game_settings.window_height))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    for i in range(len(game_settings.animated_background)):
        game_settings.window.blit(game_settings.animated_background[i], (0, 0))
        game_settings.window.blit(player_ship.player_img,
                                (player_ship.x, player_ship.y))

        # if i % 10 == 0:
        pygame.display.update()
        game_settings.clock.tick(60)
   