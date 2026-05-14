# CHANGELOG


## v0.1.0 (2026-05-14)

### Bug Fixes

- Better demo with pyproject command
  ([`669ca9a`](https://github.com/DiegoLibonati/lend-book/commit/669ca9a1a75c6f31b88b739daac450d5194778f5))

- Better repository name/description and better system test
  ([`516eaa3`](https://github.com/DiegoLibonati/lend-book/commit/516eaa3172e097a6840c6c3528290c59633e0a1e))

- Fix typings and properties
  ([`00180f7`](https://github.com/DiegoLibonati/lend-book/commit/00180f7189848034d9ce83bad1447d122010be7d))

- Pip version to fix vulnerabilities and ci updated
  ([`66dc17f`](https://github.com/DiegoLibonati/lend-book/commit/66dc17f3ab704780ba2c48d666824e946de1d932))

- Remove migrations exclude in pre commit config and update requirements dev
  ([`0f10e63`](https://github.com/DiegoLibonati/lend-book/commit/0f10e634a71cf60c621d9959b0b55635e195b308))

- Rename model files
  ([`a4c9b70`](https://github.com/DiegoLibonati/lend-book/commit/a4c9b706542532da589380d185487a447212e0f3))

- Title app
  ([`5b6ade4`](https://github.com/DiegoLibonati/lend-book/commit/5b6ade4838d8672cabeab452ceb72cbe5a76aaca))

### Chores

- Apply architecture review — packaging, CI, and code quality
  ([`c936fb7`](https://github.com/DiegoLibonati/lend-book/commit/c936fb7fb8a0dc74561a04892d90bb5f2c3cec16))

- Move dev/test deps into pyproject.toml optional-dependencies with exact pins (==); convert
  requirements*.txt to thin -e . wrappers - Add [project.urls], extended classifiers
  (3.11/3.12/3.13, Typing :: Typed), and [tool.setuptools.package-data] for py.typed (PEP 561) - Add
  GitHub Actions CI workflow: lint matrix (3.11–3.13), build, pip-audit - Add .editorconfig (utf-8,
  LF, 4-space indent) - Add CHANGELOG.md following Keep a Changelog 1.1.0 - Fix BaseError.__init__:
  replace class-attribute default with None sentinel so subclass code/message overrides are honored
  at runtime - Add __version__ via importlib.metadata in __init__.py - Move demo code out of model
  files into examples/demo.py - Tighten ruff rule set: add B, SIM, RUF, C4 - Add .venv/ and env/ to
  .gitignore; tighten setuptools package discovery

### Continuous Integration

- Add automated changelog and versioning with python-semantic-release
  ([`35b7566`](https://github.com/DiegoLibonati/lend-book/commit/35b7566b0d0891d346242415ab98050972680007))

- Split single job into lint-and-audit, testing, and build
  ([`1d98ff6`](https://github.com/DiegoLibonati/lend-book/commit/1d98ff6e8bd0a5fa8436bc7aa8beba2dd6abfcd4))

Replaces the monolithic lint-and-build job with three chained jobs: lint-and-audit runs ruff and
  pip-audit on Python 3.13; testing runs pytest with coverage across the 3.11/3.12/3.13 matrix;
  build produces the distribution and asserts the .tar.gz artifact exists.

### Features

- .python-version file added
  ([`6bcfbdf`](https://github.com/DiegoLibonati/lend-book/commit/6bcfbdf7e34ab4f4233fa1528c66ebfa4fb5940e))

- Better code and tests added
  ([`27ad21c`](https://github.com/DiegoLibonati/lend-book/commit/27ad21cf408a20a20e2c9c2a77073ecddd713302))

- Better readme
  ([`e00b946`](https://github.com/DiegoLibonati/lend-book/commit/e00b94648d43aa19923487816eff0f7af8e234b3))

- Books and users now are dicts with key id and value book/user.
  ([`b670cd6`](https://github.com/DiegoLibonati/lend-book/commit/b670cd6268f745e1c23c54436f98f0c045f73744))

- Build with setuptools added, pre-commit added and better code
  ([`1a5ac82`](https://github.com/DiegoLibonati/lend-book/commit/1a5ac82c549cde67727b8ae1bc3baa02d5387c08))

- First commit
  ([`7359f24`](https://github.com/DiegoLibonati/lend-book/commit/7359f24ef788fc7b59cb18743a6724831982a131))

- Refactor of template library python
  ([`a7acd86`](https://github.com/DiegoLibonati/lend-book/commit/a7acd86deef07d7cf9e996e619ec789e462df5fc))

- Test_book.py added
  ([`dd328f1`](https://github.com/DiegoLibonati/lend-book/commit/dd328f12fdd3cd43e5585fa4c68a3fee59235397))
