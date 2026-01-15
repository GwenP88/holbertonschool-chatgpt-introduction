# holbertonschool-chatgpt-introduction

## Description
This repository contains the **ChatGPT - Introduction** project: a hands-on module focused on using AI (ChatGPT) to improve **code quality** and **developer efficiency** through two main skills:

- **Debugging**: identify, explain, and fix bugs in provided code samples (Python + HTML/JavaScript).
- **Automation / Documentation**: use AI to produce clearer code via comments, structure, and basic robustness (error handling).

The goal is not to “trust AI blindly”, but to **test, verify, and critically evaluate** the proposed fixes.

---

## Learning Objectives
By the end of this project, you should be able to:

- Diagnose common programming errors and explain why they happen.
- Fix buggy code and confirm the fix with real tests.
- Improve reliability with input validation and error handling.
- Write helpful documentation/comments (clear function description, parameters, returns).
- Use ChatGPT as an assistant while keeping control of the final solution.

---

## Project Structure
All tasks are located in:

- `debugging/`

Files included:
- `factorial.py`
- `print_arguments.py`
- `change_background.html`
- `mines.py`
- `factorial_recursive.py`
- `checkbook.py`
- `tic.py`

---

## Requirements
- **Python 3** for Python scripts
- A **web browser** for `change_background.html`
- Basic command line usage

---

## Tasks

### 0. Debugging - Python Factorial
**File:** `debugging/factorial.py`  

Fix the script so it correctly prints the factorial of the argument passed in the command line.

Example:
```
./factorial.py 5
120
```

### 1. Debugging - Python Arguments
**File:** `debugging/print_arguments.py`

Fix the script so it prints only the arguments, without printing the file name.

Expected:
```
./print_arguments.py 1 2 3
1
2
3
```

### 2. Debugging - HTML / JavaScript
**File:** `debugging/change_background.html`

Fix the HTML/JS so the background color changes when clicking the button.
Test: open the file in a browser and click the button.

### 3. Debugging - Python Mines (Minesweeper)
**File:** `debugging/mines.py`

Add a winning condition:
- Detect when all non-mine cells are revealed
- Display a win message and stop the game

Expected ending message:
```
Congratulations! You've won the game.
```

### 4. Documentation - Python Factorial (Recursive)
**File:** `debugging/factorial_recursive.py`

Add comments with 3 sections:
- function description
- parameters
- returns

Goal: improve readability and clarity (documentation-style comments).e

### 5. Error Handling - Python Checkbook
**File:** `debugging/checkbook.py`

Prevent crashes caused by invalid input (example: user types "test" instead of a number).
Add error handling so the program:
- does not crash
- informs the user
- asks again or safely returns to the menu

### 6. Debugging - Tic Tac Toe (Python)
**File:** `debugging/tic.py`

Fix all issues in the game logic and test all user inputs, including:
- non-numeric input
- out-of-range coordinates
- attempting to play on an occupied cell
- draw condition (no winner)
Expected: stable gameplay without crashing, with correct win/draw behavior.

---

## Usage

### Run Python scripts

From the repository root:

```
python3 debugging/factorial.py 5
python3 debugging/print_arguments.py 1 2 3
python3 debugging/mines.py
python3 debugging/checkbook.py
python3 debugging/tic.py
```

### Run the HTML file

Open in a browser:
```
debugging/change_background.html
```

---

## Testing Tips

Before considering a task “done”:
- Run multiple test cases (normal + edge cases).
- Try invalid inputs on purpose.
- Make sure behavior matches the expected output examples.
- If ChatGPT suggests a fix, verify it yourself by running the program.

## Author

Project completed as part of the Holberton School curriculum.
**Gwenaëlle Pichot**
