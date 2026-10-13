# Модуль 7. Химическое равновесие в САПР (Aspen HYSYS) — эталонные числа для сверки.
# Модель: идеальная газовая смесь (K через парциальные давления), те же уравнения, что в
# задачах 4.1 и 4.2 отчёта; расчёт повторяется независимо от solutions/m5.
# Запуск: python solutions/m7/solve.py
import numpy as np
from scipy.optimize import brentq, fsolve

ATM_KPA = 101.325
R = 8.314462618

# --- Сценарий A: равновесный реактор синтеза аммиака (задача 4.1)
Kp, P, n0 = 0.05, 220.0, np.array([1.1, 3.0, 0.2])          # 1/атм; атм; кмоль/ч
nu = np.array([-0.5, -1.5, 1.0])


def f(xi):
    n = n0 + nu * xi
    y = n / n.sum()
    return y[2] / (y[0] ** 0.5 * y[1] ** 1.5) - Kp * P


xi = brentq(f, 0, 2 - 1e-12, xtol=1e-14)
nA = n0 + nu * xi
print("Сценарий A. Equilibrium Reactor, 1/2 N2 + 3/2 H2 <=> NH3, T = 589 K, P = 220 atm")
print(f"  Keq (Fixed, Basis = Partial Pressure): {Kp} atm^-1 = {Kp/ATM_KPA:.4e} kPa^-1")
print(f"  Для записи N2 + 3H2 <=> 2NH3: Keq = {Kp**2:.4e} atm^-2 = {Kp**2/ATM_KPA**2:.4e} kPa^-2")
print(f"  Питание 1.1 / 3.0 / 0.2 kgmole/h -> выход N2 {nA[0]:.4f}, H2 {nA[1]:.4f}, "
      f"NH3 {nA[2]:.4f} kgmole/h; всего {nA.sum():.4f}")
print(f"  Мольные доли: {np.round(nA / nA.sum(), 4)}; степень полноты {xi:.4f} kgmole/h")

# --- Сценарий B: этан -> этилен + H2 при 1100 К, 1 атм (задача 4.2а)
cal = 4.184
dH = (np.array([9760, 9205.0]) - np.array([-24530, -25280.0])) * cal      # 800, 1000 К
dG1000 = (28249 - 26130) * cal
Tq = np.linspace(1000, 1100, 2001)
dHq = dH[1] + (dH[1] - dH[0]) / 200 * (Tq - 1000)
lnK = -dG1000 / (R * 1000) + np.sum((dHq / (R * Tq ** 2))[:-1] + (dHq / (R * Tq ** 2))[1:]) / 2 * (Tq[1] - Tq[0])
K = np.exp(lnK)
x = np.sqrt(K / (K + 1))
print("\nСценарий B. Gibbs Reactor (или Equilibrium Reactor с Keq), C2H6 <=> C2H4 + H2, 1100 K, 1 atm")
print(f"  K(1100 K) по справочнику IFP = {K:.4f} (atm); степень превращения {x:.4f}")
print(f"  На 1 kgmole/h этана: C2H6 {1-x:.4f}, C2H4 {x:.4f}, H2 {x:.4f}; "
      f"доли {np.round(np.array([1-x, x, x])/(1+x), 4)}")
print("  Gibbs Reactor HYSYS берёт ΔG°f из своей базы: ожидаемое x ≈ 0.78–0.80")

# --- Сценарий C: две реакции при 1367 К (задача 4.2б)
K1, K2 = 37.6, 0.769


def g(v):
    x1, x2 = v
    n = np.array([1 - x1, x1 - x2, x1 + x2, x2]); y = n / n.sum()
    return [y[1] * y[2] - K1 * y[0], y[3] * y[2] - K2 * y[1]]


x1, x2 = fsolve(g, [0.9, 0.3], xtol=1e-14)
nC = np.array([1 - x1, x1 - x2, x1 + x2, x2])
print("\nСценарий C. Equilibrium Reactor, 2 реакции, 1367 K, 1 atm, Keq1 = 37.6 atm, Keq2 = 0.769 atm")
print(f"  Keq в kPa: {K1*ATM_KPA:.1f} и {K2*ATM_KPA:.2f}")
print(f"  x1 = {x1:.4f}, x2 = {x2:.4f}; выход C2H6 {nC[0]:.4f}, C2H4 {nC[1]:.4f}, H2 {nC[2]:.4f}, "
      f"C2H2 {nC[3]:.4f} kgmole/h; доли {np.round(nC/nC.sum(), 4)}")
