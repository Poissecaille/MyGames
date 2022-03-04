import pygame
import os

from system import System


class Player:
    def __init__(self, start_position: tuple) -> None:
        self.player_img = pygame.image.load(os.path.join(
            os.getcwd(), "images/spaceship_player.png")).convert_alpha()
        self.player_rect = self.player_img.get_rect()
        self.player_rect.center = start_position
        self.speed = 1

    def handle_keys(self) -> None:
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player_rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
            self.player_rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
            self.player_rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
            self.player_rect.move_ip(0, self.speed)

    def handle_borders(self, system: System) -> None:
        if self.player_rect.right >= system.width:
            self.player_rect.right = system.width
        if self.player_rect.left <= 0:
            self.player_rect.left = 0
        if self.player_rect.top <= 0:
            self.player_rect.top = 0
        if self.player_rect.bottom >= system.height:
            self.player_rect.bottom = system.height
