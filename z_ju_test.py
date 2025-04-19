# Just for TestPlatform
# if self.__player.check_collision(TestPlatform.get_width(), TestPlatform.get_height(), TestPlatform.get_pos()) is True:
#     if self.__player.get_speed_y() > 0: # Player landed on the platform
#         self.__player.set_pos(self.__player.get_pos()[0], TestPlatform.get_pos()[1] - self.__player.get_height())
#         self.__player.landed()
#     elif self.__player.get_speed_y() < 0: # Player's head hit a platform
#         self.__player.set_pos(self.__player.get_pos()[0], TestPlatform.get_pos()[1] + TestPlatform.get_height())
#         self.__player.hit_head()


# Draw single platform
# self.__window.get_surface().blit(TestPlatform.get_surface(), (TestPlatform.get_pos()[0] - scroll_x, TestPlatform.get_pos()[1] - scroll_y))

# def jump(self):
#         self.__speed_y = -self.__gravity_val*8
#         self.__num_jumps += 1
#         if self.__num_jumps == 1:
#             self.__fall_count = 0

# for platform in self.__platform_list:
            #     if self.__player.check_collision(platform.get_width(), platform.get_height(), platform.get_pos()) is True:
            #         sides = check_collision_side(self.__player, platform)

            #         if ("left" in sides or "right" in sides) and "top" in sides:
            #             print("fdsssssssssssssssssssssssssssssssss")
            #             if self.__player.get_speed_y() > 0: # Player landed on the platform
            #                 self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] - self.__player.get_height())
            #                 self.__player.landed()
            #             elif self.__player.get_speed_y() < 0: # Player's head hit a platform
            #                 self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] + platform.get_height() + 1)
            #                 self.__player.hit_head()
            #         elif "left" in sides and "bottom" in sides:
            #             # Move player a little bit to the left
            #             self.__player.set_pos(platform.get_pos()[0] - self.__player.get_width() - 1, self.__player.get_pos()[1])
            #         elif "right" in sides and "bottom" in sides:
            #             self.__player.set_pos(platform.get_pos()[0] + platform.get_width() + 1, self.__player.get_pos()[1])
            #         elif "left" in sides:
            #             self.__player.set_pos(platform.get_pos()[0] - self.__player.get_width() - 1, self.__player.get_pos()[1])
            #         elif "right" in sides:
            #             self.__player.set_pos(platform.get_pos()[0] + platform.get_width() + 1, self.__player.get_pos()[1])
            #         else:
            #             pass

            #             if self.__player.get_speed_y() > 0: # Player landed on the platform
            #                 self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] - self.__player.get_height())
            #                 self.__player.landed()
            #             elif self.__player.get_speed_y() < 0: # Player's head hit a platform
            #                 self.__player.set_pos(self.__player.get_pos()[0], platform.get_pos()[1] + platform.get_height() + 1)
            #                 self.__player.hit_head()

# def check_collision_side(PLAYER, PLATFORM):
#     player_position = PLAYER.get_pos()
#     player_x = player_position[0]
#     player_y = player_position[1]

#     player_vertices = [
#         (player_x, player_y), # Top-left vertex
#         (player_x, player_y + PLAYER.get_height()), # Bottom-left vertex
#         (player_x + PLAYER.get_width(), player_y), # Top-right vertex
#         (player_x + PLAYER.get_width(), player_y + PLAYER.get_height()) # Bottom-right vertex
#     ]

#     platform_position = PLATFORM.get_pos()

#     platform_left_side = platform_position[0]
#     platform_right_side = platform_left_side + PLATFORM.get_width()
#     platform_top_side = platform_position[1]
#     platform_bottom_side = platform_top_side + PLATFORM.get_height()

#     directions = []

#     for vertex_x, vertex_y in player_vertices:
#         if (vertex_x >= platform_left_side and vertex_x <= platform_right_side) and (vertex_y >= platform_top_side and vertex_y <= platform_bottom_side):
#             left_distance = abs(vertex_x - platform_left_side)
#             right_distance = abs(vertex_x - platform_right_side)
#             top_distance = abs(vertex_y - platform_top_side)
#             bottom_distance = abs(vertex_y - platform_bottom_side)

#             min_distance = min(left_distance, right_distance, top_distance, bottom_distance)

#             # if min_distance == top_distance:
#             #     # print("top")
#             #     directions.append("top")
#             # elif min_distance == bottom_distance:
#             #     # print("bottom")
#             #     directions.append("bottom")
#             # elif min_distance == left_distance:
#             #     # print("left")
#             #     directions.append("left")
#             # elif min_distance == right_distance:
#             #     # print("right")
#             #     directions.append("right")

#             if top_distance <= 0.2:
#                 directions.append("top")
#             else:
#                 if min_distance == top_distance:
#                     # print("top")
#                     directions.append("top")
#                 elif min_distance == bottom_distance:
#                     # print("bottom")
#                     directions.append("bottom")
#                 elif min_distance == left_distance:
#                     # print("left")
#                     directions.append("left")
#                 elif min_distance == right_distance:
#                     # print("right")
#                     directions.append("right")
            
#             print(min_distance)
#             print(left_distance, right_distance, top_distance, bottom_distance)
#     print(directions)
    
#     return directions


