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



class Game():
    def __init__(self):
        self.__window = Window("Platformer", 750, 600, 60)
        self.__level = 1
        self.__player = Player(3, 50, 50, 5)
        self.__enemy_list = []
        self.__platform_list = []
        self.__star_list = []
        self.__stars_collected = 0

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
        black_heading = Player(0, self.__window.get_width(), 75, 0)
        black_heading.set_color((0, 0, 0))

        star1 = Star(70, 300, 20, 20)
        self.__star_list.append(star1)

        player_lives_text = Text(f"Lives: {self.__player.get_lives()}", "Arial")
        level_text = Text(f"Level: {self.__level}", "Arial", 36, 150, 0)
        stars_text = Text(f"Stars Collected: {self.__stars_collected}", "Arial", 36, 300, 0)

        self.__player.set_pos(0, 200)

        test_enemy = Enemy(600, 450, 50, 50, 1)

        # --- Variables to control how the camera moves as the player moves ---
        scroll_x = 0
        scroll_area_width = 150
        scroll_y = 0
        scroll_area_bottom = 100
        scroll_area_top = 225

        TestPlatform = Platform(350, 350, 100)
        TestPlatform.set_color((0, 255, 0))

        # self.__platform_list.append(TestPlatform)
        # self.__platform_list.append(Platform(320, 200, 50))

        # floor = [Platform(i * 100, self.__window.get_height() - 100, 100)
        #      for i in range(-self.__window.get_width() // 100, (self.__window.get_width() * 2) // 100)]
        # self.__platform_list += floor

        Map = [[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        
        Count = 0
        for i in range(len(Map) - 1, -1, -1):
            for j in range(len(Map[0])):
                if Map[i][j] == 1:
                    self.__platform_list.append(Platform(100*j, (100*Count*-1) + self.__window.get_height() - 100, 100))
                    self.__platform_list[-1].set_color((0, 255, 0))
            Count += 1


        while True:
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

                    elif event.key == pygame.K_SPACE and len(self.__player.get_bullet_list()) < 2: # Add this later to allow only a few bullets at a time
                        self.__player.shoot()
                    elif event.key == pygame.K_t: # For collision testing purposes
                        # print(self.__player.check_collision(TestPlatform.get_width(), TestPlatform.get_height(), TestPlatform.get_pos()))
                        # print(self.__player.get_speed_y())
                        # if check_touching_platform(self.__player, self.__platform_list) is True:
                        #     print(True)
                        # else:
                        #     print(False)
                        see_player, direction = test_enemy.detect_player(self.__player.get_pos(), self.__player.get_height())
                        print(see_player)
                        print(direction)
                        if see_player is True:
                            test_enemy.shoot(direction)
            
            for bullet in test_enemy.get_bullet_list():
                bullet.move()

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
                    if bullet_x > self.__window.get_width() + scroll_x:
                        self.__player.remove_bullet(bullet)
                elif bullet_direction == -1: # Bullet moving to the left
                    if bullet_x < 0 + scroll_x - bullet.get_width():
                        self.__player.remove_bullet(bullet)
                
                for platform in self.__platform_list:
                    try:
                        if bullet.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()):
                            self.__player.remove_bullet(bullet)
                            break
                    except:
                        pass
  
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
                    stars_text.update_text(f"Stars Collected: {self.__stars_collected}")
                    self.__star_list.remove(star)


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

            # Don't delete the code below as it is the original one without any scrolling
            # self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2, self.__window.get_height()/2 - title_text.get_height()/2))

            # This text below includes scrolling to help with testing purposes
            self.__window.get_surface().blit(title_text.get_surface(), (self.__window.get_width()/2 - title_text.get_width()/2 - scroll_x, self.__window.get_height()/2 - title_text.get_height()/2 - scroll_y))

            for bullet in self.__player.get_bullet_list():
                self.__window.get_surface().blit(bullet.get_surface(), (bullet.get_pos()[0] - scroll_x, bullet.get_pos()[1] - scroll_y))

            
            for platform in self.__platform_list:
                self.__window.get_surface().blit(platform.get_surface(), (platform.get_pos()[0] - scroll_x, platform.get_pos()[1] - scroll_y))
            
            self.__window.get_surface().blit(black_heading.get_surface(), black_heading.get_pos())
            self.__window.get_surface().blit(player_lives_text.get_surface(), player_lives_text.get_pos())
            self.__window.get_surface().blit(level_text.get_surface(), level_text.get_pos())
            self.__window.get_surface().blit(stars_text.get_surface(), stars_text.get_pos())

            # Test enemy
            self.__window.get_surface().blit(test_enemy.get_surface(), (test_enemy.get_pos()[0] - scroll_x, test_enemy.get_pos()[1] - scroll_y))
            for bullet in test_enemy.get_bullet_list():
                self.__window.get_surface().blit(bullet.get_surface(), (bullet.get_pos()[0] - scroll_x, bullet.get_pos()[1] - scroll_y))

            for star in self.__star_list:
                self.__window.get_surface().blit(star.get_surface(), (star.get_pos()[0] - scroll_x, star.get_pos()[1] - scroll_y))


            self.__window.get_surface().blit(self.__player.get_surface(), (self.__player.get_pos()[0] - scroll_x, self.__player.get_pos()[1] - scroll_y))


            self.__window.update_frame()

if __name__ == "__main__":
    pygame.init()
    GAME = Game()
    GAME.create_texts()
    GAME.run()









