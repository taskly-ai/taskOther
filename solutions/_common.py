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
    """Сетка на графике (десятичный разделитель — точка, как во всём отчёте)."""
    ax.grid(alpha=0.3)


FIG_DIR = None      # при сборке отчёта сюда записывается папка для рисунков
RESULTS = {}        # результаты задач: выводятся вместе в последней ячейке блокнота
FIGS = []           # графики задач: выводятся в самой последней ячейке
_CUR = [None]


def task(key, title):
    """Начать задачу: дальнейший вывод out() относится к ней."""
    _CUR[0] = key
    RESULTS[key] = {"title": title, "lines": []}


def out(*args, sep=" "):
    """Запомнить строку результата текущей задачи (вместо print)."""
    RESULTS[_CUR[0]]["lines"].append(sep.join(str(a) for a in args))


def show(fig, name):
    """Сохранить рисунок: в Colab он выводится в конце, при сборке отчёта — в PNG."""
    fig.tight_layout()
    if FIG_DIR is not None:
        fig.savefig(f"{FIG_DIR}/{name}.png")
    else:
        FIGS.append((name, fig))
    plt.close(fig)


def show_results():
    """Все результаты подряд; каждый блок — один скриншот (имя файла указано в заголовке)."""
    for key, r in RESULTS.items():
        print("=" * 78)
        print(f"{r['title']}   ->  скриншот: {key}.png")
        print("=" * 78)
        print("\n".join(r["lines"]))
        print()


def show_figures():
    """Все графики (в отчёте они уже вставлены как рисунки; скриншоты не нужны)."""
    try:
        from IPython.display import display
    except ImportError:
        display = None
    for name, fig in FIGS:
        print(name)
        if display:
            display(fig)


plt.rcParams.update({"figure.dpi": 110, "font.size": 10, "savefig.dpi": 200})
