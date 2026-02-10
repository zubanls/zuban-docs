(integrations_start)=
# Integration with other tools

Zuban can be used both as an LSP and as a standalone type checker, depending on the
context in which it is executed.

While the LSP focuses on fast, interactive feedback during development, Zuban can
also be used as a building block in larger workflows, either through its LSP
interface, its command-line interface, or a combination of both.

This makes it possible to integrate Zuban with a wide range of tools and
orchestration systems, depending on the needs of the workflow.

The examples below show a few common integration patterns.

## pre-commit hooks

Pre-commit hooks are a common way to enforce checks locally before changes are
committed. In this context, Zuban can be used to provide early feedback about
the state of the codebase.

### pre-commit

Zuban can be integrated into a [pre-commit](https://pre-commit.com/) workflow as a
local hook. This is useful when you want to run a full-project type check before
commits or as part of a CI pipeline.

```yaml
repos:
  - repo: local
    hooks:
      - id: zuban
        name: zuban
        entry: "zuban check --config-file pyproject.toml"
        language: system
        pass_filenames: false
```

- `language: system`: uses the system Python environment where Zuban is installed.
- `pass_filenames: false`: runs Zuban on the entire project instead of only the staged files.

These options can be adjusted depending on your workflow or environment.

```{note}
When using `pre-commit` in CI (for example, the
[official pre-commit GitHub Action](https://github.com/marketplace/actions/pre-commit))
with `language: system`, make sure Zuban is installed in a previous step of the workflow.
```

### prek

Zuban can also be used with [prek](https://prek.j178.dev/). If you're not using the new
format (`prek.toml`), you can follow a similar local-repository setup:

```toml
[[repos]]
repo = "local"
hooks = [
    { 
        id = "zuban",
        name = "zuban",
        entry = "zuban check --config-file pyproject.toml",
        language = "system",
        pass_filenames = false
    }
]
```

The same configuration principles apply to prek: `language` specifies the execution
environment, and `pass_filenames` controls whether Zuban runs on the full project or
only on selected files.
