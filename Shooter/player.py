import pygame
import os


class Player:
    def __init__(self, start_position: tuple) -> None:
        self.player_img = pygame.image.load(os.path.join(
            "Shooter/images/", "spaceship_player.png")).convert_alpha()
        self.x = start_position[0]/2
        self.y = start_position[1]/4
