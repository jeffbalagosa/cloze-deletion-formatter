## Context
The project is a small, standard-library-only Python app with a Tkinter GUI. It currently has no linting or formatting tooling. The goal is to add developer-only tooling without affecting runtime usage.

## Goals / Non-Goals
- Goals: Provide standard linting + auto-formatting; keep tooling dev-only; minimize configuration; document usage.
- Non-Goals: Introduce runtime dependencies, restructure modules, or add CI workflows in this change.

## Decisions
- Decision: Use Ruff for both linting and formatting.
  - Rationale: Single tool minimizes setup while covering common lint rules and formatting.
- Decision: Configure Ruff in `pyproject.toml` with PEP 8-aligned defaults and import sorting.
  - Rationale: Central config is standard for Python tooling and avoids extra files.
- Decision: Track tooling as dev-only dependencies in `requirements-dev.txt`.
  - Rationale: Keeps the runtime environment standard-library-only.

## Alternatives considered
- Flake8 + Black + isort: More common but introduces multiple tools and config files.
- Pylint: Deeper analysis but heavier configuration and noise for a small codebase.

## Risks / Trade-offs
- Ruff version drift could change lint/format behavior → Mitigation: pin a specific version in dev requirements.
- Formatting may reflow code style → Mitigation: run formatter once and keep future edits consistent.

## Migration Plan
- Add dev dependency manifest and Ruff configuration.
- Run formatting once and fix lint issues.
- Update documentation for install and usage.

## Open Questions
- None.
