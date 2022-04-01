import pygame
import os


class Player:
    def __init__(self, start_position: tuple) -> None:
        self.img = pygame.image.load(os.path.join(
            os.getcwd(), "images/spaceship_player.png")).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = start_position
        self.speed = 6
        self.life = 10

    def handle_keys(self) -> None:
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)
