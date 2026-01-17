# Change: Add linting and formatting toolchain

## Why
The project currently lacks automated linting and formatting, which makes style drift and small defects harder to catch early. Adding a standard Python lint/format setup improves consistency while keeping runtime dependencies unchanged.

## What Changes
- Add a dev-only linting and formatting toolchain using Ruff with PEP 8-aligned defaults.
- Define tool configuration in a shared config file.
- Document installation and usage for contributors.

## Impact
- Affected specs: lint-code (new)
- Affected code: new tooling/config files (e.g., `pyproject.toml`, `requirements-dev.txt`), `README.md`
