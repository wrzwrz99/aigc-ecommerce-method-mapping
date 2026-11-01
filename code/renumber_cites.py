# -*- coding: utf-8 -*-
"""Renumber citations so they follow the order of first appearance in the text.

SAGE Vancouver requires references to be numbered and listed in the order in
which they are first cited in the text. The current manuscript cites some
sources out of order (e.g. [23] Donthu first appears in the Discussion, [30]
Braun & Clarke appears before [27-29], the Chinese refs [47-49] appear before
[35-46]). This script rebuilds the numbering from the text order, reorders the
reference list, and rewrites every in-text citation accordingly.

Run with --write to apply; without it, a dry-run preview is printed.
"""
import re
import sys
from pathlib import Path

PATH = Path("manuscript_JIS_draft.md")
WRITE = "--write" in sys.argv

txt = PATH.read_text(encoding="utf-8")
body = txt.split("## References")[0]
refs = txt.split("## References")[1]

# 1. Parse the reference list (old number -> full entry text, no "N. ")
ref_entries = {}
for m in re.finditer(r"^(\d+)\.\s*(.*)$", refs, re.M):
    ref_entries[int(m.group(1))] = m.group(2).strip()

# 2. First appearance position of every cited number in the body
CITE_RE = re.compile(r"\[([0-9\-\s,]+)\]")
first = {}
for m in CITE_RE.finditer(body):
    for part in m.group(1).split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            for i in range(int(a), int(b) + 1):
                first.setdefault(i, m.start())
        elif part.isdigit():
            first.setdefault(int(part), m.start())

ordered = sorted(first.items(), key=lambda x: x[1])   # [(old, pos), ...]
old_to_new = {old: new for new, (old, _) in enumerate(ordered, start=1)}

# 3. Reorder the reference list
new_refs = [None] * (len(ordered) + 1)
for old, new in old_to_new.items():
    new_refs[new] = ref_entries[old]

# 4. Rewrite in-text citations
def rewrite(m):
    inner = m.group(1)
    nums = set()
    for part in inner.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            nums.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            nums.add(int(part))
    new_nums = sorted(old_to_new[n] for n in nums)
    parts, i = [], 0
    while i < len(new_nums):
        j = i
        while j + 1 < len(new_nums) and new_nums[j + 1] == new_nums[j] + 1:
            j += 1
        parts.append(f"{new_nums[i]}-{new_nums[j]}" if j > i else str(new_nums[i]))
        i = j + 1
    return "[" + ", ".join(parts) + "]"

new_body = CITE_RE.sub(rewrite, body)

# ---- report ----
print("=== old -> new mapping ===")
for old in sorted(old_to_new):
    new = old_to_new[old]
    mark = "" if old == new else "  *"
    print(f"  [{old:2d}] -> [{new:2d}]{mark}")
print()
print("=== reordered reference list (new number -> old number -> first author) ===")
for new in range(1, len(new_refs)):
    entry = new_refs[new]
    first_author = entry.split(",")[0]
    print(f"  {new:2d}. (was {ordered[new-1][0]:2d}) {first_author}")
print()
print("=== changed in-text citations ===")
changed = 0
for m in CITE_RE.finditer(body):
    new = rewrite(m)
    if new != m.group(0):
        changed += 1
        print(f"  {m.group(0)} -> {new}")
print(f"  ({changed} citations changed)")

if WRITE:
    new_txt = new_body.rstrip() + "\n\n## References\n\n" + "\n\n".join(
        f"{i}. {new_refs[i]}" for i in range(1, len(new_refs))
    )
    PATH.write_text(new_txt, encoding="utf-8")
    print("\nWROTE renumbered manuscript.")
else:
    print("\n(dry run; pass --write to apply)")
