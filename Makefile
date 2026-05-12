SCRIPT ?= pysandbox.hello

.PHONY: test run lint format install-hooks

test:
	uv run pytest

run:
	uv run python -m $(SCRIPT)

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

install-hooks:
	uv run pre-commit install
