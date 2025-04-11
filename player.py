
import pygame
from sprite import Sprite

class Player(Sprite):
    def __init__(self, lives, width, height, speed_x):
        Sprite.__init__(self, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.__lives = lives
        self.__speed_x = speed_x
        self.__fall_count = 0
        self.__hit = False
        self.__bullet_list = []

    # --- Methods ---
    def move_x(self, pressed_keys):
        if pressed_keys[pygame.K_d] == 1: # Move right
            self.__x += self.__speed_x

        if pressed_keys[pygame.K_a] == 1:
            self.__x -= self.__speed_x

        self.__pos = (self.__x, self.__y)

    def lose_life(self):
        self.__lives -= 1

    # --- Accessors ---
    def get_lives(self):
        return self.__lives

    def jump(self):
        pass

    def shoot(self):
        pass

    def landed(self):
        pass

    def hit_head(self):
        pass






