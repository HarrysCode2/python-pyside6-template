# Python PySide6 Template

A minimal, production-structured Python desktop application template.

## What's included

- PySide6 GUI boilerplate
- Virtual environment configuration
- `pyproject.toml` for dependency management
- `pytest` test suite setup
- `.gitignore` pre-configured for Python

## Requirements

- pyenv
- Python 3.12.9 (via pyenv)
- pip

## Getting started

Clone this repo, then:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m app
```

## Running tests

```bash
pytest
```