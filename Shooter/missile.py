import pygame
import os



class Missile:
    DISTANCE_FROM_SHIP = 75
    DISTANCE_FROM_MISSILE = 50
    FLAME_DURATION = 100 # millisecs
    SPAWN_TIMER = 1000

    def __init__(self, start_position: tuple) -> None:
        self.img = pygame.image.load(os.path.join(
            os.getcwd(), "images/missile-1.png")).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = start_position
        self.rect.move_ip(0, -Missile.DISTANCE_FROM_SHIP)
        
        self.speed = 4
        self.flame_countdown_start = pygame.time.get_ticks()

    def move(self) -> None:
        self.rect.move_ip(0, -self.speed)

    def handle_range(self, height):
        if self.rect.top <= 0 or self.rect.bottom >= height:
            return True
        else:
            return False
            

