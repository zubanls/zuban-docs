# The Zuban Language Server

**FOR NOW ZUBANLS IS PRE-ALPHA, CONTACT info@zubanls.com IF YOU WANT TO TRY**

ZubanLS is a Mypy-compatible, high-performance Python Language Server
implemented in Rust, by the author of [Jedi](https://github.com/davidhalter/jedi).

Currently only diagnostics are supported, feel free to use the [Jedi Language
Server](https://github.com/pappasam/jedi-language-server/) for autocompletion,
goto and renames.

{ref}`Installing ZubanLS <installation_start>`

---

ZubanLS passes over 90% of Mypy’s relevant test suite and offers comprehensive
support for the Python type system, including:

- TypeVar / TypeVarTuple / ParamSpec support
- `TypedDict` / `NamedTuple` / `Enum` / `Dataclasses` / `dataclass_transform` support
- Overloads / Protocols / NewType
- Support for the Python 3.13 syntax including type parameter syntax

A few things are currently not yet implemented:

- The match statement may result in names being assigned the type Any.
- Function bodies using bounded TypeVar definitions (e.g., `TypeVar("T", str, bytes)`) are not currently type-checked. This limitation is unlikely to affect most users.
- Unused `# type: ignore` comments are not yet reported.
- The `--allow-redefinition` and `--allow-redefinition-new` flags are not yet implemented.
- General plugin support is not planned; however, targeted plugins for popular
  libraries, such as Django, will be provided.

## Chapters

```{toctree}
:maxdepth: 2

installation.md
usage.md
logs.md
license.md
```
