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
objects["enemies"].append(enemy)
projectile = Projectile(game_system.window, enemy.rect.center,game_system.aim_projectile_vector(enemy,player))


# MAIN LOOP
background_iter = 0 
iter = 0
while True:

    game_system.clock.tick(60)
    enemy_spawn = pygame.time.get_ticks()
    missile_spawn = pygame.time.get_ticks()

    if enemy_spawn - objects["enemies"][-1].spawn_time > Enemy.SPAWN_TIMER:
        objects["enemies"].append(
            Enemy((random.randint(0+X_MARGIN_ENEMY_SPAWN,
                                  game_system.width-X_MARGIN_ENEMY_SPAWN), 0)))
        enemy_spawn = pygame.time.get_ticks()


    for i,enemy in enumerate(objects["enemies"]):
        timer = pygame.time.get_ticks()
        if(timer > enemy.shoot_cooldown + Enemy.SHOOT_COOLDOWN):
            objects["projectiles"].append(Projectile(game_system.window, enemy.rect.center, game_system.aim_projectile_vector(enemy,player)))
            enemy.shoot_cooldown = timer

    

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
    player.handle_borders(game_system.width, game_system.height)


    game_system.handle_collisions(objects)
    game_system.clear_objects(objects)
    game_system.move_objects(objects)
    game_system.display_background(background_iter)
    game_system.display_objects(objects)
    

    iter += 1
    if iter%2 ==0 :
        background_iter +=1
    if background_iter >= 159:
        background_iter =0
    pygame.display.update()

    
