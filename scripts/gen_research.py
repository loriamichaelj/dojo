"""Generate a docs page for every research note under ``research/``.

Mirrors ``scripts/gen_leetcode.py``: walks the research folder and emits one
page per markdown file (Research -> topic -> file), wired into the nav via
``mkdocs-gen-files`` + ``mkdocs-literate-nav``. Each file is its own page; the
content is pulled from the source with the ``include-markdown`` plugin so notes
stay single-sourced. New topics/notes appear on the site automatically.
"""

import re
from pathlib import Path

import mkdocs_gen_files
from mkdocs.structure.files import InclusionLevel

REPO_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_ROOT = REPO_ROOT / "research"

# Topic display order; folders not listed fall back to alphabetical after these.
TOPIC_ORDER = [
    "ai",
    "defi",
    "quantitative-analysis",
    "strategy-development",
    "math",
    "game-theory",
    "macro-economics",
    "poker",
]

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
# Relative markdown link targets, e.g. `](../math/)` or `](../README.md)`.
REL_LINK_RE = re.compile(r"(\]\()(\.\.?/[^)]*?)(\))")


def read_h1(path: Path, fallback: str) -> str:
    match = H1_RE.search(path.read_text())
    return match.group(1) if match else fallback


def fix_links(text: str) -> str:
    """Point folder/README cross-links at the generated index pages.

    Each topic folder becomes ``<topic>/index.md`` and each README becomes the
    folder's ``index.md``. Rewriting to real ``.md`` targets lets MkDocs resolve
    them to correct directory URLs from any page depth.
    """

    def repl(match: re.Match) -> str:
        target = match.group(2)
        if target.endswith("/"):
            target += "index.md"
        elif target.endswith("README.md"):
            target = target[: -len("README.md")] + "index.md"
        return match.group(1) + target + match.group(3)

    return REL_LINK_RE.sub(repl, text)


def humanize(slug: str) -> str:
    return slug.replace("-", " ").title()


def topic_sort_key(folder: str) -> tuple[int, str]:
    rank = TOPIC_ORDER.index(folder) if folder in TOPIC_ORDER else len(TOPIC_ORDER)
    return (rank, folder)


def include_page(doc_path: Path, source: Path) -> None:
    """Emit a docs page with the source markdown content embedded directly."""
    src_rel = source.relative_to(REPO_ROOT).as_posix()
    with mkdocs_gen_files.open(doc_path.as_posix(), "w") as page:
        page.write(fix_links(source.read_text()))
    mkdocs_gen_files.set_edit_path(doc_path.as_posix(), src_rel)


# Top-level Research overview (research/README.md).
include_page(Path("research/index.md"), RESEARCH_ROOT / "README.md")
summary_lines = ["* [Overview](index.md)\n"]

topic_dirs = sorted(
    (d for d in RESEARCH_ROOT.iterdir() if d.is_dir()),
    key=lambda d: topic_sort_key(d.name),
)
for topic_dir in topic_dirs:
    readme = topic_dir / "README.md"
    if not readme.exists():
        continue

    label = read_h1(readme, humanize(topic_dir.name))
    summary_lines.append(f"* {label}\n")

    # The topic README is the topic's overview page.
    include_page(Path("research") / topic_dir.name / "index.md", readme)
    summary_lines.append(f"    * [Overview]({topic_dir.name}/index.md)\n")

    # Then one page per note file, ordered by filename.
    for note in sorted(f for f in topic_dir.glob("*.md") if f.name != "README.md"):
        title = read_h1(note, humanize(note.stem))
        include_page(Path("research") / topic_dir.name / f"{note.stem}.md", note)
        summary_lines.append(f"    * [{title}]({topic_dir.name}/{note.stem}.md)\n")

with mkdocs_gen_files.open("research/SUMMARY.md", "w") as summary:
    summary.writelines(summary_lines)

# SUMMARY.md only feeds literate-nav; keep it out of the built site.
summary_file = mkdocs_gen_files.files.get_file_from_path("research/SUMMARY.md")
if summary_file is not None:
    summary_file.inclusion = InclusionLevel.EXCLUDED
