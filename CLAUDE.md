# Dojo

One-year structured learning repo targeting quantitative developer / researcher readiness.

## Curriculum domains

1. **CS Fundamentals** — algorithms, data structures, daily LeetCode
2. **Python & Tools** — professional Python, testing, packaging, databases
3. **Quantitative Methods** — statistics, probability, financial math, time-series
4. **Finance & Markets** — microstructure, factor models, portfolio construction

## Toolchain

| Tool | Purpose |
|------|---------|
| `uv` | Dependency management (not pip) |
| `ruff` | Lint + format (line length 88, rules: E F I UP B SIM) |
| `pytest` | Testing — run from repo root |
| `jupyterlab` + `jupytext` | Notebooks stored as `.py` files |
| PostgreSQL 16 | Database (Week 9+) |

Python version: **3.12** (pinned in `.python-version`).

## Directory layout

```
leetcode/
  conftest.py           # shared fixtures: make_list, list_to_vals, make_tree, tree_to_vals
  utils.py              # ListNode, TreeNode
  pattern/
    <pattern-name>/
      p<NNNN>_<slug>/
        solution.py
        test_solution.py
weekly-notes/           # weekly progress logs
projects/               # capstone / end-to-end quant projects
reading-notes/          # book and paper notes
```

## Adding a LeetCode solution

1. Create `leetcode/pattern/<pattern>/p<NNNN>_<slug>/solution.py` and `test_solution.py`.
2. `solution.py` header: problem URL, difficulty, topics, approach, time/space complexity.
3. `test_solution.py`: cover the LeetCode examples plus edge cases; use fixtures from `conftest.py` for linked lists and trees.
4. Run `pytest leetcode/` to verify.

## Running tests

```bash
uv run pytest leetcode/
```

Pytest is configured (in `pyproject.toml`) to discover tests under `leetcode/` with `.` on the Python path.

## Code style

Ruff is authoritative. Double quotes, 4-space indent, no line-length errors (E501 ignored). Format before committing:

```bash
uv run ruff check --fix .
uv run ruff format .
```

## Notebooks

Store notebooks as jupytext `.py` files (percent format), not `.ipynb`. `.ipynb_checkpoints/` is gitignored.

## SSH GitHub setup

How to generate a new SSH key and connect to GitHub for `git push`.

### 1. Generate a new ED25519 key

```bash
ssh-keygen -t ed25519 -C "loriamichaelj"
```

- Accept the default file path (`~/.ssh/id_ed25519`)
- Press Enter twice for no passphrase

### 2. Copy the public key to your clipboard

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

### 3. Add the key to GitHub

1. Go to **github.com → Settings → SSH and GPG keys**
2. Click **New SSH key**
3. Title: e.g. `MacBook`
4. Key type: **Authentication Key**
5. Paste the key and click **Add SSH key**

### 4. Load the key into the SSH agent

```bash
ssh-add ~/.ssh/id_ed25519
```

### 5. Test the connection

```bash
ssh -T git@github.com
# Hi loriamichaelj! You've successfully authenticated...
```

### 6. Push

```bash
git push
```

### Notes

- The `-C` flag is just a label — it doesn't affect which GitHub account the key connects to.
- If you see `Permission denied (publickey)`, your key isn't loaded — run `ssh-add` again.
- To check loaded keys: `ssh-add -l`
