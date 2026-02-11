# The Zuban Language Server & Type Checker

Zuban is a high-performance Python Language Server and type checker implemented
in Rust, by the author of [Jedi](https://github.com/davidhalter/jedi).
Zuban is 20–200× faster than Mypy, while using roughly half the memory and CPU
compared to Ty and Pyrefly. It offers both a PyRight-like mode and a
Mypy-compatible mode, which behaves just like Mypy; supporting the same config
files, command-line flags, and error messages.

Zuban has full LSP (Language Server Protocol) support. Features include
diagnostics, completions, goto, references, rename, hover and document
highlights.

{ref}`Installing Zuban <installation_start>`

Zuban passes over 95% of Mypy’s relevant test suite and offers comprehensive
support for Python's {ref}`type system <type-features>`.

![Zuban Diagnostics](_static/vscode.png)

Zuban is licensed {ref}`AGPL <license>`

## Chapters

```{toctree}
:maxdepth: 2

installation.md
usage.md
features.md
license.md
comparison.md
integrations.md
changelog.md
```
