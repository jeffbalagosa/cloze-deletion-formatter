## 1. Implementation
- [ ] 1.1 Add dev dependency manifest (`requirements-dev.txt`) with a pinned Ruff version.
- [ ] 1.2 Add `pyproject.toml` with Ruff linting and formatting configuration (PEP 8-aligned, import sorting, line length 88).
- [ ] 1.3 Apply auto-formatting to the current Python sources (`ruff format .`).
- [ ] 1.4 Fix any remaining lint findings after formatting (`ruff check .`).
- [ ] 1.5 Update `README.md` with install and usage commands for linting and formatting.

## 2. Validation
- [ ] 2.1 Run `python -m ruff check .`.
- [ ] 2.2 Run `python -m ruff format --check .`.
- [ ] 2.3 Run `python -m unittest test_cloze_parser.py`.
