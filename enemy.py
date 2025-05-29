
import pygame
from sprite import Sprite
from bullet import Bullet

class Enemy(Sprite):
    def __init__(self, x, y, width=1, height=1, lives=1):
        Sprite.__init__(self, x=x, y=y, width=width, height=height)
        self._SURFACE = pygame.Surface(self._dim, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._color)
        self.__lives = lives
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

    def detect_player(self, player_pos, player_height):
        """
        Checks if the player lines up with the enemy
        :param player_pos: tuple
        :param player_height: int
        :return: bool, str
        """

        player_x = player_pos[0]
        player_y = player_pos[1]

        enemy_pos = self.get_pos()
        enemy_x = enemy_pos[0]
        enemy_y = enemy_pos[1]

        see_player = False
        direction = None

        # Check to see if the player is on the same horizontal as the enemy (y-vertices between enemy's y-vertices)
        if (player_y >= enemy_y and player_y <= enemy_y + self.get_height()) or (player_y + player_height >= enemy_y and player_y + player_height <= enemy_y + self.get_height()):
            # Make sure the player is at a reasonable distance from the enemy
            x_distance = abs(enemy_x - player_x)
            # print(x_distance)
            if x_distance <= 600: # Player close enough
                see_player = True
                if player_x <= enemy_x: # Player is on the left of the enemy
                    direction = "left"
                else: # Player is on the right of the enemy
                    direction = "right"
                return see_player, direction
            else:
                see_player = False
                return see_player, direction
            
        # x_distance = abs(enemy_x - player_x)
        # print(x_distance)
        return see_player, direction

    def lose_lives(self):
        self.__lives -= 1
    
    def remove_bullet(self, bullet):
        self.__bullet_list.remove(bullet)

    # --- Accessors ---
    def get_lives(self):
        return self.__lives

    def get_bullet_list(self):
        return self.__bullet_list


