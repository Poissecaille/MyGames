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
        
        self.background_images_paths = ['frames/frame_' +
                                        str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]

        # On charge toutes les images du background dans une liste
        self.animated_background = [pygame.transform.scale(pygame.image.load(
            frame).convert_alpha(), (self.width, self.height)) for frame in self.background_images_paths]

    def display_objects(self, objects: dict) -> None:
        for key in objects:
            if key == "player":
                self.window.blit(objects[key].img, objects[key].rect)

            if key == "missiles" and objects["missiles"]:
                for missile in objects[key]:
                    self.window.blit(missile.img, missile.rect)

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

                        
