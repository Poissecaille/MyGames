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

# OBJECTS INITIALIZATION
game_system = System('Shoot them all!', (600, 1000))
player = Player(game_system.window_center)
objects = {}
objects["player"] = player
objects["missiles"] = []
objects["enemies"] = []
objects["projectiles"] = {}
#objects["projectiles"]["timers"] = []
objects["effects"] = []
enemy = Enemy((random.randint(0, game_system.width), 0))
objects["enemies"].append(enemy)
projectile = Projectile(game_system.window, enemy.rect.center)

iteration = 0

# MAIN LOOP
while True:
    enemy_spawn = pygame.time.get_ticks()
    missile_spawn = pygame.time.get_ticks()
    projectile_spawn = pygame.time.get_ticks()

    if enemy_spawn - objects["enemies"][-1].spawn_time > Enemy.SPAWN_TIMER:
        objects["enemies"].append(
            Enemy((random.randint(0, game_system.width), 0)))
        enemy_spawn = pygame.time.get_ticks()

    for i, enemy in enumerate(objects["enemies"]):
        if not "enemy{}".format(str(i)) in objects["projectiles"]:
            objects["projectiles"]["enemy{}".format(str(i))] = []
            objects["projectiles"]["enemy{}".format(str(i))].append(Projectile(
                game_system.window, enemy.rect.center))
            objects["projectiles"]["timer{}".format(
                str(i))] = pygame.time.get_ticks()
        else:
            if projectile_spawn - objects["projectiles"]["enemy{}".format(str(i))][-1].spawn_time > Projectile.SPAWN_TIMER:
                objects["projectiles"]["enemy{}".format(str(i))].append(Projectile(
                    game_system.window, enemy.rect.center))
                projectile_spawn = pygame.time.get_ticks()

    dt = game_system.clock.tick(60)

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
                    # objects["missiles"] = Missile(player.rect.center)
                    objects["missiles"].append(Missile(player.rect.center))
                    missile_spawn = pygame.time.get_ticks()
    player.handle_keys()
    player.handle_borders(game_system.width, game_system.height)

    # TODO ANIMATION
    # for i in range(len(game_system.animated_background)):
    #     game_system.clock.tick(100)
    #     game_system.window.blit(game_system.animated_background[i], (0, 0))
    game_system.handle_collisions(objects)
    game_system.clear_objects(objects)
    game_system.move_objects(objects)
    # if iteration % 2 == 0:
    game_system.move_projectiles(objects["projectiles"], player.rect)
        # iteration = 0
    game_system.display(objects)
    # print(objects["effects"])
    pygame.display.update()
    # iteration += 1
    # print(iteration)