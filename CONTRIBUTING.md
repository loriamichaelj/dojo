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

## Continuous deployment

Two workflows handle the "CD" half of the pipeline.

### Documentation site

[`.github/workflows/docs.yml`](./.github/workflows/docs.yml) builds a
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site from the repo's
markdown and publishes it to **GitHub Pages** on every push to `main` that touches
docs-relevant files (and on manual `workflow_dispatch`). The site is single-sourced:
pages under `docs/` use the `include-markdown` plugin to pull in the existing
`README.md`, `research/`, and `reference/` notes, so there's nothing to
keep in sync by hand. The build runs `mkdocs build --strict`, so a structural problem
fails the deploy.

Build and preview locally:

```bash
uv sync --frozen --only-group docs
uv run mkdocs serve          # live preview at http://127.0.0.1:8000
uv run mkdocs build --strict # same build CI runs
```

**One-time setup (admin only):** GitHub Pages source must be set to *GitHub Actions*.
**Settings → Pages → Build and deployment → Source → GitHub Actions.** Until that's
set, the `deploy` job will fail. The site publishes to
`https://loriamichaelj.github.io/dojo/`.

### Releases

[`.github/workflows/release.yml`](./.github/workflows/release.yml) runs when you push a
version tag matching `v*`. It re-runs the full CI gate (ruff lint, ruff format check,
pytest) so a tag can only ship from a green tree, then creates a GitHub Release with
auto-generated notes. Tags containing a hyphen (e.g. `v0.2.0-rc1`) are marked as
pre-releases.

Cut a release:

```bash
git tag v0.2.0
git push origin v0.2.0
```

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
