
import pygame
from sprite import Sprite

class Platform(Sprite):
    def __init__(self, x, y, size): # Assume each individual platform is a square
        Sprite.__init__(self, x=x, y=y, width=size, height=size)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
