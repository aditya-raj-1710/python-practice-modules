# Etch-A-Sketch - Interactive Drawing App

An interactive drawing application that mimics the classic Etch-A-Sketch toy using turtle graphics and keyboard controls.

## Description

This project creates an interactive drawing application where users can control a turtle using keyboard keys to draw on the screen. It includes functions for movement, rotation, and screen clearing.

## Features

- **Keyboard Controls**: WASD-style movement controls
- **Drawing Functions**: Move forward, backward, rotate left/right
- **Screen Clearing**: Reset the drawing area
- **Interactive Graphics**: Real-time drawing with keyboard input
- **Event Handling**: Responds to key presses

## Controls

| Key | Action |
|-----|--------|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Turn left (counter-clockwise) |
| **D** | Turn right (clockwise) |
| **C** | Clear screen and reset position |

## Project Structure

```
06-etch-a-sketch/
├── main.py           # Main application with event handlers
└── README.md         # This file
```

## Functions

### move_forward()
- Moves the turtle forward by 10 units
- Leaves a trail (draws a line)

### move_backward()
- Moves the turtle backward by 10 units
- Leaves a trail (draws a line)

### move_counter_clockwise()
- Rotates the turtle left by 10 degrees
- Changes direction without drawing

### move_clockwise()
- Rotates the turtle right by 10 degrees
- Changes direction without drawing

### clear_screen()
- Clears all drawn content
- Resets turtle position to center (0, 0)
- Resets pen state for continued drawing

## Usage

```bash
python main.py
```

1. A graphics window will open
2. Use the keyboard controls to draw
3. Click on the window to exit

## Key Concepts

- **Event-Driven Programming**: Responding to user input events
- **Keyboard Input Handling**: Using turtle's key event system
- **State Management**: Managing turtle position and orientation
- **Interactive Graphics**: Real-time user interaction
- **Function Binding**: Connecting functions to keyboard events

## Technical Details

- **Color Mode**: RGB color mode enabled (255, 255, 255)
- **Movement Distance**: 10 units per key press
- **Rotation Angle**: 10 degrees per rotation
- **Screen Management**: Maintains drawing state between actions

## Example Usage

1. Press **W** several times to draw a line upward
2. Press **D** to turn right
3. Press **W** to continue drawing in the new direction
4. Press **C** to clear and start over

## Extensions

Potential improvements:
- Add different pen colors
- Implement variable pen sizes
- Add undo functionality
- Create save/load features
- Add different drawing modes (lines, circles, etc.)
- Implement mouse drawing
- Add color palette selection
- Create drawing tools (eraser, fill, etc.)
- Add keyboard shortcuts for colors
- Implement drawing export to image files

## Educational Value

This project teaches:
- Event-driven programming concepts
- User interface design basics
- Keyboard input handling
- Interactive graphics programming
- Function organization and modularity
