# -*- coding: utf-8 -*-
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = 'manuscript_JIS_draft.md'
OUT = 'Methodological_Approaches_AIGC_EC_JIS.docx'

doc = Document()

# 默认样式：Times New Roman 12pt
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

def set_double(p):
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)

def add_runs(p, text):
    """解析 **bold** 和 *italic* 内联格式。"""
    # 先处理 bold（**...**），再处理 italic（*...*）
    token_re = re.compile(r'(\*\*.*?\*\*|\*.*?\*)')
    pos = 0
    for m in token_re.finditer(text):
        if m.start() > pos:
            p.add_run(text[pos:m.start()])
        tok = m.group(0)
        if tok.startswith('**'):
            r = p.add_run(tok[2:-2]); r.bold = True
        else:
            r = p.add_run(tok[1:-1]); r.italic = True
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
    r = p.add_run(text); r.bold = True
    return p

def add_heading2(text):
    p = doc.add_paragraph()
    set_double(p)
    r = p.add_run(text); r.bold = True; r.italic = True
    return p

def add_table(rows):
    ncol = len(rows[0])
    tbl = doc.add_table(rows=len(rows), cols=ncol)
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = tbl.cell(i, j)
            c.text = ''
            p = c.paragraphs[0]
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_after = Pt(0)
            add_runs(p, cell)
            for r in p.runs:
                r.font.size = Pt(11)
                if i == 0:
                    r.bold = True
    # 表后空行
    sp = doc.add_paragraph(); set_double(sp)

lines = open(SRC, encoding='utf-8').read().split('\n')

i = 0
in_refs = False
while i < len(lines):
    line = lines[i].rstrip()
    if not line.strip():
        i += 1
        continue

    # 标题
    if line.startswith('# ') and not line.startswith('## '):
        t = doc.add_paragraph()
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_double(t)
        r = t.add_run(line[2:].strip()); r.bold = True; r.font.size = Pt(14)
        i += 1
        continue

    # 一级标题
    if line.startswith('## '):
        add_heading1(line[3:].strip())
        i += 1
        continue

    # 二级标题
    if line.startswith('### '):
        add_heading2(line[4:].strip())
        i += 1
        continue

    # 表格：收集连续的 | 行
    if line.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].strip().startswith('|'):
            raw = lines[i].strip().strip('|')
            cells = [c.strip() for c in raw.split('|')]
            # 跳过分隔行
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                i += 1
                continue
            rows.append(cells)
            i += 1
        add_table(rows)
        continue

    # 关键词行
    if line.startswith('**Keywords:**'):
        p = doc.add_paragraph(); set_double(p)
        r = p.add_run('Keywords: '); r.bold = True
        add_runs(p, line[len('**Keywords:**'):].strip())
        i += 1
        continue

    # 参考文献
    if line.startswith('## References'):
        add_heading1('References')
        in_refs = True
        i += 1
        continue

    # 普通段落
    add_body(line, indent=(not in_refs))
    i += 1

doc.save(OUT)
print('saved', OUT)
