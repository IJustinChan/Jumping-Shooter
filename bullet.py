
import pygame
from sprite import Sprite

class Bullet(Sprite):
    def __init__(self, x, y, width, height, speed=9):
        Sprite.__init__(self, x=x, y=y, width=width, height=height, speed=speed)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.__dir_x = 1

    # --- Methods ---
    def set_dir_x(self, VAL):
        self.__dir_x = VAL

    def move(self):
        pos = self.get_pos()
        new_x = pos[0] + (self.__dir_x*self.get_speed()) # Add the speed to its x-position to move it
        self.set_pos(new_x, pos[1])

    # --- Accessors ---
    def get_dir_x(self):
        return self.__dir_x


