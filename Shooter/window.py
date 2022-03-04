import string
import pygame
import os


class GameSettings:
    def __init__(self, title: string, window_size: tuple) -> None:
        self.width = window_size[0]
        self.height = window_size[1]
        self.window = pygame.display.set_mode(
            (self.width, self.height))
        self.window_center = self.window.get_rect().center
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)
        self.icon = pygame.image.load(os.path.join(
            os.getcwd(), "images/alien.png")).convert_alpha()
        self.police = pygame.font.Font(os.path.join(
            os.getcwd(), "polices/MountainBridge.otf"), 25)
        self.radio = pygame.mixer.Sound(os.path.join(
            os.getcwd(), "sounds/the-man-who-sold-the-world-1982.wav"))
        self.background_images_paths = ['frames/frame_' +
                                        str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
        self.animated_background = [pygame.image.load(
            frame).convert_alpha() for frame in self.background_images_paths]
