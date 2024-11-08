

  <h3 align="center">Snake Game</h3>


## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🤸 [Quick Start](#quick-start)

## <a name="introduction">🤖 Introduction</a>

A classic snake game, developed using Python and pygame. This project introduces various advanced mechanics that enhance gameplay, including passing through walls, a self-collision-free snake, and challenging obstacles within the arena. With engaging visuals and a smooth interface, the game offers a dynamic and entertaining experience for players.

**How to play the game**
The main objective is to control the snake, collect apples, and achieve the highest possible score without colliding with obstacles or losing control.

**Basic Controls:**

**Arrow Keys:**
- Up: Move the snake up.
- Down: Move the snake down.
- Left: Move the snake left.
- Right: Move the snake right.

**Pause/Resume**
- Press P to pause or resume the game.


## <a name="tech-stack">⚙️ Tech Stack</a>

- Python

## <a name="features">🔋 Features</a>

👉 The snake can pass through walls 

👉The snake cannot collide with itself 

👉The snake gets bigger when it eats apples

👉Walls inside the arena to make the game harder

👉A score board

👉Game over screen

👉Pause Function


## <a name="quick-start">🤸 Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed on your machine:

- Git 
- Python
- Pygame
- Random

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
## <a name="Code Overview"> Code Overview</a>
- snake.py - Handles the snake's movement, growth, and collision detection.
- apple.py - Handles the apple's appearance and random positioning on the screen.
- walls.py - Defines the positions and dimensions of walls within the game.
- main.py - The main game loop that integrates the snake, apples, and walls, and handles user inputs and game state.

## <a name="Future Improvements"> Future Improvements</a> 
- Add difficulty levels (easy, medium, hard)
- Add a start up window with the name of the game
- Implement a high score feature
- Add power ups to the game 
