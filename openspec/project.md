# Project Context

## Purpose
Provide a simple, offline Python tool to create cloze-deletion flashcards from text, with a Tkinter GUI for interactive editing, preview, and export.

## Tech Stack
- Python 3 (standard library only)
- Tkinter for GUI
- `unittest` for tests

## Project Conventions

### Code Style
- PEP 8 style, 4-space indentation
- `snake_case` for functions/variables, `CamelCase` for classes
- Keep modules small and focused (parser, GUI, export)
- Prefer clear, readable code over abstraction

### Architecture Patterns
- Simple, module-per-concern structure
- Parsing logic isolated in `cloze_parser.py`
- GUI in `flashcard_gui.py`
- Export formatting in `export.py`

### Testing Strategy
- Unit tests via `unittest` in `test_cloze_parser.py`
- Focus on parser correctness and edge cases

### Git Workflow
- Keep `main` stable
- Prefer small, focused commits

## Domain Context
- Cloze format: `{{c<number>::text}}` where `<number>` groups deletions into the same card
- Parser replaces only the target tag with `_____` for each generated card
- Export formats front/back pairs with configurable field/record separators

## Important Constraints
- Standard-library only (no third-party dependencies)
- Works offline and cross-platform
- GUI must remain Tkinter-based

## External Dependencies
- None
