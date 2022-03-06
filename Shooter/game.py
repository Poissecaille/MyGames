import pygame
from pygame.locals import *
import sys
from collision import Collision
from missile import Missile
from player import Player
from enemy import Enemy
from system import System
import random


def collide(rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
    if pygame.Rect.colliderect(rect1, rect2):
        return True
    else:
        return False


TIMER_SPAWN_ENEMY = 3000

# OBJECTS INITIALIZATION
game_system = System('Shoot them all!', (600, 1000))
player = Player(game_system.window_center)
objects = {}
objects["player"] = player
# objects["missile"] = None
objects["missiles"] = []
objects["enemies"] = []
objects["projectiles"] = []

enemy = Enemy((random.randint(0, game_system.width), 0))
objects["enemies"].append(enemy)

# MAIN LOOP
while True:

    enemy_spawn = pygame.time.get_ticks()
    missile_spawn = pygame.time.get_ticks()

    if enemy_spawn - objects["enemies"][-1].spawn_time > Enemy.SPAWN_TIMER:
        objects["enemies"].append(
            Enemy((random.randint(0, game_system.width), 0)))
        enemy_spawn = pygame.time.get_ticks()

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

    if objects["missiles"]:
        for missile in objects["missiles"]:
            missile.move()
            if missile.handle_range(game_system.height):
                del missile

            if objects["missiles"]:
                for enemy in objects["enemies"]:
                    if collide(missile.rect, enemy.rect):
                        del objects["enemies"]
                        Collision(enemy.rect.center)

    if objects["enemies"]:
        for enemy in objects["enemies"]:
            enemy.move()
    [enemy.move() for enemy in objects["enemies"] if objects["enemies"]]
    game_system.display(objects)

    pygame.display.update()
