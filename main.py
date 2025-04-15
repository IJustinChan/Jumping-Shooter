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
        # self.__player =
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

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.__window.clear_screen()


            # self.__window.get_surface().blit(title_text.get_surface(), title_text.get_pos())
            self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2, self.__window.get_height()/2 - title_text.get_height()/2))


            self.__window.update_frame()

if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.create_texts()
    GAME.run()









