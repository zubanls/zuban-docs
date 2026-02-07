# Usage

There are two main ways to use Zuban, either as a {ref}`type checker <usage-type-checking>`
on the command line like `zuban check` or as a
{ref}`language server <usage-language-server>` in your IDE/Editor.

There are two basic {ref}`modes <usage-modes>` for running Zuban, the `default`
mode and the `mypy`-compatible mode. Zuban tries to find the optimal mode for
you depending on your config. {ref}`Configuration <usage-configuration>` is
possible with `pyproject.toml` or `mypy.ini`.

You can use both `zuban: ignore` and `type: ignore`. It is possible to filter
errors like you would in Mypy: `zuban: ignore[attr-defined]`. Zuban is fully
[standards compliant](https://htmlpreview.github.io/?https://github.com/python/typing/blob/main/conformance/results/results.html).

(usage-type-checking)=
## Type Checking / Command Line

For type checking there are three fundamental command line options:

- `zuban check` - This is the default mode that makes zuban run in a PyRight
  like mode by default, but if Mypy configs are found it will try to imitate mypy.
- `zuban mypy` - Tries to be as much as possible like running `mypy`
- `zmypy` - An alias for `zuban mypy`

Many of [Mypy's docs](https://mypy.readthedocs.io) apply, for example:

- Mypy's [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- Mypy's [command line
  interface](https://mypy.readthedocs.io/en/stable/command_line.html) is very
  similar. You can also see all available options in `zmypy --help`.

You can for example use all of these:

```
zuban check --strict
zuban mypy --warn-unreachable
zmypy --disallow-untyped-defs
```

(usage-language-server)=
## Language Server

To use zubanls, simply [install](installation_start) it, add to your editor of
choice and start coding. There are currently no command line options.

(usage-modes)=
## Modes

Unless you run `zuban mypy`, Zuban will try to guess the mode in the following
order:

1. An explicit mode: `zuban check --mode default`
2. An explicit mode in `pyproject.toml` in `[tool.zuban]` like `mode = "mypy"` or `mode = "default"`.
3. A precence of the key `[tool.zuban]` in `pyproject.toml` implies the mode `default`.
4. A precense of `[tool.zuban]` in `pyproject.toml` or a `mypy.ini` file imply the mode `mypy`.
5. As a fallback the `default` mode is used.

It is recommended to use the default mode unless you are converting from a Mypy
codebase. The `default` mode works mostly like Mypy with different default flags.
These are the differences:

- The following command line options are enabled: `--allow-untyped-globals`,
  `--check-untyped-defs`, `--allow-redefinition`, `--local-partial-types`,
  `--warn-unreachable`, `--no-warn-no-return`, `--follow-untyped-imports`,
  `--exclude-gitignore`.
- Zuban uses unions instead of what Mypy calls "Joins". `[1, ""]` is inferred as `list[int | str]` in   Zuban's default mode instead of `list[object]`.
- Untyped code is checked by default and its return types are inferred. Zuban
  by default also enables `--untyped-strict-optional`, which is similar to
  `--strict-optional` for untyped code. Issues around unions with None are very
  typical for untyped code and are therefore not reported by default. Untyped
  code is a concept introduced by Mypy where a function has neither typed
  parameters nor a typed return value.

(usage-configuration)=
## Configuration

Zuban supports both Mypy config and it's own entry in `pyproject.toml`:

```toml
[tool.zuban]
strict = true
disallow_untyped_defs = true
warn_unreachable = true
allow_untyped_globals = false
check_untyped_defs = false
follow_untyped_imports = true
exclude_gitignore = true
# And many more Mypy options
```

Like the options above, you can use most configuration options [available in
Mypy](https://mypy.readthedocs.io/en/stable/config_file.html).

Zuban adds the following configuration options:

```
[tool.zuban]
mode = "default"  # Or "mypy"

# Recommended (and the default) for untyped code
untyped_strict_optional = true

# Mypy's default is "any", Zuban's "inferred"
untyped_function_return_mode = "inferred"
```

If you are a Mypy user you can leave your Mypy [config file
options](https://mypy.readthedocs.io/en/stable/config_file.html) in place and
Zuban should pick up your Mypy configuration.

It is also possible to use both the old Mypy config and new Zuban configuration
together like this:

```
[tool.zuban]
check_untyped_defs = true

[tool.mypy]
# Your old Mypy config
strict = true
```

Keep in mind that by adding the `[tool.zuban]` section, the {ref}`mode
<usage-modes>` might change.

## Dealing with the sys.path

Zuban tries to find the best possible path itself. In some cases, a custom path
might need to be provided.

This is possible for example with a `pyproject.toml`:

```toml
[tool.zuban]
mypy_path = ["src", "src2/nested"]
```

or for Mypy users (also in `pyproject.toml`):

```toml
[tool.mypy]
mypy_path = "$MYPY_CONFIG_FILE_DIR/src"
```

Alternatively you could also supply the environment variable `PYTHONPATH` like this:

```bash
PYTHONPATH="src:src2/nested" zuban check
```

The same is also possible with `MYPYPATH`.

## Logging

To enable logging you can set the environment variable `ZUBAN_LOG_FILE=<some-file>`.

Most of the time you are probably interested in more verbose logging and you
should set the environment variable `ZUBAN_LOG=info` or `ZUBAN_LOG=debug`. If
you are running the language server, please avoid writing the log file to your
working directory, because writing the log files will cause numerous file
system events.
