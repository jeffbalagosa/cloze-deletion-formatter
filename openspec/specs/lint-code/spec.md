# lint-code Specification

## Purpose
TBD - created by archiving change add-linting-formatting. Update Purpose after archive.
## Requirements
### Requirement: Linting toolchain
The system SHALL provide a dev-only linting toolchain for Python sources using Ruff, configured to enforce standard PEP 8 conventions and common error checks.

#### Scenario: Linting run
- **WHEN** a developer runs `ruff check .`
- **THEN** lint violations are reported and the command exits non-zero if any are found.

### Requirement: Formatting toolchain
The system SHALL provide a dev-only auto-formatting configuration for Python sources using Ruff's formatter.

#### Scenario: Formatting run
- **WHEN** a developer runs `ruff format .`
- **THEN** source files are reformatted to match the configured style.

#### Scenario: Formatting check
- **WHEN** a developer runs `ruff format --check .`
- **THEN** the command fails if files are not already formatted.

### Requirement: Dev-only dependency boundary
The system SHALL keep linting and formatting tooling as development-only dependencies that are not required to run the application or tests.

#### Scenario: Runtime usage
- **WHEN** a user runs the GUI or parser without dev tools installed
- **THEN** the application operates normally with only the Python standard library.

### Requirement: Tooling documentation
The system SHALL document how to install and run linting and formatting tools.

#### Scenario: Contributor onboarding
- **WHEN** a contributor reads the README
- **THEN** they can find the commands needed to install and run the lint/format tools.

