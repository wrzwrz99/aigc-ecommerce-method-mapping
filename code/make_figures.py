# -*- coding: utf-8 -*-
"""Generate all figures for the JIS manuscript in SAGE/Journal of Information
Science style.

Style basis (verified against SAGE artwork guidelines and the JIS submission
guidelines, 1 November 2026):
  * 300 dpi minimum for figures containing text/labels; line art is supplied
    here at 600 dpi. PDF is vector, with TrueType fonts embedded (editable).
  * Figures are published in colour online but in black and white in print, so
    every category is distinguished by greyscale shade AND hatching, and no
    caption uses colour words.
  * Sans-serif lettering (Arial), 8 pt, kept consistent across all figures.
  * Double column width (170 mm / 6.69 in) because the labels are long.
  * No title inside the image; captions are written in the manuscript and must
    stand alone (n, source, exclusions, hatching key).

Layout follows the ssci-figure skill's 'sage' preset (scripts/ssci_style.py,
copied next to this file so the repository is self-contained).

Figures
-------
  Figure 1  PRISMA 2020 flow diagram (identification / screening / eligibility /
            inclusion), 1,449 -> 187 articles.
  Figure 2  Annual number of articles by method category, 2015-2026, stacked
            bars from zero.
  Figure 3  The eight journals with seven or more articles (sorted horizontal
            bars from zero). Three journals tie at six articles, so a "top ten"
            cut would be arbitrary at the boundary; the >=7 threshold matches
            the eight outlets enumerated in Section 4.4 of the manuscript.

The citation regression is intentionally NOT plotted: it yields only two
comparable method-category coefficients (plus a log-age term on a different
scale), and the ssci-figure selection guide advises against a figure for two
or three coefficients when a table already reports them. See Table 5.

Usage
-----
    py -3.10 _make_figures.py

Data are read from openalex_ssci_q12_clean.csv, searched next to this script,
in ./data/ or in ../data/ so the same file works both in the working folder and
in the reproducibility repository.
"""
from pathlib import Path
import sys
import textwrap

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Patch

import ssci_style as S

S.apply_style(preset="sage", width="double")


# --------------------------------------------------------------------------
# Locate data and output folder
# --------------------------------------------------------------------------
def find_data() -> Path:
    for p in (
        HERE / "openalex_ssci_q12_clean.csv",
        HERE / "data" / "openalex_ssci_q12_clean.csv",
        HERE.parent / "data" / "openalex_ssci_q12_clean.csv",
    ):
        if p.exists():
            return p
    raise FileNotFoundError("openalex_ssci_q12_clean.csv not found")


DATA = find_data()
ROOT = DATA.parent.parent if DATA.parent.name == "data" else DATA.parent
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, encoding="utf-8-sig")
df["year"] = df["year"].astype(int)
CATS = ["quantitative", "conceptual", "computational", "qualitative"]

# Greyscale + hatching: readable in black-and-white print (SAGE requirement)
CAT = {
    "quantitative":  dict(color="#3D3D3D", hatch="",     label="Quantitative empirical"),
    "conceptual":    dict(color="#9C9C9C", hatch="///",  label="Conceptual/review"),
    "computational": dict(color="#DEDEDE", hatch="\\\\\\", label="Computational"),
    "qualitative":   dict(color="#FFFFFF", hatch="xxxx", label="Qualitative"),
}
EDGE = "#222222"


def save_both(fig, stem, dpi=600):
    """Save exact-size PDF (vector) + PNG (high-res line art), no tight bbox so
    the physical width stays at the target journal dimension."""
    try:
        fig.tight_layout()
    except Exception:
        pass
    for ext in ("pdf", "png"):
        p = OUT / f"{stem}.{ext}"
        fig.savefig(p, dpi=dpi, format=ext)
        print(f"wrote {p}")
    plt.close(fig)


# ==========================================================================
# Figure 1 - PRISMA 2020 flow diagram
# ==========================================================================
def draw_box(ax, x, y, w, h, text, face="#F2F2F2", lw=0.8, fs=8.0, bold=False):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=face, edgecolor=EDGE, linewidth=lw, zorder=2,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, fontweight="bold" if bold else "normal",
            linespacing=1.28, zorder=3)


def v_arrow(ax, x, y_from, y_to):
    ax.annotate("", xy=(x, y_to), xytext=(x, y_from),
                arrowprops=dict(arrowstyle="-|>", color=EDGE, lw=0.8,
                                shrinkA=0, shrinkB=0, mutation_scale=9),
                zorder=1)


def h_arrow(ax, x_from, x_to, y):
    ax.annotate("", xy=(x_to, y), xytext=(x_from, y),
                arrowprops=dict(arrowstyle="-|>", color=EDGE, lw=0.8,
                                shrinkA=0, shrinkB=0, mutation_scale=9),
                zorder=1)


def figure1_prisma():
    fig, ax = plt.subplots(figsize=(6.69, 8.7))
    ax.set_xlim(0, 12.4)
    ax.set_ylim(0.7, 14.4)
    ax.axis("off")

    MX, MW = 2.05, 5.05          # main-flow boxes  -> right edge 7.10
    EX, EW = 7.85, 4.25          # exclusion boxes  -> left edge 7.85
    CX = MX + MW / 2             # centre of main column = 4.575
    EH = 1.30                    # exclusion box height

    # Main boxes: (bottom y, height, text, face, bold, fontsize)
    boxes = [
        (12.55, 1.25,
         "Records identified from OpenAlex\n20 queries, 1 Jan 2015 to 1 Nov 2026\n(n = 1,449 unique records, deduplicated)",
         "#EDEDED", False, 8.0),
        (10.85, 1.05,
         "Records screened: type and title checks\n(n = 1,449)", "#F5F5F5", False, 8.0),
        (9.15, 1.05,
         "Records retained after type/title checks\n(n = 1,205)", "#F5F5F5", False, 8.0),
        (7.15, 1.25,
         "Records assessed for eligibility\n(title and abstract, three topic criteria)\n(n = 261)",
         "#F5F5F5", False, 8.0),
        (5.35, 1.05,
         "Eligible records\n(n = 238)", "#F5F5F5", False, 8.0),
        (3.65, 1.05,
         "Records in SSCI Q1/Q2 journals\n(n = 205)", "#F5F5F5", False, 8.0),
        (1.45, 1.25,
         "Articles included in the review\n(n = 187)", "#D9D9D9", True, 9.0),
    ]
    tops, bottoms = [], []
    for y, h, txt, face, bold, fs in boxes:
        draw_box(ax, MX, y, MW, h, txt, face=face, bold=bold, fs=fs)
        bottoms.append(y)
        tops.append(y + h)

    # Vertical arrows between consecutive main boxes
    for i in range(len(boxes) - 1):
        v_arrow(ax, CX, bottoms[i], tops[i + 1])

    # Exclusion boxes, aligned to the centre of the box being filtered
    exclusions = [
        (1, "Excluded (n = 244)\nPreprints, predatory or non-reviewed\noutlets, conference proceedings,\nmissing journal title"),
        (2, "Excluded (n = 944)\nOutside the peer-reviewed Scopus/WoS\njournal whitelist"),
        (3, "Excluded (n = 23)\nDid not meet all three topic criteria\n(technology, setting, user behavior)"),
        (4, "Excluded (n = 33)\nNot in an SSCI Q1/Q2 journal"),
        (5, "Excluded (n = 18)\nCompanion or non-SSCI outlets\n(JCR verification pass)"),
    ]
    for idx, txt in exclusions:
        cy = bottoms[idx] + boxes[idx][1] / 2
        draw_box(ax, EX, cy - EH / 2, EW, EH, txt, face="#FFFFFF", lw=0.7, fs=7.3)
        h_arrow(ax, MX + MW, EX, cy)

    # Stage labels down the left margin
    stages = [
        (12.55, 1.25, "Identification"),
        (9.15, 2.75, "Screening"),
        (7.15, 1.25, "Eligibility"),
        (1.45, 4.95, "Inclusion"),
    ]
    for y, h, label in stages:
        ax.add_patch(Rectangle((0.30, y), 0.52, h, facecolor="#E2E2E2",
                               edgecolor=EDGE, linewidth=0.6, zorder=1))
        ax.text(0.56, y + h / 2, label, ha="center", va="center",
                rotation=90, fontsize=8.2, fontweight="bold", zorder=3)

    save_both(fig, "Figure1_PRISMA")


# ==========================================================================
# Figure 2 - annual stacked bar chart by method category
# ==========================================================================
def figure2_annual():
    ct = pd.crosstab(df["year"], df["paradigm"]).reindex(columns=CATS, fill_value=0)
    years = [int(y) for y in ct.index.tolist()]      # years with >=1 article
    totals = ct.sum(axis=1).values.astype(int)
    x = np.arange(len(years))

    fig, ax = S.figure("double", height=3.7)
    bottom = np.zeros(len(years), dtype=float)
    for cat in CATS:
        vals = ct[cat].reindex(years, fill_value=0).values.astype(float)
        ax.bar(x, vals, bottom=bottom, width=0.62,
               color=CAT[cat]["color"], edgecolor=EDGE, linewidth=0.6,
               hatch=CAT[cat]["hatch"], label=CAT[cat]["label"], zorder=3)
        bottom += vals

    for xi, tot in zip(x, totals):
        ax.text(xi, tot + 1.8, str(tot), ha="center", va="bottom",
                fontsize=7.2, color="#222222", zorder=4)

    ax.set_xticks(x)
    ax.set_xticklabels([str(y) for y in years])
    ax.set_xlabel("Publication year")
    ax.set_ylabel("Number of articles")
    ax.set_ylim(0, max(totals) + 12)
    ax.set_xlim(-0.6, len(years) - 0.4)
    S.style_axes(ax, grid="y")
    ax.tick_params(axis="x", length=2.5)

    handles = [
        Patch(facecolor=CAT[c]["color"], edgecolor=EDGE, linewidth=0.6,
              hatch=CAT[c]["hatch"], label=CAT[c]["label"])
        for c in CATS
    ]
    ax.legend(handles=handles, loc="upper left", ncol=2, frameon=False,
              handlelength=1.6, columnspacing=1.2)

    print(f"[Figure 2] years={years}")
    print(f"[Figure 2] totals={totals.tolist()}  sum={int(totals.sum())}")
    save_both(fig, "Figure2_annual_methods")


# ==========================================================================
# Figure 3 - most frequent journals (sorted horizontal bars)
# ==========================================================================
JLABEL = {
    "Journal of theoretical and applied electronic commerce research":
        "Journal of Theoretical and Applied\nElectronic Commerce Research",
    "Journal of Retailing and Consumer Services":
        "Journal of Retailing and\nConsumer Services",
    "Journal of the Association for Information Systems":
        "Journal of the Association for\nInformation Systems",
    "Journal of Consumer Behaviour": "Journal of Consumer Behaviour",
    "Frontiers in Psychology": "Frontiers in Psychology",
    "Decision Support Systems": "Decision Support Systems",
    "International Journal of Human-Computer Interaction":
        "International Journal of Human-\nComputer Interaction",
    "Electronic Commerce Research and Applications":
        "Electronic Commerce Research\nand Applications",
    "Behavioral Sciences": "Behavioral Sciences",
    "Asia Pacific Journal of Marketing and Logistics":
        "Asia Pacific Journal of Marketing\nand Logistics",
}


# Explicit order: identical to the eight outlets listed in Section 4.4. Counts
# are still read from the data, but the order is fixed so the figure is stable
# and directly comparable with the text.
ORDER8 = [
    "Journal of theoretical and applied electronic commerce research",   # 34
    "Journal of Retailing and Consumer Services",                          # 28
    "Journal of the Association for Information Systems",                  # 14
    "Journal of Consumer Behaviour",                                        # 13
    "Frontiers in Psychology",                                              # 10
    "Decision Support Systems",                                             # 8
    "International Journal of Human-Computer Interaction",                  # 7
    "Electronic Commerce Research and Applications",                        # 7
]


def figure3_journals():
    vc = df["journal"].value_counts()
    missing = [j for j in ORDER8 if j not in vc.index]
    if missing:
        raise SystemExit(f"[Figure 3] journal labels not found in corpus: {missing}")
    names = ORDER8
    counts = np.array([int(vc[j]) for j in ORDER8])
    assert (counts >= 7).all(), "all plotted journals must have >=7 articles"
    y = np.arange(len(names))[::-1]        # largest on top

    fig, ax = S.figure("double", height=4.3)
    ax.barh(y, counts, height=0.62, color="#8A8A8A", edgecolor=EDGE,
            linewidth=0.6, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels([JLABEL.get(n, textwrap.fill(str(n), 34)) for n in names])
    ax.tick_params(axis="y", length=0)
    for yi, c in zip(y, counts):
        ax.text(c + 0.6, yi, str(c), ha="left", va="center",
                fontsize=7.6, color="#222222", zorder=4)
    ax.set_xlabel("Number of articles")
    ax.set_xlim(0, int(max(counts)) + 6)
    S.style_axes(ax, grid="x")
    ax.tick_params(axis="x", length=2.5)

    print(f"[Figure 3] 8 journals (>=7 articles) sum={int(counts.sum())} of "
          f"{len(df)} articles; journals in corpus={df['journal'].nunique()}")
    save_both(fig, "Figure3_top_journals")


if __name__ == "__main__":
    print(f"data: {DATA}")
    print(f"output: {OUT}")
    print(f"corpus: {len(df)} articles, {df['paradigm'].value_counts().to_dict()}")
    figure1_prisma()
    figure2_annual()
    figure3_journals()
    print("done")
