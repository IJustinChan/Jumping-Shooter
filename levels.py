# Dictionary that will be used to store all the levels and fundamental platforms used to create it
# This reduces the amount of platforms that needs to be hardcoded in
levels_building_blocks = {}

# Dictionary to additional platforms that will be hardcoded into a level
# This makes the game more dynamic as the platforms will be at unique positions
extra_platforms = {}

"""
Symbols that will be used to represent what each object is at certain positions
0 - No object
1 - Platform
2 - Platform with enemy on it
3 - Star
4 - Portal
9 - Platform that the player spawns on
"""

# --- Make each level here ---
# --- Level 1 ---
level_1_main_platforms = []
level_1_extra_platforms = []

# --- Level 2 ---
level_2_main_platforms = []
level_2_extra_platforms = []


# --- Add each level to the Levels dictionary here ---
levels_building_blocks[1] = level_1_main_platforms
extra_platforms[1] = level_1_extra_platforms

levels_building_blocks[2] = level_2_main_platforms
extra_platforms[2] = level_2_extra_platforms






