# Usage

## Configuration

Zuban supports both Mypy config and it's own entry in `pyproject.toml`:

```toml
[tool.zuban]
strict = true
disallow_untyped_defs = true
warn_unreachable = true
```

We still need to document the exact options possible, but you can use most
configuration options available in Mypy.

If you are a Mypy user you can leave your Mypy
 [config file options](https://mypy.readthedocs.io/en/stable/config_file.html)
 in place and Zuban should pick up your Mypy configuration.

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

## Language Server

To use zubanls, simply [install](installation_start) it, add to your editor of
choice and start coding. There are currently no command line options.

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
