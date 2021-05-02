import pygame

class Window_manager():
    def __init__(self, width, height, window_name):
        self.width = width
        self.height = height
        self.window = pygame.display.setmode((self.width, self.height))
        self.window_name = pygame.display.set_caption(window_name)
    def window_update(self):
        self.window.fill((255,255,255))
        pygame.display.update()