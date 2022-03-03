import pygame
import os


class Missile:
    DISTANCE_FROM_SHIP = 20

    def __init__(self, start_position: tuple) -> None:
        self.missile_img = pygame.image.load(os.path.join(
            "Shooter/images/", "missile-1.png")).convert_alpha()
        self.missile_rect = self.missile_img.get_rect()
        self.missile_rect.center = start_position
        #self.missile_rect.center[1] + Missile.DISTANCE_FROM_SHIP
        self.fire_img = pygame.image.load(os.path.join(
            "Shooter/images/", "fire-missile.png")).convert_alpha()
        self.missile_noise = pygame.mixer.Sound(
            os.path.join("Shooter/sounds", "missile.wav"))
        self.missile_noise.play()
        self.missile_speed = 1
        # self.missile_rect.move_ip(0, self.missile_speed)
