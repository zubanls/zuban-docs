# Usage

## zmypy

Most of [Mypy's docs](https://mypy.readthedocs.io) apply, for example:

- Mypy's [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- Mypy [config file options](https://mypy.readthedocs.io/en/stable/config_file.html)
- Mypy's [command line
  interface](https://mypy.readthedocs.io/en/stable/command_line.html) is very
  similar. You can also see all available options in `zmypy --help`.

## zubanls

To use zubanls, simply [install](installation_start) it, add to your editor of
choice and start coding. There are currently no command line options.

## Logging

To enable logging you can set the environment variable `ZUBAN_LOG_FILE=<some-file>`.

Most of the time you are probably interested in more verbose logging and you
should set the environment variable `ZUBAN_LOG=info` or `ZUBAN_LOG=debug`.
