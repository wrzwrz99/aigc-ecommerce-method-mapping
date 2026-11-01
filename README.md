# Mapping the methodological approaches of AIGC-driven e-commerce user behavior research

Data and code repository for the manuscript:

> **Mapping the methodological approaches of AIGC-driven e-commerce user behavior research: a systematic review of SSCI-indexed literature (2015-2026)**

This repository is provided for reproducibility and peer review. The data are released so that reviewers and readers can reproduce the screening flow, the method-category coding, the trend tests and the citation analysis reported in the manuscript.

## Contents

```
data/        Final coded corpus (CSV, UTF-8)
code/        Retrieval, statistical analysis, figure and manuscript scripts
figures/     Publication figures (vector PDF + 600 dpi PNG)
manuscript/  Manuscript source (Markdown) and the SAGE-formatted Word draft
```

## Data files

| File | Records | Stage |
| --- | --- | --- |
| `data/openalex_ssci_q12_clean.csv` | **187** | **Final corpus**, after removing 18 companion/non-SSCI outlets and correcting one coding error |

The CSV contains `openalex_id`, `doi`, `title`, `year`, `date`, `cited_by_count`, `journal`, `n_authors`, `abstract`, `concepts` and the `paradigm` column with the method-category label (`quantitative`, `conceptual`, `computational`, `qualitative`). Citation counts were captured from OpenAlex on 1 November 2026. The intermediate screening snapshots are not deposited; the complete PRISMA flow is reported below.

## Search strategy

Titles and abstracts were searched in OpenAlex (https://api.openalex.org) with 20 queries combining a technology family (generative artificial intelligence, generative AI, large language model, ChatGPT, AI-generated content, virtual influencer, AI avatar, AI chatbot, digital human, virtual anchor, conversational AI, text-to-image) with an e-commerce and consumer family (e-commerce, online shopping, online retail, livestreaming commerce, social commerce, consumer, purchase intention, recommendation, review). Records were limited to English-language journal articles published from 2015 to 1 November 2026. The queries are reproduced in `code/retrieve_openalex.py`.

## Screening (PRISMA)

1. Identification: 1,449 unique records.
2. Screening 1: removed 244 preprints, predatory or conference records, leaving 1,205.
3. Screening 2: retained peer-reviewed Scopus/WoS journals only, leaving 261.
4. Eligibility: title-and-abstract screening against three criteria (generative/intelligent technology; e-commerce or online retail setting; consumer or user behavior object), leaving 238.
5. Inclusion: retained SSCI Q1/Q2 journals only, leaving 205; a JCR verification pass removed 18 companion or non-SSCI outlets, leaving the final corpus of **187 articles**.

## Method-category coding

Each article was coded into one of four categories defined by research object and data type:

- **Conceptual/review**: no primary data; theory building, frameworks, reviews, bibliometrics.
- **Quantitative empirical**: primary quantitative data used to test hypotheses (survey, experiment, econometrics, eye-tracking).
- **Computational**: ML/NLP/LLM applied to user-generated data (review mining, fake review detection, recommendation, sentiment).
- **Qualitative**: interviews, cases, grounded theory, or thematic/discourse analysis.

Mixed-method work was assigned to the category on which its main contribution depends. Coding used a rule-based first pass followed by dual-coder manual refinement (Cohen's kappa = 0.89 on the jointly coded set).

## Analysis

- Annual counts and shares, with tie-corrected Mann-Kendall trend tests.
- Negative binomial regressions of citation counts, controlling for log article age and journal, with journal-clustered standard errors (`code/nb2_cluster.py`).

## Figures

All three figures follow the SAGE/Journal of Information Science artwork
requirements: double-column width (170 mm), Arial 8 pt, no title inside the
image, bars starting at zero, and greyscale shades combined with hatched
patterns so every category remains distinguishable in black-and-white print.
Each figure is exported as vector PDF (for separate submission, which SAGE
requires for artwork created outside Word) and as 600 dpi PNG (embedded in the
Word draft). Captions stand alone and avoid colour words, because SAGE publishes
figures in colour online but in black and white in print.

| File | Content | Section |
| --- | --- | --- |
| `figures/Figure1_PRISMA.pdf` / `.png` | PRISMA flow, 1,449 records to 187 included articles | 3.2 |
| `figures/Figure2_annual_methods.pdf` / `.png` | Annual stacked counts by method category, 2015-2026 | 4.3 |
| `figures/Figure3_top_journals.pdf` / `.png` | The eight journals with seven or more articles | 4.4 |

Figure 3 is limited to the eight journals with at least seven articles (121 of
187): three journals tie at six articles, so a "top ten" cut at that boundary
would be arbitrary. The citation regression is reported in Table 5 rather than
plotted, following the convention that two or three coefficients do not warrant
a figure.

## Reproducing the results

Python 3.10 with `pandas`, `numpy`, `scipy`, `matplotlib` and (for the Word
output) `python-docx`:

```
pip install pandas numpy scipy matplotlib python-docx
python code/analysis.py        # recompute distributions, trends, citations, NB2
python code/make_figures.py    # rebuild all three figures (PDF + PNG)
python code/gen_docx.py        # rebuild the Word draft from the Markdown source
```

Run `code/analysis.py` from the directory that contains the data files, or adjust the input path at the top of the script.

## License

The data and code are provided for scholarly reproduction and peer review. If you reuse the corpus, please cite the manuscript. The manuscript text is the authors' own work.
