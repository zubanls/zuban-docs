# Type Checker Comparison

## Mypy

Mypy is a powerful and well-maintained type checker, but it can be a bit slow
in practice. I created Zuban with the goal of replacing both Mypy and Jedi
with a single, consistent tool.

Zuban strives for a high level of compatibility with Mypy, and in most cases,
you can use `zmypy` as a drop-in replacement for the `mypy` command-line tool.
Mypy is in terms of correctness still the best type checker in the Python
universe. The conformance tests show that there are some issues, but these are
mostly minor. Mypy has a lot of upsides over Pyright that are less known. Mypy
for example infers `list.append()`.

## Pyright

Zuban’s default mode is very similar to Pyright.  However, Zuban offers
significantly better performance - running faster and using substantially less
memory than Pyright.

Pyright has very few bugs and is an all around really solid tool.  Pyright has
limitations that Mypy does not. A notable example is that Pyright assigns Any
in cases of [circular
references](https://microsoft.github.io/pyright/#/mypy-comparison?id=circular-references),
which can silently result in untyped code. It also skips certain checks in
loops by design, missing true positives. 

## Ty

Ty is still lacking a lot of fundamental type system features and is therefore
not tracket yet on the [conformance test](https://htmlpreview.github.io/?https://github.com/python/typing/blob/main/conformance/results/results.html).
Ty - like Zuban - is very fast and is doing really well with big code bases. I
would personally not recommend using Ty until they pass big parts of the
conformance tests. It might become a good tool, but currently lacks many
fundamental checks.

## Pyrefly

Pyrefly has been making big progress with passing [conformance tests](https://htmlpreview.github.io/?https://github.com/python/typing/blob/main/conformance/results/results.html).
It is slightly slower than Ty and Zuban, but is still really fast and has been
getting closer to Pylance's feature set. The biggest drawback is probably its
file based invalidation, which can make LSP usage really slow in some cases in
big codebases.

## Jedi

Jedi is not a type checker, but it provides high-quality — albeit relatively
slow — autocompletion, go-to-definition, rename, and other basic IDE features.
Unlike the other tools listed, it does not perform static type checking.

The slow performance of Jedi was the main reason why I decided to start
building Zuban.
