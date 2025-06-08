# Features

By default, ZubanLS runs in a non-Mypy-compatible mode. If a Mypy configuration
is found in `mypy.ini` or `pyproject.toml`, it will switch to Mypy-compatible mode.
Currently, false positives can be an issue, but this is expected to improve
over time.

If you're experiencing issues but are otherwise satisfied with performance, you
can report them via GitHub Issues. For commercial support or prioritized help,
contact info (at) zubanls.com.

## Features

The full specification of the Python typing system can be found on
[typing.python.org](https://typing.python.org/en/latest/spec/).
Any deviations from this specification are considered bugs and will be
addressed promptly. Below is a list of the features supported by ZubanLS, along
with their corresponding PEPs.

(type_features)=
### Type System Support

- Generic types - Full support for TypeVar, bounded types, variance, etc. ([PEP 484](https://peps.python.org/pep-0484/))
- Overloads / NewType / NamedTuple / Enum support ([PEP 484](https://peps.python.org/pep-0484/))
- Type Parameter Syntax: `class Foo[T]: ...` ([PEP 695](https://peps.python.org/pep-0695/))
- Protocols and structural subtyping ([PEP 544](https://peps.python.org/pep-0544/)).
- Union and Optional types - including the new `X | Y` syntax ([PEP 604](https://peps.python.org/pep-0604/))
- Literal types ([PEP 586](https://peps.python.org/pep-0586/)).
- Final ([PEP 591](https://peps.python.org/pep-0591/)), Annotated
  ([PEP 593](https://peps.python.org/pep-0593/)), and ClassVar ([PEP 526](https://peps.python.org/pep-0526/))
- TypeVarTuple / Variadic Generics ([PEP 646](https://peps.python.org/pep-0646/)
- ParamSpec/Concatenate support ([PEP 612](https://peps.python.org/pep-0612/))
- Self Types ([PEP 673](https://peps.python.org/pep-0673/))
- Dataclass and `dataclass_transform` support ([PEP 681](https://peps.python.org/pep-0681/))
- TypedDict support ([PEP 589](https://peps.python.org/pep-0589/)) including
  Required / NotRequired ([PEP 655](https://peps.python.org/pep-0655/)),
  kwargs unpacking ([PEP 692](https://peps.python.org/pep-0692/)) and read-only
  items ([PEP 705](https://peps.python.org/pep-0705/))
- Explicit Type Aliases ([PEP 613](https://peps.python.org/pep-0613/))
- Override decorator ([PEP 698](https://peps.python.org/pep-0698/))
- Narrowing types with TypeGuard ([PEP 647](https://peps.python.org/pep-0647/))
  and TypeIs ([PEP 742](https://peps.python.org/pep-0742/))

### General Code Understanding

- Correct resolution of relative, absolute, and stub-only (`.pyi`) imports
- Type narrowing - Based on isinstance, assert, if conditions, etc
- Inferring the type context (e.g. `x: list[object] = [1]`)
- Mypy's `--new-type-inference` (enabled by default in [Mypy 1.7.0](https://github.com/python/mypy/issues/15906))
- Understanding `list.append`, `list.extend`, `set.add` and `set.extend`

### Development Tooling

- Mypy config compatibility - Honors `.mypy.ini`, `mypy.ini`, or `pyproject.toml` settings
- Incremental checking - Only rechecks changed files for performance when
  running the language server
- [LSP protocol](https://microsoft.github.io/language-server-protocol/specifications/specification-current/)
  support - Diagnostics through Language Server Protocol (even if
  other LSP features like completion aren't present).
- Watch mode - Rechecks files automatically on change.

### Performance

- ZubanLS is written in Rust for high performance. It runs on a single core but
  is already over 20× faster than Mypy. Multi-core support is planned.
  existing performance.
- Optimized to minimize memory usage.

## Missing Features

- Unused `# type: ignore` comments are not yet reported.
- General plugin support is not planned; however, targeted plugins for popular
  libraries, such as Django, will be provided.
- The match statement may result in names being assigned the type Any.
- Function bodies using bounded TypeVar definitions (e.g., `TypeVar("T", str, bytes)`)
  are not currently type-checked. This limitation is unlikely to affect most users.
- Literal strings ([PEP 675](https://peps.python.org/pep-0675/)), note that
  this is also not implemented in Mypy
- Marking deprecations using the type system ([PEP 702](https://peps.python.org/pep-0702/))
