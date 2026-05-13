# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `py.typed` marker (PEP 561) so downstream consumers can pick up inline type hints.
- `__version__` attribute exposed from `lend_book.__init__` via `importlib.metadata`.
- `[project.urls]` (Homepage, Repository, Issues, Changelog) and extended classifiers in `pyproject.toml`.
- `[project.optional-dependencies]` for `dev` and `test` extras in `pyproject.toml`.
- `.editorconfig` with utf-8, LF endings, 4-space indent (2 for yml/toml/json).
- `CHANGELOG.md` following Keep a Changelog 1.1.0.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) running lint, build, and `pip-audit` on Python 3.11, 3.12, 3.13.
- `examples/demo.py` with the runnable demo previously embedded in `manager.py`.

### Changed
- `BaseError.__init__` no longer uses the class attribute `code` as a default-argument value (which evaluated at class-body time); it now takes `code: str | None = None` and falls back to the class attribute at runtime.
- `requirements*.txt` files now act as thin wrappers (`-e .`, `-e .[dev]`, `-e .[test]`).
- Ruff `select` rule set extended with `B`, `SIM`, `RUF`, `C4`.
- `[tool.setuptools.packages.find]` restricted with `include = ["lend_book*"]`.

### Removed
- Per-module `main()` demo blocks from `manager.py`, `models/book_model.py`, `models/user_normal_model.py`, and `models/user_premium_model.py`. The demo now lives in `examples/demo.py`.

## [1.0.0] - 2025-09-24

### Added
- Initial release of the `lend-book` library management system.
- `Manager` orchestrator with in-memory dicts of books and users keyed by UUID.
- `BookModel` with inventory tracking (`units`, `stock`, `decrease_unit`, `increase_unit`).
- `UserModel` abstract base class plus `UserNormalModel` (single rental) and `UserPremiumModel` (multiple rentals).
- Structured exception hierarchy: `BaseError`, `ValidationError`, `AuthenticationError`, `NotFoundError`, `ConflictError`, `BusinessError`, `InternalError`.
- Centralized error codes and messages in `constants/`.
- Ruff linting/formatting configuration and pre-commit hooks.

[Unreleased]: https://github.com/DiegoLibonati/Library-Python-POO/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/DiegoLibonati/Library-Python-POO/releases/tag/v1.0.0
