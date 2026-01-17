# Cloze Deletion Flashcard Generator

A simple Python application for creating cloze deletion flashcards from text. The project includes a parser to convert specially formatted text into flashcards and a GUI built with Tkinter for an interactive experience. Automated tests are also provided.

---

## Features

- **Cloze Parsing:** Convert text with cloze deletion tags (`{{c<number>::text}}`) into flashcard front/back pairs.
- **Interactive GUI:** Use the Tkinter interface to input notes, create cloze deletions with keyboard shortcuts, preview flashcards, and copy them to the clipboard.
- **Export Options:** Export your flashcards with various field and record separator options for compatibility with different flashcard applications.
- **Testing:** Unit tests to ensure the cloze parsing works correctly.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/cloze-flashcard-generator.git
   cd cloze-flashcard-generator
   ```

2. **Dependencies:**

   This project uses only the Python standard library (including `tkinter` for the GUI), so no additional runtime packages are required.

   For development, we use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting. Install development dependencies with:

   ```bash
   pip install -r requirements-dev.txt
   ```

---

## Usage

### Running the GUI

Launch the flashcard generator GUI by executing:

```bash
python flashcard_gui.py
```

- **Input:** Type or paste your notes into the "Input Notes" field.
- **Creating Cloze Deletions:**
  - **Same Card:** Highlight text and press <kbd>Ctrl+Shift+C</kbd> or click "Add Cloze (Same Card)".
  - **New Card:** Highlight text and press <kbd>Ctrl+Alt+Shift+C</kbd> or click "Add Cloze (New Card)".
- **Preview:** The flashcard preview updates automatically as you edit your notes.
- **Export:** Click "Export" to open the export screen with the following options:
  - **Field Separator:** Choose Tab, Comma, or Custom separator between front and back content.
  - **Record Separator:** Choose New Line, Semicolon, or Custom separator between different flashcards.
  - Preview the exported data and copy it to clipboard.
- **Clipboard:** Click "Copy to Clipboard" to copy the generated flashcards in preview format.
- **Clear All:** Reset the input area and tag counter with the "Clear All" button.

---

## Linting and Formatting

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting. To ensure code quality and consistency:

```bash
# Check for linting issues
python -m ruff check .

# Automatically fix linting issues
python -m ruff check . --fix

# Format code
python -m ruff format .

# Check if code is properly formatted (without making changes)
python -m ruff format --check .
```

---

## Running Tests

To run the unit tests, execute:

```bash
python -m unittest test_cloze_parser.py
```

This will run a series of tests to verify that cloze deletions are parsed correctly.

---

## File Structure

- **.gitignore:** Ignores common files and directories not needed in the repository.
- **cloze_parser.py:** Contains the logic for parsing cloze deletion tags and generating flashcards.
- **flashcard_gui.py:** Provides a Tkinter-based graphical user interface for creating and previewing flashcards.
- **export.py:** Handles the export functionality with different formatting options.
- **test_cloze_parser.py:** Unit tests for the cloze parser functionality.

---

## Contributing

Feel free to fork the repository and submit pull requests. When contributing, please maintain clarity and consistency with the existing code style.

---

## License

**MIT License**

Copyright (c) 2025 Jeff Balagosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

---

## Acknowledgements

This tool is designed to help you quickly convert your study notes into effective flashcards using the cloze deletion technique. Enjoy and happy studying!
