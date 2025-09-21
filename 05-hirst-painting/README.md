# Hirst Painting - Dot Art Generator

A turtle graphics project that recreates Damien Hirst's famous dot paintings using Python.

## Description

This project generates a 10x10 grid of colored dots using turtle graphics, inspired by Damien Hirst's "Spot Paintings" series. Each dot is randomly colored from a predefined palette of RGB colors.

## Features

- **Grid Layout**: 10x10 dot grid (100 dots total)
- **Random Colors**: Each dot uses a random color from the palette
- **RGB Color Palette**: Predefined color list with 30 unique colors
- **Automatic Positioning**: Calculates dot positions automatically
- **Interactive Display**: Click to exit the graphics window

## Project Structure

```
05-hirst-painting/
├── main.py           # Main painting logic
├── color_data.py     # RGB color palette
└── README.md         # This file
```

## Color Palette

The project uses a curated palette of 30 RGB colors stored in `color_data.py`:
- Warm tones: oranges, reds, pinks
- Cool tones: blues, greens, cyans
- Neutral tones: browns, grays
- Vibrant colors: yellows, magentas

## Algorithm

1. **Setup**: Initialize turtle, screen, and color mode
2. **Positioning**: Start at bottom-left corner (-300, -300)
3. **Grid Creation**: 
   - Draw 10 dots horizontally
   - Move up one row when reaching 10th dot
   - Repeat until 100 dots are placed
4. **Random Coloring**: Each dot gets a random color from the palette

## Usage

```bash
python main.py
```

## Key Concepts

- **Grid Mathematics**: Calculating positions in a 2D grid
- **RGB Colors**: Using RGB color tuples
- **Random Selection**: Choosing random colors from a list
- **Turtle Positioning**: Moving turtle to specific coordinates
- **Pattern Generation**: Creating artistic patterns with code

## Output

Creates a window displaying a 10x10 grid of colorful dots, similar to Hirst's spot paintings.

## Extensions

Potential improvements:
- Add user input for grid size
- Implement different color palettes
- Add dot size variation
- Create multiple painting styles
- Add color gradient effects
- Save paintings as image files
- Add animation effects
- Implement different dot shapes

## Artistic Inspiration

This project is inspired by Damien Hirst's "Spot Paintings" series, which features grids of colored dots. The algorithmic approach to art creation demonstrates how programming can be used for artistic expression.
