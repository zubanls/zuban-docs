# Type Checker Comparison

## Mypy

Mypy is a powerful and well-maintained type checker, but it can be a bit slow
in practice. I created ZubanLS with the goal of replacing both Mypy and Jedi
with a single, consistent tool.

ZubanLS strives for a high level of compatibility with Mypy, and in most cases,
you can use `zmypy` as a drop-in replacement for the `mypy` command-line tool.

## Pyright

ZubanLS’s default mode is designed to be functionally similar to Pyright.
However, ZubanLS offers significantly better performance - running faster and
using substantially less memory than Pyright.

Pyright additionally provides IDE features such as autocompletion,
go-to-definition, and more. These capabilities are currently under development
for ZubanLS and may take some time to be fully implemented.
In the meantime, you can use [Jedi](https://github.com/davidhalter/jedi) via
[Jedi Language Server](https://github.com/pappasam/jedi-language-server/) to
supplement ZubanLS with most features it does not yet support.

## ty / pyrefly

Both type checkers are still in early alpha stages and currently lack several
fundamental {ref}`type system features <installation_start>`.


## Jedi

Jedi is not a type checker, but it provides high-quality — albeit relatively
slow — autocompletion, go-to-definition, rename, and other basic IDE features.
Unlike the other tools listed, it does not perform static type checking.

The slow performance of Jedi was the main reason why I decided to start
building ZubanLS.
