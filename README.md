# pyapp

A simple Python CLI for math operations, used as the training project for the **Git/GitHub** workshop.

## Features

- `add` — Add two integers
- `sub` — Subtract two integers

## Requirements

- Python 3.10+
- See `pyapp/requirements.txt` for dependencies

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r pyapp/requirements.txt
```

## Usage

```bash
python pyapp/app.py add 3 5   # → 8
python pyapp/app.py sub 10 4  # → 6
```

## Run tests

```bash
pytest -q pyapp/test_app.py
```

## Docker

```bash
docker build -f pyapp/Dockerfile -t pyapp .
docker run pyapp add 3 5
```

## Environment

Copy `.env.example` to `.env` and adjust values:

```bash
cp pyapp/.env.example .env
```

## CI

Tests run automatically on every push and pull request via GitHub Actions.  
See `.github/workflows/ci.yml`.

## Contributing

See `docs/contributors.md` to add your name during the workshop.  
See `docs/setup.md` for detailed setup instructions.
