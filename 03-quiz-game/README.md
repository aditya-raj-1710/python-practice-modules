# Quiz Game

An interactive quiz game demonstrating Object-Oriented Programming with question management and scoring.

## Description

This project creates a True/False quiz game using OOP principles. It manages questions, tracks user progress, and calculates final scores.

## Features

- **Question Management**: Load questions from data structure
- **Interactive Interface**: User-friendly question prompts
- **Score Tracking**: Real-time score updates
- **Progress Tracking**: Shows current question number
- **Result Summary**: Final score display

## Project Structure

```
03-quiz-game/
├── main.py           # Main application logic
├── question_model.py # Question class
├── quiz_brain.py     # QuizBrain class
├── data.py          # Question data
└── README.md        # This file
```

## Classes

### Question
- Represents a single quiz question
- Stores question text and correct answer

### QuizBrain
- Manages the quiz flow and logic
- Tracks question number and score
- Handles user input and answer validation

## Usage

```bash
python main.py
```

## Example Interaction

```
Q.1: Psychology is the science of behavior and mind. (True/False): True
You are correct!
The correct answer was: True
Your score is 1/1

Q.2: In "To Love-Ru: Darkness", Yami reveals her real name is Eve. (True/False): False
You are incorrect!
The correct answer was: True
Your score is 1/2

...

You have completed the quiz.
Your final score is 7/10
```

## Key OOP Concepts

- **Object Creation**: Creating question objects from data
- **Class Methods**: Methods within classes for specific functionality
- **State Management**: Tracking quiz state (score, question number)
- **Data Processing**: Converting raw data into objects
- **User Interaction**: Handling input and providing feedback

## Data Structure

Questions are stored in `data.py` with the following format:
```python
{
    "question": "Question text here",
    "correct_answer": "True" or "False"
}
```

## Extensions

Potential improvements:
- Add multiple choice questions
- Implement different difficulty levels
- Add question categories
- Create a GUI interface
- Add timer functionality
- Implement question shuffling
- Save high scores
- Add hints system
