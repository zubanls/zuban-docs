# Changelog

## 0.0.18

* Add language server (LSP) capabilities for
    * Completions
    * Goto (definitions, declarations, implementations, type-definitions)
    * Hover
    * References / Document Highlights
* Add type inference for untyped params, when running `zmypy --no-mypy-compatible`.
  `def foo(x): return [x]` would be inferred as Callable[[T], list[T]]

## 0.0.1 - 0.0.17

* Initial releases of zuban with basic type checking
