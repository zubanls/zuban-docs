# Changelog

## Changes

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
