"""
title:
authors: Jordan and Justin
date-created: 2025-04-03
"""

import pygame
from window import Window
from bullet import Bullet
from enemy import Enemy
from platforms import Platform
from player import Player
from star import Star
from text import Text


class Game():
    def __init__(self):
        self.__window = Window("Platformer", 750, 600, 60)
        self.__level = 1
        self.__player = Player(3, 50, 50, 5)
        self.__enemy_list = []
        self.__platform_list = []
        self.__star_list = []

    def __setup(self):
        pass

    def next_level(self):
        pass

    def create_level(self):
        pass

    # --- Text methods ---
    def create_texts(self):
        pass

    def draw_texts(self):
        #self.__window.get_surface().blit(title_text.get_surface(), title_text.get_pos())
        pass

    # --- Main program code ---
    def run(self):
        title_text = Text("Jumping Shooter", "Arial", 36)

        self.__player.set_pos(400, 200)

        # --- Variables to control how the camera moves as the player moves ---
        scroll_x = 0
        scroll_area_width = 100
        scroll_y = 0
        scroll_area_bottom = 100
        scroll_area_top = 150

        TestPlatform = Platform(350, 400, 100)
        TestPlatform.set_color((0, 255, 0))

        self.__platform_list.append(TestPlatform)
        self.__platform_list.append(Platform(320, 200, 50))


        while True:
            # --- INPUTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    # --- PROCESSING ---
                    if event.key == pygame.K_w or event.key == pygame.K_UP: # We will need to add extra condition if we are doing double jumps (check jump count)
                        self.__player.jump()
                    elif event.key == pygame.K_SPACE: # elif event.key == pygame.K_SPACE and len(self.__player.get_bullet_list()) <= 2: # Add this later to allow only a few bullets at a time
                        self.__player.shoot()

                    elif event.key == pygame.K_t: # For collision testing purposes
                        print(self.__player.check_collision(TestPlatform.get_width(), TestPlatform.get_height(), TestPlatform.get_pos()))
                        print(self.__player.get_speed_y())

            keys_pressed = pygame.key.get_pressed()

            # --- PROCESSING ---
            self.__player.move_x(keys_pressed)
            self.__player.apply_gravity()

            for bullet in self.__player.get_bullet_list():
                bullet.move()
            
            # --- Collisions ---
            for platform in self.__platform_list:
                if self.__player.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()) is True:
                    if self.__player.get_speed_y() > 0: # Player landed on the platform
                        self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] - self.__player.get_height())
                        self.__player.landed()
                    elif self.__player.get_speed_y() < 0: # Player's head hit a platform
                        self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] + platform.get_height())
                        self.__player.hit_head()


            # --- Handle camera movement (make camera scroll according to how the player moves) ---
            if (self.__player.get_pos()[0] + self.__player.get_width() - scroll_x >= self.__window.get_width() - scroll_area_width) and self.__player.get_moving_right() is True:
                scroll_x += self.__player.get_speed_x()

            if (self.__player.get_pos()[0] - scroll_x <= scroll_area_width) and self.__player.get_moving_left() is True:
                scroll_x -= self.__player.get_speed_x()

            if (self.__player.get_pos()[1] - scroll_y <= scroll_area_top) and self.__player.get_speed_y() <= 0: # Player is jumping up
                if self.__player.get_speed_y() != 0:
                    scroll_y += self.__player.get_speed_y()
                else:
                    scroll_y -= 5

            if (self.__player.get_pos()[1] + self.__player.get_height() - scroll_y >= self.__window.get_height() - scroll_area_bottom) and self.__player.get_speed_y() > 0: # Player is falling
                scroll_y += self.__player.get_speed_y()

            if scroll_y > 0:
                scroll_y = 0

            # --- OUTPUTS ---
            self.__window.clear_screen()

            # Don't delete the code below as it is the original one without any scrolling
            # self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2, self.__window.get_height()/2 - title_text.get_height()/2))

            # This text below includes scrolling to help with testing purposes
            self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2 - scroll_x, self.__window.get_height()/2 - title_text.get_height()/2 - scroll_y))

            for bullet in self.__player.get_bullet_list():
                self.__window.get_surface().blit(bullet.get_surface(), (bullet.get_pos()[0] - scroll_x, bullet.get_pos()[1] - scroll_y))

            self.__window.get_surface().blit(self.__player.get_surface(), (self.__player.get_pos()[0] - scroll_x, self.__player.get_pos()[1] - scroll_y))

            for platform in self.__platform_list:
                self.__window.get_surface().blit(platform.get_surface(), (platform.get_pos()[0] - scroll_x, platform.get_pos()[1] - scroll_y))


            self.__window.update_frame()

if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.create_texts()
    GAME.run()









