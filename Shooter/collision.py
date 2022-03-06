import pygame
import os


class Collision:
    def __init__(self, position: tuple) -> None:
        self.img = pygame.image.load(os.path.join(
            os.getcwd(), "images/explosion.png")).convert_alpha()
        self.sound = pygame.mixer.Sound(os.path.join(
            os.getcwd(), "sounds/explosion.wav"))
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.sound.play()