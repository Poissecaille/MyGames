from window_handler import Window_manager
import pygame

class Game:
    def __init__(self):
        self.running = True

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
