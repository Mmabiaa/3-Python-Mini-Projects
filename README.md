# Python Mini Projects

This repository contains several small Python projects to demonstrate basic Python programming skills. The current project is a **Multi-player Dice Rolling Game** that can be played by 2 to 4 players. Players take turns rolling dice and accumulate points, with exciting bonus rolls if they roll a six!

## Dice Rolling Game

### Description
This is a simple, interactive multi-player dice rolling game written in Python. The game allows players to roll a dice and accumulate points. The first player to reach 20 points wins! Additionally, if a player rolls a six, they are allowed to roll again for a bonus, adding to the excitement.

### Features
- **Multi-player support**: Play with 2 to 4 players.
- **Dice faces displayed**: Custom ASCII art is shown for each dice roll.
- **Bonus rolls**: Rolling a six gives players an extra roll for more points.
- **Game flow**: Players alternate turns and accumulate points. The game ends when one player reaches the target score of 20.

### Files in this Project:
- **dice_game.py**: Contains the main game logic for the Dice Rolling Game. Players take turns, roll the dice, and accumulate points. The game ends when a player reaches 20 points.
- **dice_faces.py**: Contains the ASCII representations of the dice faces (1-6), used in the main game to display the dice face after each roll.
- **game_utils.py**: A utility file that handles common functions like rolling the dice, updating scores, and checking for a winner.

### Installation

To run this project, you need Python installed on your machine. The game is written in Python 3.x.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python_mini_projects.git
