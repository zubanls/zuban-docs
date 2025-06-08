# The Zuban Language Server

**FOR NOW ZUBANLS IS PRE-ALPHA, CONTACT info (at) zubanls.com IF YOU WANT TO TRY IT**

ZubanLS is a Mypy-compatible, high-performance Python Language Server
implemented in Rust, by the author of [Jedi](https://github.com/davidhalter/jedi).

Currently only diagnostics are supported, feel free to use the [Jedi Language
Server](https://github.com/pappasam/jedi-language-server/) for autocompletion,
goto and renames.

{ref}`Installing ZubanLS <installation_start>`

ZubanLS passes over 90% of Mypy’s relevant test suite and offers comprehensive
support for Python's {ref}`type system <type_features>`.

![ZubanLS Diagnostics](_static/vscode.png)

ZubanLS is not open source, but it is free for most users. Small
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
```
