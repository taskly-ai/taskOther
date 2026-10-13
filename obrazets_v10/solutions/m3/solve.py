# Модуль 3. Фазовые равновесия, вариант 10 (образец, альтернативное решение).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задачи 3.1–3.2. Общая часть: K-корреляция задания и метод Ньютона для Рачфорда–Райса
# A, B, C, D, форма: (1) ln K = -A/T^2 + B - C·ln P + D/P^2; (2) ... + D/P; T в °R, P в psia
KDATA = {"C2H4": (600076.9, 7.90595, 0.84677, 42.94594, 1),
         "CH4": (292860.0, 8.2445, 0.8951, 59.8465, 1),
         "C2H6": (687248.2, 7.90694, 0.866, 49.02654, 1),
         "C3H8": (970688.6, 7.15059, 0.76984, 6.90224, 2),
         "iC4": (1166846.0, 7.72668, 0.92213, 0.0, 1),
         "nC4": (1280557.0, 7.94986, 0.96455, 0.0, 1),
         "nC5": (1524891.0, 7.33129, 0.89143, 0.0, 1)}


def Kval(comp, T_K, P_Pa):
    TR, P = 1.8 * T_K, P_Pa / PSI
    A, B, Cc, D, form = (np.array([KDATA[c][i] for c in comp]) for i in range(5))
    return np.exp(-A / TR ** 2 + B - Cc * np.log(P) + np.where(form == 1, D / P ** 2, D / P))


def rr_newton(z, K, tol=1e-13):
    """Уравнение Рачфорда–Райса методом Ньютона (функция монотонна, старт e = 0.5)."""
    if z @ K <= 1:
        return 0.0, 0
    if z @ (1 / K) <= 1:
        return 1.0, 0
    lo, hi = 1 / (1 - K.max()), 1 / (1 - K.min())      # асимптоты функции
    e, it = 0.5, 0
    while True:
        d = 1 + e * (K - 1)
        f, df = np.sum(z * (K - 1) / d), -np.sum(z * (K - 1) ** 2 / d ** 2)
        e_new = e - f / df
        if not lo < e_new < hi:                  # страховка: шаг пополам к границе
            e_new = (e + (hi if e_new >= hi else lo)) / 2
        it += 1
        if abs(e_new - e) < tol:
            return min(max(e_new, 0.0), 1.0), it
        e = e_new


# %% Задача 3.1. ТНК и ТКК смеси этилен 20 %, пропан 30 %, изобутан 30 %, н-бутан 20 % при 14 атм
comp31 = ["C2H4", "C3H8", "iC4", "nC4"]
z31 = np.array([0.20, 0.30, 0.30, 0.20])


def bubble_dew(P_atm):
    P = P_atm * ATM
    # ln ΣKz = 0 и ln Σz/K = 0: логарифм делает функции почти линейными по T -> метод секущих
    fb = lambda T: np.log(z31 @ Kval(comp31, T, P))
    fd = lambda T: np.log(z31 @ (1 / Kval(comp31, T, P)))
    return optimize.newton(fb, 280.0), optimize.newton(fd, 330.0)


Tb, Td = bubble_dew(14.0)
Kb, Kd = Kval(comp31, Tb, 14 * ATM), Kval(comp31, Td, 14 * ATM)
print(f"P = 14 атм = {14*ATM/1e6:.4f} МПа = {14*ATM/PSI:.2f} psia")
print(f"ТНК = {Tb:.2f} К ({Tb-273.15:.2f} °C), ТКК = {Td:.2f} К ({Td-273.15:.2f} °C)")
print("y пузырька:", np.round(Kb * z31, 4), " x капли:", np.round(z31 / Kd, 4))
Pgrid = np.arange(4.0, 31.0, 1.0)
curve = np.array([bubble_dew(p) for p in Pgrid])
res31 = dict(Tb=Tb, Td=Td, Kb=Kb, Kd=Kd, Pgrid=Pgrid, curve=curve)

fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(curve[:, 0] - 273.15, Pgrid, label="линия кипения (ТНК)")
ax.plot(curve[:, 1] - 273.15, Pgrid, label="линия росы (ТКК)")
ax.plot([Tb - 273.15, Td - 273.15], [14, 14], "ko-", label="14 атм")
ax.set(xlabel="t, °C", ylabel="P, атм")
ax.legend()
draw(fig, "o31")

# %% Задача 3.2. Сепараторы: базовый режим (С1 9.8 МПа/40.8 °C, С2 8.7/12.8, С3 8.7/-40.8)
comp32 = ["CH4", "C2H6", "C3H8", "iC4", "nC4", "nC5"]
zF = np.array([0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706])
STAGE = {"С1": (9.8e6, 40.8), "С2": (8.7e6, 12.8), "С3": (8.7e6, -40.8)}


def run_block(stages, F=100.0):
    """Цепочка сепараторов на 100 моль/ч сырья; возвращает ступени и покомпонентные потоки."""
    feed, out, liq = F * zF, [], np.zeros(len(zF))
    for s in stages:
        P, t = STAGE[s]
        Fs = feed.sum()
        zs = feed / Fs
        K = Kval(comp32, t + 273.15, P)
        e, it = rr_newton(zs, K)
        x = zs / (1 + e * (K - 1))
        yv = K * x if e > 0 else np.zeros_like(zs)
        x = x if e < 1 else np.zeros_like(zs)
        out.append(dict(name=s, e=e, it=it, K=K, x=x, y=yv, F=Fs))
        liq += Fs * (1 - e) * x
        feed = Fs * e * yv
    return out, feed, liq                        # feed – товарный газ, моль/ч по компонентам


base, gas, liq = run_block(["С1", "С2", "С3"])
for s in base:
    print(f"{s['name']}: e = {s['e']:.5f} ({s['it']} итераций Ньютона), питание {s['F']:.3f} моль/ч")
    print("   x:", " ".join(f"{v:.5f}" for v in s["x"]))
    print("   y:", " ".join(f"{v:.5f}" for v in s["y"]))
print(f"Газ: {gas.sum():.3f} моль/ч; жидкость: {liq.sum():.3f} моль/ч; "
      f"баланс: {100 - gas.sum() - liq.sum():.1e}")
res32 = dict(base=base, gas=gas, liq=liq)

# %% Задача 3.2. Исследование: влияние количества сепараторов (1, 2 или 3)
SCHEMES = [("1", ["С1"]), ("2", ["С1", "С2"]), ("3", ["С1", "С2", "С3"]),     # ряд А: С1 -> ...
           ("1", ["С3"]), ("2", ["С2", "С3"]), ("3", ["С1", "С2", "С3"])]     # ряд Б: ... -> С3
study = []
for nst, st in SCHEMES:
    _, g, l = run_block(st)
    G = g.sum()
    study.append(dict(n=int(nst), stages=" + ".join(st), G=G,
                      CH4_gas=g[0] / (100 * zF[0]) * 100,                     # извлечение метана в газ, %
                      C3p_gas=g[2:].sum() / G * 100 if G > 0 else np.nan,     # C3+ в газе, %
                      C3_liq=l[2] / (100 * zF[2]) * 100))                     # пропан в жидкость, %
print(f"{'схема':16s} {'газ, моль/ч':>11s} {'CH4 в газ, %':>13s} {'C3+ в газе, %':>14s} {'C3H8 в жидк., %':>16s}")
for r_ in study:
    c3 = "—" if np.isnan(r_["C3p_gas"]) else f"{r_['C3p_gas']:.3f}"
    print(f"{r_['n']}: {r_['stages']:13s} {r_['G']:11.3f} {r_['CH4_gas']:13.2f} {c3:>14s} {r_['C3_liq']:16.2f}")
res32["study"] = study

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
for lab, part in (("ряд А: С1 → … (отключаются последние)", study[:3]),
                  ("ряд Б: … → С3 (отключаются первые)", study[3:])):
    ax[0].plot([r_["n"] for r_ in part], [r_["CH4_gas"] for r_ in part], "o-", label=lab)
    ax[1].plot([r_["n"] for r_ in part], [r_["C3p_gas"] for r_ in part], "o-", label=lab)
ax[0].set(xlabel="Число сепараторов", ylabel="Извлечение CH₄ в газ, %", xticks=[1, 2, 3])
ax[1].set(xlabel="Число сепараторов", ylabel="C₃₊ в газе, %", xticks=[1, 2, 3])
ax[0].legend(fontsize=7)
draw(fig, "o32")
