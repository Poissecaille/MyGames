import pygame
import random
from math import sqrt

class Projectile:
    DISTANCE_FROM_SHIP = 75
    MAX_SPEED = 10

    def __init__(self, surface, start_position: tuple, vector : tuple) -> None:
        self.color = (255, 0, 0)
        self.radius = 5
        self.circle_rect = pygame.draw.circle(
            surface, (self.color), start_position, self.radius)
        self.circle_rect.center = start_position
        #self.spawn_time = pygame.time.get_ticks()

    
        self.speed_x = vector[0]
        self.speed_y = vector[1]




    def move(self) -> None:
        self.circle_rect.x += self.speed_x
        self.circle_rect.y += self.speed_y

    def handle_range(self, width: int, height: int) -> None:
        if self.circle_rect.right >= width or self.circle_rect.left <= 0 or self.circle_rect.bottom >= height or self.circle_rect.bottom <= 0:
            return True
        else:
            return False
