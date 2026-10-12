"""Генерация блокнота Jupyter (nbformat 4) из mhtp_v8.py (формат ячеек «# %%»).

    python make_notebook.py   -> mhtp_v8.ipynb рядом
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "mhtp_v8.py").read_text(encoding="utf-8")
cells = []
for block in re.split(r"(?m)^(?=# %%)", src):
    if not block.strip():
        continue
    first, _, body = block.partition("\n")
    if first.startswith("# %% [markdown]"):
        text = "\n".join(line[2:] if line.startswith("# ") else line.lstrip("#")
                         for line in body.rstrip().split("\n"))
        cells.append({"cell_type": "markdown", "metadata": {},
                      "source": text.splitlines(keepends=True)})
    else:
        title = first[4:].strip()
        code = (f"# {title}\n" if title else "") + body.rstrip() + "\n"
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {},
                      "outputs": [], "source": code.splitlines(keepends=True)})
# последняя ячейка: в блокноте __name__ == "__main__", поэтому run_all() выполнится
cells.insert(1, {"cell_type": "markdown", "metadata": {}, "source": [
    "Запуск: «Run All». Для Google Colab достаточно загрузить этот файл; ",
    "графики сохраняются в папку fig/ рядом с блокнотом и выводятся под ячейками.\n"]})
nb = {"cells": cells,
      "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                   "language_info": {"name": "python", "version": "3"}},
      "nbformat": 4, "nbformat_minor": 5}
for i, c in enumerate(nb["cells"]):
    c["id"] = f"cell-{i:02d}"
(HERE / "mhtp_v8.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("ячеек:", len(cells))
