# Модуль 2. Уравнения состояния и расчёт однофазных потоков (тема 2), варианты 9 и 10.
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

import atexit; atexit.register(show_results)  # noqa: консольный запуск — вывод в конце

# %% Задачи 2.1–2.2. Общая часть: параметры RK/SRK и решение кубического уравнения
# Tc, К; Pc, атм; ω — справочник Refining & Chemicals (IFP Training, 2014), раздел A2
CRIT = {"H2": (33.2, 12.8, -0.22),
        "CH4": (190.6, 45.4, 0.008),
        "C2H6": (305.4, 48.2, 0.098),
        "C3H8": (369.8, 41.9, 0.152)}


def eos_ab(gas, T, eos):
    """a, Па∙м6/моль2 и b, м3/моль для RK или SRK."""
    Tc, Pc_atm, w = CRIT[gas]
    Pc, Tr = Pc_atm * ATM, T / Tc
    if eos == "RK":
        alpha = Tr ** -0.5
    else:
        m = 0.480 + 1.574 * w - 0.176 * w ** 2
        alpha = (1 + m * (1 - Tr ** 0.5)) ** 2
    return 0.42748 * R ** 2 * Tc ** 2 / Pc * alpha, 0.08664 * R * Tc / Pc


def solve_z(a, b, T, P):
    """Z^3 − Z^2 + (A − B − B^2)·Z − A·B = 0; газ — наибольший корень Z > B."""
    A, B = a * P / (R * T) ** 2, b * P / (R * T)
    roots = np.roots([1.0, -1.0, A - B - B ** 2, -A * B])
    real = roots[np.abs(roots.imag) < 1e-10].real
    return real[real > B].max(), roots, A, B


def volumes(names, y, T, P_atm):
    P = P_atm * ATM
    res = {"ИГ": dict(Z=1.0, v=R * T / P)}
    for eos in ("RK", "SRK"):
        ab = np.array([eos_ab(g, T, eos) for g in names])
        ai, bi = ab[:, 0], ab[:, 1]
        a = np.sum(np.outer(y, y) * np.sqrt(np.outer(ai, ai)))  # ΣΣ yi·yj·√(ai·aj)
        b = np.sum(y * bi)                                       # b = Σ yi·bi
        Z, roots, A, B = solve_z(a, b, T, P)
        res[eos] = dict(Z=Z, v=Z * R * T / P, a=a, b=b, ai=ai, bi=bi,
                        A=A, B=B, roots=roots)
    for k, d in res.items():
        d["v_L"] = d["v"] * 1000                                  # м3/моль -> л/моль
        d["dev"] = (d["v"] / res["ИГ"]["v"] - 1) * 100
        out(f"{k:4s} Z = {d['Z']:.4f}  v = {d['v']:.4e} м3/моль"
            f" = {d['v_L']:.4f} л/моль"
            f"  отклонение от ИГ {d['dev']:+.2f} %")
    return res


# %% Задача 2.1. Водород, P = 50 атм, T = 400 К
task("t21", "Задача 2.1")
T21, P21 = 400.0, 50.0
out(f"P = {P21} атм = {P21*ATM/1e6:.4f} МПа; Tr = {T21/CRIT['H2'][0]:.3f}; "
    f"Pr = {P21/CRIT['H2'][1]:.3f}")
res21 = volumes(["H2"], np.array([1.0]), T21, P21)
for eos in ("RK", "SRK"):
    out(eos, "корни Z:", np.round(res21[eos]["roots"], 5))

# %% Задача 2.2. Смесь 25 % CH4, остальное C2H6 : C3H8 = 1 : 3; P = 120 атм, T = 420 К
task("t22", "Задача 2.2")
names22 = ["CH4", "C2H6", "C3H8"]
y22 = np.array([0.25, 0.75 * 1 / 4, 0.75 * 3 / 4])
T22, P22 = 420.0, 120.0
out("Состав, мол. доли:", ", ".join(f"{n} {v:.4f}" for n, v in zip(names22, y22)))
res22 = volumes(names22, y22, T22, P22)
for eos in ("RK", "SRK"):
    out(eos, "a_i =", np.round(res22[eos]["ai"], 5), " b_i =", res22[eos]["bi"])
    out(eos, "корни Z:", np.round(res22[eos]["roots"], 5))

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
for axx, res, T, P, title in ((ax[0], res21, T21, P21, "Водород, 50 атм, 400 К"),
                              (ax[1], res22, T22, P22, "CH₄–C₂H₆–C₃H₈, 120 атм, 420 К")):
    Zg = np.linspace(-0.1, 1.4, 300)
    for eos in ("RK", "SRK"):
        A, B = res[eos]["A"], res[eos]["B"]
        axx.plot(Zg, Zg ** 3 - Zg ** 2 + (A - B - B ** 2) * Zg - A * B, label=eos)
        axx.plot(res[eos]["Z"], 0, "o")
    axx.axhline(0, color="k", lw=0.8)
    axx.axvline(1, color="gray", ls=":", label="ИГ (Z = 1)")
    axx.set(xlabel="Z", ylabel="f(Z)", title=title, ylim=(-0.3, 0.6))
    axx.legend()
    style_axes(axx)
show(fig, "t2")
