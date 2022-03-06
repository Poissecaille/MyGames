import pygame
from pygame.locals import *
import sys
from missile import Missile
from player import Player
from enemy import Enemy
from system import System

# OBJECTS INITIALIZATION
game_system = System('Shoot them all!', (800, 600))
player = Player(game_system.window_center)
enemy = Enemy((game_system.width/2,0))
objects = {}
objects["player"] = player
objects["missile"] = None
objects["enemies"] = []
objects["enemies"].append(enemy)
objects["projectiles"] = []

TIMER_SPAWN_ENEMY = 3000
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
            elif event.key == pygame.K_SPACE:
                objects["missile"] = Missile(player.rect.center)

                

    player.handle_keys()
    player.handle_borders(game_system.width,game_system.height)
    enemy.move()
    #enemy_spawned_timer = pygame.time.get_ticks()




    # TODO ANIMATION
    # for i in range(len(game_system.animated_background)):
    #     game_system.clock.tick(100)
    #     game_system.window.blit(game_system.animated_background[i], (0, 0))

    if  objects["missile"]:
        objects["missile"].move()
        if objects["missile"].handle_range(game_system.height):
                    objects["missile"] = None


    game_system.display(objects)
    
    pygame.display.update()
