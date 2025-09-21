# Turtle Race Game

An interactive racing game where players bet on which colored turtle will win a race.

## Description

This project creates a racing game featuring six turtles of different colors racing across the screen. Players can place bets on their favorite turtle and watch the race unfold with random movement patterns.

## Features

- **Six Racing Turtles**: Different colored turtles (red, green, blue, yellow, magenta, cyan)
- **Betting System**: Players bet on which turtle will win
- **Random Movement**: Each turtle moves randomly each turn
- **Race Tracking**: Detects when a turtle crosses the finish line
- **Result Display**: Shows winning turtle and bet outcome

## Game Mechanics

### Turtle Setup
- 6 turtles positioned at starting line
- Each turtle has a unique color
- Starting positions spread vertically

### Movement System
- Each turn, turtles move forward by random distance (1-20 units)
- Race continues until any turtle crosses finish line (x > 230)
- First turtle to cross wins

### Betting System
- Player inputs their bet color before race starts
- Game compares bet with winning turtle color
- Displays win/loss message with actual winner

## Project Structure

```
07-turtle-race/
├── main.py           # Main game logic
└── README.md         # This file
```

## Usage

```bash
python main.py
```

1. A dialog box appears asking for your bet
2. Enter one of: red, green, blue, yellow, magenta, cyan
3. Watch the race unfold
4. See if you won your bet!

## Example Interaction

```
Make your bet: Which turtle will win the race? Enter a color: red

You won! The ('red', 'red') turtle won the race!
```

## Key Concepts

- **Game Logic**: Implementing game rules and conditions
- **Random Movement**: Using random numbers for unpredictability
- **User Input**: Getting player choices through dialog
- **Event Detection**: Checking for race completion
- **Object Management**: Handling multiple turtle objects
- **Conditional Logic**: Determining win/loss conditions

## Technical Details

- **Screen Size**: 500x400 pixels
- **Start Position**: x = -230 (left side)
- **Finish Line**: x > 230 (right side)
- **Movement Range**: 1-20 units per turn
- **Turtle Colors**: 6 predefined colors

## Code Structure

### set_turtle(position, t_color)
- Creates a new turtle with specified position and color
- Returns configured turtle object

### Race Loop
- Continues until any turtle crosses finish line
- Updates all turtle positions each iteration
- Checks for race completion after each move

## Extensions

Potential improvements:
- Add multiple race rounds
- Implement betting amounts and payouts
- Add turtle names/personalities
- Create different race tracks
- Add power-ups or obstacles
- Implement multiplayer betting
- Add race statistics
- Create tournament mode
- Add turtle customization
- Implement save/load game state

## Educational Value

This project teaches:
- Game development concepts
- Random number generation
- User interaction patterns
- Object-oriented programming with multiple instances
- Event-driven programming
- Conditional logic and game state management
- Simple betting/prediction systems
