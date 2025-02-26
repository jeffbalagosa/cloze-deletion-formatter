# Cloze Deletion Flashcard Generator

A simple Python application for creating cloze deletion flashcards from text. The project includes a parser to convert specially formatted text into flashcards and a GUI built with Tkinter for an interactive experience. Automated tests are also provided.

---

## Features

- **Cloze Parsing:** Convert text with cloze deletion tags (`{{c<number>::text}}`) into flashcard front/back pairs.
- **Interactive GUI:** Use the Tkinter interface to input notes, create cloze deletions with keyboard shortcuts, preview flashcards, and copy them to the clipboard.
- **Testing:** Unit tests to ensure the cloze parsing works correctly.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/cloze-flashcard-generator.git
   cd cloze-flashcard-generator
   ```

2. **Dependencies:**

   This project uses only the Python standard library (including `tkinter` for the GUI), so no additional packages are required.

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
- **Clipboard:** Click "Copy to Clipboard" to copy the generated flashcards.

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
