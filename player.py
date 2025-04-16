
import pygame
from sprite import Sprite

class Player(Sprite):
    def __init__(self, lives, width, height, speed_x):
        Sprite.__init__(self, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.__lives = lives
        self.__speed_x = speed_x
        self.__speed_y = 0
        self.__fall_count = 0
        self.__hit = False
        self.__bullet_list = []
        self.__direction_facing = "right"
        self.__gravity_val = 1

    # --- Methods ---
    def apply_gravity(self):
        self.__fall_count += 1 # Add one to keep track of how long the player has been falling for

        # Increase the y-speed by a certain value with 1 being the maximum (ensures it doesn't accelerate too fast)
        # self.__fall_count is how long the player has been falling for but it is in frames per second (everytime the loop runs, we increase self.__fall_count by one)
        # We convert self.__fall_count to seconds by dividing by the FPS, which is 60. This value tells us how long the player has been in the air for in seconds.
        # We then multiply by gravity's constant, which can be any number. Default is 1, but a larger value means larger gravity.

        self.__speed_y += min(1, (self.__fall_count/60)*self.__gravity_val)
        # self.__speed_y += (self.__fall_count/60)*self.__gravity_val # Could also just use this if you want player to have unlimited acceleration

        current_position = self.get_pos()
        y_pos = current_position[1]

        y_pos += self.__speed_y
        self.set_pos(current_position[0], y_pos)

    def move_x(self, pressed_keys):
        current_position = self.get_pos()
        x_pos = current_position[0]

        if pressed_keys[pygame.K_d] == 1: # Move right
            x_pos += self.__speed_x
            self.__direction = "right"

        if pressed_keys[pygame.K_a] == 1:
            x_pos -= self.__speed_x
            self.__direction = "left"

        self.set_pos(x_pos, current_position[1])

    def lose_life(self):
        self.__lives -= 1

    def jump(self):
        pass

    def shoot(self):
        pass

    def landed(self):
        pass

    def hit_head(self):
        pass

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






