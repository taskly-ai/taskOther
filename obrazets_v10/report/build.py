"""Сборка образца решения МХТП, 7 семестр, вариант 10 (альтернативный способ решения).

    python report/build.py          # расчёт -> report.md -> DOCX -> PDF, блокнот .ipynb, линтер

Шаги: 1) все ячейки solutions/_common.py и solutions/mN/solve.py выполняются как в Colab;
2) текст report/text.py с подстановкой чисел -> report/report.md (ссылки [@ключ] -> [N]);
3) pandoc -> DOCX (стили и колонтитулы из reference.docx, формулы — редактор формул Word);
4) доводка DOCX: титульный лист, рамки таблиц, знак «∙», шрифт кода, пустая строка
   после подписи рисунка; 5) линтер; 6) PDF через LibreOffice с обновлённым содержанием.
Скриншоты Colab из report/screens/<ячейка>.png автоматически заменяют код-текст.
"""
from __future__ import annotations

import copy
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import runner  # noqa: E402
import text_sample as T  # noqa: E402

OUT = ROOT / "out"
# варианты 9 и 10 в задании совпадают (строка «9 и 10»): расчёт общий, титулы разные
STUDENTS = [dict(key="Образец", fio="", var=10, book="", gen="образец")]
GROUP = "ЗХТ-232"


def docx_path(st):
    return OUT / f"МХТП_Образец_решения_7сем_вар{st['var']}.docx"


def notebook_path(st):
    return OUT / f"МХТП_Образец_вар{st['var']}.ipynb"


def title(st):
    return {
        "top": ["Министерство науки и высшего образования Российской Федерации",
                "Федеральное государственное автономное образовательное учреждение",
                "высшего образования",
                "«Омский государственный технический университет»",
                "Кафедра «Химия и химическая технология»"],
        "middle": ["ОБРАЗЕЦ РЕШЕНИЯ", "задач за 7 семестр по курсу «Моделирование химико-технологических процессов»", "",
                   f"Вариант {st['var']}", "(альтернативный способ решения)"],
        "who": ["", "", "", "", "", "", "", "", ""],
        "city": "Омск 2026",
    }


BIB = {
    "task": "Горбунов, В. А. Задачи для 7 семестра по курсу «Моделирование химико-технологических процессов» / В. А. Горбунов ; Омский государственный технический университет. – Омск : ОмГТУ, 2026. – 9 с. – Текст : электронный.",
    "lectures": "Горбунов, В. А. Моделирование химико-технологических процессов : курс лекций и практических занятий / В. А. Горбунов ; Омский государственный технический университет. – Омск : ОмГТУ, 2025. – Текст : электронный.",
    "gumerov": "Математическое моделирование химико-технологических процессов : учебное пособие / Ас. М. Гумеров, Н. Н. Валеев, Аз. М. Гумеров, В. М. Емельянов ; Казанский государственный технологический университет. – Казань : КГТУ, 2006. – 216 с. – Текст : непосредственный.",
    "usheva": "Математическое моделирование химико-технологических процессов : учебное пособие / Н. В. Ушева, О. Е. Мойзес, О. Е. Митянина, Е. А. Кузьменко ; Томский политехнический университет. – Томск : Изд-во ТПУ, 2014. – 135 с. – Текст : непосредственный.",
    "samoylov": "Самойлов, Н. А. Моделирование в химической технологии и расчет реакторов : учебное пособие / Н. А. Самойлов. – Уфа : Изд-во УГНТУ, 2006. – 195 с. – Текст : непосредственный.",
    "finlayson": "Finlayson, B. A. Introduction to Chemical Engineering Computing / B. A. Finlayson. – 2nd ed. – Hoboken : John Wiley & Sons, 2012. – 391 p. – ISBN 978-0-470-93295-7. – Текст : непосредственный.",
    "numpy": "NumPy documentation : официальный сайт. – URL: https://numpy.org/doc/stable/ (дата обращения: 12.10.2026). – Текст : электронный.",
    "scipy": "SciPy documentation : официальный сайт. – URL: https://docs.scipy.org/doc/scipy/ (дата обращения: 12.10.2026). – Текст : электронный.",
    "ifp": "Refining & Chemicals. Folder Zero : Index of Data and Diagrams / IFP Training. – Rueil-Malmaison : IFP Training, 2014. – 309 p. – Текст : непосредственный.",
    "rk": "Redlich, O. On the Thermodynamics of Solutions. V. An Equation of State. Fugacities of Gaseous Solutions / O. Redlich, J. N. S. Kwong // Chemical Reviews. – 1949. – Vol. 44, № 1. – P. 233–244. – Текст : непосредственный.",
    "soave": "Soave, G. Equilibrium constants from a modified Redlich–Kwong equation of state / G. Soave // Chemical Engineering Science. – 1972. – Vol. 27, № 6. – P. 1197–1203. – Текст : непосредственный.",
    "mcw": "McWilliams, M. L. An equation to relate K-factors to pressure and temperature / M. L. McWilliams // Chemical Engineering. – 1973. – Vol. 80, № 25. – P. 138. – Текст : непосредственный.",
    "pr": "Peng, D.-Y. A New Two-Constant Equation of State / D.-Y. Peng, D. B. Robinson // Industrial & Engineering Chemistry Fundamentals. – 1976. – Vol. 15, № 1. – P. 59–64. – Текст : непосредственный.",
    "wegstein": "Wegstein, J. H. Accelerating convergence of iterative processes / J. H. Wegstein // Communications of the ACM. – 1958. – Vol. 1, № 6. – P. 9–13. – Текст : непосредственный.",
    "rr": "Rachford, H. H. Procedure for use of electronic digital computers in calculating flash vaporization hydrocarbon equilibrium / H. H. Rachford, J. D. Rice // Journal of Petroleum Technology. – 1952. – Vol. 4, № 10. – P. 19. – Текст : непосредственный.",
}

PAGEBREAK = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'


def citations(md: str) -> str:
    body, _, tail = md.partition("<!-- BIBLIOGRAPHY -->")
    order = []
    for mo in re.finditer(r"@([a-z]+)", " ".join(re.findall(r"\[@[^\]]+\]", body))):
        if mo.group(1) not in order:
            order.append(mo.group(1))
    num = {k: i + 1 for i, k in enumerate(order)}

    def rep(mo):
        inner = mo.group(1)
        keys = re.findall(r"@([a-z]+)", inner)
        loc = re.sub(r"(;\s*)?@[a-z]+", "", inner).strip(" ;")
        s = ", ".join(str(num[k]) for k in keys)
        return f"[{s}{', ' + loc.lstrip(', ') if loc else ''}]"
    body = re.sub(r"\[(@[^\]]+)\]", rep, body)
    missing = [k for k in order if k not in BIB]
    if missing:
        raise KeyError(missing)
    unused = [k for k in BIB if k not in num]
    if unused:
        print("Источники без ссылок:", unused)
    bib = "# Список литературы\n\n" + "\n".join(f"{i + 1}. {BIB[k]}" for i, k in enumerate(order)) + "\n"
    return body + bib + tail


def make_markdown(ns, cells) -> str:
    C = T.Counter()
    parts = [T.intro(ns, cells, C), T.sec1(ns, cells, C), T.sec2(ns, cells, C), T.sec3(ns, cells, C),
             T.sec4(ns, cells, C), T.sec5(ns, cells, C), T.conclusion(ns, C)]
    md = "".join(parts)
    md = citations(md)
    md = md.replace("\\newpage", PAGEBREAK)
    left = re.findall(r"\[@|\{n\(|\{m\(", md)
    if left:
        raise ValueError(f"неподставленные метки: {left[:5]}")
    return md


# ---------------------------------------------------------------- доводка DOCX
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"


def tune(path: Path, st: dict):
    TITLE = title(st)
    import docx
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt

    d = docx.Document(str(path))
    body = d.element.body
    # --- титульный лист (вставляется перед содержанием)
    first = body[0]

    def para(text, align=WD_ALIGN_PARAGRAPH.CENTER, bold=False, indent_cm=None):
        p = d.add_paragraph()
        p.style = d.styles["Normal"]
        p.alignment = align
        pf = p.paragraph_format
        pf.first_line_indent = Pt(0)
        if indent_cm:
            pf.left_indent = Pt(indent_cm * 28.35)
        if text:
            r = p.add_run(text)
            r.bold = bold
        first.addprevious(p._p)
        return p

    for t in TITLE["top"]:
        para(t)
    for _ in range(4):
        para("")
    for i, t in enumerate(TITLE["middle"]):
        para(t, bold=(i == 0))
    for _ in range(3):
        para("")
    for t in TITLE["who"]:
        para(t, WD_ALIGN_PARAGRAPH.LEFT, indent_cm=9.5)
    para("")
    city = para(TITLE["city"])
    # титул — отдельный раздел (без номера страницы); основной раздел — с номерами
    final_sect = body.find(qn("w:sectPr"))
    title_sect = copy.deepcopy(final_sect)
    t_ = OxmlElement("w:type")
    t_.set(qn("w:val"), "nextPage")
    title_sect.insert(0, t_)
    city._p.get_or_add_pPr().append(title_sect)
    tp = final_sect.find(qn("w:titlePg"))
    if tp is not None:
        final_sect.remove(tp)

    # --- разрыв страницы после содержания
    sdt = body.find(qn("w:sdt"))
    if sdt is not None:
        pb = OxmlElement("w:p")
        r_ = OxmlElement("w:r")
        b_ = OxmlElement("w:br")
        b_.set(qn("w:type"), "page")
        r_.append(b_)
        pb.append(r_)
        sdt.addnext(pb)
    # --- выключные формулы: без абзацного отступа, по центру
    for p in d.paragraphs:
        if p._p.find(M + "oMathPara") is not None:
            p.paragraph_format.first_line_indent = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # --- код: Courier New 10 пт, одинарный интервал
    for p in d.paragraphs:
        if p.style.name == "Source Code":
            p.paragraph_format.first_line_indent = Pt(0)
            for r in p.runs:
                r.font.size = Pt(9)
                r.font.name = "Courier New"
    d.styles["Source Code"].font.size = Pt(9)
    # --- подпись рисунка: пустая строка после неё (требование 8)
    for p in list(d.paragraphs):
        if p.style.name == "Image Caption":
            p._p.addnext(OxmlElement("w:p"))
    # --- таблицы: рамки, 12 пт, без абзацного отступа, по центру
    for t in d.tables:
        tblPr = t._tbl.tblPr
        for old in tblPr.findall(qn("w:tblBorders")):
            tblPr.remove(old)
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{edge}")
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), "4")
            e.set(qn("w:space"), "0")
            e.set(qn("w:color"), "000000")
            borders.append(e)
        tblPr.append(borders)
        jc = tblPr.find(qn("w:jc"))
        if jc is None:
            jc = OxmlElement("w:jc")
            tblPr.append(jc)
        jc.set(qn("w:val"), "center")
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.first_line_indent = Pt(0)
                    p.paragraph_format.line_spacing = 1.0
                    for r in p.runs:
                        r.font.size = Pt(12)
    # --- знак умножения в формулах: «∙»
    for t in body.iter(M + "t"):
        if t.text and ("⋅" in t.text or "·" in t.text):
            t.text = t.text.replace("⋅", "∙").replace("·", "∙")
    # --- ячейки таблиц с формулами: размер формул 12 пт
    d.save(str(path))


# ---------------------------------------------------------------- линтер
def lint(path: Path) -> list[str]:
    import docx
    d = docx.Document(str(path))
    texts = [p.text for p in d.paragraphs if p.style.name not in ("Source Code",)]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                texts += [p.text for p in c.paragraphs]
    probs = []
    for s in texts:
        s2 = re.sub(r"https?://\S+", "", s)
        for ch in ("*", "^", "×", "$", "\\", "[@", "{", "}"):
            if ch in s2:
                probs.append(f"«{ch}»: {s[:100]}")
        if re.search(r"\d,\d", re.sub(r"\[[\d, ]+\]", "", s2)) and "раздел" not in s2:
            probs.append(f"десятичная запятая?: {s[:100]}")
        if re.search(r"[а-яА-Я] - [а-яА-Я]|\d - \d", s2):
            probs.append(f"дефис вместо тире: {s[:100]}")
    return probs


def main(pdf=True):
    OUT.mkdir(exist_ok=True)
    cells_list = runner.all_cells()
    ns = runner.run_cells(cells_list, HERE / "fig")
    cells = {c.cid: c for c in cells_list}
    md = make_markdown(ns, cells)
    meta = "---\ntoc-title: Содержание\nlang: ru-RU\n---\n\n"
    for st in STUDENTS:
        src = HERE / f"report_{st['key']}.md"
        src.write_text(meta + md.replace("@@VAR@@", str(st["var"])), encoding="utf-8")
        out = docx_path(st)
        subprocess.run(["pandoc", str(src), "-o", str(out), "--from",
                        "markdown+tex_math_dollars+superscript+subscript+pipe_tables+implicit_figures+raw_attribute",
                        f"--reference-doc={HERE / 'reference.docx'}", f"--resource-path={HERE}",
                        "--toc", "--toc-depth=2"], check=True)
        tune(out, st)
        probs = lint(out)
        print(st["key"], "– линтер:", "замечаний нет" if not probs else f"{len(probs)} замечаний")
        for p in probs[:60]:
            print("   ", p)
        runner.write_notebook(cells_list, notebook_path(st),
                              f"# МХТП, 7 семестр, вариант {st['var']} – образец решения (альтернативный способ)\n"
                              "Выполнить ячейки по порядку (Среда выполнения → Выполнить все).")
        print("DOCX:", out)
        if pdf:
            from lo_pdf import docx_to_pdf_toc
            print("PDF:", docx_to_pdf_toc(out))
    (HERE / "report.md").write_text(meta + md, encoding="utf-8")   # общий текст для module_docs
    return ns


if __name__ == "__main__":
    main(pdf="--no-pdf" not in sys.argv)
