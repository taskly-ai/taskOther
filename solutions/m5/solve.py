# Модуль 5. Расчёт химического равновесия (тема 4, задачи 4.1, 4.2а, 4.2б).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

import atexit; atexit.register(show_results)  # noqa: консольный запуск — вывод в конце

# %% Задача 4.1. Синтез аммиака: 1/2 N2 + 3/2 H2 <=> NH3 (N2 + 3 H2 <=> 2 NH3)
task("t41", "Задача 4.1")
Kp41, P41, T41 = 0.05, 220.0, 589.0          # Kp, 1/атм; P, атм; T, К
n0_41 = np.array([1.1, 3.0, 0.2])            # N2, H2, NH3, моль/ч (1.1 : 3 : 0.2)
nu41 = np.array([-0.5, -1.5, 1.0])           # стехиометрические коэффициенты


def comp41(xi):
    n = n0_41 + nu41 * xi                    # моль/ч на выходе
    return n, n / n.sum()


def eq41(xi):                                # Kp·P = yNH3 / (yN2^0,5 · yH2^1,5)
    n, y = comp41(xi)
    return y[2] / (y[0] ** 0.5 * y[1] ** 1.5) - Kp41 * P41


xi_max = min(n0_41[0] / 0.5, n0_41[1] / 1.5)          # ограничение по N2 и H2
xi41 = brentq(eq41, 0.0, xi_max * (1 - 1e-12), xtol=1e-14)
n41, y41 = comp41(xi41)
res41 = dict(xi=xi41, n=n41, y=y41,
             X_N2=xi41 * 0.5 / n0_41[0], X_H2=xi41 * 1.5 / n0_41[1],
             check=y41[2] / (y41[0] ** 0.5 * y41[1] ** 1.5) / P41)
out(f"xi = {xi41:.6f} моль/ч (xi_max = {xi_max:.4f})")
for nm, a, b, c in zip(("N2", "H2", "NH3"), n0_41, n41, y41):
    out(f"{nm:4s} начало {a:.4f}  конец {b:.4f} моль/ч  y = {c:.4f}")
out(f"Всего {n0_41.sum():.4f} -> {n41.sum():.4f} моль/ч; "
    f"проверка Kp = {res41['check']:.6f} 1/атм")
out(f"Степень превращения: N2 {res41['X_N2']*100:.2f} %,"
    f" H2 {res41['X_H2']*100:.2f} %")

# %% Задача 4.2а. C2H6 <=> C2H4 + H2 при 1100 К и 1 атм; K по справочным данным
task("t42a", "Задача 4.2а")
# ΔH°f и ΔG°f, кал/моль (справочник IFP, разделы E18 и E19); H2 — простое вещество, 0
Tref = np.array([298.0, 400.0, 600.0, 800.0, 1000.0])
dHf = {"C2H6": np.array([-20236, -21419, -23280, -24530, -25280.0]),
       "C2H4": np.array([12496, 11766, 10600, 9760, 9205.0])}
dGf = {"C2H6": np.array([-7860, -3447, 5970, 15920, 26130.0]),
       "C2H4": np.array([16282, 17675, 20918, 24490, 28249.0])}
dH_r = (dHf["C2H4"] - dHf["C2H6"]) * CAL          # Дж/моль
dG_r = (dGf["C2H4"] - dGf["C2H6"]) * CAL          # Дж/моль
K_ref = np.exp(-dG_r / (R * Tref))                # K = exp(−ΔG°/(R·T))
T42, P42 = 1100.0, 1.0
# Основной способ: уравнение Вант-Гоффа d ln K/dT = ΔH°/(R·T^2) от 1000 до 1100 К,
# ΔH°r(T) — линейная экстраполяция по точкам 800 и 1000 К
dH_lin = lambda T: dH_r[-1] + (dH_r[-1] - dH_r[-2]) / 200.0 * (T - 1000.0)
Tq = np.linspace(1000.0, T42, 2001)
trap = getattr(np, "trapezoid", None) or np.trapz
lnK_vh = np.log(K_ref[-1]) + trap(dH_lin(Tq) / (R * Tq ** 2), Tq)
K42 = np.exp(lnK_vh)
# Проверка: линейная экстраполяция ΔG°r(T) по точкам 800 и 1000 К
dG_ext = dG_r[-1] + (dG_r[-1] - dG_r[-2]) / 200.0 * (T42 - 1000.0)
K42_check = np.exp(-dG_ext / (R * T42))
x42 = np.sqrt(K42 / (K42 + P42))                  # Kp = x^2·P/((1 − x)(1 + x))
n42 = np.array([1 - x42, x42, x42])               # C2H6, C2H4, H2 на 1 моль этана
y42 = n42 / n42.sum()
res42 = dict(dH_r=dH_r, dG_r=dG_r, K_ref=K_ref, K=K42, K_check=K42_check,
             dG_ext=dG_ext,
             dH1100=dH_lin(T42), x=x42, n=n42, y=y42,
             x_check=np.sqrt(K42_check / (K42_check + P42)))
for T, a, b, k in zip(Tref, dH_r, dG_r, K_ref):
    out(f"T = {T:6.0f} К  ΔH°r = {a/1000:7.2f}  ΔG°r = {b/1000:7.2f} кДж/моль"
        f"  K = {k:.4e}")
out(f"K(1100 К): Вант-Гофф {K42:.4f}; экстраполяция ΔG° {K42_check:.4f}")
out(f"x = {x42:.5f}; y: C2H6 {y42[0]:.4f}, C2H4 {y42[1]:.4f}, H2 {y42[2]:.4f}")

fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(Tref, dG_r / 1000, "o-", label="ΔG°r по справочнику")
ax.plot([1000, T42], [dG_r[-1] / 1000, -R * T42 * lnK_vh / 1000], "s--",
        label="Вант-Гофф")
ax.axhline(0, color="k", lw=0.8)
ax.set(xlabel="T, К", ylabel="ΔG°r, кДж/моль")
ax.legend()
style_axes(ax)
show(fig, "t42")

# %% Задача 4.2б. Две реакции при 1367 К: C2H6 <=> C2H4 + H2, C2H4 <=> C2H2 + H2
task("t42b", "Задача 4.2б")
K1, K2, P43 = 37.6, 0.769, 1.0


def comp43(x):
    x1, x2 = x
    n = np.array([1 - x1, x1 - x2, x1 + x2, x2])   # C2H6, C2H4, H2, C2H2
    return n, n / n.sum()


def eqs43(x):
    n, y = comp43(x)
    return [y[1] * y[2] * P43 - K1 * y[0],         # K1 = yC2H4·yH2·P / yC2H6
            y[3] * y[2] * P43 - K2 * y[1]]         # K2 = yC2H2·yH2·P / yC2H4


x43 = fsolve(eqs43, [0.9, 0.3], xtol=1e-14)
n43, y43 = comp43(x43)
res43 = dict(x=x43, n=n43, y=y43, resid=np.array(eqs43(x43)),
             K1c=y43[1] * y43[2] * P43 / y43[0], K2c=y43[3] * y43[2] * P43 / y43[1])
out(f"x1 = {x43[0]:.5f}, x2 = {x43[1]:.5f}; невязки {res43['resid']}")
for nm, a, b in zip(("C2H6", "C2H4", "H2", "C2H2"), n43, y43):
    out(f"{nm:5s} {a:.5f} моль  y = {b:.4f}")
out(f"Проверка: K1 = {res43['K1c']:.4f}, K2 = {res43['K2c']:.5f}")
