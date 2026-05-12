# PySandbox Agent Guide

## Project Overview

This is a simple Python sandbox project for experimenting with scripts, modules, and tools.

## Project Structure

```
pysandbox/
├── src/pysandbox/       # Main package
├── tests/               # Unit tests
├── scripts/             # Standalone scripts (if any)
├── pyproject.toml       # Project configuration
├── Makefile             # Common commands
└── .pre-commit-config.yaml  # Git hooks
```

## Development Commands

All commands are run via `make`:

| Command | Description |
|---------|-------------|
| `make test` | Run all tests with pytest |
| `make run` | Run the default script (`pysandbox.hello`) |
| `make run SCRIPT=foo.bar` | Run a specific module |
| `make lint` | Run ruff linter and format checker |
| `make format` | Auto-fix lint issues and format code |
| `make install-hooks` | Install pre-commit hooks |

## Running Tests

```bash
make test
```

## Running Scripts

```bash
# Default hello world
make run

# Custom module
make run SCRIPT=pysandbox.another_module
```

## Pre-commit Hooks

Hooks are configured in `.pre-commit-config.yaml` and include:

- `trailing-whitespace`
- `end-of-file-fixer`
- `check-yaml`
- `ruff` (lint + auto-fix)
- `ruff-format`

Install them with:

```bash
make install-hooks
```

## Coding Style

- Line length: **120**
- Formatter: **ruff**
- Python version: **>=3.12**
