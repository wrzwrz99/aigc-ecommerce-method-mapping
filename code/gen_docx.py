# -*- coding: utf-8 -*-
"""Build the SAGE double-spaced Word draft from the Markdown source.

Markdown conventions understood here:
  # Title                      -> centred bold title
  ## Section                   -> bold heading
  ### Subsection               -> bold italic heading
  | a | b |                     -> table (first row is the header)
  **Keywords:** ...            -> keywords line
  ![Figure N. caption](path)   -> centred image + a standalone caption
  [n], [n, m], [n-m]           -> plain text (Vancouver numeric citations)

Figures are embedded in the Word draft so the manuscript reads as a complete
document. For submission, SAGE asks that figures created outside Word be
uploaded separately (EPS/PDF) with a placeholder note in the running text;
the PDF counterparts in figures/ are supplied for that purpose.
"""
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

SRC = "manuscript_JIS_draft.md"
if not Path(SRC).exists() and Path("manuscript/manuscript.md").exists():
    # Repository layout: the source lives in manuscript/, figures/ one level up
    SRC = "manuscript/manuscript.md"
OUT = "Methodological_Approaches_AIGC_EC_JIS.docx"
if SRC.startswith("manuscript/"):
    OUT = "manuscript/" + OUT

MD_DIR = Path(SRC).resolve().parent
IMG_RE = re.compile(r"^!\[(.*)\]\((.*)\)\s*$")
FIG_CAPTION_RE = re.compile(r"^(Figure\s+\d+\.)(.*)$", re.S)


def resolve_image(rel):
    """Resolve an image path relative to the Markdown file, its parent folder
    (the repository layout keeps figures/ one level up), or the working dir."""
    for base in (MD_DIR, MD_DIR.parent, Path.cwd()):
        cand = base / rel
        if cand.exists():
            return cand
    return None


doc = Document()

# Default style: Times New Roman 12 pt, double spaced
style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(12)
style.element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")


def set_double(p):
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)


def add_runs(p, text):
    """Parse **bold** and *italic* inline markers."""
    token_re = re.compile(r"(\*\*.*?\*\*|\*.*?\*)")
    pos = 0
    for m in token_re.finditer(text):
        if m.start() > pos:
            p.add_run(text[pos:m.start()])
        tok = m.group(0)
        if tok.startswith("**"):
            r = p.add_run(tok[2:-2])
            r.bold = True
        else:
            r = p.add_run(tok[1:-1])
            r.italic = True
        pos = m.end()
    if pos < len(text):
        p.add_run(text[pos:])


def add_body(text, indent=False):
    p = doc.add_paragraph()
    set_double(p)
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)
    add_runs(p, text)
    return p


def add_heading1(text):
    p = doc.add_paragraph()
    set_double(p)
    r = p.add_run(text)
    r.bold = True
    return p


def add_heading2(text):
    p = doc.add_paragraph()
    set_double(p)
    r = p.add_run(text)
    r.bold = True
    r.italic = True
    return p


def add_table(rows):
    ncol = len(rows[0])
    tbl = doc.add_table(rows=len(rows), cols=ncol)
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = tbl.cell(i, j)
            c.text = ""
            p = c.paragraphs[0]
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_after = Pt(0)
            add_runs(p, cell)
            for r in p.runs:
                r.font.size = Pt(11)
                if i == 0:
                    r.bold = True
    sp = doc.add_paragraph()
    set_double(sp)


def add_figure(caption, rel):
    """Embed the image centred and add a standalone, double-spaced caption."""
    img = resolve_image(rel)
    if img is None:
        print(f"[warn] image not found: {rel}")
        add_body(f"[Figure image missing: {rel}]")
        return 0

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(str(img), width=Inches(6.3))

    cp = doc.add_paragraph()
    set_double(cp)
    cp.paragraph_format.space_before = Pt(2)
    cp.paragraph_format.space_after = Pt(8)
    m = FIG_CAPTION_RE.match(caption)
    if m:
        r = cp.add_run(m.group(1))
        r.bold = True
        r.font.size = Pt(11)
        r2 = cp.add_run(m.group(2))
        r2.font.size = Pt(11)
    else:
        r = cp.add_run(caption)
        r.font.size = Pt(11)
    print(f"embedded {rel} -> {img.name}")
    return 1


lines = open(SRC, encoding="utf-8").read().split("\n")

i = 0
in_refs = False
n_fig = 0
while i < len(lines):
    line = lines[i].rstrip()
    if not line.strip():
        i += 1
        continue

    # Title
    if line.startswith("# ") and not line.startswith("## "):
        t = doc.add_paragraph()
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_double(t)
        r = t.add_run(line[2:].strip())
        r.bold = True
        r.font.size = Pt(14)
        i += 1
        continue

    if line.startswith("## "):
        add_heading1(line[3:].strip())
        i += 1
        continue

    if line.startswith("### "):
        add_heading2(line[4:].strip())
        i += 1
        continue

    # Table: collect consecutive | rows
    if line.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            raw = lines[i].strip().strip("|")
            cells = [c.strip() for c in raw.split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                i += 1
                continue
            rows.append(cells)
            i += 1
        add_table(rows)
        continue

    # Figure: ![caption](path)
    m = IMG_RE.match(line)
    if m:
        n_fig += add_figure(m.group(1).strip(), m.group(2).strip())
        i += 1
        continue

    # Keywords line
    if line.startswith("**Keywords:**"):
        p = doc.add_paragraph()
        set_double(p)
        r = p.add_run("Keywords: ")
        r.bold = True
        add_runs(p, line[len("**Keywords:**"):].strip())
        i += 1
        continue

    if line.startswith("## References"):
        add_heading1("References")
        in_refs = True
        i += 1
        continue

    add_body(line, indent=(not in_refs))
    i += 1

doc.save(OUT)
print(f"saved {OUT} (embedded {n_fig} figures)")
