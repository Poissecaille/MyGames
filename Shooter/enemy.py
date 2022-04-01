import pygame
import os


class Enemy:
    SHOOT_COOLDOWN = 2000
    SPAWN_TIMER = 1000

    def __init__(self, start_position: tuple) -> None:
        self.img = pygame.image.load(os.path.join(
            os.getcwd(), "images/alien_spaceship.png")).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = start_position
        self.speed = 4
        self.shoot_cooldown = pygame.time.get_ticks()
        self.spawn_time = pygame.time.get_ticks()

    def move(self) -> None:
        self.rect.move_ip(0, self.speed)

    def handle_borders(self, height: int) -> bool:
        if self.rect.bottom >= height:
            return True
        else:
            return False


        