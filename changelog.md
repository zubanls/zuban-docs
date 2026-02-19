# Changelog

## Changes

### 0.6.0 (2026-02-19)

- Add pytest fixture inference, completions and goto
- Added the code action to add `# type: ignore[<error-code>]` at the end of the
  line when errors are present
- Code actions are now more gracious and give you actions for the full line
  even if the cursor is not directly on it

### 0.5.1 (2026-02-09)

- Implemented Mypy's `ignore_errors = true` correctly. This makes it possible
  to avoid showing diagnostics in a LSP process.
- Fixed the sys path when site-packages are used in a default environment

### 0.5.0 (2026-02-07)

- By default enable --untyped-strict-optional in the default mode. This reduces
  a lot of false positives in untyped code.
- Fixed many issues around untyped code
  - Muted errors for example around incomplete list generics, which are common
    in untyped code.
  - Does not infer generics for params anymore by default, this is too noisy for now.
- `try: ... except AttributeError` now mutes errors in the case where an
  attribute exists on some parts of the union, but not on others.
- In addition to specifying `type: ignore` you can now use `zuban: ignore`
- Changed `--mypy-compatible` to `--mode mypy` and `--no-mypy-compatible` to `--mode default`
- It is now possible to specify `mode = "mypy"` or `mode = "default"` in `pyproject.toml`

### 0.4.2 (2026-01-16)

- Bugfixes

### 0.4.1 (2025-12-27)

- Bugfixes

### 0.4.0 (2025-12-20)

- Get a lot closer to passing conformance tests

### 0.3.0 (2025-12-02)

- Add inlay hints (LSP)
- Django model support, implements type checking and completions (LSP)
- Added autocompletion resolve, which means documentation for completion items is now available (LSP)
- Added support for Conda (that `CONDA_PREFIX` is now recognized)
- Many fixes for crashes

### 0.2.3 (2025-11-17)

- Added autoimport actions (LSP)
- Better documentation Markdown formatting (LSP)

### 0.2.2 (2025-11-03)

- Bug fixes

### 0.2.1 (2025-10-30)

- Implemented semantic colors and selection ranges (LSP)
- Fixed a problem that caused Zuban to not terminate

### 0.2.0 (2025-10-23)

- Added Notebook support in LSP (completions, goto, rename, etc.)

### 0.1.2 (2025-10-22)

- Added musllinux builds to the PyPI release:
  - `armv7-unknown-linux-musleabihf`
  - `aarch64-unknown-linux-musl`
  - `x86_64-unknown-linux-musl`
  - `i686-unknown-linux-musl`

### 0.1.1 (2025-10-15)

- Added call signatures to LSP

### 0.1.0 (2025-10-10)

- This is the Zuban Beta release, because it feels very stable now
- Fix more crashes

### 0.0.25 (2025-10-07)

- Full support for pattern matching (`match` and `case` narrowing)
- The `PYTHONPATH` and `MYPYPATH` environment variables are now used for the `sys.path`
- Fixes for many crashes and bugs

### 0.0.24 (2025-09-23)

* Full support for TypedDict `extra_items`/`closed` ([PEP 728](https://peps.python.org/pep-0728/))
* Support for reporting deprecated usages of classes/functions, by using `--enable-error-code deprecated`
* Support for LiteralString and Literal operations, `"a" + "b"` would result in the type `Literal["ab"]`.
* Support for the `TypeVar(..., infer_variance=True)` argument
* Now all conformance tests are at least partially supported

### 0.0.23 (2025-09-12)

* Better virtualenv support: In case where no `$VIRTUAL_ENV` is found
* `.pth` file support, this enables for example uv workspaces
* Added colors to the command line
* Support for `--pretty` and the `pretty = true` to have more infos about the
  error location when running on the command line
* Added support for `typing.LiteralString` and literal operations (e.g. `"a" +
  "b"` would result in the literal `"ab"`
* Added support for `__call__` in metaclasses

### 0.0.22 (2025-09-04)

* `pyproject.toml` now supports `[tool.zuban]` for configuration
* Various bug fixes

### 0.0.21 (2025-09-03)

* Open Sourced with an AGPL license

### 0.0.20 (2025-08-28)

* Performance optimizations (some multi-threading, generally about 20% faster)
* `zuban` is now the main executable, `zubanls` and `zmypy` simply call `zuban`.
  To type check code, use `zuban check` or `zuban mypy` (to ensure Mypy-like behavior).
  To start the language server, you can simply use `zuban server`.
* Fixing a lot of crashes

### 0.0.19 (2025-08-11)

* Fix a lot of details around diagnostics to satisfy most conformance tests

### 0.0.18 (2025-07-31)

* Add language server (LSP) capabilities for
    * Completions
    * Goto (definitions, declarations, implementations, type-definitions)
    * Hover
    * References / Document Highlights
    * Rename
* Add type inference for untyped returns, when running `zuban check`.
  `def foo(x): return [x]` would be inferred as Callable[[T], list[T]]

### 0.0.1 - 0.0.17

* Initial releases of zuban with basic type checking
