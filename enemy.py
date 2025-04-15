
import pygame
from sprite import Sprite
from bullet import Bullet

class Enemy(Sprite):
    def __init__(self, x, y, width=1, height=1, lives=1):
        Sprite.__init__(self, x=x, y=y, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.__lives == lives
        self.__bullet_list = []

    # --- Methods ---
    def shoot(self, direction):
        """
        Make the enemy shoot a bullet when it sees the player
        :param direction: str
        :return: None
        """
        # direction is a string indicating which way to shoot the bullet
        # direction is either "left" or "right"

        bullet_width = 40
        bullet_height = 20

        current_position = self.get_pos()
        bullet_x = current_position[0] + (self.get_width()/2) - bullet_width/2
        bullet_y = current_position[1] + (self.get_height()/2) - bullet_height/2

        bullet = Bullet(bullet_x, bullet_y, bullet_width, bullet_height)

        if direction == "left": # Shoot left
            bullet.set_dir_x(-1)
        elif direction == "right": # Shoot right
            bullet.set_dir_x(1)

        self.__bullet_list.append(bullet)

    def lose_lives(self):
        self.__lives -= 1

    # --- Accessors ---
    def get_lives(self):
        return self.__lives

    def get_bullet_list(self):
        return self.__bullet_list


