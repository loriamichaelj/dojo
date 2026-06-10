# Overview

Original long-form writing — essays, articles, and write-ups meant to be read,
not just filed. Where `research/` is where ideas are worked out, this is where
they're shaped into something finished. Each piece is a single markdown file;
lead with a one-line hook so it stays scannable later.

## Sections

| Folder | Scope |
|---|---|
| [`articles/`](./articles/) | Essays, articles, and standalone long-form pieces |

## How to use this folder

- One section per subfolder; create a new `.md` file per piece.
- Suggested file naming: `slug.md`, or `YYYY-MM-DD-slug.md` for dated pieces.

## Article file structure

Each piece follows the same structure: the **title** as the H1, a short metadata
table, then the body.

```markdown
# Title

| | |
|---|---|
| **Published** | YYYY-MM-DD |

A short standfirst or one-line summary, then the body.
```

The H1 title doubles as the page's title and nav label.
