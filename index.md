# The Zuban Language Server

ZubanLS is a Mypy-compatible, high-performance Python Language Server and type
checker implemented in Rust, by the author of
[Jedi](https://github.com/davidhalter/jedi).

Most relevant LSP features are supported. Features include diagnostics,
completions, goto, references, rename, hover and document highlights.

{ref}`Installing ZubanLS <installation_start>`

ZubanLS passes over 90% of Mypy’s relevant test suite and offers comprehensive
support for Python's {ref}`type system <type_features>`.

![ZubanLS Diagnostics](_static/vscode.png)

ZubanLS is not open source, but it is free for most users. Small and mid-sized
projects — around 50,000 lines of code — can continue using it for free, even in
commercial settings, after the beta and full release. Larger codebases will
require a {ref}`commercial license <license>`.

## Chapters

```{toctree}
:maxdepth: 2

installation.md
usage.md
features.md
license.md
comparison.md
changelog.md
```
