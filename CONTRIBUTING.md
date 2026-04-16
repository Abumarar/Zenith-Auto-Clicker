# Contributing to Zenith Auto Clicker

First off, thank you for considering contributing to Zenith Auto Clicker! It's people like you that make the open-source community such a great place to learn, inspire, and create.

## Setup Instructions for Developers

1. **Fork the Repository:** Start by forking the `ZenithAutoClicker` repository to your GitHub account.
2. **Clone your Fork:**
   ```bash
   git clone https://github.com/<your-username>/ZenithAutoClicker.git
   cd ZenithAutoClicker
   ```
3. **Set up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. **Install Dependencies:**
   * On Windows: `pip install -r requirements_windows.txt`
   * On Linux: 
     ```bash
     sudo apt install xdotool python3-xlib
     pip install -r requirements_linux.txt
     ```
5. **Install Development Requirements (if not included above):**
   We use `flake8` for linting and `pytest` for testing. You can install them manually:
   ```bash
   pip install flake8 pytest
   ```

## Coding Standards

To ensure code consistency, we follow these guidelines:

* **Style Guide:** We adhere to the PEP 8 style guide for Python code.
* **Linting:** We use `flake8`. Before committing, run `flake8` against your changes. Our `.flake8` configuration enforces a line length of 100 characters.
* **Type Hints:** Use Python type hints (`module: Type`) wherever possible. It significantly improves code readability and maintainability.
* **UI/UX Consistency:** Be sure to follow the design guidelines described in the `README.md`. Use the defined color palette, typography and component styling.

## PR Review Criteria

When submitting a Pull Request (PR), it will be evaluated based on the following criteria:

* **Functionality:** Does the code solve the issue or add the feature as described?
* **Code Quality:** Is the code clean, well-commented, and typed? Does it pass `flake8` linting?
* **Testing:** Have tests been added or updated to cover the new changes? (Ensure all GitHub Action checks pass).
* **Documentation:** Have any new dependencies been added to the respective `requirements_*.txt` files? Is the `README.md` updated if there are user-facing changes?

Thank you for helping us make Zenith Auto Clicker the best it can be!
