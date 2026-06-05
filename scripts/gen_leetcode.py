"""Generate a docs page for every LeetCode solution under ``leetcode/pattern/``.

Run automatically by the ``mkdocs-gen-files`` plugin during the docs build. It
walks the pattern tree, emits one page per problem (embedding ``solution.py``),
writes an overview table, and produces a ``SUMMARY.md`` that
``mkdocs-literate-nav`` turns into the "1337" nav subtree. New solutions show up
on the site automatically — no manual nav edits required.
"""

import re
from pathlib import Path

import mkdocs_gen_files
from mkdocs.structure.files import InclusionLevel

REPO_ROOT = Path(__file__).resolve().parent.parent
PATTERN_ROOT = REPO_ROOT / "leetcode" / "pattern"
GH_BLOB = "https://github.com/loriamichaelj/dojo/blob/main"

PROB_DIR_RE = re.compile(r"^p(\d+)_(.+)$")
HEADER_TITLE_RE = re.compile(r"^#\s*(\d+)\.\s*(.+?)\s*$", re.MULTILINE)
ROMAN = {"ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}


def humanize(slug: str) -> str:
    words = []
    for word in slug.split("_"):
        words.append(word.upper() if word in ROMAN else word.title())
    return " ".join(words)


def meta_field(code: str, key: str) -> str | None:
    match = re.search(rf"^#\s*{key}:\s*(.+)$", code, re.MULTILINE)
    return match.group(1).strip() if match else None


nav = mkdocs_gen_files.Nav()
nav["Overview"] = "index.md"

rows: list[tuple[int, str, str, str, str]] = []

for pattern_dir in sorted(p for p in PATTERN_ROOT.iterdir() if p.is_dir()):
    pattern_label = humanize(pattern_dir.name)
    problem_dirs = sorted(
        d
        for d in pattern_dir.iterdir()
        if d.is_dir() and (d / "solution.py").exists()
    )
    for prob_dir in problem_dirs:
        dir_match = PROB_DIR_RE.match(prob_dir.name)
        if not dir_match:
            continue

        sol_path = prob_dir / "solution.py"
        code = sol_path.read_text()
        rel_src = sol_path.relative_to(REPO_ROOT).as_posix()

        header = HEADER_TITLE_RE.search(code)
        if header:
            number, name = int(header.group(1)), header.group(2)
        else:
            number, name = int(dir_match.group(1)), humanize(dir_match.group(2))
        title = f"{number}. {name}"

        difficulty = meta_field(code, "Difficulty") or "—"
        topics = meta_field(code, "Topics")
        url = meta_field(code, "URL")

        doc_path = Path("leetcode") / pattern_dir.name / f"{prob_dir.name}.md"
        with mkdocs_gen_files.open(doc_path, "w") as page:
            page.write(f"# {title}\n\n")
            badges = [f"**Pattern:** {pattern_label}", f"**Difficulty:** {difficulty}"]
            if topics:
                badges.append(f"**Topics:** {topics}")
            page.write("  \n".join(badges) + "\n\n")
            links = []
            if url:
                links.append(f"[Problem on LeetCode]({url})")
            links.append(f"[Source on GitHub]({GH_BLOB}/{rel_src})")
            page.write(" · ".join(links) + "\n\n")
            page.write("```python\n")
            page.write(code.rstrip("\n") + "\n")
            page.write("```\n")
        mkdocs_gen_files.set_edit_path(doc_path, rel_src)

        nav_target = f"{pattern_dir.name}/{prob_dir.name}.md"
        nav[(pattern_label, title)] = nav_target
        rows.append((number, name, pattern_label, difficulty, nav_target))

with mkdocs_gen_files.open("leetcode/index.md", "w") as index:
    index.write("# 1337\n\n")
    index.write(
        f"Every solved problem from [`leetcode/pattern/`]({GH_BLOB}/leetcode/pattern), "
        f"grouped by pattern in the sidebar. **{len(rows)} solved** so far.\n\n"
    )
    index.write("| # | Problem | Pattern | Difficulty |\n")
    index.write("|---|---------|---------|------------|\n")
    for number, name, pattern_label, difficulty, target in sorted(rows):
        index.write(f"| {number} | [{name}]({target}) | {pattern_label} | {difficulty} |\n")

with mkdocs_gen_files.open("leetcode/SUMMARY.md", "w") as summary:
    summary.writelines(nav.build_literate_nav())

# SUMMARY.md exists only to feed mkdocs-literate-nav. Exclude it from the built
# site: literate-nav still reads excluded files to build the nav, but MkDocs
# won't render it as an orphan page.
summary_file = mkdocs_gen_files.files.get_file_from_path("leetcode/SUMMARY.md")
if summary_file is not None:
    summary_file.inclusion = InclusionLevel.EXCLUDED
