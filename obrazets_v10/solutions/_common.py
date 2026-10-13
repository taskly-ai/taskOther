# %% Ячейка 0. Библиотеки, константы, вспомогательные функции
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, integrate

R = 8.314462618      # Дж/(моль∙К)
ATM = 101325.0       # Па
PSI = 6894.757       # Па
CAL = 4.184          # Дж


def quality(y, y_model, n_par):
    """Показатели адекватности модели: SSE, R2, скорректированный R2, s, max отн. ошибка, %."""
    y, y_model = np.asarray(y, float), np.asarray(y_model, float)
    e = y - y_model
    sse = float(e @ e)
    sst = float(((y - y.mean()) ** 2).sum())
    n = len(y)
    r2 = 1 - sse / sst
    return dict(SSE=sse, R2=r2, R2adj=1 - (1 - r2) * (n - 1) / (n - n_par),
                s=np.sqrt(sse / (n - n_par)), dmax=float(np.max(np.abs(e / y))) * 100)


FIG_DIR = None      # папка для сохранения рисунков; None - рисунки выводятся в конце
RESULTS = {}        # результаты по задачам (печатаются в последней ячейке)
FIGS = []
_TASK = [None]


def task(key, title):
    _TASK[0] = key
    RESULTS[key] = {"title": title, "lines": []}


def report(*args, sep=" "):
    RESULTS[_TASK[0]]["lines"].append(sep.join(str(a) for a in args))


def draw(fig, name):
    fig.tight_layout()
    if FIG_DIR is None:
        FIGS.append(fig)
    else:
        fig.savefig(f"{FIG_DIR}/{name}.png", dpi=200)
    plt.close(fig)


def show_results():
    for r in RESULTS.values():
        print("=" * 78)
        print(r["title"])
        print("=" * 78)
        print("\n".join(r["lines"]))
        print()


def show_figures():
    from IPython.display import display
    for fig in FIGS:
        display(fig)


plt.rcParams.update({"figure.dpi": 110, "font.size": 10, "axes.grid": True, "grid.alpha": 0.3})
