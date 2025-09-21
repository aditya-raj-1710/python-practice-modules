# Turtle Graphics Basics

A collection of basic turtle graphics examples demonstrating various drawing techniques and patterns.

## Description

This project showcases fundamental turtle graphics concepts including drawing shapes, creating patterns, and using random colors. It includes multiple drawing functions that can be uncommented to run different examples.

## Features

- **Random Color Generation**: RGB color creation
- **Shape Drawing**: Polygons with varying sides
- **Pattern Creation**: Dotted lines and circle patterns
- **Interactive Graphics**: Click to exit
- **Multiple Examples**: Various drawing techniques

## Functions

### random_color()
- Generates random RGB colors
- Returns tuple of (red, green, blue) values

### dotted_line(total_length)
- Creates dotted lines by alternating pen up/down
- Demonstrates basic turtle movement

### draw_polygon(edges)
- Draws regular polygons with specified number of sides
- Calculates angles automatically

### draw_polygons(edges)
- Draws multiple polygons (triangle to nonagon)
- Uses random colors for each polygon

### draw_random_path()
- Creates random walking patterns
- Demonstrates infinite loops and random movement

### draw_circles(size_of_gap)
- Draws overlapping circles in a pattern
- Creates artistic spiral effects

## Usage

```bash
python main.py
```

Currently runs `draw_circles(5)` which creates a colorful circle pattern.

To try other examples, uncomment the desired function calls:
```python
# draw_random_path()  # Uncomment to run
draw_circles(5)       # Currently active
```

## Key Concepts

- **Turtle Graphics**: Python's built-in graphics library
- **RGB Colors**: Color representation using red, green, blue values
- **Mathematical Drawing**: Using angles and geometry for shapes
- **Randomization**: Creating unpredictable patterns
- **Event Handling**: Screen interaction (click to exit)

## Prerequisites

- Python 3.6+
- Turtle graphics module (built-in)

## Output

The program creates a window with colorful circle patterns. Click anywhere on the window to exit.

## Extensions

Potential improvements:
- Add user input for pattern parameters
- Create interactive drawing tools
- Add shape customization options
- Implement animation effects
- Create fractal patterns
- Add color palette selection
- Save drawings as images
