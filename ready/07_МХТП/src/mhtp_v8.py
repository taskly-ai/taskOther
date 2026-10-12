# %% [markdown]
# # Моделирование химико-технологических процессов — 7 семестр, вариант 8
# Суханов С.В., группа ЗХТ-232. Все расчёты по 5 темам (12 заданий).
#
# Запуск: `python mhtp_v8.py` (печать результатов, графики в папку `fig/`)
# или ячейка за ячейкой в Jupyter/Colab (файл `mhtp_v8.ipynb`).
# Единицы внутри расчётов — СИ; атм, psia, °R, кал — только на входе/выходе.

# %% Общие импорты, константы и вспомогательные функции
import sys
from pathlib import Path

import numpy as np
import matplotlib
if "ipykernel" not in sys.modules:
    matplotlib.use("Agg")                      # без окна при запуске из консоли
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.patches import FancyBboxPatch
from scipy import stats
from scipy.optimize import brentq, curve_fit, fsolve, least_squares

R = 8.314462618         # универсальная газовая постоянная, Дж/(моль·К)
ATM = 101325.0          # 1 атм, Па
PSI = 6894.757293168    # 1 psi (фунт-сила на кв. дюйм), Па
CAL = 4.184             # 1 кал (термохимическая), Дж
MPA = 1.0e6             # 1 МПа, Па

try:
    BASE = Path(__file__).resolve().parent
except NameError:                              # Jupyter / Colab
    BASE = Path.cwd()
FIG = BASE / "fig"
FIG.mkdir(exist_ok=True)

trapezoid = getattr(np, "trapezoid", None) or np.trapz   # NumPy 2.x / 1.x
IN_NOTEBOOK = "ipykernel" in sys.modules

# синий, оранжевый, бирюзовый, жёлтый
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
MARKERS = ["o", "s", "^", "D"]
LINES = ["-", "--", "-.", ":"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "savefig.dpi": 200,
                     "axes.grid": True, "grid.color": "#d9d9d9", "grid.linewidth": 0.6,
                     "axes.edgecolor": "#52514e", "lines.linewidth": 1.6,
                     "legend.frameon": True, "legend.framealpha": 0.9})


def sse(y, yfit):
    """Остаточная сумма квадратов SSE."""
    return float(np.sum((np.asarray(y) - np.asarray(yfit)) ** 2))


def r2_score(y, yfit):
    """Коэффициент детерминации R² = 1 − SSE/TSS."""
    y = np.asarray(y)
    return 1.0 - sse(y, yfit) / float(np.sum((y - y.mean()) ** 2))


def _comma(v, pos=None):
    """Подпись делений осей с десятичной запятой и знаком минус."""
    s = "%.6g" % v
    return s.replace(".", ",").replace("-", "−")


def finish(fig, name):
    """Десятичная запятая на осях, сохранение PNG (dpi 200), показ в блокноте."""
    for ax in fig.axes:
        if ax.get_xscale() == "linear":
            ax.xaxis.set_major_formatter(ticker.FuncFormatter(_comma))
        if ax.get_yscale() == "linear":
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(_comma))
        else:
            ax.yaxis.set_major_formatter(ticker.FuncFormatter(_comma))
    fig.tight_layout()
    path = FIG / name
    fig.savefig(path, dpi=200)
    if IN_NOTEBOOK:
        plt.show()
    plt.close(fig)
    return path


# %% [markdown]
# ## Тема 1. Эмпирические модели и регрессия
# ### Задание 1. Средняя теплоёмкость пропана

# %% Т1 З1: полином 4-й степени и средняя теплоёмкость
# T, К и C, Дж/(моль·К) (в шапке задания ошибочно «кДж/кг К»)
T1_T = np.array([50, 100, 150, 200, 273.15, 300, 400, 500, 600, 700, 800, 900,
                 1000, 1100, 1200, 1300])
T1_C = np.array([34.16, 41.3, 48.79, 56.07, 68.74, 73.93, 94.01, 112.59, 128.7,
                 142.67, 154.77, 163.35, 174.6, 182.67, 189.74, 195.85])
M_C3H8 = 44.097                     # молярная масса пропана, г/моль


def t1z1(deg=4, T0=50.0, T=1300.0):
    p = np.polyfit(T1_T, T1_C, deg)                  # коэффициенты от старшей степени
    C_fit = np.polyval(p, T1_T)
    P = np.polyint(p)                                # первообразная полинома
    I_poly = np.polyval(P, T) - np.polyval(P, T0)    # интеграл C dT, Дж/моль
    C_poly = I_poly / (T - T0)                       # <C> по модели
    I_trap = trapezoid(T1_C, T1_T)                   # интеграл по таблице (трапеции)
    C_trap = I_trap / (T - T0)
    I_trap_poly = trapezoid(C_fit, T1_T)             # трапеции по значениям полинома
    return dict(p=p, C_fit=C_fit, resid=T1_C - C_fit, R2=r2_score(T1_C, C_fit),
                SSE=sse(T1_C, C_fit), I_poly=I_poly, C_poly=C_poly,
                I_trap=I_trap, C_trap=C_trap,
                delta_rel=abs(C_poly - C_trap) / C_trap * 100,
                # погрешность метода трапеций
                err_trap_rule=(I_trap_poly - I_poly) / (T - T0),
                # вклад остатков модели
                err_model=(I_trap - I_trap_poly) / (T - T0),
                C_poly_mass=C_poly / M_C3H8, C_trap_mass=C_trap / M_C3H8)


def print_t1z1(r):
    print("Коэффициенты полинома (от T^4 к T^0):", np.array2string(r["p"], precision=6))
    print(f"R2 = {r['R2']:.6f}; SSE = {r['SSE']:.4f} (Дж/(моль·К))^2")
    print(f"Интеграл по полиному  = {r['I_poly']:.1f} Дж/моль -> <C> = {r['C_poly']:.3f} Дж/(моль·К)")
    print(f"Интеграл трапециями   = {r['I_trap']:.1f} Дж/моль -> <C> = {r['C_trap']:.3f} Дж/(моль·К)")
    print(f"Расхождение = {r['delta_rel']:.3f} %; <C> = {r['C_poly_mass']:.4f} кДж/(кг·К)")


def plot_t1z1(r):
    TT = np.linspace(50, 1300, 400)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.5, 6.2), sharex=True,
                                 gridspec_kw={"height_ratios": [2.2, 1]})
    a1.plot(T1_T, T1_C, MARKERS[0], color=COLORS[0], ms=6, label="Табличные данные")
    a1.plot(TT, np.polyval(r["p"], TT), LINES[0], color=COLORS[1], label="Полином 4-й степени")
    a1.axhline(r["C_poly"], ls="--", color="#52514e", lw=1.0,
               label="Средняя теплоёмкость 50–1300 К")
    a1.set_ylabel("C, Дж/(моль∙К)")
    a1.legend(loc="lower right")
    a2.axhline(0, color="#52514e", lw=0.8)
    a2.plot(T1_T, r["resid"], MARKERS[1], color=COLORS[0], ms=5)
    a2.set_xlabel("T, К")
    a2.set_ylabel("Остаток, Дж/(моль∙К)")
    return finish(fig, "t1z1_cp.png")


# %% [markdown]
# ### Задание 2. Содержание воды в дистилляте от расхода пара

# %% Т1 З2: заданная модель и альтернативы (scipy.optimize.curve_fit)
X2 = np.array([0.263, 0.294, 0.321, 0.367, 0.429, 0.608, 1.33, 1.36])   # x, кг/с
Y2 = np.array([0.34, 0.32, 0.24, 0.20, 0.16, 0.11, 0.06, 0.04])        # y, доли


def m_given(x, a, b):
    """Заданная модель y = a·(ln(x/b))^(-2/3)."""
    return a * np.log(x / b) ** (-2.0 / 3.0)


def m_power(x, a, b):
    """Степенная модель y = a·x^b."""
    return a * x ** b


def m_hyper(x, a, c):
    """Гипербола со сдвигом y = a/(x − c)."""
    return a / (x - c)


def m_exp(x, a, b, c):
    """Экспонента с асимптотой y = a·exp(−b·x) + c."""
    return a * np.exp(-b * x) + c


def t1z2():
    xmin = X2.min()
    # линеаризация y^(-3/2) = a^(-3/2)·ln x − a^(-3/2)·ln b
    # даёт b > min(x) — недопустимо
    k, m = np.polyfit(np.log(X2), Y2 ** -1.5, 1)
    a_lin, b_lin = k ** (-2.0 / 3.0), np.exp(-m / k)
    # начальное приближение: при фиксированном b модель линейна по a,
    # a(b) = Σg·y/Σg²; перебор b на сетке (0; min x) и выбор b с минимальной SSE
    b_grid = np.linspace(0.001, 0.999 * xmin, 2000)
    sse_grid = []
    for b in b_grid:
        g = np.log(X2 / b) ** (-2.0 / 3.0)
        sse_grid.append(sse(Y2, (g @ Y2) / (g @ g) * g))
    b0 = b_grid[int(np.argmin(sse_grid))]
    g = np.log(X2 / b0) ** (-2.0 / 3.0)
    a0 = (g @ Y2) / (g @ g)
    specs = {
        "given": (m_given, [a0, b0], ([0, 1e-6], [10, 0.999 * xmin])),   # b < min(x)
        "power": (m_power, [0.05, -1.0], (-np.inf, np.inf)),
        "hyper": (m_hyper, [0.05, 0.1], ([0, -1], [10, 0.999 * xmin])),   # c < min(x)
        "exp":   (m_exp, [1.0, 5.0, 0.05], (-np.inf, np.inf)),
    }
    n, fits = len(X2), {}
    for name, (f, p0, bounds) in specs.items():
        popt, pcov = curve_fit(f, X2, Y2, p0=p0, bounds=bounds, maxfev=20000,
                               ftol=1e-15, xtol=1e-15, gtol=1e-15)
        yf = f(X2, *popt)
        kpar, s = len(popt), sse(Y2, yf)
        r2 = r2_score(Y2, yf)
        fits[name] = dict(p=popt, perr=np.sqrt(np.diag(pcov)), yfit=yf, resid=Y2 - yf,
                          SSE=s, R2=r2, R2adj=1 - (1 - r2) * (n - 1) / (n - kpar),
                          AIC=n * np.log(s / n) + 2 * kpar, k=kpar)
    return dict(a0=a0, b0=b0, a_lin=a_lin, b_lin=b_lin, fits=fits)


def print_t1z2(r):
    print(f"Линеаризация: a = {r['a_lin']:.4f}, b = {r['b_lin']:.4f} кг/с > min(x) — недопустимо")
    print(f"Начальное приближение (сетка по b): a0 = {r['a0']:.4f}, b0 = {r['b0']:.4f} кг/с")
    for name, f in r["fits"].items():
        print(f"{name:6s} p = {np.array2string(f['p'], precision=5)} ± "
              f"{np.array2string(f['perr'], precision=5)}; R2 = {f['R2']:.4f}; "
              f"R2adj = {f['R2adj']:.4f}; SSE = {f['SSE']:.5f}; AIC = {f['AIC']:.2f}")


T1Z2_LABELS = {"given": r"Заданная: $a\cdot(\ln(x/b))^{-2/3}$", "power": r"Степенная: $a\cdot x^{b}$",
               "hyper": r"Гипербола: $a/(x - c)$", "exp": r"Экспонента: $a\cdot e^{-b\cdot x} + c$"}


def plot_t1z2(r):
    xx = np.linspace(0.27, 1.40, 300)
    funcs = {"given": m_given, "power": m_power, "hyper": m_hyper, "exp": m_exp}
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    ax.plot(X2, Y2, "ko", ms=6, label="Эксперимент", zorder=5)
    for i, (name, f) in enumerate(funcs.items()):
        ax.plot(xx, f(xx, *r["fits"][name]["p"]), LINES[i], color=COLORS[i],
                label=f"{T1Z2_LABELS[name]} (R² = {r['fits'][name]['R2']:.3f})".replace(".", ","))
    ax.set_xlabel("Расход пара x, кг/с")
    ax.set_ylabel("Содержание воды в дистилляте y, доли")
    ax.legend(fontsize=8.5)
    p1 = finish(fig, "t1z2_models.png")
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.axhline(0, color="#52514e", lw=0.8)
    for i, name in enumerate(funcs):
        ax.plot(X2, r["fits"][name]["resid"], LINES[i], marker=MARKERS[i], color=COLORS[i],
                ms=5, lw=1.0, label=T1Z2_LABELS[name].split(":")[0])
    ax.set_xlabel("Расход пара x, кг/с")
    ax.set_ylabel(r"Остаток $y - y_{\mathrm{мод}}$, доли")
    ax.legend(fontsize=8.5, ncol=2)
    p2 = finish(fig, "t1z2_resid.png")
    return p1, p2


# %% [markdown]
# ### Задание 3. Уравнение Аррениуса

# %% Т1 З3: линеаризация ln k = ln A − Ea/(R·T)
T3_t = np.arange(100.0, 501.0, 50.0)                                     # t, °C
T3_k = np.array([0.01, 0.10, 0.25, 0.78, 1.68, 2.98, 4.66, 8.94, 25.13])  # k, 1/с


def arrhenius(T, A, Ea):
    return A * np.exp(-Ea / (R * T))


def t1z3():
    TK = T3_t + 273.15                                   # перевод в кельвины
    # МНК для прямой ln k = b0 + b1/T
    lr = stats.linregress(1.0 / TK, np.log(T3_k))
    Ea, A = -lr.slope * R, np.exp(lr.intercept)
    tq = stats.t.ppf(0.975, len(TK) - 2)                 # квантиль Стьюдента, 95 %
    lnk_fit = lr.intercept + lr.slope / TK
    k_fit = np.exp(lnk_fit)
    lr_in = stats.linregress(1.0 / TK[1:-1], np.log(T3_k[1:-1]))   # без 100 и 500 °C
    # нелинейный МНК по k
    popt, _ = curve_fit(arrhenius, TK, T3_k, p0=[A, Ea], maxfev=20000)
    k_nl = arrhenius(TK, *popt)
    return dict(TK=TK, Ea=Ea, A=A, Ea_ci=tq * lr.stderr * R,
                lnA_ci=tq * lr.intercept_stderr, R2_ln=lr.rvalue ** 2,
                R2_k=r2_score(T3_k, k_fit), k_fit=k_fit,
                resid_ln=np.log(T3_k) - lnk_fit, ratio=T3_k / k_fit,
                Ea_in=-lr_in.slope * R, A_in=np.exp(lr_in.intercept),
                R2_in=lr_in.rvalue ** 2, A_nl=popt[0], Ea_nl=popt[1],
                R2_nl_k=r2_score(T3_k, k_nl),
                R2_nl_ln=r2_score(np.log(T3_k), np.log(k_nl)))


def print_t1z3(r):
    print(f"Ea = {r['Ea']/1000:.2f} ± {r['Ea_ci']/1000:.2f} кДж/моль; A = {r['A']:.4g} 1/с "
          f"(ln A = {np.log(r['A']):.3f} ± {r['lnA_ci']:.3f})")
    print(f"R2 (ln k) = {r['R2_ln']:.4f}; R2 (k) = {r['R2_k']:.4f}")
    print("Остатки ln k:", np.array2string(r["resid_ln"], precision=3))
    print(f"Без крайних точек: Ea = {r['Ea_in']/1000:.2f} кДж/моль, A = {r['A_in']:.4g} 1/с, R2 = {r['R2_in']:.4f}")
    print(f"Нелинейный МНК по k: Ea = {r['Ea_nl']/1000:.2f} кДж/моль, A = {r['A_nl']:.4g} 1/с, "
          f"R2(k) = {r['R2_nl_k']:.4f}, R2(ln k) = {r['R2_nl_ln']:.4f}")


def plot_t1z3(r):
    TK = r["TK"]
    xx = np.linspace(TK.min() - 5, TK.max() + 5, 300)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.0, 3.9))
    a1.plot(1000 / TK, np.log(T3_k), "ko", ms=6, label="Эксперимент")
    a1.plot(1000 / xx, np.log(arrhenius(xx, r["A"], r["Ea"])), LINES[0], color=COLORS[0],
            label="МНК по всем точкам")
    a1.plot(1000 / xx, np.log(arrhenius(xx, r["A_in"], r["Ea_in"])), LINES[1], color=COLORS[1],
            label="Без 100 и 500 °C")
    a1.set_xlabel("1000/T, 1/К")
    a1.set_ylabel("ln k (k в 1/с)")
    a1.legend(fontsize=8.5)
    a2.plot(TK - 273.15, T3_k, "ko", ms=6, label="Эксперимент")
    a2.plot(xx - 273.15, arrhenius(xx, r["A"], r["Ea"]), LINES[0], color=COLORS[0],
            label="Линеаризация (все точки)")
    a2.plot(xx - 273.15, arrhenius(xx, r["A_nl"], r["Ea_nl"]), LINES[2], color=COLORS[2],
            label="Нелинейный МНК по k")
    a2.set_xlabel("t, °C")
    a2.set_ylabel("k, 1/с")
    a2.legend(fontsize=8.5)
    return finish(fig, "t1z3_arrhenius.png")


# %% [markdown]
# ### Задание 4. Вязкость гексана: полиномы 1–3 степени

# %% Т1 З4: серия полиномиальных моделей
# T, К и динамическая вязкость гексана μ, мПа·с
T4_T = np.array([250, 260, 270, 280, 290, 300, 310, 320, 330, 350, 370, 390.0])
T4_mu = np.array([0.497, 0.426, 0.397, 0.355, 0.320, 0.290, 0.264, 0.241, 0.221,
                  0.190, 0.158, 0.132])


def t1z4():
    n, models = len(T4_T), {}
    for deg in (1, 2, 3):
        p = np.polyfit(T4_T, T4_mu, deg)
        f = np.polyval(p, T4_T)
        s, r2, kp = sse(T4_mu, f), r2_score(T4_mu, f), deg + 1
        # перекрёстная проверка «без одной точки»
        press = 0.0
        for i in range(n):
            m = np.arange(n) != i
            p_i = np.polyfit(T4_T[m], T4_mu[m], deg)
            press += (T4_mu[i] - np.polyval(p_i, T4_T[i])) ** 2
        models[deg] = dict(p=p, fit=f, resid=T4_mu - f, SSE=s, R2=r2,
                           R2adj=1 - (1 - r2) * (n - 1) / (n - kp),
                           S=np.sqrt(s / (n - kp)), PRESS=press)
    # F-критерий значимости добавления члена степени 3 к полиному степени 2
    F = (models[2]["SSE"] - models[3]["SSE"]) / (models[3]["SSE"] / (n - 4))
    Fcrit = stats.f.ppf(0.95, 1, n - 4)
    # уравнение Андраде ln(mu) = A + B/T — физически обоснованная альтернатива
    B_, A_ = np.polyfit(1 / T4_T, np.log(T4_mu), 1)
    mu_and = np.exp(A_ + B_ / T4_T)
    # проверка подозрительной точки 260 К
    m = T4_T != 260
    B2, A2 = np.polyfit(1 / T4_T[m], np.log(T4_mu[m]), 1)
    p3m = np.polyfit(T4_T[m], T4_mu[m], 3)
    return dict(models=models, F=F, Fcrit=Fcrit, andrade=(A_, B_),
                R2_and=r2_score(T4_mu, mu_and), SSE_and=sse(T4_mu, mu_and),
                mu260_and=np.exp(A2 + B2 / 260), mu260_p3=np.polyval(p3m, 260))


def print_t1z4(r):
    for deg, d in r["models"].items():
        print(f"Степень {deg}: p = {np.array2string(d['p'], precision=6)}")
        print(f"   R2 = {d['R2']:.5f}; R2adj = {d['R2adj']:.5f}; SSE = {d['SSE']:.3e}; "
              f"S = {d['S']:.4f} мПа·с; PRESS = {d['PRESS']:.3e}")
    print(f"F(3 против 2) = {r['F']:.2f}; Fкрит(0,95; 1; 8) = {r['Fcrit']:.2f}")
    print(f"Андраде: ln mu = {r['andrade'][0]:.4f} + {r['andrade'][1]:.2f}/T; "
          f"R2 = {r['R2_and']:.5f}; SSE = {r['SSE_and']:.3e}")
    print(f"Ожидаемое mu(260 К) без этой точки: Андраде {r['mu260_and']:.3f}, "
          f"полином 3 {r['mu260_p3']:.3f} мПа·с (в таблице 0.426)")


def plot_t1z4(r):
    TT = np.linspace(245, 395, 300)
    fig, ax = plt.subplots(figsize=(6.5, 4.3))
    ax.plot(T4_T, T4_mu, "ko", ms=6, label="Эксперимент", zorder=5)
    for i, deg in enumerate((1, 2, 3)):
        d = r["models"][deg]
        ax.plot(TT, np.polyval(d["p"], TT), LINES[i], color=COLORS[i],
                label=f"Полином {deg}-й степени (R² = {d['R2']:.4f})".replace(".", ","))
    ax.set_xlabel("T, К")
    ax.set_ylabel("Динамическая вязкость μ, мПа∙с")
    ax.legend()
    p1 = finish(fig, "t1z4_visc.png")
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.axhline(0, color="#52514e", lw=0.8)
    for i, deg in enumerate((1, 2, 3)):
        ax.plot(T4_T, r["models"][deg]["resid"], LINES[i], marker=MARKERS[i], color=COLORS[i],
                ms=5, lw=1.0, label=f"Степень {deg}")
    ax.set_xlabel("T, К")
    ax.set_ylabel(r"Остаток $\mu - \mu_{\mathrm{мод}}$, мПа∙с")
    ax.legend()
    p2 = finish(fig, "t1z4_resid.png")
    return p1, p2


# %% [markdown]
# ## Тема 2. Уравнения состояния и расчёт однофазных потоков

# %% Т2: кубические уравнения состояния (ИГ, RK, SRK) + контроль по Ли–Кеслеру
# Tc, К; Pc, атм; ω — справочник Refining & Chemicals (IFP Training), табл. A2
CRIT = {
    "NH3": (405.6, 111.3, 0.250),
    "CO2": (304.2, 72.8, 0.225),
    "O2": (154.6, 49.8, 0.021),
    "N2": (126.2, 33.5, 0.040),
}


def eos_ab(Tc, Pc_atm, w, T, eos):
    """Параметры a (Па·м6/моль2) и b (м3/моль) уравнений RK и SRK."""
    Pc = Pc_atm * ATM
    Tr = T / Tc
    if eos == "RK":
        alpha = Tr ** -0.5
    else:                                            # SRK (Соаве)
        m = 0.480 + 1.574 * w - 0.176 * w ** 2
        alpha = (1 + m * (1 - Tr ** 0.5)) ** 2
    a = 0.42748 * R ** 2 * Tc ** 2 / Pc * alpha
    b = 0.08664 * R * Tc / Pc
    return a, b


def cubic_volume(a, b, T, P):
    """Корни P·v^3 − R·T·v^2 + (a − P·b^2 − R·T·b)·v − a·b = 0 и физичный корень."""
    roots = np.roots([P, -R * T, a - P * b ** 2 - R * T * b, -a * b])
    real = np.sort(roots[np.abs(roots.imag) < 1e-9 * np.abs(roots).max()].real)
    # объём больше собственного объёма молекул
    phys = real[real > b]
    # газ — наибольший действительный корень
    v = phys.max()
    return v, roots, real


# Константы обобщённого уравнения Ли–Кеслера (Lee, Kesler, AIChE J., 1975)
LK_SIMPLE = dict(b=(0.1181193, 0.265728, 0.154790, 0.030323),
                 c=(0.0236744, 0.0186984, 0.0, 0.042724),
                 d=(0.155488e-4, 0.623689e-4), beta=0.65392, gamma=0.060167)
LK_REF = dict(b=(0.2026579, 0.331511, 0.027655, 0.203488),
              c=(0.0313385, 0.0503618, 0.016901, 0.041577),
              d=(0.48736e-4, 0.0740336e-4), beta=1.226, gamma=0.03754)


def _lk_z(Tr, Pr, c):
    b1, b2, b3, b4 = c["b"]
    c1, c2, c3, c4 = c["c"]
    d1, d2 = c["d"]
    B = b1 - b2 / Tr - b3 / Tr ** 2 - b4 / Tr ** 3
    C = c1 - c2 / Tr + c3 / Tr ** 3
    D = d1 + d2 / Tr

    def f(Vr):
        g = c["gamma"] / Vr ** 2
        Z = (1 + B / Vr + C / Vr ** 2 + D / Vr ** 5
             + c4 / (Tr ** 3 * Vr ** 2) * (c["beta"] + g) * np.exp(-g))
        return Z - Pr * Vr / Tr
    grid = np.geomspace(3 * Tr / Pr, 0.05, 3000)     # от «газовых» объёмов к малым
    vals = np.array([f(v) for v in grid])
    i = np.nonzero(np.sign(vals[:-1]) != np.sign(vals[1:]))[0][0]
    Vr = brentq(f, grid[i + 1], grid[i])
    return Pr * Vr / Tr


def lee_kesler_z(Tr, Pr, w):
    """Z = Z0 + ω·Zcorr (простое вещество + поправка по н-октану, ωr = 0,3978)."""
    z0 = _lk_z(Tr, Pr, LK_SIMPLE)
    zr = _lk_z(Tr, Pr, LK_REF)
    return z0 + w / 0.3978 * (zr - z0), z0, (zr - z0) / 0.3978


def t2z1(T=450.0, P_atm=80.0):
    P = P_atm * ATM
    Tc, Pc, w = CRIT["NH3"]
    res = {"ИГ": dict(v=R * T / P)}
    for eos in ("RK", "SRK"):
        a, b = eos_ab(Tc, Pc, w, T, eos)
        v, roots, real = cubic_volume(a, b, T, P)
        res[eos] = dict(a=a, b=b, v=v, roots=roots, real=real)
    Z, z0, zc = lee_kesler_z(T / Tc, P_atm / Pc, w)
    res["LK"] = dict(v=Z * R * T / P, z0=z0, zcorr=zc)
    for d in res.values():
        d["Z"] = P * d["v"] / (R * T)
        d["v_L"] = d["v"] * 1000                      # м3/моль -> л/моль
    return dict(T=T, P=P, P_atm=P_atm, Tr=T / Tc, Pr=P_atm / Pc, res=res)


def t2z2(T=420.0, P_atm=150.0):
    P = P_atm * ATM
    names = ["CO2", "O2", "N2"]
    # 25 % CO2, O2 : N2 = 1 : 3
    y = np.array([0.25, 0.75 * 1 / 4, 0.75 * 3 / 4])
    res = {"ИГ": dict(v=R * T / P)}
    for eos in ("RK", "SRK"):
        ab = np.array([eos_ab(*CRIT[n], T, eos) for n in names])
        ai, bi = ab[:, 0], ab[:, 1]
        # правило смешения для a
        a = np.sum(y * np.sqrt(ai)) ** 2
        # правило смешения для b
        b = np.sum(y * bi)
        v, roots, real = cubic_volume(a, b, T, P)
        res[eos] = dict(ai=ai, bi=bi, a=a, b=b, v=v, roots=roots, real=real)
    Tpc = sum(yi * CRIT[n][0] for yi, n in zip(y, names))      # правило Кея
    Ppc = sum(yi * CRIT[n][1] for yi, n in zip(y, names))
    wm = sum(yi * CRIT[n][2] for yi, n in zip(y, names))
    Z, z0, zc = lee_kesler_z(T / Tpc, P_atm / Ppc, wm)
    res["LK"] = dict(v=Z * R * T / P, z0=z0, zcorr=zc)
    for d in res.values():
        d["Z"] = P * d["v"] / (R * T)
        d["v_L"] = d["v"] * 1000
    return dict(T=T, P=P, P_atm=P_atm, y=y, names=names, Tpc=Tpc, Ppc=Ppc, w=wm,
                Tpr=T / Tpc, Ppr=P_atm / Ppc, res=res)


def print_t2(r, title):
    print(title, f"T = {r['T']} К, P = {r['P_atm']} атм = {r['P']/MPA:.4f} МПа")
    for k, d in r["res"].items():
        extra = ""
        if "roots" in d:
            extra = f"; a = {d['a']:.5f} Па·м6/моль2; b = {d['b']:.4e} м3/моль; корни v, л/моль: " + \
                    np.array2string(d["roots"] * 1000, precision=4)
        print(f"{k:4s}: v = {d['v_L']:.4f} л/моль = {d['v']:.4e} м3/моль; Z = {d['Z']:.4f}{extra}")


def plot_t2(r1, r2):
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8))
    for ax, r, title in ((axes[0], r1, "Аммиак: 80 атм, 450 К"),
                         (axes[1], r2, "Смесь CO₂–O₂–N₂: 150 атм, 420 К")):
        Z = np.linspace(-0.05, 1.25, 400)
        for i, eos in enumerate(("RK", "SRK")):
            d = r["res"][eos]
            A = d["a"] * r["P"] / (R * r["T"]) ** 2
            B = d["b"] * r["P"] / (R * r["T"])
            f = Z ** 3 - Z ** 2 + (A - B - B ** 2) * Z - A * B
            ax.plot(Z, f, LINES[i], color=COLORS[i], label=f"{eos}: корень Z = {d['Z']:.4f}".replace(".", ","))
            ax.plot(d["Z"], 0, MARKERS[i], color=COLORS[i], ms=7)
        ax.axhline(0, color="#52514e", lw=0.8)
        ax.set_xlabel("Коэффициент сжимаемости Z")
        ax.set_ylabel("f(Z)")
        ax.set_title(title, fontsize=10)
        ax.legend(fontsize=8.5)
    return finish(fig, "t2_cubic.png")


# %% [markdown]
# ## Тема 3. Расчёт фазовых равновесий (корреляция McWilliams)

# %% Т3: константы фазового равновесия K(T, P) и однократное испарение
# A, B, C, D, форма: ln K = −A/T^2 + B − C·ln P + D/P^2 (1) или + D/P (2);
# T в °R, P в psia
MCW = {
    "CH4": (292860.0, 8.2445, 0.8951, 59.8465, 1),
    "C2H6": (687248.2, 7.90694, 0.866, 49.02654, 1),
    "C3H8": (970688.6, 7.15059, 0.76984, 6.90224, 2),
    "i-C4H10": (1166846.0, 7.72668, 0.92213, 0.0, 1),
    "n-C4H10": (1280557.0, 7.94986, 0.96455, 0.0, 1),
    "n-C5H12": (1524891.0, 7.33129, 0.89143, 0.0, 1),
}


def k_mcw(names, T_K, P_Pa):
    """Константы фазового равновесия McWilliams; вход в К и Па, внутри °R и psia."""
    TR, Pp = 1.8 * T_K, P_Pa / PSI
    K = []
    for n in names:
        A, B, C, D, form = MCW[n]
        last = D / Pp ** 2 if form == 1 else D / Pp
        K.append(np.exp(-A / TR ** 2 + B - C * np.log(Pp) + last))
    return np.array(K)


def bubble_T(x, names, P):
    """Температура начала кипения: ln(Σ K_i·x_i) = 0."""
    f = lambda T: np.log(np.sum(k_mcw(names, T, P) * x))
    return brentq(f, 120.0, 700.0, xtol=1e-12)


def dew_T(y, names, P):
    """Температура конца кипения (начала конденсации): ln(Σ y_i/K_i) = 0."""
    f = lambda T: np.log(np.sum(y / k_mcw(names, T, P)))
    return brentq(f, 120.0, 900.0, xtol=1e-12)


T3Z1_NAMES = ["CH4", "C2H6", "C3H8", "n-C5H12"]
T3Z1_Z = np.array([0.15, 0.30, 0.35, 0.20])


def t3z1(P_atm=14.0):
    P = P_atm * ATM
    Tb, Td = bubble_T(T3Z1_Z, T3Z1_NAMES, P), dew_T(T3Z1_Z, T3Z1_NAMES, P)
    Kb, Kd = k_mcw(T3Z1_NAMES, Tb, P), k_mcw(T3Z1_NAMES, Td, P)
    return dict(P=P, P_psia=P / PSI, Tb=Tb, Td=Td, tb=Tb - 273.15, td=Td - 273.15,
                Kb=Kb, Kd=Kd, y_bubble=Kb * T3Z1_Z, x_dew=T3Z1_Z / Kd,
                res_b=np.sum(Kb * T3Z1_Z) - 1, res_d=np.sum(T3Z1_Z / Kd) - 1)


def print_t3z1(r):
    print(f"P = {r['P']/MPA:.4f} МПа = {r['P_psia']:.2f} psia")
    print(f"t начала кипения = {r['tb']:.2f} °C (T = {r['Tb']:.2f} К); невязка {r['res_b']:.1e}")
    print(f"t конца кипения  = {r['td']:.2f} °C (T = {r['Td']:.2f} К); невязка {r['res_d']:.1e}")
    print("Состав первого пузырька пара y:", np.array2string(r["y_bubble"], precision=4))
    print("Состав первой капли жидкости x:", np.array2string(r["x_dew"], precision=4))


def plot_t3z1(r):
    t = np.linspace(-80, 120, 400)
    sK = [np.sum(k_mcw(T3Z1_NAMES, ti + 273.15, r["P"]) * T3Z1_Z) for ti in t]
    sY = [np.sum(T3Z1_Z / k_mcw(T3Z1_NAMES, ti + 273.15, r["P"])) for ti in t]
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.semilogy(t, sK, LINES[0], color=COLORS[0], label=r"$\sum K_i \cdot x_i$ (условие начала кипения)")
    ax.semilogy(t, sY, LINES[1], color=COLORS[1], label=r"$\sum y_i / K_i$ (условие конца кипения)")
    ax.axhline(1, color="#52514e", lw=0.9)
    for tt, lab in ((r["tb"], r"$t_{\mathrm{нк}}$"), (r["td"], r"$t_{\mathrm{кк}}$")):
        ax.axvline(tt, color="#52514e", ls=":", lw=1.0)
        ax.annotate(f"{lab} = {tt:.1f} °C".replace(".", ",").replace("-", "−"),
                    (tt, 1), xytext=(5, 12), textcoords="offset points", fontsize=9)
    ax.set_xlabel("t, °C")
    ax.set_ylabel("Значение суммы (лог. шкала)")
    ax.legend(fontsize=8.5, loc="upper center")
    return finish(fig, "t3z1_tb_td.png")


# %% Т3 З2: сепарационный блок С1 -> С2 -> С3 (уравнение Рачфорда–Райса)
SEP_NAMES = ["CH4", "C2H6", "C3H8", "i-C4H10", "n-C4H10", "n-C5H12"]
SEP_Z = np.array([0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706])
SEP_BASE = [(9.8 * MPA, 40.8 + 273.15),     # (P, Па; T, К) для С1, С2, С3
            (8.7 * MPA, 12.8 + 273.15),
            (8.7 * MPA, -40.8 + 273.15)]


def rachford_rice(z, K):
    """Решение Σ z_i·(K_i − 1)/(1 + e·(K_i − 1)) = 0 на интервале между асимптотами.
    Возвращает (e, e_формальное, состояние); e вне [0; 1] — однофазная смесь."""
    f = lambda e: np.sum(z * (K - 1) / (1 + e * (K - 1)))
    if K.max() <= 1:
        return 0.0, -np.inf, "жидкость"
    if K.min() >= 1:
        return 1.0, np.inf, "газ"
    lo, hi = 1 / (1 - K.max()), 1 / (1 - K.min())   # асимптоты функции РР
    eps = 1e-12 * (hi - lo)
    e_formal = brentq(f, lo + eps, hi - eps, xtol=1e-15)
    # Σ z·K ≤ 1: переохлаждённая жидкость
    if e_formal <= 0:
        return 0.0, e_formal, "жидкость"
    if e_formal >= 1:                                 # Σ z/K ≤ 1: перегретый газ
        return 1.0, e_formal, "газ"
    return e_formal, e_formal, "двухфазная"


def flash(z, T, P, names=SEP_NAMES):
    K = k_mcw(names, T, P)
    e, e_formal, state = rachford_rice(z, K)
    if state == "двухфазная":
        x = z / (1 + e * (K - 1))
        y = K * x
    elif state == "газ":
        x, y = np.full_like(z, np.nan), z.copy()
    else:
        x, y = z.copy(), np.full_like(z, np.nan)
    return dict(K=K, e=e, e_formal=e_formal, state=state, x=x, y=y,
                rr=(np.sum(z * (K - 1) / (1 + e * (K - 1)))
                    if state == "двухфазная" else np.nan))


def separator_train(conds, z=SEP_Z, F=1.0):
    """Газ каждого сепаратора — питание следующего. F — моль сырья (на 1 моль)."""
    out, feed = [], z
    for (P, T) in conds:
        s = flash(feed, T, P)
        s.update(F=F, z=feed, P=P, T=T, V=F * s["e"], L=F * (1 - s["e"]))
        out.append(s)
        F, feed = s["V"], s["y"]
    return out


def train_summary(tr, z=SEP_Z):
    """Показатели блока: выход и состав газа С3, извлечение C3H8, потери CH4."""
    # покомпонентно, моль/моль сырья
    liq = sum(s["L"] * np.nan_to_num(s["x"]) for s in tr)
    # если С3 весь в жидкости — газа нет
    gas = tr[-1]["V"] * np.nan_to_num(tr[-1]["y"])
    rec = liq / z
    return dict(e=[s["e"] for s in tr], states=[s["state"] for s in tr],
                V_out=tr[-1]["V"], y_out=tr[-1]["y"],
                yC3plus=float(np.sum(tr[-1]["y"][2:])),
                rec_C3=rec[2], loss_CH4=rec[0],
                rec_C4plus=float(np.sum(liq[3:]) / np.sum(z[3:])),
                sharp=rec[2] - rec[0], closure=float(np.max(np.abs(liq + gas - z))))


def t3z2_base():
    tr = separator_train(SEP_BASE)
    return dict(train=tr, summary=train_summary(tr))


def p_dew_at(y, T, names=SEP_NAMES):
    """Давление начала конденсации газа состава y при температуре T: Σ y_i/K_i = 1."""
    return brentq(lambda P: np.sum(y / k_mcw(names, T, P)) - 1, 0.2 * MPA, 30 * MPA)


def t3z2_study(P2_grid=None, rule="P3=P2"):
    """Влияние давления во втором сепараторе. Газ идёт С2 -> С3 без компрессора,
    поэтому P3 ≤ P2; основное правило P3 = P2 (как в базе); P2 ≤ P1 = 9,8 МПа."""
    if P2_grid is None:
        P2_grid = np.round(np.arange(4.0, 9.8 + 1e-9, 0.1), 2)
    rows = []
    for P2 in P2_grid:
        P3 = P2 if rule == "P3=P2" else min(P2, 8.7)
        conds = [SEP_BASE[0], (P2 * MPA, SEP_BASE[1][1]), (P3 * MPA, SEP_BASE[2][1])]
        tr = separator_train(conds)
        s = train_summary(tr)
        s.update(P2=P2, P3=P3, e_formal=[t["e_formal"] for t in tr])
        rows.append(s)
    # газ С1 (не зависит от P2)
    y1 = separator_train(SEP_BASE[:1])[0]["y"]
    # ниже — С2 однофазен (газ)
    P2_dew = p_dew_at(y1, SEP_BASE[1][1]) / MPA
    return dict(rows=rows, P2_dew=P2_dew, rule=rule)


def print_t3z2(base, study):
    for j, s in enumerate(base["train"], 1):
        print(f"С{j}: P = {s['P']/MPA:.1f} МПа, t = {s['T']-273.15:.1f} °C, питание F = {s['F']:.5f}; "
              f"{s['state']}; e = {s['e']:.5f}; невязка РР = {s['rr']:.1e}")
        print("    K =", np.array2string(s["K"], precision=4))
        print("    x =", np.array2string(s["x"], precision=5), " Σx =", f"{np.sum(s['x']):.10f}")
        print("    y =", np.array2string(s["y"], precision=5), " Σy =", f"{np.sum(s['y']):.10f}")
    b = base["summary"]
    print(f"Газ С3: {b['V_out']:.4f} моль/моль сырья; извлечение C3H8 в жидкость {b['rec_C3']*100:.2f} %; "
          f"метан в жидкости {b['loss_CH4']*100:.2f} %; невязка МБ {b['closure']:.1e}")
    print(f"Давление начала конденсации газа С1 при 12,8 °C: P2* = {study['P2_dew']:.3f} МПа")
    print(" P2   e1     e2     e3     V_out   yC3+,%  rec_C3,%  CH4_liq,%  Ч")
    for s in study["rows"]:
        if abs(s["P2"] * 2 - round(s["P2"] * 2)) < 1e-9 or abs(s["P2"] - 9.8) < 1e-9:
            print(f"{s['P2']:4.1f} {s['e'][0]:.4f} {s['e'][1]:.4f} {s['e'][2]:.4f} {s['V_out']:.4f} "
                  f"{s['yC3plus']*100:6.3f} {s['rec_C3']*100:8.3f} {s['loss_CH4']*100:9.3f} {s['sharp']:.4f}")


def plot_t3z2(base, study, P2_choice):
    rows = study["rows"]
    P2 = np.array([s["P2"] for s in rows])
    fig, axs = plt.subplots(2, 2, figsize=(9.0, 6.8))
    a = axs[0, 0]
    for j in range(3):
        a.plot(P2, [s["e"][j] for s in rows], LINES[j], color=COLORS[j], label=f"Сепаратор С{j+1}")
    a.set_ylabel("Доля отгона e, моль/моль")
    a.legend(fontsize=8.5)
    a = axs[0, 1]
    a.plot(P2, [s["V_out"] for s in rows], LINES[0], color=COLORS[0])
    a.set_ylabel("Выход газа С3, моль/моль сырья")
    a = axs[1, 0]
    a.plot(P2, [s["rec_C3"] * 100 for s in rows], LINES[0], color=COLORS[0], label="Извлечение C₃H₈ в жидкость")
    a.plot(P2, [s["loss_CH4"] * 100 for s in rows], LINES[1], color=COLORS[1], label="Доля CH₄, ушедшая в жидкость")
    a.set_ylabel("Доля от количества в сырье, %")
    a.legend(fontsize=8.5)
    a = axs[1, 1]
    a.plot(P2, [s["yC3plus"] * 100 for s in rows], LINES[0], color=COLORS[0])
    a.set_ylabel("Содержание C₃₊ в газе С3, % мол.")
    for a in axs.flat:
        h1 = a.axvline(8.7, color="#52514e", ls=":", lw=1.0)
        h2 = a.axvline(P2_choice, color=COLORS[2], ls="--", lw=1.0)
        h3 = a.axvspan(4.0, study["P2_dew"], color="#f0efec", zorder=0)
        a.set_xlabel("Давление во втором сепараторе P2, МПа")
        a.set_xlim(3.8, 10.0)
    axs[1, 1].legend([h1, h2, h3], ["Базовый режим 8,7 МПа", f"Рекомендуемый {P2_choice:.1f} МПа".replace(".", ","),
                                    "С2 однофазен (газ)"], fontsize=8.5)
    return finish(fig, "t3z2_p2.png")


def plot_t3z2_rr(base):
    fig, ax = plt.subplots(figsize=(6.5, 3.9))
    e = np.linspace(0, 1, 400)
    for j, s in enumerate(base["train"]):
        f = [np.sum(s["z"] * (s["K"] - 1) / (1 + ei * (s["K"] - 1))) for ei in e]
        ax.plot(e, f, LINES[j], color=COLORS[j], label=f"С{j+1}: e = {s['e']:.4f}".replace(".", ","))
        ax.plot(s["e"], 0, MARKERS[j], color=COLORS[j], ms=7)
    ax.axhline(0, color="#52514e", lw=0.8)
    ax.set_ylim(-3, 1.5)
    ax.set_xlabel("Доля отгона e, моль/моль")
    ax.set_ylabel("Функция Рачфорда–Райса f(e)")
    ax.legend(fontsize=8.5)
    return finish(fig, "t3z2_rr.png")


def _box(ax, x, y, w, h, text, fc="#ffffff"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec="#0b0b0b", lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=10, fontweight="bold")


def _arrow(ax, pts, text=None, tpos=None, fs=8.5, ha="center"):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color="#0b0b0b", lw=1.1)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="-|>", color="#0b0b0b", lw=1.1))
    if text:
        ax.text(*tpos, text, fontsize=fs, ha=ha, va="center")


def _c(v, nd=4):
    return f"{v:.{nd}f}".replace(".", ",")


def plot_t3z2_scheme(base):
    tr = base["train"]
    fig, ax = plt.subplots(figsize=(9.0, 3.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")
    xs = [3.0, 6.3, 9.6]
    for j, x in enumerate(xs):
        s = tr[j]
        _box(ax, x, 2.5, 0.9, 2.0, f"С{j+1}")
        ax.text(x, 3.75 if j != 1 else 1.2, "", fontsize=8)
        ax.text(x + 0.55, 1.95, f"{_c(s['P']/MPA,1)} МПа\n{_c(s['T']-273.15,1)} °C".replace("-", "−"),
                fontsize=8, va="center")
        _arrow(ax, [(x, 1.5), (x, 0.5)], f"L{j+1} = {_c(s['L'])}", (x + 0.12, 0.65), ha="left")
    _arrow(ax, [(0.3, 2.5), (2.55, 2.5)], "Сырьё\nF = 1 моль", (1.3, 3.05))
    # газ С1 -> вход С2, газ С2 -> вход С3
    for j in (0, 1):
        xa, xb = xs[j], xs[j + 1]
        _arrow(ax, [(xa, 3.5), (xa, 4.3), (xb - 1.0, 4.3), (xb - 1.0, 2.9), (xb - 0.45, 2.9)],
               f"V{j+1} = {_c(tr[j]['V'])}", ((xa + xb - 1.0) / 2, 4.55))
    _arrow(ax, [(xs[2], 3.5), (xs[2], 4.3), (11.7, 4.3)], f"Газ V3 = {_c(tr[2]['V'])}", (10.7, 4.6))
    ax.text(0.3, 0.2, "Расходы, моль на 1 моль сырья", fontsize=8, color="#52514e")
    return finish(fig, "t3z2_scheme.png")


# %% [markdown]
# ## Тема 4. Расчёт химического равновесия

# %% Т4 З1: синтез аммиака 1/2 N2 + 3/2 H2 <=> NH3
def t4z1(Kp=0.05, P_atm=220.0, n0=(1.1, 3.0, 0.2)):
    n0 = np.array(n0)                       # N2, H2, NH3, моль
    nu = np.array([-0.5, -1.5, 1.0])        # стехиометрические коэффициенты

    def f(xi):                              # xi — степень полноты реакции, моль
        n = n0 + nu * xi
        y = n / n.sum()
        return y[2] / (y[0] ** 0.5 * y[1] ** 1.5) / P_atm - Kp
    xi_max = min(-n0[0] / nu[0], -n0[1] / nu[1])        # до исчерпания H2 (2 моль)
    xi_min = -n0[2]                                     # до исчезновения NH3
    grid = np.linspace(xi_min + 1e-9, xi_max - 1e-9, 2001)
    sgn = np.sign([f(g) for g in grid])
    roots = int(np.sum(sgn[:-1] != sgn[1:]))             # число смен знака на сетке
    xi = brentq(f, xi_min + 1e-12, xi_max - 1e-12, xtol=1e-15)
    n = n0 + nu * xi
    return dict(n0=n0, n=n, y=n / n.sum(), xi=xi, residual=f(xi), n_roots=roots,
                conv_N2=0.5 * xi / n0[0], conv_H2=1.5 * xi / n0[1], f=f,
                xi_lim=(xi_min, xi_max),
                Kp=Kp, P_atm=P_atm)


def print_t4z1(r):
    print(f"Корней на допустимом интервале ({r['xi_lim'][0]}; {r['xi_lim'][1]}): {r['n_roots']}")
    print(f"xi = {r['xi']:.6f} моль; невязка = {r['residual']:.1e}")
    print("n0 =", r["n0"], "-> n =", np.array2string(r["n"], precision=5), f"Σ = {r['n'].sum():.5f}")
    print("y  =", np.array2string(r["y"], precision=5))
    print(f"Степень превращения N2 = {r['conv_N2']*100:.2f} %, H2 = {r['conv_H2']*100:.2f} %")


def plot_t4z1(r):
    xi = np.linspace(0.02, 1.98, 400)
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    # отношение y_NH3/(y_N2^0,5·y_H2^1,5·P)
    Kxi = [r["f"](v) + r["Kp"] for v in xi]
    ax.semilogy(xi, Kxi, LINES[0], color=COLORS[0], label="Правая часть уравнения равновесия")
    ax.axhline(r["Kp"], color="#52514e", lw=0.9, ls="--", label="Заданная K_p = 0,05 атм⁻¹".replace("K_p", "Kp"))
    ax.plot(r["xi"], r["Kp"], "o", color=COLORS[1], ms=7, label=f"Корень ξ = {r['xi']:.4f} моль".replace(".", ","))
    ax.set_xlabel("Степень полноты реакции ξ, моль")
    ax.set_ylabel("Значение, атм⁻¹ (лог. шкала)")
    ax.legend()
    return finish(fig, "t4z1_f.png")


# %% Т4 З2а: C2H6 <=> C2H4 + H2, K по справочным ΔG°f (IFP, разделы E18, E19)
# Энергии Гиббса и энтальпии образования, кал/моль (H2 — простое вещество, 0)
DGF = {"T": np.array([298.0, 400.0, 600.0, 800.0, 1000.0]),
       "C2H6": np.array([-7860.0, -3447.0, 5970.0, 15920.0, 26130.0]),
       "C2H4": np.array([16282.0, 17675.0, 20918.0, 24490.0, 28249.0]),
       "C2H2": np.array([50000.0, 48577.0, 45835.0, 43178.0, 40604.0])}
DHF = {"T": np.array([298.0, 400.0, 600.0, 800.0, 1000.0]),
       "C2H6": np.array([-20236.0, -21419.0, -23280.0, -24530.0, -25280.0]),
       "C2H4": np.array([12496.0, 11766.0, 10600.0, 9760.0, 9205.0]),
       "C2H2": np.array([54194.0, 54134.0, 53931.0, 53627.0, 53304.0])}


def k_extrap(T, prod, reac):
    """K реакции reac -> prod + H2 при T > 1000 К двумя способами экстраполяции."""
    dG = DGF[prod] - DGF[reac]                     # ΔG°r(T) по табличным точкам
    dH = DHF[prod] - DHF[reac]
    # (1) линейная экстраполяция ΔG°r по точкам 800 и 1000 К
    dG_lin = dG[-1] + (dG[-1] - dG[-2]) / 200.0 * (T - 1000.0)
    # (2) ΔH°r и ΔS°r при 1000 К считаем постоянными: ΔG = ΔH − T·ΔS
    dS = (dH[-1] - dG[-1]) / 1000.0
    dG_hs = dH[-1] - T * dS
    K_lin = np.exp(-dG_lin * CAL / (R * T))
    K_hs = np.exp(-dG_hs * CAL / (R * T))
    return dict(dG=dG, dH=dH, dS=dS, dG_lin=dG_lin, dG_hs=dG_hs,
                K_lin=K_lin, K_hs=K_hs)


def ethane_equilibrium(K, P_atm=1.0):
    """Kp = x^2/((1 − x)(1 + x))·P -> x = sqrt(K/(K + P)) для 1 моль этана."""
    x = np.sqrt(K / (K + P_atm))
    n = np.array([1 - x, x, x])                    # C2H6, C2H4, H2
    return x, n, n / n.sum()


def t4z2a(T=1100.0, P_atm=1.0):
    ke = k_extrap(T, "C2H4", "C2H6")
    K = ke["K_lin"]                                # основной вариант
    x, n, y = ethane_equilibrium(K, P_atm)
    resid = y[1] * y[2] / y[0] * P_atm - K
    sens = {}
    for name, Kv in (("lin", ke["K_lin"]), ("hs", ke["K_hs"]), ("Finlayson", 1.76)):
        sens[name] = (Kv,) + ethane_equilibrium(Kv, P_atm)[0:1]
    dxdK = 1 / (2 * x) * P_atm / (K + P_atm) ** 2
    k1367 = k_extrap(1367.0, "C2H4", "C2H6")       # контроль заданных Kp при 1367 К
    k2_1367 = k_extrap(1367.0, "C2H2", "C2H4")
    K1000 = np.exp(-ke["dG"][-1] * CAL / (R * 1000.0))
    return dict(T=T, ke=ke, K=K, x=x, n=n, y=y, residual=resid, sens=sens, dxdK=dxdK,
                K1000=K1000, K1_1367=(k1367["K_lin"], k1367["K_hs"]),
                K2_1367=(k2_1367["K_lin"], k2_1367["K_hs"]), dG2=k2_1367["dG"])


def print_t4z2a(r):
    ke = r["ke"]
    print("ΔG°r(T), кал/моль:", "; ".join(f"{T:.0f} К: {g:.0f}" for T, g in zip(DGF["T"], ke["dG"])))
    print(f"ΔH°r(1000) = {ke['dH'][-1]:.0f} кал/моль; ΔS°r(1000) = {ke['dS']:.3f} кал/(моль·К)")
    print(f"ΔG°r(1100): линейно {ke['dG_lin']:.1f}, через ΔH–ΔS {ke['dG_hs']:.1f} кал/моль")
    print(f"K(1100) = {ke['K_lin']:.4f} (лин.), {ke['K_hs']:.4f} (ΔH–ΔS); K(1000) = {r['K1000']:.4f}")
    print(f"x = {r['x']:.5f}; n = {np.array2string(r['n'], precision=5)}; y = {np.array2string(r['y'], precision=5)}; "
          f"невязка {r['residual']:.1e}")
    print("Чувствительность (K, x):", {k: tuple(round(float(v), 4) for v in t) for k, t in r["sens"].items()})
    print(f"dx/dK = {r['dxdK']:.4f}; контроль при 1367 К: K1 = {r['K1_1367'][0]:.2f}/{r['K1_1367'][1]:.2f} "
          f"(задано 37,6), K2 = {r['K2_1367'][0]:.3f}/{r['K2_1367'][1]:.3f} (задано 0,769)")


def plot_t4z2(r):
    T = DGF["T"]
    TT = np.linspace(800, 1400, 50)
    fig, ax = plt.subplots(figsize=(6.5, 4.1))
    for i, (prod, reac, lab) in enumerate((("C2H4", "C2H6", "C₂H₆ ⇄ C₂H₄ + H₂"),
                                           ("C2H2", "C2H4", "C₂H₄ ⇄ C₂H₂ + H₂"))):
        dG = (DGF[prod] - DGF[reac]) * CAL / 1000
        ax.plot(T, dG, MARKERS[i], color=COLORS[i], ms=6, label=f"{lab}: справочные точки")
        slope = (dG[-1] - dG[-2]) / 200.0
        ax.plot(TT, dG[-1] + slope * (TT - 1000), LINES[1], color=COLORS[i], lw=1.2,
                label=f"{lab}: экстраполяция")
    ax.axhline(0, color="#52514e", lw=0.8)
    for Tm in (1100, 1367):
        ax.axvline(Tm, color="#52514e", ls=":", lw=1.0)
        ax.text(Tm + 8, 70, f"{Tm} К", fontsize=8.5)
    ax.set_xlabel("T, К")
    ax.set_ylabel("ΔG°r, кДж/моль")
    ax.legend(fontsize=8)
    return finish(fig, "t4z2_dG.png")


# %% Т4 З2б: две реакции при 1367 К — система нелинейных уравнений
def t4z2b(K1=37.6, K2=0.769, P_atm=1.0):
    # v = (x1, x2): x1 — этана прореагировало, x2 — этилена
    def F(v):
        x1, x2 = v
        nt = 1 + x1 + x2
        return [(x1 - x2) * (x1 + x2) / ((1 - x1) * nt) * P_atm - K1,
                x2 * (x1 + x2) / ((x1 - x2) * nt) * P_atm - K2]
    lo, hi = [1e-12, 1e-12], [1 - 1e-12, 1 - 1e-12]          # 0 < x1, x2 < 1
    sol = least_squares(F, [0.9, 0.3], bounds=(lo, hi),
                        xtol=1e-15, ftol=1e-15, gtol=1e-15)
    x1, x2 = sol.x
    # без ограничений — для сравнения
    raw = fsolve(F, [0.9, 0.3], full_output=True)
    # перебор начальных приближений
    found = set()
    for a in np.linspace(0.05, 0.99, 15):
        for b in np.linspace(0.01, 0.98, 15):
            if b < a:
                s, info, ier, msg = fsolve(F, [a, b], full_output=True)
                if ier == 1 and 0 < s[1] < s[0] < 1 and max(map(abs, F(s))) < 1e-9:
                    found.add((round(float(s[0]), 7), round(float(s[1]), 7)))
    n = np.array([1 - x1, x1 - x2, x1 + x2, x2])        # C2H6, C2H4, H2, C2H2
    return dict(x1=x1, x2=x2, n=n, y=n / n.sum(), residual=np.array(F(sol.x)),
                fsolve_raw=raw[0], fsolve_raw_res=np.array(F(raw[0])),
                unique=sorted(found))


def print_t4z2b(r):
    print(f"least_squares (0 < x2 < x1 < 1): x1 = {r['x1']:.6f}, x2 = {r['x2']:.6f}, "
          f"невязки {np.array2string(r['residual'], precision=2)}")
    print("fsolve без ограничений из (0.9; 0.3):", np.array2string(r["fsolve_raw"], precision=4),
          "невязки", np.array2string(r["fsolve_raw_res"], precision=3))
    print("Физичные решения при переборе начальных приближений:", r["unique"])
    print("n =", np.array2string(r["n"], precision=5), f"Σ = {r['n'].sum():.5f}")
    print("y =", np.array2string(r["y"], precision=5))


# %% [markdown]
# ## Тема 5. Расчёт материальных балансов

# %% Т5 З1: схема из трёх колонн (система линейных уравнений)
T5_COMP = ["Ксилол", "Стирол", "Толуол", "Бензол"]
T5_X = {  # мольные доли: ксилол, стирол, толуол, бензол
    "F": np.array([0.15, 0.25, 0.40, 0.20]),
    "D1": np.array([0.07, 0.04, 0.54, 0.35]),
    "B1": np.array([0.18, 0.24, 0.42, 0.16]),
    "D2": np.array([0.15, 0.10, 0.54, 0.21]),
    "B2": np.array([0.24, 0.65, 0.10, 0.01]),
}


def t5z1(F=1000.0):
    # общий покомпонентный баланс схемы: F·xF = D1·xD1 + B1·xB1 + D2·xD2 + B2·xB2
    A = np.column_stack([T5_X[s] for s in ("D1", "B1", "D2", "B2")])
    b = F * T5_X["F"]
    D1, B1, D2, B2 = np.linalg.solve(A, b)
    D, B = D1 + B1, D2 + B2                                   # балансы колонн 2 и 3
    xD = (D1 * T5_X["D1"] + B1 * T5_X["B1"]) / D
    xB = (D2 * T5_X["D2"] + B2 * T5_X["B2"]) / B
    flows = {"F": F, "D": D, "B": B, "D1": D1, "B1": B1, "D2": D2, "B2": B2}
    comp = {"F": T5_X["F"], "D": xD, "B": xB, "D1": T5_X["D1"], "B1": T5_X["B1"],
            "D2": T5_X["D2"], "B2": T5_X["B2"]}
    # невязки покомпонентных балансов каждой колонны
    res = np.concatenate([F * comp["F"] - D * xD - B * xB,
                          D * xD - D1 * comp["D1"] - B1 * comp["B1"],
                          B * xB - D2 * comp["D2"] - B2 * comp["B2"]])
    # чувствительность к погрешности составов: отклонения ±d (абс.) с нормировкой
    mc = {}
    for d in (0.001, 0.0025):
        rng = np.random.default_rng(8)
        sims = []
        for _ in range(5000):
            Ap = np.clip(A + rng.uniform(-d, d, A.shape), 0, None)
            Ap /= Ap.sum(axis=0)
            sims.append(np.linalg.solve(Ap, b))
        sims = np.array(sims)
        mc[d] = dict(p5=np.percentile(sims, 5, axis=0),
                     p95=np.percentile(sims, 95, axis=0),
                     neg=float(np.mean((sims < 0).any(axis=1))))
    return dict(A=A, b=b, flows=flows, comp=comp, residual=res,
                cond=np.linalg.cond(A), det=np.linalg.det(A),
                sv=np.linalg.svd(A, compute_uv=False), mc=mc)


def print_t5z1(r):
    print("Матрица A (столбцы D1, B1, D2, B2):\n", r["A"])
    print(f"det A = {r['det']:.3e}; число обусловленности cond(A) = {r['cond']:.1f}")
    print("Расходы, моль/ч:", {k: round(float(v), 4) for k, v in r["flows"].items()})
    print("Состав D:", np.array2string(r["comp"]["D"], precision=4), " состав B:",
          np.array2string(r["comp"]["B"], precision=4))
    print(f"Макс. невязка балансов колонн: {np.max(np.abs(r['residual'])):.1e} моль/ч")
    print("Сингулярные числа A:", np.array2string(r["sv"], precision=5))
    for d, m in r["mc"].items():
        print(f"Ошибка составов ±{d*100:.2f} % абс.: 90 %-интервалы D1, B1, D2, B2 = "
              + ", ".join(f"{lo:.0f}…{hi:.0f}" for lo, hi in zip(m["p5"], m["p95"]))
              + f"; доля решений с отрицательным расходом {m['neg']*100:.1f} %")


def plot_t5z1_scheme(r):
    fl, cp = r["flows"], r["comp"]
    fig, ax = plt.subplots(figsize=(9.0, 5.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")

    def lab(name):
        x = cp[name] * 100
        return (f"{name} = {_c(fl[name],1)} моль/ч\n" +
                "\n".join(f"{c}: {_c(v,1)} %" for c, v in zip(T5_COMP, x)))
    _box(ax, 3.2, 4.0, 0.8, 2.4, "#1")
    _box(ax, 6.8, 6.2, 0.8, 1.8, "#2")
    _box(ax, 6.8, 1.8, 0.8, 1.8, "#3")
    _arrow(ax, [(0.3, 4.0), (2.8, 4.0)], lab("F"), (0.25, 5.4), fs=7.5, ha="left")
    _arrow(ax, [(3.2, 5.2), (3.2, 6.2), (6.4, 6.2)], lab("D"), (3.4, 7.3), fs=7.5, ha="left")
    _arrow(ax, [(3.2, 2.8), (3.2, 1.8), (6.4, 1.8)], lab("B"), (3.4, 0.75), fs=7.5, ha="left")
    _arrow(ax, [(6.8, 7.1), (6.8, 7.6), (8.6, 7.6)], lab("D1"), (8.7, 7.2), fs=7.5, ha="left")
    _arrow(ax, [(6.8, 5.3), (6.8, 4.8), (8.6, 4.8)], lab("B1"), (8.7, 4.6), fs=7.5, ha="left")
    _arrow(ax, [(6.8, 2.7), (6.8, 3.2), (8.6, 3.2)], lab("D2"), (8.7, 3.0), fs=7.5, ha="left")
    _arrow(ax, [(6.8, 0.9), (6.8, 0.4), (8.6, 0.4)], lab("B2"), (8.7, 0.75), fs=7.5, ha="left")
    return finish(fig, "t5z1_scheme.png")


# %% Т5 З2: процесс Toray 2 C7H8 <=> C6H6 + C8H10 с рециклом толуола
MW = {"C7H8": 7 * 12.011 + 8 * 1.008,       # молярные массы, г/моль
      "C6H6": 6 * 12.011 + 6 * 1.008,
      "C8H10": 8 * 12.011 + 10 * 1.008}


def t5z2(F1=100.0, conv=0.58, tol=1e-12):
    n1 = np.array([F1, 0.0, 0.0])                     # толуол, бензол, ксилол, моль/ч
    # реактор: n3 = M·n2 (прореагировало conv·T2 толуола;
    # образовалось бензола и ксилола — по conv·T2/2)
    M = np.array([[1 - conv, 0, 0], [conv / 2, 1, 0], [conv / 2, 0, 1]])
    # доли компонентов потока 3, уходящие в поток 4
    a4 = np.array([0.001, 0.995, 0.0])
    # доли компонентов потока 5, уходящие в поток 7
    a7 = np.array([0.995, 1.0, 0.001])
    G = np.diag(a7) @ np.diag(1 - a4) @ M             # n7 = G·(n1 + n7)
    # (а) метод простой итерации по разрываемому потоку 7 (как в практике 5)
    n7, hist = np.zeros(3), []
    for it in range(1, 500):
        new = G @ (n1 + n7)
        hist.append((it, *new))
        if np.max(np.abs(new - n7)) < tol:
            n7 = new
            break
        n7 = new
    iters = it
    # (б) прямое решение линейной системы (I − G)·n7 = G·n1
    n7_lin = np.linalg.solve(np.eye(3) - G, G @ n1)
    n2 = n1 + n7_lin
    n3 = M @ n2
    n4 = a4 * n3
    n5 = n3 - n4
    n7 = a7 * n5
    n6 = n5 - n7
    dR = n3 - n2                                      # изменение в реакторе
    # степень полноты реакции, моль/ч
    xi = conv * n2[0] / 2
    streams = {"1": n1, "2": n2, "R": dR, "3": n3, "4": n4, "5": n5, "6": n6, "7": n7}
    out = n4 + n6
    nu = np.array([-2.0, 1.0, 1.0])
    bal = n1 - out + nu * xi                          # покомпонентный баланс схемы
    nodes = np.concatenate([n1 + n7 - n2, n3 - n4 - n5, n5 - n6 - n7])
    atoms_C = np.array([7, 6, 8])
    atoms_H = np.array([8, 6, 10])
    mw = np.array([MW["C7H8"], MW["C6H6"], MW["C8H10"]])
    return dict(streams=streams, xi=xi, iters=iters, hist=np.array(hist), n7_iter=n7,
                n7_diff=np.max(np.abs(np.array(hist[-1][1:]) - n7_lin)),
                bal=bal, nodes=nodes,
                dC=atoms_C @ n1 - atoms_C @ out, dH=atoms_H @ n1 - atoms_H @ out,
                dm=mw @ n1 - mw @ out, mass_in=mw @ n1,
                conv_total=(n1[0] - out[0]) / n1[0], conv_to_xylene=n6[2] / n1[0],
                conv_to_benzene=n4[1] / n1[0], yield_xylene=n6[2] / (n1[0] / 2),
                recycle_ratio=n7.sum() / n1.sum(), conv=conv)


def print_t5z2(r):
    print(f"Итераций до сходимости (простая итерация по потоку 7): {r['iters']}; "
          f"отличие от прямого решения {r['n7_diff']:.1e}")
    print("Поток   толуол    бензол    ксилол    всего   (моль/ч)")
    for k, n in r["streams"].items():
        print(f"{k:5s} {n[0]:9.4f} {n[1]:9.4f} {n[2]:9.4f} {n.sum():9.4f}")
    print(f"Степень полноты реакции xi = {r['xi']:.4f} моль/ч; кратность рецикла {r['recycle_ratio']:.4f}")
    print(f"Невязки: компоненты {np.max(np.abs(r['bal'])):.1e}, узлы {np.max(np.abs(r['nodes'])):.1e}, "
          f"C {r['dC']:.1e}, H {r['dH']:.1e}, масса {r['dm']:.1e} г/ч")
    print(f"Общая конверсия толуола {r['conv_total']*100:.3f} %; конверсия толуола в ксилол "
          f"{r['conv_to_xylene']*100:.3f} %; в бензол {r['conv_to_benzene']*100:.3f} %")


def plot_t5z2(r):
    h = r["hist"]
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(h[:30, 0], h[:30, 1], MARKERS[0] + LINES[0], color=COLORS[0], ms=4, lw=1.2,
            label="Толуол в рецикле (поток 7)")
    ax.axhline(r["streams"]["7"][0], color=COLORS[1], ls="--", lw=1.0,
               label=f"Решение системы: {r['streams']['7'][0]:.4f} моль/ч".replace(".", ","))
    ax.set_xlabel("Номер итерации")
    ax.set_ylabel("Расход толуола, моль/ч")
    ax.legend()
    p1 = finish(fig, "t5z2_iter.png")
    s = r["streams"]
    fig, ax = plt.subplots(figsize=(9.0, 3.4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    for x, t in ((2.6, "M"), (5.0, "R"), (7.4, "S1"), (9.8, "S2")):
        _box(ax, x, 1.6, 1.2, 0.9, t, fc="#e8eef7")

    def tb(n):
        return f"Т {_c(n[0],2)}\nБ {_c(n[1],2)}\nК {_c(n[2],2)}"
    _arrow(ax, [(0.2, 1.6), (2.0, 1.6)], "1\n" + tb(s["1"]), (1.0, 0.75), fs=7.5)
    _arrow(ax, [(3.2, 1.6), (4.4, 1.6)], "2\n" + tb(s["2"]), (3.8, 0.55), fs=7.5)
    _arrow(ax, [(5.6, 1.6), (6.8, 1.6)], "3\n" + tb(s["3"]), (6.2, 0.55), fs=7.5)
    _arrow(ax, [(8.0, 1.6), (9.2, 1.6)], "5\n" + tb(s["5"]), (8.6, 0.55), fs=7.5)
    _arrow(ax, [(10.4, 1.6), (11.8, 1.6)], "6\n" + tb(s["6"]), (11.2, 0.55), fs=7.5)
    _arrow(ax, [(7.4, 2.05), (7.4, 3.0)], "4: " + tb(s["4"]).replace("\n", "; "), (7.55, 3.2), fs=7.5, ha="left")
    _arrow(ax, [(9.8, 2.05), (9.8, 4.1), (2.6, 4.1), (2.6, 2.05)],
           "7 (рецикл): " + tb(s["7"]).replace("\n", "; "), (6.2, 4.35), fs=7.5)
    ax.text(0.2, 3.3, "Т – толуол, Б – бензол,\nК – ксилол; моль/ч", fontsize=7.5, color="#52514e")
    p2 = finish(fig, "t5z2_scheme.png")
    return p1, p2


# %% [markdown]
# ## Запуск всех расчётов

# %% Выполнение всех заданий (в блокноте — последовательно)
# рекомендуемое давление во втором сепараторе, МПа (обоснование — в отчёте)
P2_CHOICE = 6.0


def run_all(plots=True, verbose=True):
    res = {}
    steps = [("t1z1", t1z1, print_t1z1), ("t1z2", t1z2, print_t1z2), ("t1z3", t1z3, print_t1z3),
             ("t1z4", t1z4, print_t1z4), ("t2z1", t2z1, None), ("t2z2", t2z2, None),
             ("t3z1", t3z1, print_t3z1), ("t3z2_base", t3z2_base, None), ("t3z2_study", t3z2_study, None),
             ("t4z1", t4z1, print_t4z1), ("t4z2a", t4z2a, print_t4z2a), ("t4z2b", t4z2b, print_t4z2b),
             ("t5z1", t5z1, print_t5z1), ("t5z2", t5z2, print_t5z2)]
    for key, fn, pr in steps:
        res[key] = fn()
        if verbose and pr is not None:
            print(f"\n===== {key} =====")
            pr(res[key])
    if verbose:
        print("\n===== t2z1 =====")
        print_t2(res["t2z1"], "Аммиак:")
        print("\n===== t2z2 =====")
        print_t2(res["t2z2"], "Смесь CO2/O2/N2:")
        print("\n===== t3z2 =====")
        print_t3z2(res["t3z2_base"], res["t3z2_study"])
    if plots:
        plot_t1z1(res["t1z1"]); plot_t1z2(res["t1z2"]); plot_t1z3(res["t1z3"]); plot_t1z4(res["t1z4"])
        plot_t2(res["t2z1"], res["t2z2"])
        plot_t3z1(res["t3z1"]); plot_t3z2_scheme(res["t3z2_base"]); plot_t3z2_rr(res["t3z2_base"])
        plot_t3z2(res["t3z2_base"], res["t3z2_study"], P2_CHOICE)
        plot_t4z1(res["t4z1"]); plot_t4z2(res["t4z2a"])
        plot_t5z1_scheme(res["t5z1"]); plot_t5z2(res["t5z2"])
    return res


if __name__ == "__main__":
    RESULTS = run_all()
    print(f"\nГрафики сохранены в {FIG}")
