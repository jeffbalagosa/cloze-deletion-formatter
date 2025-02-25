# Cloze Deletion Formatter

## Overview
The **Cloze Deletion Formatter** is a Python-based tool that processes text containing cloze deletions (e.g., `{{c1::text}}`) to generate flashcards. It includes a parser for extracting and formatting cloze deletions and a GUI application for easy input and previewing of flashcards.

## Features
- **Cloze Deletion Parser:** Identifies and processes cloze deletion patterns in text.
- **Flashcard Generator:** Produces structured question-answer flashcards.
- **Graphical User Interface (GUI):** A simple Tkinter-based UI for inputting text and previewing flashcards.
- **Automated Tests:** A suite of unit tests ensures the correctness of the cloze parsing and flashcard generation logic.

## Installation

### Prerequisites
- Python 3.x
- Tkinter (included in standard Python distributions)

### Clone the Repository
```bash
git clone https://github.com/your-username/cloze-deletion-formatter.git
cd cloze-deletion-formatter
```

### Install Dependencies
The project does not require an explicit `requirements.txt`, but if needed, create one with:
```txt
tkinter
```
Since Tkinter is included with Python, additional installations may not be necessary.

## Usage

### Running the GUI Application
```bash
python flashcard_gui.py
```
1. Enter text containing Cloze Deletion syntax (e.g., `{{c1::Python}} is awesome`).
2. The GUI will automatically parse and generate preview flashcards.

### Running the Parser Script Directly
```bash
python cloze_parser.py
```
This will generate flashcards from a sample text and print the question/answer format.

### Running Unit Tests
```bash
python -m unittest test_cloze_parser.py
```
Executes unit tests to validate correct flashcard generation.

## Project Structure
```
├── .gitignore            # Ignored files (e.g., __pycache__, virtual environments)
├── cloze_parser.py       # Main parser for extracting and formatting cloze deletions
├── flashcard_gui.py      # GUI application for text input and flashcard preview
├── test_cloze_parser.py  # Unit tests for the parser
├── README.md             # Project documentation (this file)
```

## How It Works

### Cloze Deletion Format
Cloze deletions follow this syntax:
```plaintext
{{c1::Python}} is a programming language.
{{c2::Java}} is another language.
```
This format creates two flashcards:
1. **Question:** `_____ is a programming language.`
   **Answer:** `["Python"]`
2. **Question:** `Python is a programming language. _____ is another language.`
   **Answer:** `["Java"]`

If multiple instances of the same cloze tag exist in a sentence:
```plaintext
Learning {{c1::Python}} is fun, and {{c1::programming}} is too.
```
The generated flashcard will have:
- **Question:** `Learning _____ is fun, and _____ is too.`
- **Answer:** `["Python", "programming"]`

This means:
- The `question` field blanks out only one cloze tag per card.
- The `answer` field **returns a list** of the removed words.

## Contribution
Contributions are welcome! Fork the repository, make improvements, and submit a pull request.

## LICENSE
MIT License

Copyright (c) 2025 Jeff Balagosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
