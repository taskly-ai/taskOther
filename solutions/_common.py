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


def show(fig, name):
    """Показать рисунок (в Colab) и при сборке отчёта сохранить его в PNG."""
    fig.tight_layout()
    if FIG_DIR is not None:
        fig.savefig(f"{FIG_DIR}/{name}.png")
        plt.close(fig)
    else:
        plt.show()


plt.rcParams.update({"figure.dpi": 110, "font.size": 10, "savefig.dpi": 200})
