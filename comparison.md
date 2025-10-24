# Type Checker Comparison

## Mypy

Mypy is a powerful and well-maintained type checker, but it can be a bit slow
in practice. I created Zuban with the goal of replacing both Mypy and Jedi
with a single, consistent tool.

Zuban strives for a high level of compatibility with Mypy, and in most cases,
you can use `zmypy` as a drop-in replacement for the `mypy` command-line tool.

## Pyright

Zuban’s default mode is designed to be functionally similar to Pyright.
However, Zuban offers significantly better performance - running faster and
using substantially less memory than Pyright.

Pyright has limitations that Mypy does not. A notable example is that
Pyright assigns Any in cases of
[circular references](https://microsoft.github.io/pyright/#/mypy-comparison?id=circular-references),
which can silently result in untyped code. It also skips certain checks in
loops by design, missing true positives.

## ty / pyrefly

Both type checkers are still in early alpha stages and currently lack several
fundamental {ref}`type system features <type_features>` that Zuban currently
supports.

Progress can be tracked on the [conformance tests](https://htmlpreview.github.io/?https://github.com/python/typing/blob/main/conformance/results/results.html).

## Jedi

Jedi is not a type checker, but it provides high-quality — albeit relatively
slow — autocompletion, go-to-definition, rename, and other basic IDE features.
Unlike the other tools listed, it does not perform static type checking.

The slow performance of Jedi was the main reason why I decided to start
building Zuban.
