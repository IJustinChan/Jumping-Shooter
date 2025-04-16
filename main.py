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
        print(title_text.get_width())

        self.__player.set_pos(100, 100)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys_pressed = pygame.key.get_pressed()

            self.__player.move_x(keys_pressed)
            self.__player.apply_gravity()

            if keys_pressed[pygame.K_w] == 1 or keys_pressed[pygame.K_UP] == 1: # We will need to add extra condition we are doing double jumps (check jump count)
                self.__player.jump() # Not created yet
            
            if keys_pressed[pygame.K_SPACE] == 1:
                self.__player.shoot() # Not created yet

            self.__window.clear_screen()

            self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2, self.__window.get_height()/2 - title_text.get_height()/2))
            self.__window.get_surface().blit(self.__player.get_surface(), self.__player.get_pos())


            self.__window.update_frame()

if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.create_texts()
    GAME.run()









