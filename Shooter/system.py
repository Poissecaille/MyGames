import random
import string
import pygame
import os
from enemy import Enemy
from player import Player
from missile import Missile
from effect import Effect


class System:
    def __init__(self, title: string, window_size: tuple) -> None:
        self.width = window_size[0]
        self.height = window_size[1]
        self.window = pygame.display.set_mode(
            (self.width, self.height))
        self.window_center = self.window.get_rect().center
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.icon = pygame.image.load(os.path.join(
            os.getcwd(), "images/alien.png")).convert_alpha()
        self.police = pygame.font.Font(os.path.join(
            os.getcwd(), "polices/MountainBridge.otf"), 25)
        self.radio = pygame.mixer.Sound(os.path.join(
            os.getcwd(), "sounds/the-man-who-sold-the-world-1982.wav"))
        self.background_images_paths = ['frames/frame_' +
                                        str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
        self.animated_background = [pygame.transform.scale(pygame.image.load(
            frame).convert_alpha(), (self.width, self.height)) for frame in self.background_images_paths]

    def display_objects(self, objects: dict) -> None:
       # print(objects)
        #self.window.blit(self.animated_background[0], (0, 0))

        for key in objects:
            if key == "player":
                self.window.blit(objects[key].img, objects[key].rect)

            if key == "missiles" and objects["missiles"]:
                for missile in objects[key]:
                    self.window.blit(missile.img, missile.rect)
                    if pygame.time.get_ticks()-missile.flame_countdown_start < Missile.FLAME_DURATION:
                        self.window.blit(
                            missile.fire_img, missile.fire_rect)

            if key == "enemies" and objects["enemies"]:
                for enemy in objects[key]:
                    self.window.blit(enemy.img, enemy.rect)

            if key == "effects":
                for effect in objects[key]:
                    self.window.blit(effect.img, effect.rect)

            if key == "projectiles":
                for i, projectile in enumerate(objects[key]):
                    projectile.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    projectile.circle_rect = pygame.draw.circle(
                        self.window, projectile.color, projectile.circle_rect.center, projectile.radius, width=0)

    def display_background(self, index) -> None:
        self.window.blit(self.animated_background[index], (0, 0))


    def clear_objects(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            if missile.handle_range(self.height):
                del objects["missiles"][i]

        for i, enemy in enumerate(objects["enemies"]):
            if enemy.handle_borders(self.height):
                del objects["enemies"][i]

        for i, effect in enumerate(objects["effects"]):
            if pygame.time.get_ticks()-effect.countdown_start > effect.display_time:
                del objects["effects"][i]

        for i, key in enumerate(objects["projectiles"]):
            if key == "enemy{}".format(str(i)):
                for y, projectile in enumerate(objects["projectiles"][key]):
                    if projectile.handle_range(self.width, self.height):
                        del objects["projectiles"][key][y]

    def move_objects(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            missile.move()

        for i, enemy in enumerate(objects["enemies"]):
            enemy.move()

        for i, projectile in enumerate(objects["projectiles"]):
            projectile.move()

    def aim_projectile_vector (self, enemy , player) :
        speed_x = abs(enemy.rect.center[0] - player.rect.center[0]) // 20
        speed_y = abs(enemy.rect.center[1] - player.rect.center[1]) // 20


        if player.rect.center[1] < enemy.rect.center[1]:
            speed_y *= -1

        if player.rect.center[0] < enemy.rect.center[0]:
            speed_x *= -1
        return (speed_x,speed_y)

    def collide(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
        if pygame.Rect.colliderect(rect1, rect2):
            return True
        else:
            return False

    def handle_collisions(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            for j, enemy in enumerate(objects["enemies"]):
                if self.collide(missile.rect, enemy.rect):
                    objects["effects"].append(
                        Effect(enemy.rect.center, "images/explosion.png", "sounds/explosion.wav"))
                    del objects["missiles"][i]
                    del objects["enemies"][j]

        for i, effect in enumerate(objects["effects"]):
            if self.collide(effect.rect, objects["player"]):
                del objects["effects"][i]
                objects["player"].life -= 1
                if objects["player"].life <= 0:
                    objects["effects"].append(Effect(
                        objects["player"].rect.center, "images/explosion.png", "sounds/explosion.wav"))
        
        for i, projectile in enumerate(objects["projectiles"]):
            if self.collide(projectile.circle_rect, objects["player"]):
                objects["effects"].append(
                    Effect(projectile.circle_rect.center, "images/explosion.png", "sounds/explosion.wav"))
                del objects["projectiles"][i]
                        
