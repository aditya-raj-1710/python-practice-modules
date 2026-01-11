# Snake Game 🐍

A classic Snake game implementation using Python's Turtle graphics module.

## Description

This is a simple yet entertaining Snake game where you control a snake to eat food and grow longer. The game ends when the snake collides with the wall or its own tail.

## Features

- **Classic Snake Gameplay**: Control the snake using arrow keys
- **Score Tracking**: Live score display that increases with each food consumed
- **Collision Detection**: Wall and self-collision detection for game-over conditions
- **Growing Snake**: Snake extends each time it eats food
- **Simple Controls**: Easy-to-use arrow key controls

## Project Structure

- `main.py` - Main game loop and initialization
- `snake.py` - Snake class with movement and control logic
- `food.py` - Food class for generating random food positions
- `scoreboard.py` - Scoreboard class for score tracking and display

## Requirements

- Python 3.x
- `turtle` module (included in standard Python library)

## How to Run

```bash
python main.py
```

## Controls

- **Up Arrow** - Move snake up
- **Down Arrow** - Move snake down
- **Left Arrow** - Move snake left
- **Right Arrow** - Move snake right

## Game Rules

1. Use arrow keys to control the snake's direction
2. Eat the blue food circles to grow the snake and increase your score
3. Avoid hitting the walls (game boundary at 600x600 pixels)
4. Avoid colliding with the snake's own tail
5. Game ends when any collision occurs

## Game Over Conditions

- Snake hits any of the four walls
- Snake's head collides with any part of its body

## Technical Details

- **Screen Size**: 600x600 pixels
- **Background**: Black
- **Snake Color**: White
- **Food Color**: Blue
- **Movement Speed**: 0.1 second delay between updates
- **Collision Detection Distance**: 
  - Food: < 15 pixels
  - Tail: < 10 pixels

## Author

Created as part of a Python practice module series.
