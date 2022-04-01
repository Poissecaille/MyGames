import pygame
from pygame.locals import *
import sys
from missile import Missile
from player import Player
from enemy import Enemy
from projectile import Projectile
from system import System
import random


TIMER_SPAWN_ENEMY = 3000
X_MARGIN_ENEMY_SPAWN = 50

# OBJECTS INITIALIZATION
game_system = System('Shoot them all!', (600, 1000))
player = Player(game_system.window_center)
objects = {}
objects["player"] = player
objects["missiles"] = []
objects["enemies"] = []
objects["projectiles"] = []
objects["effects"] = []
enemy = Enemy((random.randint(0+X_MARGIN_ENEMY_SPAWN,
                              game_system.width-X_MARGIN_ENEMY_SPAWN), 0))
#objects["enemies"].append(enemy)



# MAIN LOOP
while True:

    game_system.clock.tick(60)
    
    
    missile_spawn = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                if not objects["missiles"]:
                    objects["missiles"].append(Missile(player.rect.center))
                if objects["missiles"] and missile_spawn - objects["missiles"][-1].flame_countdown_start > Missile.SPAWN_TIMER:
                    objects["missiles"].append(Missile(player.rect.center))
                    missile_spawn = pygame.time.get_ticks()
    player.handle_keys()



    game_system.display_background(0)
    game_system.display_objects(objects)
    
    pygame.display.update()

    




    
    ## TODO ##
    # 1. Gérer les bords pour le player.
    # 2. Gérer les missiles du player
    # 3. Mettre en mouvement les objets.
    # 4. Nettoyage des objets
    # 5. Gérer le spawn des ennemis.
    # 6. Gérer la collision missile/ennemi.
    # 7. Gérer le tir ennemi
    # 8. Background dynamique