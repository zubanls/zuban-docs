# Features

Zuban passes over 95% of Mypy's relevant test suite, closely matching Mypy's
behavior. Zuban has comprehensive [LSP (Language Server Protocol)][lsp] support with most of the expected [capabilities](#lsp-capabilities)
and you should therefore be able to use Zuban in any LSP compatible editor.

If you're experiencing issues but are otherwise satisfied with performance, you
can report them via [GitHub Issues](https://github.com/zubanls/zuban/issues).
For commercial support or prioritized help, contact info (at) zubanls.com.

## Typing Conformance 

The full specification of the Python typing system can be found on
[typing.python.org](https://typing.python.org/en/latest/spec/).
Any deviations from this specification are considered bugs and will be
addressed promptly.

The [conformance tests](https://htmlpreview.github.io/?https://github.com/python/typing/blob/main/conformance/results/results.html)
show the current compliance with the spec for the different type checkers.

Below is a list of the features supported by Zuban, along with their corresponding PEPs.


(type-features)=
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
- TypeVar/TypeVarTuple/ParamSpec defaults ([PEP 696](https://peps.python.org/pep-0696/))
- Narrowing types with TypeGuard ([PEP 647](https://peps.python.org/pep-0647/))
  and TypeIs ([PEP 742](https://peps.python.org/pep-0742/))
- Literal strings ([PEP 675](https://peps.python.org/pep-0675/)), note that
  this is not implemented in Mypy
- Marking deprecations using the type system ([PEP 702](https://peps.python.org/pep-0702/))
- Disjoint bases ([PEP 800](https://peps.python.org/pep-0800/))
- and probably more that have been omitted here

## LSP Capabilities

Zuban implements a comprehensive suite of LSP features, including:

- Real‑time diagnostics 
- Completions, hover documentation, signature help, inlay hints
- Navigation - go to definition, find references, highlight usages, symbol search, folding and selection ranges
- Refactoring actions - renaming, auto‑imports, adding `# type: ignore`
- Semantic tokens
- Notebook support

Formatting is out of scope - use a dedicated formatting tool like Ruff or Black.

<details id="lsp-capability-list">
<summary><strong>Full capability list (click to expand)</strong></summary>

- ✅ [`textDocument/diagnostic`][diagnostic]
- ✅ [`workspace/diagnostic`][workspacediagnostic]
- ✅ [`textDocument/completion`][completion]
- ✅ [`textDocument/hover`][hover]
- ✅ [`textDocument/signatureHelp`][signaturehelp]
- ✅ [`textDocument/inlayHint`][inlayhint]
- ✅ [`textDocument/definition`][definition]
- ✅ [`textDocument/declaration`][declaration]
- ✅ [`textDocument/implementation`][implementation]
- ✅ [`textDocument/typeDefinition`][typedefinition]
- ✅ [`textDocument/references`][references]
- ✅ [`textDocument/documentHighlight`][documenthighlight]
- ✅ [`textDocument/documentSymbol`][documentsymbol]
- ✅ [`workspace/symbol`][workspacesymbol]
- ✅ [`textDocument/codeAction`][codeaction] – Auto imports, adding `# type: ignore[<error-code>]`
- ✅ [`textDocument/prepareRename`][preparerename]
- ✅ [`textDocument/rename`][rename]
- ✅ [`textDocument/semanticTokens`][semantictokens]
- ✅ [`textDocument/foldingRange`][foldingrange]
- ✅ [`textDocument/selectionRange`][selectionrange]
- ✅ [`notebookDocument/*`][notebookdocument]
- 🚫 [`textDocument/formatting`][formatting] – Out of scope, use a formatter (e.g., Ruff/Black)
- 🚫 [`textDocument/onTypeFormatting`][ontypeformatting] – Use a formatter
- 🚫 [`textDocument/rangeFormatting`][rangeformatting] – Use a formatter
- ❌ [`textDocument/codeLens`][codelens]
- ❌ [`workspace/willRenameFiles`][willrenamefiles] – [#488]
- ❌ [`callHierarchy/*`][callhierarchy] – [#488]
- ❌ [`typeHierarchy/*`][typehierarchy] – [#488]
- ⬛ [`textDocument/documentColor`][documentcolor] – No built‑in color representation in Python
- ⬛ [`textDocument/documentLink`][documentlink] – No built‑in resource link representation in Python; imports use [`textDocument/definition`][definition]

The `experimental` field of [`ClientCapabilities`](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#clientCapabilities) is ignored – Zuban has no support for non‑standard LSP extensions.
</details>

## General Code Understanding

- Correct resolution of relative, absolute, and stub-only (`.pyi`) imports
- Type narrowing - Based on isinstance, assert, if conditions, etc
- Inferring the type context (e.g. `x: list[object] = [1]`)
- Understanding `list.append, list.extend, set.add, set.update, dict.__setitem__, dict.update` to empty collections (rather than defaulting to `list[Any]`)
  (No support for this in user-defined data structure classes, those still need annotation on initialization)

## Development Tooling

- Error recovery - Can recover gracefully from invalid Python syntax.
- Mypy config compatibility - Honors `.mypy.ini`, `mypy.ini`, or `pyproject.toml` settings
- Incremental checking - Only rechecks changed files for performance when
  running the language server
- Watch mode - Rechecks files automatically on change.
- Works on **Linux** (x86-64, AArch64, ARMv7, i686), **macOS** (ARM & x86-64) and
  **Windows** (x86-64 and i686)

## Performance

- Zuban is written in Rust for high performance. It runs on a single core but
  is already over 20× faster than Mypy. Multi-core support is planned.
- Optimized to minimize memory usage.

## Missing Features

- Unused `# type: ignore` comments are not yet reported.
- General plugin support is not planned; however, targeted plugins for popular
  libraries, such as Django, will be provided.
- Function bodies using constrained TypeVar definitions (e.g., `TypeVar("T", str, bytes)`, `[T: (str, bytes)]`)
  are not currently type-checked. This limitation is unlikely to affect most users.

<!-- Links -->
[#488]: https://github.com/zubanls/zuban/issues/488#issuecomment-4892339855
[lsp]: https://microsoft.github.io/language-server-protocol/
[diagnostic]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_diagnostic
[workspacediagnostic]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_diagnostic
[completion]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_completion
[hover]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_hover
[signaturehelp]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_signatureHelp
[inlayhint]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_inlayHint
[definition]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_definition
[declaration]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_declaration
[implementation]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_implementation
[typedefinition]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_typeDefinition
[references]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_references
[documenthighlight]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentHighlight
[documentsymbol]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentSymbol
[workspacesymbol]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_symbol
[codeaction]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_codeAction
[preparerename]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_prepareRename
[rename]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_rename
[semantictokens]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_semanticTokens
[foldingrange]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_foldingRange
[selectionrange]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_selectionRange
[notebookdocument]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#notebookDocument_synchronization
[formatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_formatting
[ontypeformatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_onTypeFormatting
[rangeformatting]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_rangeFormatting
[codelens]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_codeLens
[willrenamefiles]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#workspace_willRenameFiles
[callhierarchy]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#callHierarchy_incomingCalls
[typehierarchy]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#typeHierarchy_supertypes
[documentcolor]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentColor
[documentlink]: https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#textDocument_documentLink
