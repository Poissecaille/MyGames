import string
import pygame
import os


class GameSettings:
    def __init__(self, title: string) -> None:
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)
        self.icon = pygame.image.load(os.path.join(
            "Shooter/images", "alien.png")).convert_alpha()
        self.police = pygame.font.Font(os.path.join(
            "Shooter/polices", "MountainBridge.otf"), 25)
        self.radio = pygame.mixer.Sound(os.path.join(
            "Shooter/sounds/", "the-man-who-sold-the-world-1982.wav"))
        self.background_images_paths = ['Shooter/frames/frame_' +
                                        str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
        self.animated_background = [pygame.image.load(
            frame).convert_alpha() for frame in self.background_images_paths]
