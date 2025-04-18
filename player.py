
import pygame
from sprite import Sprite
from bullet import Bullet

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
        self.__num_jumps = 0
        self.__direction_facing = "right" # Allows us to determine which way to shoot the bullet
        self.__gravity_val = 1

        # bool values to see which direction player is moving --> helps with camera movement
        self.__moving_right = False
        self.__moving_left = False

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

        if pressed_keys[pygame.K_d] == 1 or pressed_keys[pygame.K_RIGHT] == 1: # Move right
            x_pos += self.__speed_x
            self.__direction_facing = "right"
            self.__moving_right = True
        else:
            self.__moving_right = False

        if pressed_keys[pygame.K_a] == 1 or pressed_keys[pygame.K_LEFT]: # Move left
            x_pos -= self.__speed_x
            self.__direction_facing = "left"
            self.__moving_left = True
        else:
            self.__moving_left = False

        self.set_pos(x_pos, current_position[1])

    def lose_life(self):
        self.__lives -= 1

    def jump(self):
        self.__num_jumps += 1
        if self.__num_jumps == 1:
            self.__fall_count = 0
            self.__speed_y = -self.__gravity_val*8
        elif self.__num_jumps == 2:
            self.__speed_y = -self.__gravity_val*11

    def shoot(self):
        bullet_width = 40
        bullet_height = 20

        current_position = self.get_pos()
        bullet_x = current_position[0] + (self.get_width()/2) - bullet_width/2
        bullet_y = current_position[1] + (self.get_height()/2) - bullet_height/2

        bullet = Bullet(bullet_x, bullet_y, bullet_width, bullet_height)
        bullet.set_color((255, 0, 0))

        if self.__direction_facing == "left": # Shoot left
            bullet.set_dir_x(-1)
        elif self.__direction_facing == "right": # Shoot right
            bullet.set_dir_x(1)

        self.__bullet_list.append(bullet)

    def landed(self):
        self.__fall_count = 0
        self.__speed_y = 0
        self.__num_jumps = 0

    def hit_head(self):
        self.__speed_y *= -1

    def remove_bullet(self, bullet):
        self.__bullet_list.remove(bullet)

    # --- Accessors ---
    def get_lives(self):
        return self.__lives
    
    def get_speed_x(self):
        return self.__speed_x
    
    def get_speed_y(self):
        return self.__speed_y

    def get_moving_right(self):
        return self.__moving_right
    
    def get_moving_left(self):
        return self.__moving_left
    
    def get_bullet_list(self):
        return self.__bullet_list

    def get_num_jumps(self):
        return self.__num_jumps
    
    
    








