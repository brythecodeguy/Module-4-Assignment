# Module 3 Calculator Assignment

This is a command-line calculator written in Python that uses object-oriented programming principles, input validation, and error handling.
It supports addition, subtraction, multiplication, and division using a REPL (Read–Eval–Print Loop) interface.

The project includes automated unit tests using pytest and continuous integration using GitHub Actions and builds upon Module 2 Calculator

Module 3 Calculator refactors the logic to use a class-based design.

---

## Features

- Add, subtract, multiply, divide  
- REPL command-line interface  
- Shortcut commands (add, sub, mul, div)  
- Help command for user guidance
- Input validation for incorrect formats and non-numeric values
- Error handling (invalid input, divide by zero)  
- Automated unit and integration tests with pytest  
- Continuous integration with Github Actions to enforce 100% test coverage

---

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/brythecodeguy/Module-3-Assignment.git
cd Module-3-Assignment
```

Create and activate a virtual environment, then install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Run Calculator

```bash
python main.py
```

---

## Run Tests

```bash
pytest
```

---

## Continuous Integration

All tests must pass with full coverage. Tests automatically run on every push using GitHub Actions.