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
from portal import Portal
import levels

def check_touching_platform(PLAYER, PLATFORM_LIST):
    for platform in PLATFORM_LIST:
        if PLAYER.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()) is True:
            return True
    return False

def check_collide_right(PLAYER, PLATFORM_LIST, SPEED):
    player_position = PLAYER.get_pos()
    player_x = player_position[0]
    player_y = player_position[1]
    
    new_top_right = (player_x + PLAYER.get_width() + SPEED, player_y)
    new_bottom_right = (player_x + PLAYER.get_width() + SPEED, player_y + PLAYER.get_height())

    new_top_left = (player_x + SPEED, player_y)
    new_bottom_left = (player_x + SPEED, player_y + PLAYER.get_height())

    for platform in PLATFORM_LIST:
        platform_position = platform.get_pos()

        platform_left_side = platform_position[0]
        platform_right_side = platform_left_side + platform.get_width()
        platform_top_side = platform_position[1]
        platform_bottom_side = platform_top_side + platform.get_height()

        if (new_top_left[0] >= platform_left_side and new_top_left[0] <= platform_right_side) and (new_top_left[1] >= platform_top_side and new_top_left[1] <= platform_bottom_side):
            continue
        if (new_bottom_left[0] >= platform_left_side and new_bottom_left[0] <= platform_right_side) and (new_bottom_left[1] >= platform_top_side and new_bottom_left[1] <= platform_bottom_side):
            continue

        if (new_top_right[0] >= platform_left_side and new_top_right[0] <= platform_right_side) and (new_top_right[1] > platform_top_side and new_top_right[1] < platform_bottom_side):
            return True
        if (new_bottom_right[0] >= platform_left_side and new_bottom_right[0] <= platform_right_side) and (new_bottom_right[1] > platform_top_side and new_bottom_right[1] < platform_bottom_side):
            return True
    return False
    

def check_collide_left(PLAYER, PLATFORM_LIST, SPEED):
    player_position = PLAYER.get_pos()
    player_x = player_position[0]
    player_y = player_position[1]

    new_top_left = (player_x - SPEED, player_y)
    new_bottom_left = (player_x - SPEED, player_y + PLAYER.get_height())

    new_top_right = (player_x - SPEED, player_y)
    new_bottom_right = (player_x - SPEED, player_y + PLAYER.get_height())

    for platform in PLATFORM_LIST:
        platform_position = platform.get_pos()

        platform_left_side = platform_position[0]
        platform_right_side = platform_left_side + platform.get_width()
        platform_top_side = platform_position[1]
        platform_bottom_side = platform_top_side + platform.get_height()

        if (new_top_right[0] <= platform_left_side and new_top_right[0] >= platform_right_side) and (new_top_right[1] >= platform_top_side and new_top_right[1] <= platform_bottom_side):
            continue
        if (new_bottom_right[0] <= platform_left_side and new_bottom_right[0] >= platform_right_side) and (new_bottom_right[1] >= platform_top_side and new_bottom_right[1] <= platform_bottom_side):
            continue

        if (new_top_left[0] <= platform_right_side and new_top_left[0] >= platform_right_side) and (new_top_left[1] > platform_top_side and new_top_left[1] <= platform_bottom_side):
            return True
        if (new_bottom_right[0] <= platform_right_side and new_bottom_left[0] >= platform_right_side) and (new_bottom_right[1] > platform_top_side and new_bottom_right[1] <= platform_bottom_side):
            return True
    return False

def count_stars(MAP):
    num_stars = 0
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == 3:
                num_stars += 1
    return num_stars


class Game():
    def __init__(self):
        self.__window = Window("Platformer", 800, 600, 60)
        self.__level = 1
        self.__player = Player(5, 50, 50, 5)
        self.__enemy_list = []
        self.__platform_list = []
        self.__star_list = []
        self.__stars_collected = 0
        self.__all_levels = None
        self.__all_extra_platforms = None
        self.__setup()

    def __setup(self):
        all_levels_dict, all_platforms_dict = levels.get_levels_data()
        self.__all_levels = all_levels_dict
        self.__all_extra_platforms = all_platforms_dict

    def next_level(self):
        self.__level += 1
        self.__platform_list = []
        self.__enemy_list = []
        self.__star_list = []

    def create_level(self, MAP, EXTRA_PLATFORMS, ENEMY_COLORS):
        PLATFORM_LIST = []
        ENEMY_LIST = []
        STARS_LIST = []
        
        PLAYER_POS = None

        Count = 0
        for i in range(len(MAP) - 1, -1, -1):
            for j in range(len(MAP[0])):
                if MAP[i][j] == 1:
                    PLATFORM_LIST.append(Platform(100*j, (100*Count*-1) + self.__window.get_height() - 100, 100))
                    PLATFORM_LIST[-1].set_color((0, 255, 0))
                elif MAP[i][j] == 9:
                    PLAYER_POS = (100*j, (100*Count*-1) + self.__window.get_height() - 100)
                    # self.__player.set_pos(100*j, (100*Count*-1) + self.__window.get_height() - 100)
                elif MAP[i][j] == 3:
                    STARS_LIST.append(Star(100*j, (100*Count*-1) + self.__window.get_height() - 100, 20, 20))
                elif MAP[i][j] == 2:
                    ENEMY_LIST.append(Enemy(100*j + 25, (100*Count*-1) + self.__window.get_height() - 100+50, 50, 50, 1))
                    ENEMY_LIST[-1].set_color(ENEMY_COLORS[1])
                elif MAP[i][j] == 4:
                    portal_obj = Portal(100*j + 10, (100*Count*-1) + self.__window.get_height() - 100 + 20, 80, 80)
                elif MAP[i][j] == 5:
                    ENEMY_LIST.append(Enemy(100*j + 25, (100*Count*-1) + self.__window.get_height() - 100+50, 50, 50, 2))
                    ENEMY_LIST[-1].set_color(ENEMY_COLORS[2])
            Count += 1

        for platform in EXTRA_PLATFORMS:
            PLATFORM_LIST.append(platform)

        return PLATFORM_LIST, ENEMY_LIST, STARS_LIST, PLAYER_POS, portal_obj
    
    # --- Start screen code ---
    def show_start_screen(self):
        title_text = Text("Jumping Shooter", "Arial", 70)
        play_text = Text("Press the space bar to start the game!", "Arial", 40)

        running = True
        while running:
            # --- INPUTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_SPACE] == 1:
                running = False
            
            self.__window.clear_screen()
            self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2, self.__window.get_height()/2 - title_text.get_height()/2))
            self.__window.get_surface().blit(play_text.get_surface(), (self.__window.get_width()/2 - play_text.get_width()/2, self.__window.get_height()/2 - play_text.get_height()/2 + 100))

            self.__window.update_frame()

    # --- End screen code ---
    def show_end_screen(self):
        finished_game_text = Text("You have completed the game! Thanks for playing!", "Arial", 35)
        restart_text = Text("Press the space bar if you want to restart the game", "Arial", 30)
        exit_text = Text("Press the exit button in the top right corner to quit the game", "Arial", 25)

        running = True
        while running:
            # --- INPUTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_SPACE] == 1:
                running = False
                self.__level = 1
                self.__stars_collected = 0
                self.__player.set_lives(5)
            
            self.__window.clear_screen()
            self.__window.get_surface().blit(finished_game_text.get_surface(), (self.__window.get_width()/2 - finished_game_text.get_width()/2, self.__window.get_height()/2 - finished_game_text.get_height()/2 - 20))
            self.__window.get_surface().blit(restart_text.get_surface(), (self.__window.get_width()/2 - restart_text.get_width()/2, self.__window.get_height()/2 - restart_text.get_height()/2 + 50))
            self.__window.get_surface().blit(exit_text.get_surface(), (self.__window.get_width()/2 - exit_text.get_width()/2, self.__window.get_height()/2 - exit_text.get_height()/2 + 100))

            self.__window.update_frame()

    # --- Main program code ---
    def run(self):

        # --- Enemy colors ---
        enemy_colors = {
            1: (50, 80, 200),
            2: (0, 0, 0)
        }

        black_heading = Player(0, self.__window.get_width(), 75, 0)
        black_heading.set_color((0, 0, 0))

        player_lives_text = Text(f"Lives: {self.__player.get_lives()}", "Arial")
        level_text = Text(f"Level: {self.__level}", "Arial", 36, 150, 0)

        self.__player.set_pos(0, 200)

        # --- Variables to control how the camera moves as the player moves ---
        scroll_x = 0
        scroll_area_width = 205
        scroll_y = 0
        scroll_area_bottom = 165
        scroll_area_top = 225

        max_level = len(self.__all_levels)

        Map = self.__all_levels[self.__level]
        additional_platforms = self.__all_extra_platforms[self.__level]

        self.__platform_list, self.__enemy_list, self.__star_list, player_pos, portal_obj = self.create_level(Map, additional_platforms, enemy_colors)
        total_stars = count_stars(Map)

        stars_text = Text(f"Stars Collected: {self.__stars_collected}/{total_stars}", "Arial", 36, 300, 0)

        running = True
        while running:
            # --- INPUTS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    # --- PROCESSING ---
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.__player.get_num_jumps() == 0: # Player is making their first jump
                            # Ensure the player is on a platform for them to jump
                            if check_touching_platform(self.__player, self.__platform_list) is True:
                                self.__player.jump()

                        elif self.__player.get_num_jumps() == 1: # Player is doing double jump
                            self.__player.jump()

                    elif event.key == pygame.K_SPACE and len(self.__player.get_bullet_list()) < 2:
                        self.__player.shoot()

            keys_pressed = pygame.key.get_pressed()

            # --- PROCESSING ---
            if keys_pressed[pygame.K_d] == 1 or keys_pressed[pygame.K_RIGHT] == 1:
                if check_collide_right(self.__player, self.__platform_list, self.__player.get_speed_x()) is False:
                    self.__player.move_x(keys_pressed)
            elif keys_pressed[pygame.K_a] == 1 or keys_pressed[pygame.K_LEFT] == 1:
                if check_collide_left(self.__player, self.__platform_list, self.__player.get_speed_x()) is False:
                    self.__player.move_x(keys_pressed)

            self.__player.apply_gravity()

            for bullet in self.__player.get_bullet_list():
                bullet.move()
                bullet_direction = bullet.get_dir_x()
                bullet_position = bullet.get_pos()
                bullet_x = bullet_position[0]
                if bullet_direction == 1: # Bullet moving to the right
                    if bullet_x > self.__window.get_width() + scroll_x + 150:
                        self.__player.remove_bullet(bullet)
                elif bullet_direction == -1: # Bullet moving to the left
                    if bullet_x < 0 + scroll_x - bullet.get_width() - 150:
                        self.__player.remove_bullet(bullet)
                
                for platform in self.__platform_list:
                    try:
                        if bullet.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()):
                            self.__player.remove_bullet(bullet)
                            break
                    except:
                        pass
            
            for enemy in self.__enemy_list:
                see_player, shooting_direction = enemy.detect_player(self.__player.get_pos(), self.__player.get_height())
                if see_player is True:
                    if len(enemy.get_bullet_list()) < 1:
                        enemy.shoot(shooting_direction)
                
                for bullet in enemy.get_bullet_list():
                    bullet.move()

                    enemy_bullet_x = bullet.get_pos()[0]
                    player_x = self.__player.get_pos()[0]
                    distance = abs(enemy_bullet_x - player_x)
                    if distance > 700:
                        enemy.remove_bullet(bullet)

            # Check if the player fell down the map
            if self.__player.get_pos()[1] > self.__window.get_height() + 1300: # Player dead
                # Respawn the player somewhere
                self.__player.set_pos(0, 200)
                scroll_x = 0
                scroll_y = 0
                self.__player.lose_life()
  
            # --- Collisions ---
            for platform in self.__platform_list:
                if self.__player.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()) is True:
                    # check_collision_side(self.__player, platform)
                    if self.__player.get_speed_y() > 0: # Player landed on the platform
                        self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] - self.__player.get_height())
                        self.__player.landed()
                    elif self.__player.get_speed_y() < 0: # Player's head hit a platform
                        self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] + platform.get_height() + 1)
                        self.__player.hit_head()
            
            for star in self.__star_list:
                if self.__player.check_collision(star.get_width(), star.get_height(), star.get_pos()) is True:
                    self.__stars_collected += 1
                    stars_text.update_text(f"Stars Collected: {self.__stars_collected}/{total_stars}")
                    self.__star_list.remove(star)
            
            for enemy in self.__enemy_list:
                for bullet in enemy.get_bullet_list():
                    if self.__player.check_collision(bullet.get_width(), bullet.get_height(), bullet.get_pos()) is True:
                        enemy.remove_bullet(bullet)
                        self.__player.lose_life()

            for enemy in self.__enemy_list:
                if self.__player.check_collision(enemy.get_width(), enemy.get_height(), enemy.get_pos()) is True:
                    self.__enemy_list.remove(enemy)
                    self.__player.lose_life()
            
            for enemy in self.__enemy_list:
                for bullet in enemy.get_bullet_list():
                    for platform in self.__platform_list:
                        if bullet.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()) is True:
                            enemy.remove_bullet(bullet)

            # Traverse the list backwards to make deletion easier
            for bullet in reversed(self.__player.get_bullet_list()):
                for enemy in self.__enemy_list:
                    if bullet.check_collision(enemy.get_width(), enemy.get_height(), enemy.get_pos()) is True:
                        self.__player.remove_bullet(bullet)
                        enemy.lose_lives()
                        if enemy.get_lives() < 1:
                            self.__enemy_list.remove(enemy)
                        else:
                            enemy.set_color(enemy_colors[enemy.get_lives()])
                        break
            
            # --- Check collision with portal ---
            if self.__player.check_collision(portal_obj.get_width(), portal_obj.get_height(), portal_obj.get_pos()) is True and self.__stars_collected == total_stars:
                self.next_level()
                if self.__level > max_level:
                    running = False
                else:

                    Map = self.__all_levels[self.__level]
                    additional_platforms = self.__all_extra_platforms[self.__level]
                    self.__platform_list, self.__enemy_list, self.__star_list, player_pos, portal_obj = self.create_level(Map, additional_platforms, enemy_colors)
                    self.__player.set_pos(player_pos[0], player_pos[1])
                    scroll_x = 0
                    scroll_y = 0
                    self.__player.set_lives(5)

                    total_stars = count_stars(Map)
                    self.__stars_collected = 0
                    stars_text.update_text(f"Stars Collected: {self.__stars_collected}/{total_stars}")
                    level_text.update_text(f"Level: {self.__level}")
                

            # --- Update texts ---
            player_lives_text.update_text(f"Lives: {self.__player.get_lives()}")


            # --- Check if the player died ---
            if self.__player.get_lives() <= 0:
                # Reset the level by recreating all the map and all enemies and stars
                Map = self.__all_levels[self.__level]
                additional_platforms = self.__all_extra_platforms[self.__level]
                self.__platform_list, self.__enemy_list, self.__star_list, player_pos, portal_obj = self.create_level(Map, additional_platforms, enemy_colors)
                self.__player.set_pos(player_pos[0], player_pos[1])
                scroll_x = 0
                scroll_y = 0
                self.__player.set_lives(5)
                self.__player.clear_bullet_list()

                total_stars = count_stars(Map)
                self.__stars_collected = 0
                stars_text.update_text(f"Stars Collected: {self.__stars_collected}/{total_stars}")
                level_text.update_text(f"Level: {self.__level}")


            # --- Handle camera movement (make camera scroll according to how the player moves) ---
            if (self.__player.get_pos()[0] + self.__player.get_width() - scroll_x >= self.__window.get_width() - scroll_area_width) and self.__player.get_moving_right() is True: # Right
                scroll_x += self.__player.get_speed_x()

            if (self.__player.get_pos()[0] - scroll_x <= scroll_area_width) and self.__player.get_moving_left() is True: # Left
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

            for bullet in self.__player.get_bullet_list():
                self.__window.get_surface().blit(bullet.get_surface(), (bullet.get_pos()[0] - scroll_x, bullet.get_pos()[1] - scroll_y))

            
            for platform in self.__platform_list:
                self.__window.get_surface().blit(platform.get_surface(), (platform.get_pos()[0] - scroll_x, platform.get_pos()[1] - scroll_y))
            
            for enemy in self.__enemy_list:
                for bullet in enemy.get_bullet_list():
                    self.__window.get_surface().blit(bullet.get_surface(), (bullet.get_pos()[0] - scroll_x, bullet.get_pos()[1] - scroll_y))

            for enemy in self.__enemy_list:
                self.__window.get_surface().blit(enemy.get_surface(), (enemy.get_pos()[0] - scroll_x, enemy.get_pos()[1] - scroll_y))
            
            for star in self.__star_list:
                self.__window.get_surface().blit(star.get_surface(), (star.get_pos()[0] - scroll_x, star.get_pos()[1] - scroll_y))

            self.__window.get_surface().blit(portal_obj.get_surface(), (portal_obj.get_pos()[0] - scroll_x, portal_obj.get_pos()[1] - scroll_y))
            
            self.__window.get_surface().blit(black_heading.get_surface(), black_heading.get_pos())
            self.__window.get_surface().blit(player_lives_text.get_surface(), player_lives_text.get_pos())
            self.__window.get_surface().blit(level_text.get_surface(), level_text.get_pos())
            self.__window.get_surface().blit(stars_text.get_surface(), stars_text.get_pos())


            self.__window.get_surface().blit(self.__player.get_surface(), (self.__player.get_pos()[0] - scroll_x, self.__player.get_pos()[1] - scroll_y))


            self.__window.update_frame()

if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.show_start_screen()

    while True:
        GAME.run()
        GAME.show_end_screen()









