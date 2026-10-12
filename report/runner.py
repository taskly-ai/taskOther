"""Прогон расчётных ячеек модулей так же, как в Google Colab, и сборка блокнота .ipynb.

Ячейки берутся из solutions/_common.py и solutions/mN/solve.py (разделитель «# %%»).
Каждая ячейка выполняется в общем пространстве имён; её вывод перехватывается для блока
«Результат работы программы» в отчёте, рисунки сохраняются в report/fig.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOL = ROOT / "solutions"
MODULES = ["m1", "m2", "m3", "m5", "m6"]


class Cell:
    def __init__(self, module, title, code):
        self.module, self.title, self.code = module, title, code
        self.out = ""

    @property
    def cid(self):
        """Идентификатор ячейки для имён скриншотов: «Задача 3.2. Исследование» -> t32b."""
        mo = re.search(r"Задач[аи] (\d)\.(\d)([абв]?)", self.title)
        suf = {"а": "a", "б": "b", "в": "c"}.get(mo.group(3), "") if mo else ""
        base = f"t{mo.group(1)}{mo.group(2)}{suf}" if mo else "c0"
        if "Общая часть" in self.title:
            base = f"t{mo.group(1)}_common"
        if "Исследование" in self.title:
            base += "_study"
        return base


def split_cells(path: Path, module: str) -> list[Cell]:
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"^# %% ", text, flags=re.M)
    cells = []
    for part in parts[1:]:
        title, _, body = part.partition("\n")
        cells.append(Cell(module, title.strip(), body.strip("\n")))
    return cells


def all_cells() -> list[Cell]:
    cells = split_cells(SOL / "_common.py", "common")
    for m in MODULES:
        cells += split_cells(SOL / m / "solve.py", m)
    return cells


def run_cells(cells, fig_dir: Path) -> dict:
    """Выполнить все ячейки по порядку; вернуть пространство имён."""
    import matplotlib
    matplotlib.use("Agg")
    ns: dict = {"__name__": "__colab__"}
    fig_dir.mkdir(parents=True, exist_ok=True)
    for c in cells:
        buf = io.StringIO()
        before = set(ns.get("RESULTS", {}))
        with contextlib.redirect_stdout(buf):
            exec(compile(c.code, f"<{c.cid}>", "exec"), ns)
        if c.module == "common":
            ns["FIG_DIR"] = str(fig_dir)          # show() читает глобальную FIG_DIR
        new = [k for k in ns["RESULTS"] if k not in before]
        c.out = "\n".join("\n".join(ns["RESULTS"][k]["lines"]) for k in new) or buf.getvalue().rstrip()
    return ns


def write_notebook(cells, path: Path, title_md: str):
    nb_cells = [{"cell_type": "markdown", "metadata": {}, "source": title_md}]
    for c in cells:
        src = f"# {c.title}\n{c.code}\n"
        nb_cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                         "outputs": [], "source": src.splitlines(keepends=True)})
    nb_cells.append({"cell_type": "markdown", "metadata": {}, "source":
                     "## Результаты для скриншотов\nВыполнить после всех ячеек выше. Каждый блок между "
                     "линиями «=====» — один скриншот; имя файла указано в заголовке блока."})
    nb_cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
                     "source": ["# РЕЗУЛЬТАТЫ ВСЕХ ЗАДАЧ (скриншоты делать здесь)\n", "show_results()\n"]})
    nb_cells.append({"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
                     "source": ["# Графики всех задач (скриншоты не нужны: они уже в отчёте как рисунки)\n",
                                "show_figures()\n"]})
    for i, c in enumerate(nb_cells):
        c["id"] = f"cell-{i:02d}"
    nb = {"cells": nb_cells, "nbformat": 4, "nbformat_minor": 5,
          "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"},
                       "language_info": {"name": "python"}, "colab": {"provenance": []}}}
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    cs = all_cells()
    ns = run_cells(cs, ROOT / "report" / "fig")
    for c in cs:
        print(f"[{c.cid}] {c.title}: {len(c.code.splitlines())} строк кода, {len(c.out.splitlines())} строк вывода")
    sys.exit(0)
