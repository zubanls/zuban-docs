(installation_start)=
# Installation

You can install zubanls by using:

```bash
pip install zuban --break-system-packages --upgrade
```

Note: Using `--break-system-packages` should not pose any issues, as no
third-party Python packages are actually installed.

After installation, two executables will be available:

- `zmypy` - A command-line tool compatible with Mypy usage (e.g., `zmypy --strict`)
- `zubanls` - A Language Server compatible with any editor or IDE that supports the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/specifications/specification-current/)

Installing the Language Server is straightforward. In most editors, you can
configure `zubanls` directly as the Language Server executable.

## VSCode

```{note}
   You **must** [install](installation_start) ZubanLS separately via pip before using the extension.
```

Install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=zuban.zubanls).



## VIM

Using [vim-lsp](https://github.com/prabirshrestha/vim-lsp)

```vim
au User lsp_setup call lsp#register_server({
    \ 'name': 'ZubanLS',
    \ 'cmd': ['zubanls'],
    \ 'allowlist': ['python'],
    \ })
```

## Helix

Add the following to [languages.toml](https://docs.helix-editor.com/languages.html#languagestoml-files):

```toml
[[language]]
name = "python"
language-servers = ["zuban"]

[language-server.zuban]
command = "zubanls"
```
