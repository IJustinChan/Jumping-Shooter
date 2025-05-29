# CSE3190-Project

## Game Overview
Our game is called Jumping Shooter. The objective of the player is to go through a map and collect all the stars so they can go through a portal to the next level. The player will need to defeat enemies along the way by shooting the enemies. However, the enemies can also shoot back and the player only has five lives. Once the player reaches a portal, they will be taken to the next level. There is a total of three levels made in this game. The game will be completed once the player completes the third level.


## How To Run The Program
Run the file _main.py_. Ensure that Python and Pygame are installed.


## How to Play
1. Use "A" or left arrow key to move the player left. Use "D" or right arrow key to move right.
2. Press "W" or the up arrow key to jump. The user can also double-jump by pressing the jump key for the second when the player is in the air. However, to jump for the first time, the player must be on a platform (first jump cannot be in the air, but they can double jump when player in the air after the first jump).
3. Press the space bar to shoot bullets. The player can shoot at most two bullets at the time. The bullet will shoot to the left or right depending on the last direction key pressed. For example, if the player last pressed the right arrow key to move right, then the bullet will shoot towards the right.


## Rules
1. The player needs to find and collect all the stars in a level before the portal allows them to move onto the next level.
2. The player will lose a life when they get hit by an enemy's bullet. The player has five lives. An enemy will shoot the player when the player is to the left or to the right of the enemy.
3. If the player falls off the map, they will respawn from the beginning of the level. However, all enemies that have been killed will not be respawned and the player keeps all the stars they have collected. The player will lose one life when they fall off the map.
4. Some enemies have more than one life. The player may need to shoot some enemies multiple times to kill some enemies. A blue enemy has one life while a black enemy has two lives. When hitting a black enemy, the black enemy loses a life and turns into a blue enemy.
5. If the player collides with an enemy, the enemy will be killed but the player loses one life.
6. If the player loses all their lives, the level will reset. This means that the player respawns with five lives, but all the stars and enemies killed will return. The player will need to restart the level from the beginning. However, note that the player does not need to restart the entire game; they just need to restart the level when they die.
7. There are three levels in this game. Each level has their own number of stars and the player can see how many stars they collected and what the total number of stars they need to collect is. All three levels can be completed. The player has finished the game when they complete the third level.

