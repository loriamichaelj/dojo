# Dojo

## Curriculum domains

1. **CS Fundamentals** — algorithms, data structures, daily LeetCode
2. **Python & Tools** — professional Python, testing, packaging, databases
3. **Quantitative Methods** — statistics, probability, financial math, time-series
4. **Finance & Markets** — microstructure, factor models, portfolio construction

## Toolchain

| Tool | Purpose |
|---|---|
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
research/               # research notes by domain (AI, DeFi, quant, strategy, math, macro, game theory, poker)
books/                  # reading notes by shelf (fiction, non-fiction)
projects/               # capstone / end-to-end quant projects (planned)
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
