
import pygame
from sprite import Sprite

class Portal(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x=x, y=y, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.set_color((0, 0, 200)) # Portal will be a blue square










