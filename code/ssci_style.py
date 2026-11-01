"""Shared publication style for SSCI / social-science journal figures.

Import from the other scripts in this directory:

    import ssci_style as S
    S.apply_style(preset="elsevier", width="single")
    fig, ax = S.figure(width="single", height=2.2)
    ...
    S.save(fig, "out/figure1")

Nothing here imports seaborn; matplotlib alone keeps the dependency tree small
and the output reproducible.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

# --------------------------------------------------------------------------
# Physical sizes
# --------------------------------------------------------------------------
# Journal column widths, in inches. These are the *typical* constraints; the
# authoritative number is always the target journal's own artwork guidelines.
# Sizes below are the common cases in social-science publishing.
WIDTHS = {
    # Generic, safe defaults (Wiley / Springer / SAGE single column)
    "single": 3.35,   # 85 mm
    "onehalf": 4.49,  # 114 mm
    "double": 6.69,   # 170 mm
    # Elsevier artwork guidelines
    "elsevier-single": 3.54,   # 90 mm
    "elsevier-1.5": 5.51,      # 140 mm
    "elsevier-double": 7.48,   # 190 mm
    # Wiley
    "wiley-single": 3.35,      # 85 mm
    "wiley-double": 7.09,      # 180 mm
    # Taylor & Francis
    "tandf-single": 3.15,      # 80 mm
    "tandf-double": 6.50,      # 165 mm
    # APA 7th: text block is 6.5 in wide, figures may span it
    "apa": 6.50,
    # Internal / presentation only. Never submit a 9-inch-wide figure.
    "slide": 9.00,
}

# --------------------------------------------------------------------------
# Colour
# --------------------------------------------------------------------------
# Okabe-Ito: eight hues, distinguishable under the three common types of
# colour-vision deficiency and in greyscale print. This is the default because
# reviewers and print readers both see these figures.
OKABE_ITO = [
    "#000000",  # black
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#F0E442",  # yellow
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#CC79A7",  # reddish purple
]

# Viridis sampled to 8 steps, for ordered / continuous categories.
VIRIDIS_8 = [
    "#440154", "#46327e", "#365c8d", "#277f8e",
    "#1fa187", "#4ac16d", "#a0da39", "#fde725",
]

# Two-tone emphasis used by most SSCI papers: one accent + neutral grey.
ACCENT_GREY = ["#0072B2", "#B0B0B0"]


def palette(n: int | None = None, kind: str = "okabe-ito") -> list[str]:
    """Return a colour list of length ``n`` (cycled if longer than the base)."""
    base = {
        "okabe-ito": OKABE_ITO,
        "viridis": VIRIDIS_8,
        "accent-grey": ACCENT_GREY,
    }.get(kind)
    if base is None:
        raise ValueError(f"unknown palette kind: {kind!r}")
    if n is None:
        return list(base)
    if n <= 0:
        return []
    out: list[str] = []
    while len(out) < n:
        out.extend(base)
    return out[:n]


# --------------------------------------------------------------------------
# Journal presets
# --------------------------------------------------------------------------
# base   : base font size in pt (body text of the figure, not the caption)
# family : preferred font families, first available wins
# sans   : True  -> use the sans family
# spines : which axis spines to keep
PRESETS = {
    # Elsevier (most SSCI journals in economics / management / education)
    "elsevier": dict(base=8, family=["Arial", "Helvetica", "DejaVu Sans"], sans=True),
    # Wiley (many sociology / political science / public admin journals)
    "wiley": dict(base=8, family=["Arial", "Helvetica", "DejaVu Sans"], sans=True),
    # SAGE ( sociology, political science, criminology )
    "sage": dict(base=8, family=["Arial", "Helvetica", "DejaVu Sans"], sans=True),
    # APA 7th: Times New Roman, figure text may be sans but must be consistent
    "apa": dict(base=9, family=["Times New Roman", "DejaVu Serif"], sans=False),
    # Taylor & Francis
    "tandf": dict(base=8, family=["Arial", "Helvetica", "DejaVu Sans"], sans=True),
    # Neutral / fallback, safe everywhere
    "default": dict(base=8, family=["DejaVu Sans"], sans=True),
}

# Windows and macOS CJK fonts, used only when a label contains CJK characters.
CJK_CANDIDATES = [
    "Microsoft YaHei", "SimHei", "Source Han Sans SC", "Noto Sans CJK SC",
    "PingFang SC", "Heiti SC", "WenQuanYi Micro Hei",
]


def _first_available(candidates: Iterable[str]) -> str | None:
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in candidates:
        if name in installed:
            return name
    return None


def apply_style(
    preset: str = "elsevier",
    width: str | int | float = "single",
    base_size: float | None = None,
    cjk: bool = False,
) -> None:
    """Set global rcParams for a journal-style figure.

    Parameters
    ----------
    preset
        Key of ``PRESETS``.
    width
        Key of ``WIDTHS`` or an explicit width in inches (only used to scale
        tick/label sizes sensibly; figure creation is separate).
    base_size
        Override the preset's base font size.
    cjk
        Also register a CJK font so Chinese labels render instead of tofu.
    """
    cfg = PRESETS.get(preset)
    if cfg is None:
        raise ValueError(f"unknown preset {preset!r}; choose from {sorted(PRESETS)}")

    size = base_size if base_size is not None else cfg["base"]
    family = _first_available(cfg["family"]) or "DejaVu Sans"

    rc = {
        "font.family": "sans-serif" if cfg["sans"] else "serif",
        "font.sans-serif": [family, "DejaVu Sans"],
        "font.serif": [family, "DejaVu Serif"],
        "font.size": size,
        "axes.labelsize": size,
        "axes.titlesize": size,
        "xtick.labelsize": size - 1,
        "ytick.labelsize": size - 1,
        "legend.fontsize": size - 1,
        "legend.frameon": False,
        "figure.dpi": 150,          # on-screen preview only
        "savefig.dpi": 300,         # submission default
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#333333",
        "axes.labelcolor": "#000000",
        "text.color": "#000000",
        "xtick.color": "#333333",
        "ytick.color": "#333333",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "lines.linewidth": 1.0,
        "lines.markersize": 4,
        "legend.handlelength": 1.4,
        "legend.borderpad": 0.2,
        "legend.labelspacing": 0.3,
        "pdf.fonttype": 42,         # embed TrueType, not Type 3 -> editable text
        "ps.fonttype": 42,
        "svg.fonttype": "none",     # keep text as text in SVG
    }

    if cjk:
        cjk_font = _first_available(CJK_CANDIDATES)
        if cjk_font:
            rc["font.sans-serif"] = [cjk_font, family, "DejaVu Sans"]
            rc["font.serif"] = [cjk_font, family, "DejaVu Serif"]
            rc["axes.unicode_minus"] = False
        else:
            print(
                "[ssci_style] WARNING: no CJK font found; Chinese labels will "
                "render as boxes. Install one of: "
                + ", ".join(CJK_CANDIDATES),
                file=sys.stderr,
            )

    plt.rcParams.update(rc)


def figure(
    width: str | int | float = "single",
    height: float | None = None,
    aspect: float = 0.62,
    **kwargs,
):
    """Create a figure whose width matches the journal column.

    ``aspect`` is height/width when ``height`` is not given. 0.62 is a good
    default for a single-panel coefficient plot; use 0.45-0.5 for wide
    event-study plots and 0.9-1.1 for square multi-panel blocks.
    """
    w = WIDTHS.get(width, None) if isinstance(width, str) else float(width)
    if w is None:
        raise ValueError(f"unknown width key {width!r}; use one of {sorted(WIDTHS)} or a number")
    h = height if height is not None else w * aspect
    return plt.subplots(figsize=(w, h), **kwargs)


def style_axes(ax, grid: str | None = "y", grid_color: str = "#E5E5E5") -> None:
    """Light, print-safe grid. ``grid`` is 'y', 'x', 'both' or None."""
    if grid in ("y", "both"):
        ax.yaxis.grid(True, color=grid_color, linewidth=0.5, zorder=0)
    if grid in ("x", "both"):
        ax.xaxis.grid(True, color=grid_color, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)


def save(
    fig,
    path: str | Path,
    dpi: int = 300,
    formats: Sequence[str] = ("pdf", "png"),
    close: bool = True,
) -> list[Path]:
    """Save to several formats next to each other; returns written paths.

    PDF is for submission (vector, editable text), PNG for quick review.
    300 dpi is the floor for raster; 600 for line art if the journal asks.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for fmt in formats:
        out = path.with_suffix("." + fmt)
        fig.savefig(out, dpi=dpi, format=fmt, bbox_inches="tight", pad_inches=0.02)
        written.append(out)
    if close:
        plt.close(fig)
    for p in written:
        print(f"wrote {p}")
    return written


def read_table(path: str | Path, **kwargs):
    """Read CSV/TSV/Excel into a DataFrame without guessing too much."""
    import pandas as pd

    path = Path(path)
    suffix = path.suffix.lower()
    if suffix in (".xlsx", ".xls"):
        return pd.read_excel(path, **kwargs)
    if suffix in (".tsv", ".tab"):
        return pd.read_csv(path, sep="\t", **kwargs)
    return pd.read_csv(path, **kwargs)


def ci_columns(df, est: str, lo: str, hi: str):
    """Validate that CI columns exist and lo <= est <= hi; returns the frame."""
    for col in (est, lo, hi):
        if col not in df.columns:
            raise SystemExit(
                f"column {col!r} not found. Available: {list(df.columns)}"
            )
    bad = df[(df[lo] > df[est]) | (df[hi] < df[est])]
    if len(bad):
        print(
            f"[ssci_style] WARNING: {len(bad)} row(s) violate lo <= est <= hi; "
            "check whether your CI columns are on the same scale as the estimate.",
            file=sys.stderr,
        )
    return df
