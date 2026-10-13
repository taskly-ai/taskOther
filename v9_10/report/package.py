"""Пакеты для студентов: out/Для_<Фамилия>/ (+ zip).

    python report/package.py      (после report/build.py и report/module_docs.py)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOL = ROOT / "solutions"
OUT = ROOT / "out"
PKG = OUT / "_общие_материалы"
from build import STUDENTS, GROUP, docx_path, notebook_path  # noqa: E402
sys.path.insert(0, str(HERE))
from lo_pdf import docx_to_pdf_toc  # noqa: E402

PB = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'

README = """ЧТО ЗДЕСЬ И ЗАЧЕМ (МХТП, 7 семестр, вариант {var}, {fio}, {group})

1_Отчет_для_Moodle.docx
   Главный файл. Его загрузить в Moodle (курс «Моделирование ХТП», задание
   «Решить задачи по вариантам»), НЕ в личный кабинет ОмГТУ. Срок: до 01.11.2026 00:00.
   Перед загрузкой открыть в Word, на вопрос «Обновить поля?» ответить «Да»
   (заполнится содержание), проверить титул, сохранить.

2_Отчет_просмотр.pdf
   Тот же отчёт в PDF – смотреть с телефона, распечатать при просьбе преподавателя.
   В Moodle можно приложить вторым файлом, если форма позволяет.

3_Программа_Colab.ipynb
   Программа всех 12 задач для Google Colab (colab.research.google.com →
   Файл → Загрузить блокнот → Среда выполнения → Выполнить все). Нужна, если
   преподаватель попросит показать расчёт. Результаты печатаются в предпоследней
   ячейке, графики – в последней.

4_Подготовка_к_зачету.pdf (+ .docx)
   Часть 1 – по 4–5 вопросов на каждую тему отчёта с ответами на числах варианта {var}
   и «ловушками». Часть 2 – ответы на 77 контрольных вопросов и конспект 8 лекций.
   Минимум перед зачётом: часть 1 (≈ 1 час) и карточки ключевых чисел в начале
   каждого раздела.

5_HYSYS_по_желанию.pdf
   Только если преподаватель попросит показать расчёт в Aspen HYSYS (баллов за это
   нет): пошаговое построение кейсов и таблицы, куда вписать числа из HYSYS.

Баллы: 12 задач = 100 баллов, зачёт от 60. Устный ответ на зачёте – сам студент.
"""


def md_to_docx_pdf(md: str, name: str):
    src = HERE / f"_{name}.md"
    src.write_text(md, encoding="utf-8")
    docx = PKG / f"{name}.docx"
    subprocess.run(["pandoc", str(src), "-o", str(docx), "--from",
                    "markdown+tex_math_dollars+superscript+subscript+pipe_tables+raw_attribute",
                    f"--reference-doc={HERE / 'reference.docx'}", f"--resource-path={ROOT}"], check=True)
    import docx as dx
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    d = dx.Document(str(docx))
    for t in d.tables:
        b = OxmlElement("w:tblBorders")
        for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{e}")
            el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:color"), "000000")
            b.append(el)
        t._tbl.tblPr.append(b)
    d.save(str(docx))
    docx_to_pdf_toc(docx)
    src.unlink()


def main():
    if PKG.exists():
        shutil.rmtree(PKG)
    PKG.mkdir(parents=True)
    parts = ["# Подготовка к зачёту – МХТП, 7 семестр, варианты 9 и 10\n\n"
             "Часть 1 – защита отчёта (вопросы по задачам с ответами на числах варианта). "
             "Часть 2 – теория: 77 контрольных вопросов и конспект лекций.\n\n# Часть 1. Защита отчёта"]
    for m in ("m1", "m2", "m3", "m5", "m6", "m8"):
        parts.append((SOL / m / "defense.md").read_text(encoding="utf-8").replace("\n# ", "\n## ", 1).replace("# Защита", "## Защита", 1))
    theory = (SOL / "m8" / "theory.md").read_text(encoding="utf-8")
    parts.append("# Часть 2. Теория\n\n" + theory.split("\n", 1)[1])
    md_to_docx_pdf(PB.join(parts), "4_Подготовка_к_зачету")
    hys = [(SOL / m / "result.md").read_text(encoding="utf-8") for m in ("m4", "m7")]
    md_to_docx_pdf(PB.join(hys), "5_HYSYS_по_желанию")
    for st in STUDENTS:
        d = OUT / f"Для_{st['gen']}"
        if d.exists():
            shutil.rmtree(d)
        d.mkdir()
        shutil.copy(docx_path(st), d / "1_Отчет_для_Moodle.docx")
        shutil.copy(docx_path(st).with_suffix(".pdf"), d / "2_Отчет_просмотр.pdf")
        shutil.copy(notebook_path(st), d / "3_Программа_Colab.ipynb")
        for f in ("4_Подготовка_к_зачету.pdf", "4_Подготовка_к_зачету.docx", "5_HYSYS_по_желанию.pdf"):
            shutil.copy(PKG / f, d / f)
        (d / "ПРОЧТИ_МЕНЯ.txt").write_text(README.format(var=st["var"], fio=st["fio"], group=GROUP), encoding="utf-8")
        z = OUT / f"Для_{st['gen']}.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(d.iterdir()):
                zf.write(p, f"МХТП_{st['key']}/{p.name}")
        print("ZIP:", z, z.stat().st_size // 1024, "КБ")
    shutil.rmtree(PKG)


if __name__ == "__main__":
    main()
