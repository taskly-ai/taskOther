# Модуль 5. Химическое равновесие, вариант 10 (образец, альтернативное решение).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задача 4.1. Синтез аммиака: уравнение равновесия как полином по степени полноты ξ
task("t41", "Задача 4.1")
Kp, P, T = 0.05, 220.0, 589.0                # 1/атм, атм, К
nN, nH, nA = 1.1, 3.0, 0.2                   # моль/ч на входе
# yA/(yN^0.5·yH^1.5) = Kp·P;  n = 4.3 - ξ  ->  (nA + ξ)^2·n^2 = (Kp·P)^2·(nN - ξ/2)(nH - 3ξ/2)^3
p = np.polynomial.Polynomial
xi_ = p([0, 1])
lhs = (nA + xi_) ** 2 * (nN + nH + nA - xi_) ** 2
rhs = (Kp * P) ** 2 * (nN - xi_ / 2) * (nH - 1.5 * xi_) ** 3
roots = (lhs - rhs).roots()
xi = float([r.real for r in roots if abs(r.imag) < 1e-9 and 0 < r.real < 2][0])
n41 = np.array([nN - xi / 2, nH - 1.5 * xi, nA + xi])
y41 = n41 / n41.sum()
report("корни полинома 4-й степени:", np.round(roots, 4))
report(f"физический корень ξ = {xi:.6f} моль/ч (0 < ξ < 2)")
for nm, a, b, c in zip(("N2", "H2", "NH3"), (nN, nH, nA), n41, y41):
    report(f"{nm:4s} {a:.4f} -> {b:.4f} моль/ч, y = {c:.4f}")
report(f"проверка: Kp = {y41[2] / (y41[0] ** 0.5 * y41[1] ** 1.5) / P:.6f} 1/атм")
# влияние давления на равновесный выход NH3 (Kp при 589 К постоянна)
Pg = np.linspace(20, 400, 60)
yA = []
for Pi in Pg:
    rr = ((nA + xi_) ** 2 * (4.3 - xi_) ** 2 - (Kp * Pi) ** 2 * (nN - xi_ / 2) * (nH - 1.5 * xi_) ** 3).roots()
    x_ = [r.real for r in rr if abs(r.imag) < 1e-9 and -0.2 < r.real < 2][0]
    yA.append((nA + x_) / (4.3 - x_))
res41 = dict(xi=xi, n=n41, y=y41, roots=roots, Pg=Pg, yA=np.array(yA))

fig, ax = plt.subplots(figsize=(6, 3.4))
ax.plot(Pg, np.array(yA) * 100)
ax.plot(P, y41[2] * 100, "ko")
ax.set(xlabel="P, атм", ylabel="Равновесная доля NH₃, % (589 К)")
draw(fig, "o41")

# %% Задача 4.2а. C2H6 <=> C2H4 + H2 при 1100 К: K по уравнению Кирхгофа от 298 К
task("t42a", "Задача 4.2а")
# ΔH°f, ΔG°f (298 К), кал/моль – справочник IFP, E18, E19; Cp = a + bT + cT^2 + dT^3, кал/(моль·К) – D1
dHf = {"C2H6": -20236.0, "C2H4": 12496.0, "H2": 0.0}
dGf = {"C2H6": -7860.0, "C2H4": 16282.0, "H2": 0.0}
cp = {"C2H6": (1.648, 4.124e-2, -1.53e-5, 1.74e-9),
      "C2H4": (0.944, 3.735e-2, -1.993e-5, 4.22e-9),
      "H2": (6.483, 0.221e-2, -0.333e-5, 1.826e-9)}
nu = {"C2H4": 1, "H2": 1, "C2H6": -1}
dCp = lambda T: sum(v * (cp[s][0] + cp[s][1] * T + cp[s][2] * T ** 2 + cp[s][3] * T ** 3) for s, v in nu.items())
dH298 = sum(v * dHf[s] for s, v in nu.items()) * CAL               # Дж/моль
dG298 = sum(v * dGf[s] for s, v in nu.items()) * CAL
dS298 = (dH298 - dG298) / 298.15


def K_kirchhoff(T):
    dH = dH298 + integrate.quad(dCp, 298.15, T)[0] * CAL
    dS = dS298 + integrate.quad(lambda x: dCp(x) / x, 298.15, T)[0] * CAL
    dG = dH - T * dS
    return np.exp(-dG / (R * T)), dH, dG


K1000_table = np.exp(-(28249 - 26130) * CAL / (R * 1000))   # по ΔG°f при 1000 К из таблицы
K1000, _, _ = K_kirchhoff(1000.0)
K42, dH1100, dG1100 = K_kirchhoff(1100.0)
x42 = np.sqrt(K42 / (K42 + 1.0))                              # P = 1 атм
n42 = np.array([1 - x42, x42, x42])
y42 = n42 / n42.sum()
report(f"ΔH°298 = {dH298/1000:.2f} кДж/моль, ΔG°298 = {dG298/1000:.2f} кДж/моль, ΔS°298 = {dS298:.2f} Дж/(моль·К)")
report(f"проверка при 1000 К: K(Кирхгоф) = {K1000:.4f}, K(таблица ΔG°f) = {K1000_table:.4f}")
report(f"1100 К: ΔH° = {dH1100/1000:.2f} кДж/моль, ΔG° = {dG1100/1000:.3f} кДж/моль, K = {K42:.4f}")
report(f"x = {x42:.5f}; y: C2H6 {y42[0]:.4f}, C2H4 {y42[1]:.4f}, H2 {y42[2]:.4f}")
Tg = np.linspace(300, 1150, 60)
res42 = dict(dH298=dH298, dG298=dG298, dS298=dS298, K1000=K1000, K1000_table=K1000_table,
             K=K42, dH1100=dH1100, dG1100=dG1100, x=x42, n=n42, y=y42,
             curve=np.array([K_kirchhoff(t_)[2] for t_ in Tg]), Tg=Tg)

fig, ax = plt.subplots(figsize=(6, 3.4))
Tt = np.array([298, 400, 600, 800, 1000.0])
dGt = (np.array([16282, 17675, 20918, 24490, 28249]) - np.array([-7860, -3447, 5970, 15920, 26130])) * CAL
ax.plot(Tg, res42["curve"] / 1000, label="Кирхгоф (Cp из D1)")
ax.plot(Tt, dGt / 1000, "ks", label="таблица E19")
ax.plot(1100, dG1100 / 1000, "ro", label="1100 К")
ax.axhline(0, color="k", lw=0.8)
ax.set(xlabel="T, К", ylabel="ΔG°r, кДж/моль")
ax.legend()
draw(fig, "o42")

# %% Задача 4.2б. Две реакции при 1367 К: сведение системы к одному уравнению
task("t42b", "Задача 4.2б")
K1, K2 = 37.6, 0.769                          # P = 1 атм


def x2_of_x1(x1):
    """Из K2 = x2·(x1 + x2)/((x1 - x2)·(1 + x1 + x2)) — квадратное уравнение относительно x2."""
    a = 1 + K2
    b = x1 + K2                              # (1 + K2)·x2^2 + (x1 + K2)·x2 - K2·x1·(1 + x1) = 0
    c = -K2 * x1 * (1 + x1)
    return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)


def g(x1):
    x2 = x2_of_x1(x1)
    n_ = np.array([1 - x1, x1 - x2, x1 + x2, x2])
    y_ = n_ / n_.sum()
    return y_[1] * y_[2] - K1 * y_[0]


x1 = optimize.brentq(g, 1e-9, 1 - 1e-12, xtol=1e-14)
x2 = x2_of_x1(x1)
n43 = np.array([1 - x1, x1 - x2, x1 + x2, x2])
y43 = n43 / n43.sum()
report(f"x1 = {x1:.5f}, x2 = {x2:.5f}")
for nm, a, b in zip(("C2H6", "C2H4", "H2", "C2H2"), n43, y43):
    report(f"{nm:5s} {a:.5f} моль  y = {b:.4f}")
report(f"проверка: K1 = {y43[1]*y43[2]/y43[0]:.4f}, K2 = {y43[3]*y43[2]/y43[1]:.5f}")
res43 = dict(x1=x1, x2=x2, n=n43, y=y43)
