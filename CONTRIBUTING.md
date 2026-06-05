# Contributing

Workflow and automation notes for this repo. For curriculum structure, toolchain, and
code-style rules, see [`CLAUDE.md`](./CLAUDE.md).

## Local checks before pushing

Run the same checks CI runs, from the repo root:

```bash
uv sync --frozen
uv run ruff check .          # lint
uv run ruff format --check . # formatting (use `ruff format .` to fix)
uv run pytest leetcode/      # tests
```

## Continuous integration

[`.github/workflows/ci.yml`](./.github/workflows/ci.yml) runs on every push and pull
request to `main`. The single `Lint & test` job (Ubuntu, Python pinned via
`.python-version`) installs deps with `uv sync --frozen`, then runs ruff lint, ruff
format check, and pytest. Superseded runs on the same ref are cancelled automatically.

## Dependency updates

[`.github/dependabot.yml`](./.github/dependabot.yml) opens grouped version-update PRs
weekly:

- **GitHub Actions** — all action bumps batched into one PR (`ci:` prefix).
- **Python (uv)** — `pyproject.toml` + `uv.lock`; dev tooling (ruff, pytest) grouped
  together (`deps:` prefix).

Dependabot PRs run through the same CI as everything else.

## Branch protection (one-time, admin only)

CI and Dependabot are committed to the repo, but **branch protection is a GitHub
repository setting and must be enabled in the web UI** — it can't be set from a config
file. Enable it once:

**Settings → Branches → Add branch ruleset** (or *Add classic branch protection rule*):

1. **Branch name pattern:** `main`
2. ☑ **Require a pull request before merging** (approvals: `0` is fine for a solo repo).
3. ☑ **Require status checks to pass before merging**
   - ☑ Require branches to be up to date before merging
   - Add the required check: **`Lint & test`** (the job name from `ci.yml`; it only
     appears in the search box after CI has run at least once).
4. *(Optional)* ☑ **Do not allow bypassing the above settings** to enforce it for admins
   too.
5. **Save changes.**

**Optional —** *Settings → General → Pull Requests → ☑ Allow auto-merge* lets a PR merge
itself once `Lint & test` passes, instead of merging by hand.
