# Setup Guide for Python Practice Modules

This guide will help you set up the environment for running the Python practice modules.

## Quick Start

1. **Clone the repository** (if not already done)
2. **Install dependencies**
3. **Set up environment variables** (if needed)
4. **Run the projects**

## Installation Steps

### 1. Install Python Dependencies

```bash
# Navigate to the project directory
cd python-practice-modules

# Install required packages
pip install -r requirements.txt
```

### 2. Environment Variables Setup

If you're working on projects that require API keys or sensitive data:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your actual values
nano .env  # or use your preferred editor
```

### 3. Using Environment Variables in Python

For projects that need environment variables, use the `python-dotenv` library:

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('OPENAI_API_KEY')
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
```

## Running Individual Projects

Each project can be run independently:

```bash
# PrettyTable Demo
cd 01-pretty-table-demo
python main.py

# Coffee Machine
cd ../02-coffee-machine
python main.py

# Quiz Game
cd ../03-quiz-game
python main.py

# Turtle Graphics Basics
cd ../04-turtle-graphics-basics
python main.py

# Hirst Painting
cd ../05-hirst-painting
python main.py

# Etch-A-Sketch
cd ../06-etch-a-sketch
python main.py

# Turtle Race
cd ../07-turtle-race
python main.py
```

## Adding New Dependencies

When adding new projects that require additional packages:

1. **Update requirements.txt**:
   ```bash
   # Add new package
   echo "new-package>=1.0.0" >> requirements.txt
   
   # Install new package
   pip install new-package
   ```

2. **For API-based projects**:
   - Add your API key to `.env` file
   - Use `python-dotenv` to load environment variables
   - Never commit API keys to version control

## Project Structure

```
python-practice-modules/
├── .env                    # Your environment variables (not committed)
├── .env.example           # Template for environment variables
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
├── SETUP.md              # This setup guide
├── README.md             # Project overview
└── 01-pretty-table-demo/
    ├── main.py
    └── README.md
    # ... other projects
```

## Troubleshooting

### Common Issues

1. **ImportError for prettytable**:
   ```bash
   pip install prettytable
   ```

2. **Environment variables not loading**:
   - Ensure `.env` file exists in the root directory
   - Check that `python-dotenv` is installed
   - Verify variable names match exactly

3. **Turtle graphics not displaying**:
   - Ensure you have a display available (not SSH without X11)
   - On macOS/Linux, turtle should work out of the box
   - On Windows, ensure tkinter is installed

### Virtual Environment (Recommended)

For better dependency management, use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

## Contributing

When adding new projects:

1. Create a new numbered directory (e.g., `08-new-project/`)
2. Include a `main.py` file
3. Add a comprehensive `README.md`
4. Update the main `README.md` with project description
5. Add any new dependencies to `requirements.txt`
6. If using API keys, add them to `.env.example`

## Security Notes

- **Never commit `.env` files** - they contain sensitive information
- **Use `.env.example`** as a template for others
- **Keep API keys secure** and rotate them regularly
- **Review `.gitignore`** to ensure sensitive files are excluded
