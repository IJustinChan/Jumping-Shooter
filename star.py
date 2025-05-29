
import pygame
from sprite import Sprite

class Star(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x=x, y=y, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._color = (255, 255, 0) # Star is a yellow square
        self._SURFACE.fill(self._color)






