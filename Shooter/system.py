import random
import string
import pygame
import os
from enemy import Enemy
from player import Player
from missile import Missile
from effect import Effect


class System:
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
        self.clock = pygame.time.Clock()
        self.icon = pygame.image.load(os.path.join(
            os.getcwd(), "images/alien.png")).convert_alpha()
        self.police = pygame.font.Font(os.path.join(
            os.getcwd(), "polices/MountainBridge.otf"), 25)
        self.radio = pygame.mixer.Sound(os.path.join(
            os.getcwd(), "sounds/the-man-who-sold-the-world-1982.wav"))
        self.background_images_paths = ['frames/frame_' +
                                        str(i + 1) + '_delay-0.03s.png' for i in range(0, 159)]
        self.animated_background = [pygame.transform.scale(pygame.image.load(
            frame).convert_alpha(), (self.width, self.height)) for frame in self.background_images_paths]

    def display(self, objects: dict) -> None:
       # print(objects)
        self.window.blit(self.animated_background[0], (0, 0))

        for key in objects:
            if key == "player":
                self.window.blit(objects[key].img, objects[key].rect)

            if key == "missiles" and objects["missiles"]:
                for missile in objects[key]:
                    self.window.blit(missile.img, missile.rect)
                    if pygame.time.get_ticks()-missile.flame_countdown_start < Missile.FLAME_DURATION:
                        self.window.blit(
                            missile.fire_img, missile.fire_rect)

            if key == "enemies" and objects["enemies"]:
                for enemy in objects[key]:
                    self.window.blit(enemy.img, enemy.rect)

            if key == "effects":
                for effect in objects[key]:
                    self.window.blit(effect.img, effect.rect)

            if key == "projectiles":
                for i, k in enumerate(objects[key]):
                    if "enemy{}".format(str(i)) in objects[key].keys():
                        for projectile in objects[key]["enemy{}".format(str(i))]:
                            projectile.color = (random.randint(
                                0, 255), random.randint(0, 255), random.randint(0, 255))
                            pygame.draw.circle(
                                self.window, projectile.color, projectile.circle_rect.center, projectile.radius, width=0)

    def clear_objects(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            if missile.handle_range(self.height):
                del objects["missiles"][i]

        for i, enemy in enumerate(objects["enemies"]):
            if enemy.handle_borders(self.height):
                del objects["enemies"][i]

        for i, effect in enumerate(objects["effects"]):
            if pygame.time.get_ticks()-effect.countdown_start > effect.display_time:
                del objects["effects"][i]

    def move_objects(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            missile.move()

        for i, enemy in enumerate(objects["enemies"]):
            enemy.move()

    def move_projectiles(self, projectiles: dict, player_rect) -> None:
        for i, enemy in enumerate(projectiles):
            if "enemy{}".format(str(i)) in projectiles:
                for projectile in projectiles["enemy{}".format(str(i))]:
                    if not projectile.path_updated:
                        projectile.speed_x = abs(
                            projectile.circle_rect.x - player_rect.x) // 20
                        projectile.speed_y = abs(
                            projectile.circle_rect.y - player_rect.y) // 20
                        # if projectile.speed_x <= 0:
                        #     projectile.speed_x = 1
                        if projectile.circle_rect.x > player_rect.x:
                            projectile.speed_x = projectile.speed_x * -1
                            if projectile.circle_rect.y > player_rect.y:
                                projectile.speed_y = projectile.speed_y * -1
                                projectile.move(projectile.speed_x,
                                                projectile.speed_y)
                                projectile.path_updated = True
                            else:
                                projectile.move(projectile.speed_x,
                                                projectile.speed_y)
                                projectile.path_updated = True
                        else:
                            if projectile.circle_rect.y > player_rect.y:
                                projectile.speed_y = projectile.speed_y * -1
                                projectile.move(projectile.speed_x,
                                                projectile.speed_y)
                                projectile.path_updated = True
                            else:
                                projectile.move(projectile.speed_x,
                                                projectile.speed_y)
                                projectile.path_updated = True
                    else:
                        projectile.move(projectile.speed_x, projectile.speed_y)

    def collide(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
        if pygame.Rect.colliderect(rect1, rect2):
            return True
        else:
            return False

    def handle_collisions(self, objects: dict) -> None:
        for i, missile in enumerate(objects["missiles"]):
            for j, enemy in enumerate(objects["enemies"]):
                if self.collide(missile.rect, enemy.rect):
                    objects["effects"].append(
                        Effect(enemy.rect.center, "images/explosion.png", "sounds/explosion.wav"))
                    del objects["missiles"][i]
                    del objects["enemies"][j]

        for i, effect in enumerate(objects["effects"]):
            if self.collide(effect.rect, objects["player"]):
                del objects["effects"][i]
                objects["player"].life -= 1
                if objects["player"].life <= 0:
                    objects["effects"].append(Effect(
                        objects["player"].rect.center, "images/explosion.png", "sounds/explosion.wav"))
