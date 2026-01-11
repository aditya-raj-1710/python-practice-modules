# AGENTS.md

This file provides guidance to agents (i.e., ADAL) when working with code in this repository.

## Repository Overview

This is a **monorepo of independent Python learning modules**, not a unified application. Each numbered directory (`01-pretty-table-demo/`, `02-coffee-machine/`, etc.) is a self-contained mini-project demonstrating specific Python concepts. Projects share minimal dependencies and no inter-project imports.

**Key Characteristic**: Modules are pedagogical examples, not production code. Focus on clarity and learning objectives over enterprise patterns.

## Essential Commands

### Running Projects
```bash
# Navigate to any project directory and run directly
cd 01-pretty-table-demo
python main.py

# Or from root (less common)
python 01-pretty-table-demo/main.py
```

### Dependency Management
```bash
# Install all dependencies (only prettytable currently required)
pip install -r requirements.txt

# For individual projects using standard library only
python main.py  # No installation needed

# Virtual environment (recommended for isolation)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Environment Variables
```bash
# Set up .env for API-based projects (currently unused but prepared for future)
cp .env.example .env
# Edit .env with actual values

# In Python code:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
```

**Critical Gotchas**:
- **No build step**: Projects run directly with `python main.py`
- **Turtle graphics requires display**: Won't work in headless environments or SSH without X11 forwarding
- **prettytable dependency**: Only required for `01-pretty-table-demo/`, all other projects use standard library
- **No tests**: These are learning examples without test suites

## Architecture & Project Structure

### Directory Organization
```
python-practice-modules/
├── 01-pretty-table-demo/       # PrettyTable library demo
├── 02-coffee-machine/          # OOP coffee vending machine
├── 03-quiz-game/               # OOP quiz with data structures
├── 04-turtle-graphics-basics/  # Basic turtle drawing
├── 05-hirst-painting/          # Dot painting with RGB colors
├── 06-etch-a-sketch/           # Event-driven drawing app
├── 07-turtle-race/             # Racing game with randomization
├── 08-snake-game/              # Classic Snake game
├── requirements.txt            # Shared dependencies
├── .env / .env.example         # Environment variables template
└── SETUP.md                    # Detailed setup instructions
```

### Project Independence
- **No shared modules**: Each project is standalone; no imports between projects
- **No common utilities**: Intentional duplication for learning (each project shows complete implementation)
- **Minimal dependencies**: Most projects use only Python standard library (turtle, random, etc.)

### Module Patterns

**OOP Projects** (`02-coffee-machine/`, `03-quiz-game/`):
- Entry point: `main.py` instantiates classes and runs game loop
- Classes in separate files: e.g., `coffee_maker.py`, `menu.py`, `money_machine.py`
- Pattern: Composition over inheritance, simple class hierarchies

**Turtle Graphics Projects** (`04-turtle-graphics-basics/` through `08-snake-game/`):
- Entry point: `main.py` sets up screen and game loop
- Game objects: Separate classes (e.g., `snake.py`, `food.py`, `scoreboard.py`)
- Common flow:
  1. Initialize `Screen()` with dimensions and colors
  2. Create game objects (snake, food, etc.)
  3. Set up event listeners (`screen.onkey()`)
  4. Main loop with `screen.update()` and `time.sleep()`
  5. Exit on `screen.exitonclick()`

**Example: Snake Game Flow** (`08-snake-game/`):
```
main.py:
  1. Screen setup (600x600, black background)
  2. Instantiate Snake(), Food(), Scoreboard()
  3. Register keyboard handlers (arrow keys -> snake.up/down/left/right)
  4. Game loop:
     - screen.update()
     - snake.move()
     - Collision detection: food (extend snake, increase score), walls, tail (game over)
  5. Exit on click
```

## Key Entry Points

### Project Entry Points
Every project runs via `main.py` in its directory:
- `01-pretty-table-demo/main.py` - Table formatting demo
- `02-coffee-machine/main.py` - Coffee machine user interface
- `03-quiz-game/main.py` - Quiz game initialization and loop
- `04-turtle-graphics-basics/main.py` - Drawing examples (square, dashed line, spirograph, random walk)
- `05-hirst-painting/main.py` - Dot painting generator
- `06-etch-a-sketch/main.py` - Drawing app with keyboard controls
- `07-turtle-race/main.py` - Turtle racing game with betting
- `08-snake-game/main.py` - Snake game with collision detection

### Configuration Files
- **requirements.txt**: Python dependencies (currently only `prettytable>=3.0.0`)
- **.env.example**: Template for API keys (prepared for future projects, not currently used)
- **.gitignore**: Excludes `.env`, `__pycache__`, `.DS_Store`, etc.

## Non-Obvious Relationships

### Turtle Graphics Screen Management
Turtle projects use **non-persistent screen state**:
- `screen.tracer(0)` disables auto-update for manual control
- Manual `screen.update()` in game loop enables frame-based animation
- `time.sleep(0.1)` controls game speed (100ms per frame in snake game)
- **Gotcha**: Forgetting `screen.tracer(0)` causes flickering; forgetting `screen.update()` causes frozen screen

### Snake Game Collision Detection
Multiple collision types with different thresholds:
- **Food collision**: `snake.head.distance(food) < 15` (larger threshold for forgiveness)
- **Tail collision**: `snake.head.distance(segment) < 10` (stricter threshold to prevent false positives)
- **Wall collision**: Direct coordinate checks (`xcor() < -280` or `> 280`, same for `ycor()`)
- **Why different thresholds?**: Food uses circle shape (radius-based), tail uses precise segments

### OOP in Coffee Machine
Class responsibilities demonstrate separation of concerns:
- `CoffeeMaker`: Resource management (water, milk, coffee)
- `Menu`: Drink definitions and availability
- `MoneyMachine`: Payment processing and profit tracking
- Pattern: Each class has single responsibility, no circular dependencies

## Domain-Specific Information

### Turtle Graphics Constraints
- **Coordinate system**: Center is (0, 0), positive x/y = right/up
- **Screen boundaries**: Typically ±300 pixels from center (600x600 screen)
- **Colors**: Accept named strings ("black", "white", "blue") or RGB tuples
- **Shapes**: Limited set ("square", "circle", "turtle", "arrow", "triangle")
- **Performance**: Slow for complex animations (Python interpreter overhead)

### Quiz Game Data Structure
Questions stored as list of dictionaries in `data.py`:
```python
question_data = [
    {"text": "Question text", "answer": "True"},
    ...
]
```
- QuizBrain iterates through questions, tracks score
- Simple True/False questions only (extend for multiple choice)

### Coffee Machine Resources
Hardcoded resource requirements in `menu.py`:
```python
drinks = {
    "espresso": {"water": 50, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    ...
}
```
- Resource checking before drink preparation (fail-fast pattern)
- Coin processing: quarters ($0.25), dimes ($0.10), nickels ($0.05), pennies ($0.01)

## Adding New Projects

### Naming Convention
- Use numbered directories: `09-new-project/`, `10-another-project/`
- Keep names lowercase with hyphens
- Prefix with sequential number for ordering

### Required Files Per Project
1. **main.py**: Entry point with clear execution flow
2. **README.md**: Include description, features, requirements, how to run, learning objectives
3. Update root **README.md** table with new project description

### Dependency Management
- Add new dependencies to **requirements.txt** with version pinning: `new-package>=1.0.0`
- Comment in requirements.txt if dependency is project-specific
- Keep dependencies minimal (prefer standard library)

### Git Workflow
- Standard git commands (no hooks or automated checks)
- Commit `.env.example` but NEVER `.env`
- `.gitignore` already configured for Python projects

## Common Pitfalls

1. **Turtle graphics in wrong directory**: Must run from project directory for relative imports to work
2. **Missing prettytable**: Only needed for project 01, but included in shared requirements.txt
3. **Display issues**: Turtle graphics won't work in CI/CD or headless environments
4. **Event handling timing**: Turtle event listeners must be registered BEFORE main loop starts
5. **Screen update frequency**: Balance `time.sleep()` duration vs. game responsiveness (too fast = CPU intensive, too slow = sluggish)

## Development Workflow

### Testing Projects
No automated tests. Manual testing workflow:
1. Run `python main.py` in project directory
2. Interact with program (keyboard input, mouse clicks)
3. Verify expected behavior (visual output, game logic)
4. Check for errors in terminal output

### Debugging Turtle Graphics
Common issues:
- **Blank screen**: Check `screen.tracer(0)` and `screen.update()` calls
- **Shapes not appearing**: Verify `penup()` called before positioning
- **Slow performance**: Reduce loop frequency or complexity of drawings
- **Screen closes immediately**: Add `screen.exitonclick()` at end

### Code Style
- Follow PEP 8 conventions (imports at top, snake_case for functions/variables, PascalCase for classes)
- Use descriptive variable names (learning-focused code)
- Include comments explaining non-obvious logic (educational context)
- Prefer readability over micro-optimizations

## Quick Reference

### Find all projects
```bash
ls -d [0-9]*
```

### Run specific project
```bash
cd 08-snake-game && python main.py
```

### Check dependencies
```bash
pip list | grep prettytable
```

### Create new project skeleton
```bash
mkdir 09-new-project
cd 09-new-project
touch main.py README.md
echo "# New Project" > README.md
```
