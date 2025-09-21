# Python Practice Modules

A collection of mini Python projects demonstrating various programming concepts and libraries.

## Projects Overview

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| [01-pretty-table-demo](./01-pretty-table-demo/) | Simple table formatting demo | PrettyTable library |
| [02-coffee-machine](./02-coffee-machine/) | OOP-based coffee vending machine | Object-Oriented Programming |
| [03-quiz-game](./03-quiz-game/) | Interactive quiz game | OOP, data structures |
| [04-turtle-graphics-basics](./04-turtle-graphics-basics/) | Basic turtle graphics examples | Turtle graphics, loops |
| [05-hirst-painting](./05-hirst-painting/) | Damien Hirst-inspired dot painting | Turtle graphics, RGB colors |
| [06-etch-a-sketch](./06-etch-a-sketch/) | Interactive drawing application | Event handling, keyboard input |
| [07-turtle-race](./07-turtle-race/) | Racing game with betting | Game logic, user input, randomization |

## Requirements

- Python 3.6+
- prettytable (for project 01)
- No additional dependencies for other projects (uses built-in modules)

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd python-practice-modules

# Install required dependencies
pip install -r requirements.txt

# Set up environment variables (if needed for future projects)
cp .env.example .env
# Edit .env file with your actual values
```

## Configuration Files

- **`requirements.txt`** - Python dependencies for all projects
- **`.env.example`** - Template for environment variables (API keys, etc.)
- **`.env`** - Your actual environment variables (not committed to git)
- **`.gitignore`** - Excludes sensitive files from version control
- **`SETUP.md`** - Detailed setup instructions

## Running Projects

Each project has its own directory with a `main.py` file. Navigate to the project directory and run:

```bash
cd <project-directory>
python main.py
```

## Learning Objectives

These projects cover:
- **Object-Oriented Programming**: Classes, methods, encapsulation
- **Turtle Graphics**: Drawing, colors, shapes, animation
- **User Interaction**: Input handling, event-driven programming
- **Data Structures**: Lists, dictionaries, custom objects
- **Game Logic**: Loops, conditionals, randomization
- **Code Organization**: Modular design, separation of concerns

## Contributing

Feel free to add new mini projects or improve existing ones. Each project should be self-contained and demonstrate specific Python concepts.
