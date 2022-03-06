import pygame
import os


class Effect:
    def __init__(self,position: tuple,img : str, sound : str, display_time :int = 1000) -> None:
        self.img = pygame.image.load(os.path.join(
            os.getcwd(), img)).convert_alpha()
        self.sound = pygame.mixer.Sound(os.path.join(
            os.getcwd(), sound))
        self.rect = self.img.get_rect()
        self.rect.center = position
        self.display_time= display_time
        self.countdown_start = pygame.time.get_ticks()
        #self.sound.play()