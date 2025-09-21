# Coffee Machine - OOP Project

An object-oriented coffee vending machine simulation demonstrating OOP principles in Python.

## Description

This project simulates a coffee machine using Object-Oriented Programming concepts. It includes classes for managing the menu, coffee making process, and payment handling.

## Features

- **Menu System**: Display available drinks (latte, espresso, cappuccino)
- **Resource Management**: Track water, milk, and coffee supplies
- **Payment Processing**: Handle coin-based payments with change calculation
- **Report Generation**: Display current resources and profit
- **Input Validation**: Check for sufficient resources before making coffee

## Project Structure

```
02-coffee-machine/
├── main.py           # Main application logic
├── menu.py           # Menu and MenuItem classes
├── coffee_maker.py   # CoffeeMaker class
├── money_machine.py  # MoneyMachine class
└── README.md         # This file
```

## Classes

### MenuItem
- Represents individual menu items with ingredients and cost

### Menu
- Manages the available drinks menu
- Provides methods to find drinks and list options

### CoffeeMaker
- Handles resource management (water, milk, coffee)
- Checks resource sufficiency
- Makes coffee and updates resources

### MoneyMachine
- Processes coin payments
- Calculates change
- Tracks profit

## Usage

```bash
python main.py
```

## Commands

- **Order drinks**: Type drink name (latte/espresso/cappuccino)
- **Report**: Type "report" to see resources and profit
- **Turn off**: Type "off" to exit

## Key OOP Concepts

- **Encapsulation**: Data and methods bundled together
- **Classes and Objects**: Multiple classes working together
- **Methods**: Functions within classes
- **Attributes**: Data stored within objects
- **Separation of Concerns**: Each class has a specific responsibility

## Example Interaction

```
What would you like to order? latte/espresso/cappuccino/report/off: latte
Please insert coins.
How many quarters?: 4
How many dimes?: 2
How many nickles?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte ☕️. Enjoy!
```

## Extensions

Potential improvements:
- Add more drink types
- Implement inventory restocking
- Add user accounts and preferences
- Create a GUI interface
- Add drink customization options
