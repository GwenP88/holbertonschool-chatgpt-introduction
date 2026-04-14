# Debugging

> Squashing bugs and automating the boring stuff — with a little help from AI.

---

## 📝 Description

This project is part of a specialized module exploring how artificial intelligence can be integrated into everyday coding practices. I work on two core pillars: debugging and automation. Using ChatGPT as a co-pilot, I diagnose and fix bugs across multiple programming languages, and I automate repetitive tasks like writing documentation and error handling. The goal is simple — write smarter code, faster, with fewer headaches (and fewer infinite loops).

---

## 🎯 Learning Objectives

By the end of this project, I am able to use ChatGPT as a practical debugging assistant to identify and correct errors in code across different languages, including Python, HTML, and JavaScript. I understand how to clearly articulate a problem to an AI tool and critically evaluate the solutions it suggests. I am also able to leverage AI to automate repetitive coding tasks such as adding documentation, implementing error handling, and generating boilerplate code. Most importantly, I have learned to verify, test, and question AI-generated outputs rather than blindly trusting them — because AI is a tool, not a magic wand.

---

## 🛠️ Technologies Used

This project uses Python 3 as the primary scripting language, along with HTML and JavaScript for one web-based task. ChatGPT is used as the AI assistant throughout the debugging and automation workflow. No external Python libraries are required.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all Python files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- No module imports allowed unless explicitly stated

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-chatgpt-introduction.git
cd holbertonschool-chatgpt-introduction/debugging
```

---

## ▶️ Usage / Execution

All Python scripts can be executed in two ways:

### 1. Direct execution
Make the file executable and run it directly:
```bash
chmod +x filename.py
./filename.py
```

### 2. Using Python interpreter
Run the script with Python:
```bash
python3 filename.py
```

For the HTML file, simply open it in any modern web browser.

---

## 📊 Project Progress

<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100%</sub>
</p>

---

## ✨ Features

### Task 0 - Debugging - Python Factorial

- **Status:** Mandatory
- **Objective:** Use ChatGPT to identify and correct a bug in a Python factorial function.
- **Constraint:** The fixed script must correctly compute the factorial of the argument passed via command line.
- **Expected behavior:** Running `./factorial.py 5` prints `120`. The original code caused an infinite loop because `n` was never decremented inside the `while` loop.

**Files:** `factorial.py`

---

### Task 1 - Debugging - Python Arguments

- **Status:** Mandatory
- **Objective:** Use ChatGPT to fix a script that prints all command-line arguments.
- **Constraint:** The script must print only the actual arguments, excluding the script name itself.
- **Expected behavior:** Running `./print_arguments.py 1 2 3` prints `1`, `2`, `3` — one per line, no filename.

**Files:** `print_arguments.py`

---

### Task 2 - Debugging - HTML / Javascript

- **Status:** Mandatory
- **Objective:** Use ChatGPT to identify and fix a bug in an HTML/JavaScript file.
- **Constraint:** A button click must trigger a background color change on the page.
- **Expected behavior:** The button labeled "Change Color" correctly changes the page background to a random color. The bug was a typo in the element ID (`colorButon` vs `colorButton`).

**Files:** `change_background.html`

---

### Task 3 - Debugging - Python Mines

- **Status:** Mandatory
- **Objective:** Use ChatGPT to add a win condition to a Minesweeper game in Python.
- **Constraint:** The game must detect when all non-mine cells have been revealed and declare the player a winner.
- **Expected behavior:** When all safe cells are uncovered, the game prints `Congratulations! You've won the game.` and exits gracefully.

**Files:** `mines.py`

---

### Task 4 - Documentation - Python Factorial

- **Status:** Mandatory
- **Objective:** Use ChatGPT to document a recursive factorial function.
- **Constraint:** The docstring must include three sections: function description, parameters, and return value.
- **Expected behavior:** The function is fully documented with a proper docstring. Running `./factorial_recursive.py 4` prints `24`.

**Files:** `factorial_recursive.py`

---

### Task 5 - Error Handling - Python Checkbook

- **Status:** Mandatory
- **Objective:** Use ChatGPT to add error handling to a checkbook program.
- **Constraint:** The program must not crash when the user enters non-numeric input for deposit or withdrawal amounts.
- **Expected behavior:** Entering a string like `test` when prompted for an amount displays a friendly error message and prompts again, instead of raising a `ValueError`.

**Files:** `checkbook.py`

---

### Task 6 - Debugging - Tic Tac Toe Python

- **Status:** Mandatory
- **Objective:** Use ChatGPT to identify and fix multiple bugs in a Tic Tac Toe game.
- **Constraint:** All user inputs must be properly validated. There may be several bugs to find and fix.
- **Expected behavior:** The game correctly alternates between players X and O, prevents overwriting occupied cells, detects a winner accurately, and handles all invalid inputs without crashing.

**Files:** `tic.py`

---

## 🤝 Contributions & Acknowledgements

Big thanks to the Holberton School curriculum team for designing a project that makes debugging feel like detective work — and to ChatGPT for being a patient (if occasionally overconfident) coding partner. Always verify what the AI tells you. It's fast, but it's not infallible.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-chatgpt-introduction
- Project: Debugging