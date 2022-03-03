import pygame
import os

from missile import Missile


class Player:
    def __init__(self, start_position: tuple) -> None:
        self.player_img = pygame.image.load(os.path.join(
            "Shooter/images/", "spaceship_player.png")).convert_alpha()
        self.player_rect = self.player_img.get_rect()
        self.player_rect.center = start_position
        self.speed = 1

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player_rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
            self.player_rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
            self.player_rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
            self.player_rect.move_ip(0, self.speed)

    def shoot_missile(self):
        self.missile = Missile(self.player_rect.center)
