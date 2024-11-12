
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

**Game Objects**
- Snake: The player controls the snake and tries to grow it by eating     
  apples.
- Apple: Increases the snake’s size and score when eaten.
- Banana: A power-up that appears after a certain number of apples are eaten. Gives a score boost and speed increase.
- Grape: Another power-up that appears after eating more apples. Gives a bigger score boost and speed increase.

- **Passing through walls**: The snake can move from one side of the screen to the other by passing through the walls, adding a new challenge.
- **Self-collision-free snake**: The snake is immune to self-collisions, enabling more creative and complex movement.
- **Challenging obstacles**: Obstacles are placed inside the arena to increase difficulty, requiring the player to maneuver carefully.
  
With smooth controls and engaging visuals, this game provides a dynamic and entertaining experience.

**How to play the game**
The main objective is to control the snake, collect apples, and achieve the highest possible score without colliding with obstacles or losing control.

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

1. The snake can pass through walls 

2. The snake cannot collide with itself 

3. The snake gets bigger when it eats apples

4. Walls inside the arena to make the game harder

5. A score board

6. Show the player's score on the game over screen

7. Pause Function

8. Implement a high score feature

9. Player can restart the game

10. Add a splash screen with the name of the game


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
## <a name="code-overview"> Code Overview</a>
- snake.py - Handles the snake's movement, growth, and collision detection.
- apple.py - Handles the apple's appearance and random positioning on the screen.
- walls.py - Defines the positions and dimensions of walls within the game.
- main.py - The main game loop that integrates the snake, apples, and walls, and handles user inputs and game state.
- powerups.py - 

## <a name="Future Improvements"> Future Improvements</a> 
- Add difficulty levels
- implement multiplayer mode
- Implement a background, snake skin and apple skin
- Add more power ups to the game
