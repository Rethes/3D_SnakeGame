
<h3 align="center">Snake Game</h3>

##  <a name="table">Table of Contents</a>

1.  [Introduction](#introduction)
2.  [Tech Stack](#tech-stack)
3.  [Features](#features)
4.  [Quick Start](#quick-start)
5.  [Code Overview](#code-overview)
6.  [Future Improvements](#future-improvements)
7.  [Acknowledgements](#acknowledgements)

## <a name="introduction">Introduction</a>

A **classic snake game**, developed using **Python** and **Pygame**. This project introduces several advanced mechanics to enhance gameplay, including:

- **Passing through walls**: The snake can move from one side of the screen to the other by passing through the walls, adding a new challenge.
- **Self-collision-free snake**: The snake is immune to self-collisions, enabling more creative and complex movement.
- **Challenging obstacles**: Obstacles are placed inside the arena to increase difficulty, requiring the player to maneuver carefully.
  
With smooth controls and engaging visuals, this game provides a dynamic and entertaining experience.

### How to Play the Game

The goal of the game is to control the snake, collect apples, and achieve the highest possible score without colliding with obstacles or losing control of the snake.

**Basic Controls:**

- **Arrow Keys:**
  - Up: Move the snake up.
  - Down: Move the snake down.
  - Left: Move the snake left.
  - Right: Move the snake right.

- **Pause/Resume**: Press **P** to pause or resume the game.

- **Restart**: Press **R** to restart the game if it’s over.

- **Quit**: Press **Q** to quit the game.

## <a name="tech-stack">Tech Stack</a>

- **Python**: Programming language used for game development.
- **Pygame**: Game development library for handling graphics, events, and game logic.

## <a name="features">Features</a>

1. **Snake can pass through walls**: The snake reappears on the opposite side when it passes through a wall.
2. **Self-collision-free snake**: The snake can pass through its own body without ending the game.
3. **Snake grows with each apple eaten**: The snake’s size increases as it eats apples, making it harder to maneuver.
4. **Walls inside the arena**: Obstacles in the form of walls make navigating the arena more challenging.
5. **Scoreboard**: Displays the player’s score during the game and on the game-over screen.
6. **High score**: Tracks the highest score achieved across sessions.
7. **Pause functionality**: Pause and resume the game by pressing the P key.
8. **Game over screen**: Displays the player’s score and high score after the game ends, with options to restart or quit.
9. **Restart game**: Press R to restart the game after it’s over.
10. **Start-up splash screen**: A welcoming screen with the game title and instructions.


## <a name="quick-start">Quick Start</a>

Follow these steps to set up the project locally on your machine.

### **Prerequisites**

Make sure you have the following installed:

- **Git** for version control
- **Python** (preferably Python 3.x)

**Cloning the Repository**

```bash
git clone https://github.com/Rethes/3D_SnakeGame.git
cd 3D_SnakeGame
```

**Installation**

Install the project dependencies using pip:

```bash
 pip install -r requirements.sh
```

**Running the Project**

```bash
python main.py
```
## <a name="code-overview">Code Overview</a>

- **snake.py**: Manages the snake's movement, growth, and collision detection. It defines the behavior when the snake eats apples, grows, or collides with obstacles.
- **apple.py**: Controls the apple's appearance and random positioning on the screen. It ensures apples spawn at different locations for the player to collect.
- **walls.py**: Defines the positions and dimensions of walls within the game arena. It adds obstacles that the player must avoid.
- **main.py**: Contains the main game loop that integrates the snake, apples, and walls. It handles user inputs, game state management, and renders the game screen.
- **powerups.py**: Manages the appearance and random positioning of powerups on the screen. It controls the behavior of powerups when collected by the player.

## <a name="future-improvements">Future Improvements</a>

- **Difficulty Levels**: Add different difficulty levels with faster speeds and more obstacles to provide players with varying challenges.
- **Visual Enhancements**: Implement background images, different snake skins, and apple skins to improve the overall game aesthetics.
- **Power-ups**: Introduce power-ups like extra lives, speed boosts, or other abilities to enhance the gameplay experience.

## <a name="acknowledgements">Acknowledgements</a>

- **Pygame**: For providing the game development library that powered this project.
- **Original Snake Game**: For serving as the inspiration for this project. The classic Snake game has been a staple of game design and has influenced countless variations, including this one.
