# Changelog

## Changes

All of these changes are highlights, there's always smaller bugfixes included.

### 0.7.1 (2026-04-25)

- Basic support for template strings (Python 3.14 `t"..."` syntax)
- Upgrade typeshed
- Completions in comments (LSP)
- Implement `disjoint_base` (PEP 800)
- Implement conditional fields for NamedTuple and TypedDict
- Implement shell expansion for `mypy_path` in config
- Fix finding typeshed for Debian based systems if installed as root

### 0.7.0 (2026-04-06)

- **Breaking:** The default mode is now "default" even if there is Mypy
  specific config (e.g. mypy.ini). Previously the "mypy" mode would be chosen
  in such cases. Mypy config is still read, though. This does not matter if you
  run `zmypy` or `zuban mypy`. However if you want to use the language server
  you may want to add a `mode = "mypy"` to the `[tool.zuban]` section in `pyproject.toml`.
  The reason for this change is that the previous logic was too complicated for
  users to understand. Now it's pretty simple: The mode is always "default"
  except if it's explicitly chosen otherwise.
- Django `*_id` attributes and completions now work
- Error codes for overrides do now match Mypy's error codes closer
- Better hover for type aliases, type variables (LSP)
- References are now sorted in a more useful way (LSP)
- Removed the undocumented `zubanls` executable which was documented only in
  very early releases (before 0.0.20)
- Improved support for `typing_extensions` usages
- Improved speed a lot for some TypedDict matching
- Fixed a lot of crashes

### 0.6.2 (2026-03-16)

- Union matching for large literal unions (> 100 items) is now not exponential
  anymore and therefor exponentially faster :-)
- sys.path improvements (mostly for uv users):
  - The `src/` subfolder in a project is now added to the path
  - Nested folders with their own local imports are now also possible. The
    parent folder of the most outer `__init__.py` is assumed to be the package
    name
  - Added `--explicit-package-bases`, which Mypy also uses to disable these heuristics
  - `$VIRTUAL_ENV` now has lower priority than searching local folders for
    virtual envs. The problem is that this variable is quite unreliable in some
    cases, especially when zuban is run from a virtualenv itself
- Better keyword argument completions (LSP)
- Zuban is in general about 30% faster for large projects:
  - Imports are now a lot faster in large projects
  - The parser is now faster by a few percent
- The parser had stalls due to exponential reparsing, which is now fixed

### 0.6.1 (2026-02-25)

- Using zmypy is now possible from a subdir. It respects relative paths and
  will typecheck the whole project if no explicit paths are given
- Fixed a problematic bug when working with nested workspaces. This was often
  problematic when using uv
- Added a few more cases where inlay hints are useful when generics are present (LSP)

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
