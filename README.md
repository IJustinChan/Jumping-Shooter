# Jumping Shooter

Jumping Shooter is a 2D platform shooter built with Python and Pygame. Players navigate through platform-based levels, collect stars, defeat enemies, and reach a portal to advance to the next level.

The game features gravity, double jumping, shooting, camera movement and multiple enemy types. The first three levels are predefined, while later levels are randomly generated for endless gameplay.

## Features
* 2D platforming with gravity and double jumping
* Camera movement that follows the player
* Player and enemy projectile combat
* Multiple enemy types with different health values
* Collectible stars required to unlock the portal
* Life, respawn, and level reset systems
* Randomly generated levels after Level 3

## Technologies Used
* Python
* Pygame
* Object Oriented Programming (OOP)

## How to Run

Ensure Python and Pygame are installed.

```
pip install pygame
```

Then, run the file `main.py`

## Controls

* A / Left Arrow — Move left
* D / Right Arrow — Move right
* W / Up Arrow — Jump / double jump
* Spacebar — Shoot
* Y — Skip current level
* T — Set lives to 99

## How to Play

Collect all stars in the level to unlock the portal. Defeat or avoid enemies while navigating across platforms.

The player starts with five lives and loses one when hit by a bullet, colliding with an enemy, or falling off the map.

Falling off the map respawns the player while keeping collected stars and defeated enemies. Losing all five lives resets the current level.

## Enemies
* Blue Enemy — 1 health
* Black Enemy — 2 health

After being hit once, a black enemy becomes a blue enemy.

## Level Progression
The first three levels are fixed. Every level afterward is randomly generated using a grid-based system that represents platforms, enemies, stars, and other level elements.

Because some generated levels may be impossible to complete, players can press Y to skip them. The game can continue through an unlimited number of generated levels.

## Project Structure
```
JUMPING-SHOOTER/
├── media/
│   └── star_image.png
├── bullet.py
├── enemy.py
├── extra_levels.py
├── levels.py
├── main.py
├── platforms.py
├── player.py
├── portal.py
├── sprite.py
├── star.py
├── text.py
└── window.py
```
