# Repository Overview — Dojo

A one-year, structured learning repository aimed at **quantitative developer / quant
researcher** readiness. It serves as a disciplined, public record of everything built
and learned across a week-by-week curriculum, with an emphasis on professional tooling,
tested code, and reproducibility.

> See [`README.md`](./README.md) for the goal statement and [`CLAUDE.md`](./CLAUDE.md)
> for the authoritative contributor conventions.

## Purpose & Goal

Become able to build, test, and deploy production-quality quantitative systems — the full
stack from data pipelines and statistical modeling through backtesting, risk management,
and live execution. The concrete one-year target is to ship at least one end-to-end quant
project (signal research → backtest → paper trade) and be interview-ready for quant roles.

## Curriculum Domains

| Domain | Focus |
|---|---|
| **CS Fundamentals** | Algorithms, data structures, systems thinking (daily LeetCode) |
| **Python & Tools** | Professional Python, testing, packaging, databases |
| **Quantitative Methods** | Statistics, probability, financial math, time-series |
| **Finance & Markets** | Market microstructure, factor models, portfolio construction |

## Toolchain

| Tool | Purpose |
|---|---|
| Python 3.12 | Version pinned in `.python-version` |
| `uv` | Dependency management (not pip) — see `pyproject.toml` / `uv.lock` |
| `ruff` | Lint + format (line length 88; rules `E F I UP B SIM`, `E501` ignored; double quotes) |
| `pytest` | Testing — discovers tests under `leetcode/`, repo root on `pythonpath` |
| `jupyterlab` + `jupytext` | Notebooks version-controlled as `.py` files (percent format) |
| PostgreSQL 16 | Relational database (introduced Week 9+) |
| Git + GitHub | Everything committed and public |

## Directory Layout

```
dojo/
├── leetcode/            # Daily algorithm problems, organized by pattern
│   ├── conftest.py      # Shared fixtures: make_list, list_to_vals, make_tree, tree_to_vals
│   ├── utils.py         # ListNode, TreeNode definitions
│   └── pattern/
│       └── <pattern>/
│           └── p<NNNN>_<slug>/
│               ├── solution.py        # Solution + complexity-annotated header
│               └── test_solution.py   # Examples + edge cases
├── reference/           # Cheatsheets and quick-reference docs
├── pyproject.toml       # Project + ruff + pytest configuration
├── README.md            # Program goal and structure
└── CLAUDE.md            # Contributor conventions (authoritative)
```

The `README.md` also references `weekly-notes/`, `projects/`, and `reading-notes/`
directories as part of the intended structure; these are planned and not yet populated.

## LeetCode Module — Current State

Solutions are grouped by algorithmic pattern. Each problem lives in its own package with a
`solution.py` (carrying a header documenting URL, difficulty, topics, approach, and
time/space complexity) and a `test_solution.py`.

**Patterns with solutions:**

| Pattern | Problems |
|---|---|
| Array & Hashing | Two Sum (1), Group Anagrams (49), Longest Consecutive Sequence (128), Contains Duplicate (217), Valid Anagram (242) |
| Two Pointers | Container With Most Water (11), 3Sum (15), Trapping Rain Water (42), Valid Palindrome (125), Two Sum II (167) |
| Sliding Window | Best Time to Buy and Sell Stock (121), Contains Duplicate II (219) |
| Stack | Valid Parentheses (20) |
| Prefix Sum | Subarray Sum Equals K (560) |
| Greedy | Best Time to Buy and Sell Stock II (122) |
| Dynamic Programming | Maximum Subarray (53) |
| Heap / Priority Queue | Top K Frequent Elements (347) |
| Linked List | LRU Cache (146) |

**Patterns scaffolded but not yet started:** backtracking, binary search, graphs,
intervals, math & bit manipulation, matrix, trees, trie.

### Shared test infrastructure

- `leetcode/utils.py` — `ListNode` and `TreeNode` classes used across linked-list and tree
  problems.
- `leetcode/conftest.py` — pytest fixtures for building/flattening linked lists
  (`make_list`, `list_to_vals`) and building/serializing binary trees
  (`make_tree`, `tree_to_vals`, using LeetCode level-order convention). A
  `pytest_configure` hook auto-creates `__init__.py` files so relative imports in tests
  work without manual setup.

## Common Commands

```bash
# Run the test suite
uv run pytest leetcode/

# Lint + format (run before committing)
uv run ruff check --fix .
uv run ruff format .
```

## Adding a LeetCode Solution

1. Create `leetcode/pattern/<pattern>/p<NNNN>_<slug>/solution.py` and `test_solution.py`.
2. Give `solution.py` a header: problem URL, difficulty, topics, approach, time/space
   complexity.
3. In `test_solution.py`, cover the LeetCode examples plus edge cases; use the
   `conftest.py` fixtures for linked lists and trees.
4. Verify with `uv run pytest leetcode/`.

## Conventions

- **Ruff is authoritative**: double quotes, 4-space indent, line length 88 (E501 ignored).
- Commit messages follow a conventional style, e.g.
  `feat(leetcode): solve <Problem Name> (#<number>)`.
- Notebooks are stored as jupytext `.py` files, never `.ipynb`
  (`.ipynb_checkpoints/` is gitignored).
</content>
</invoke>
