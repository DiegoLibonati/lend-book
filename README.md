# Lend Book

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Lend Book** is a library management system built in Python using object-oriented programming principles. It provides a clean, structured API to manage an inventory of books and a registry of users, supporting the full lifecycle of book rentals and returns.

The system revolves around a central `Manager` class that acts as the single orchestrator for all operations. It maintains an in-memory catalog of books and a registry of users, each identified by a unique UUID. Through the `Manager`, you can register and remove users, add and remove books from the catalog, and process book rentals and returns — all with validation and business rules enforced at every step.

Books are modeled with an inventory counter (`units`). A book is considered in stock as long as it has at least one unit available. Renting a book decreases its unit count; returning it restores it. The system prevents renting a book that is out of stock.

Two types of users are supported, each with different rental policies:

- **Normal users** can hold only one rented book at a time. They must return their current book before they can rent another one.
- **Premium users** can rent multiple books simultaneously. Each rental and return is tracked individually, and returning a specific book removes only that title from their active rentals.

The codebase includes a structured exception hierarchy (`ValidationError`, `NotFoundError`, `ConflictError`, `BusinessError`, `AuthenticationError`, `InternalError`) that makes error handling predictable and explicit. Every error carries a `code` constant and a human-readable `message`, making it straightforward to integrate with any UI or API layer on top.

The package is installed in editable mode via `pyproject.toml` using a `src/` layout, and exposes a clean public API (`Manager`, `BookModel`, `UserModel`, `UserNormalModel`, `UserPremiumModel`) from its top-level `__init__.py`. The project follows modern Python conventions: strict typing throughout, Ruff for linting and formatting, pre-commit hooks for code quality enforcement, and a full pytest test suite covering models, business logic, exceptions, constants, and the manager orchestration layer.

## Technologies used

The project relies on a minimal, modern Python stack:

1. Python >= 3.11

## Libraries used

Dependencies are declared in `pyproject.toml` and split into optional groups so production installs stay minimal.

#### Runtime (`[project.dependencies]`)

```
None — the library has no third-party runtime dependencies.
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

## Getting Started

With the dependencies listed above in mind, follow these steps to set up the project locally:

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install the package in editable mode with dev and test extras: `pip install -e .[dev,test]`
6. Run the project:
    1. From CLI (demo): `python -m examples.demo`
    2. Or import as a library in Python: `from lend_book import Manager, BookModel`

### Pre-Commit for Development

Once the environment is ready, enable the pre-commit hooks so that linting and formatting run automatically on every commit:

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Testing

After completing [Getting Started](#getting-started), the full test suite can be run from the repository root:

1. Activate your virtual environment
2. Execute: `pytest --log-cli-level=INFO`

## Security Audit

In addition to running tests, you can check your dependencies for known vulnerabilities using **pip-audit** (already included in the `dev` extra):

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip-audit`

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/lend-book`](https://www.diegolibonati.com.ar/#/project/lend-book)
