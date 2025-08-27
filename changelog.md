# Changelog

## 0.0.20 (2025-08-28)

* Performance optimizations (some multi-threading, generally about 20% faster)
* `zuban` is now the main executable, `zubanls` and `zmypy` simply call `zuban`
* Fixing a lot of crashes

## 0.0.19 (2025-08-11)

* Fix a lot of details around diagnostics to satisfy most conformance tests

## 0.0.18 (2025-08-11)

* Add language server (LSP) capabilities for
    * Completions
    * Goto (definitions, declarations, implementations, type-definitions)
    * Hover
    * References / Document Highlights
    * Rename
* Add type inference for untyped params, when running `zmypy --no-mypy-compatible`.
  `def foo(x): return [x]` would be inferred as Callable[[T], list[T]]

## 0.0.1 - 0.0.17

* Initial releases of zuban with basic type checking
