# PySandbox

A simple Python sandbox project for experiments, scripts, and quick prototypes.

## Quick Start

```bash
# Run tests
make test

# Run the default hello script
make run

# Run a specific module
make run SCRIPT=pysandbox.hello
```

## Development Commands

| Command | Description |
|---------|-------------|
| `make test` | Run all tests with pytest |
| `make run` | Run the default script |
| `make run SCRIPT=<module>` | Run a specific module |
| `make lint` | Run ruff linter and format checker |
| `make format` | Auto-fix lint issues and format code |
| `make install-hooks` | Install pre-commit git hooks |

## Project Structure

```
pysandbox/
├── src/pysandbox/       # Main package
├── tests/               # Unit tests
├── pyproject.toml       # Project & tool configuration
├── Makefile             # Common commands
└── .pre-commit-config.yaml  # Git hooks
```

## Tools

- **pytest** — unit testing
- **ruff** — linting & formatting (line length: 120)
- **pre-commit** — git hooks for code quality
- **uv** — package & environment manager
