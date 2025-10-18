(installation_start)=
# Installation

You can install zuban by using:

```bash
pip install zuban --break-system-packages --upgrade
```

Using `--break-system-packages` should not pose any issues, as no
third-party Python packages are actually installed.

After installation, two executables will be available:

- `zuban` - Use `zuban check` for type checking and `zuban server` for the
  [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/specifications/specification-current/)
- `zmypy` - An alias for `zuban mypy` that is compatible with Mypy usage (e.g., `zmypy --strict`)

Installing the Language Server is straightforward. In most editors, you can
configure `zuban` directly as the Language Server executable. Here are
example configs for some IDE's/Editors.

## VSCode

```{note}
   You **must** [install](installation_start) Zuban separately via pip before using the extension.
```

Install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=zuban.zubanls).

If you're using a virtual environment, make sure to activate it and start
Zuban from the corresponding directory. VSCode integration is limited for
now, but future updates will aim to support virtual environment selection
within the editor.

## VIM

After [installing](installation_start) Zuban, add LSP support using
[vim-lsp](https://github.com/prabirshrestha/vim-lsp):

```vim
au User lsp_setup call lsp#register_server({
    \ 'name': 'Zuban',
    \ 'cmd': ['zuban', 'server'],
    \ 'allowlist': ['python'],
    \ })
```

## Helix

After [installing](installation_start) Zuban, add the following to
[languages.toml](https://docs.helix-editor.com/languages.html#languagestoml-files):

```toml
[[language]]
name = "python"
language-servers = ["zuban"]

[language-server.zuban]
command = "zuban"
args = ["server"]
```

## Zed

You should probably try this [inofficial
extension](https://zed.dev/extensions/zuban) here.

## Emacs

After [installing](installation_start) Zuban, add LSP support using
[eglot](https://www.gnu.org/software/emacs/manual/html_mono/eglot.html):

```elisp
(use-package eglot
  :config
  (add-to-list 'eglot-server-programs
               '((python-mode python-ts-mode) . ("zubanls"))))
```
