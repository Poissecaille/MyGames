import string
import pygame
import os
from enemy import Enemy
from player import Player
from missile import Missile

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
        self.animated_background = [pygame.image.load(
            frame).convert_alpha() for frame in self.background_images_paths]
        

    def display( self , objects :dict ) -> None:
        print (objects)
        self.window.blit(self.animated_background[0], (0, 0))
        
        for key in objects:
            if key == "player":
                self.window.blit(objects[key].img, objects[key].rect)

            if key == "missile" and objects["missile"]:
                self.window.blit(objects[key].img, objects[key].rect)
                if pygame.time.get_ticks()-objects[key].flame_countdown_start < Missile.FLAME_DURATION:
                    self.window.blit(objects[key].fire_img, objects[key].fire_rect)

            if key =="enemies" and objects["enemies"] :
                for enemy in objects[key]:
                    self.window.blit(enemy.img, enemy.rect)
        
            