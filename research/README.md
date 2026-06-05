# Research

A workspace for exploration, notes, and discussion across quantitative and strategic
topics. Unlike `leetcode/` (drilled problems), this
is where ideas are **worked out** — derivations, experiments, half-formed arguments, and
write-ups that may later graduate into `projects/`.

## Topics

| Folder | Scope |
|---|---|
| [`math/`](./math/) | Foundations — linear algebra, calculus, probability, stochastic processes, optimization |
| [`quantitative-analysis/`](./quantitative-analysis/) | Statistics, time-series, factor models, signal research, backtesting methodology |
| [`game-theory/`](./game-theory/) | Equilibria, mechanism design, auctions, adversarial and multi-agent settings |
| [`defi/`](./defi/) | AMMs, lending, MEV, on-chain microstructure, protocol/tokenomics analysis |
| [`ai/`](./ai/) | ML/DL, RL, LLMs, and their application to research and strategy |
| [`macro-economics/`](./macro-economics/) | Monetary policy, rates, FX, business cycles, cross-asset regimes |
| [`strategy-development/`](./strategy-development/) | Idea → hypothesis → backtest → risk → execution; turning the above into trading strategies |

## How to use this folder

- One topic per subfolder; create a new `.md` (or jupytext `.py`) file per idea or thread.
- Suggested file naming: `YYYY-MM-DD-short-slug.md` for dated notes, or `topic-slug.md`
  for living documents.
- Lead each note with a one-line **question or claim** so it's scannable later.
- Math renders in GitHub-flavored markdown via `$...$` (inline) and `$$...$$` (block).
- Notebooks follow the repo convention: store as jupytext `.py` (percent format), not
  `.ipynb`.
- When a note becomes settled/reusable, promote it into a full build under `projects/`.

## Cross-cutting questions

These threads naturally span several folders — link notes across topics rather than
duplicating:

- How do macro regimes change which signals work? (`macro-economics` × `strategy-development`)
- Where does game theory explain DeFi mechanism failures and MEV? (`game-theory` × `defi`)
- When does ML beat a well-specified statistical model — and when does it just overfit?
  (`ai` × `quantitative-analysis`)
</content>
