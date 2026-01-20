# Pong Game

A classic Pong game implementation using Python's Turtle graphics module.

## Description

This is a two-player Pong game where players control paddles to hit a ball back and forth. The game features:
- Two-player gameplay with keyboard controls
- Score tracking for both players
- Ball speed increases after each paddle hit
- Wall collision detection
- Classic black and white retro aesthetic

## Requirements

- Python 3.x
- turtle module (comes pre-installed with Python)

## How to Run

```bash
python main.py
```

## Controls

**Left Paddle (Player 1):**
- `W` - Move up
- `S` - Move down

**Right Paddle (Player 2):**
- `↑` (Up Arrow) - Move up
- `↓` (Down Arrow) - Move down

## Game Rules

- The ball bounces off the top and bottom walls
- Players must hit the ball with their paddle to keep it in play
- If a player misses the ball, the opponent scores a point
- The ball speeds up slightly after each successful paddle hit
- Click the game window to exit

## Project Structure

- `main.py` - Main game loop and setup
- `ball.py` - Ball class with movement and collision logic
- `paddle.py` - Paddle class with movement controls
- `scoreboard.py` - Score tracking and display

## Features

- **Ball Physics**: The ball moves diagonally and bounces off walls and paddles
- **Dynamic Speed**: Ball accelerates after each paddle hit for increased difficulty
- **Score System**: Automatic score tracking for both players
- **Responsive Controls**: Smooth paddle movement with keyboard input

## License

This is a learning project created for educational purposes.
