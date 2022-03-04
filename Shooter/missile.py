import pygame
import os

from system import System


class Missile:
    DISTANCE_FROM_SHIP = 75
    DISTANCE_FROM_MISSILE = 50
    FLAME_DURATION = 100 # millisecs
    def __init__(self, start_position: tuple) -> None:
        self.missile_img = pygame.image.load(os.path.join(
            os.getcwd(), "images/missile-1.png")).convert_alpha()
        self.missile_rect = self.missile_img.get_rect()
        self.missile_rect.center = start_position
        self.missile_rect.move_ip(0, -Missile.DISTANCE_FROM_SHIP)
        self.fire_img = pygame.image.load(os.path.join(
            os.getcwd(), "images/fire-missile.png")).convert_alpha()
        self.fire_rect = self.fire_img.get_rect()
        self.fire_rect.center = start_position
        self.fire_rect.move_ip(0, -Missile.DISTANCE_FROM_MISSILE)
        self.missile_noise = pygame.mixer.Sound(
            os.path.join(os.getcwd(), "sounds/missile.wav"))
        self.missile_noise.play()
        self.missile_speed = 1

    def move(self) -> None:
        self.missile_rect.move_ip(0, -self.missile_speed)

    def handle_range(self, system: System):
        if self.missile_rect.top <= 0:
            system.shoot_event()
        if self.missile_rect.bottom >= system.height:
            system.shoot_event()
