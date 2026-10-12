# %% Ячейка 0. Общие библиотеки, константы и функции (выполнить первой)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, brentq, fsolve

R = 8.314462618      # универсальная газовая постоянная, Дж/(моль∙К)
ATM = 101325.0       # 1 атм = 101325 Па
PSI = 6894.757       # 1 psi = 6894.757 Па
CAL = 4.184          # 1 кал = 4.184 Дж


def sse(y, y_calc):
    """Остаточная сумма квадратов."""
    return float(np.sum((np.asarray(y) - np.asarray(y_calc)) ** 2))


def r2(y, y_calc):
    """Коэффициент детерминации R2 = 1 - SSE/SST."""
    y = np.asarray(y)
    return 1.0 - sse(y, y_calc) / float(np.sum((y - y.mean()) ** 2))


def style_axes(ax):
    """Сетка на графике."""
    ax.grid(alpha=0.3)


FIG_DIR = None      # папка для сохранения рисунков (None - рисунки выводятся в конце)
RESULTS = {}        # результаты расчёта по задачам
FIGS = []           # построенные графики
_CUR = [None]


def task(key, title):
    """Начало новой задачи."""
    _CUR[0] = key
    RESULTS[key] = {"title": title, "lines": []}


def out(*args, sep=" "):
    """Запись строки результата текущей задачи."""
    RESULTS[_CUR[0]]["lines"].append(sep.join(str(a) for a in args))


def show(fig, name):
    """Сохранение рисунка в файл или отложенный вывод."""
    fig.tight_layout()
    if FIG_DIR is not None:
        fig.savefig(f"{FIG_DIR}/{name}.png")
    else:
        FIGS.append((name, fig))
    plt.close(fig)


def show_results():
    """Вывод результатов всех задач."""
    for key, r in RESULTS.items():
        print("=" * 78)
        print(r["title"])
        print("=" * 78)
        print("\n".join(r["lines"]))
        print()


def show_figures():
    """Вывод всех графиков."""
    from IPython.display import display
    for name, fig in FIGS:
        display(fig)


plt.rcParams.update({"figure.dpi": 110, "font.size": 10, "savefig.dpi": 200})
