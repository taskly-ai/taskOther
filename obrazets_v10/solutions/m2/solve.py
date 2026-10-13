# Модуль 2. Уравнения состояния, вариант 10 (образец, альтернативное решение).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задачи 2.1–2.2. Общая часть: RK, SRK, PR и метод Ньютона для Z
# Tc, К; Pc, атм; ω — справочник IFP Training, раздел A2
PROPS = {"H2": (33.2, 12.8, -0.22), "CH4": (190.6, 45.4, 0.008),
         "C2H6": (305.4, 48.2, 0.098), "C3H8": (369.8, 41.9, 0.152)}
# u, w в P = RT/(v - b) - a/(v^2 + u·b·v + w·b^2); Ωa, Ωb
EOS = {"RK": (1, 0, 0.42748, 0.08664), "SRK": (1, 0, 0.42748, 0.08664),
       "PR": (2, -1, 0.45724, 0.07780)}


def alpha(eos, Tr, w):
    if eos == "RK":
        return Tr ** -0.5
    m = (0.480 + 1.574 * w - 0.176 * w ** 2) if eos == "SRK" else (0.37464 + 1.54226 * w - 0.26992 * w ** 2)
    return (1 + m * (1 - np.sqrt(Tr))) ** 2


def z_newton(A, B, u, w, z0=1.0, tol=1e-12):
    """Корень кубического уравнения в Z методом Ньютона от газового приближения Z0 = 1."""
    c2, c1, c0 = -(1 + B - u * B), A + w * B ** 2 - u * B - u * B ** 2, -(A * B + w * B ** 2 + w * B ** 3)
    z, it = z0, 0
    while True:
        f, df = z ** 3 + c2 * z ** 2 + c1 * z + c0, 3 * z ** 2 + 2 * c2 * z + c1
        dz = f / df
        z, it = z - dz, it + 1
        if abs(dz) < tol:
            return z, it


def molar_volume(comp, y, T, P_atm, eos):
    P = P_atm * ATM
    u, w, Oa, Ob = EOS[eos]
    ai, bi = [], []
    for g in comp:
        Tc, Pc, om = PROPS[g]
        ai.append(Oa * (R * Tc) ** 2 / (Pc * ATM) * alpha(eos, T / Tc, om))
        bi.append(Ob * R * Tc / (Pc * ATM))
    ai, bi = np.array(ai), np.array(bi)
    sa = np.sqrt(ai)
    a, b = float((y @ sa) ** 2), float(y @ bi)          # правила смешения, kij = 0
    A, B = a * P / (R * T) ** 2, b * P / (R * T)
    z, it = z_newton(A, B, u, w)
    return dict(Z=z, v=z * R * T / P, a=a, b=b, A=A, B=B, it=it, ai=ai, bi=bi)


def table_volumes(comp, y, T, P_atm):
    out = {"ИГ": dict(Z=1.0, v=R * T / (P_atm * ATM), it=0)}
    for eos in ("RK", "SRK", "PR"):
        out[eos] = molar_volume(comp, y, T, P_atm, eos)
    print(f"{'модель':6s} {'Z':>8s} {'v, л/моль':>10s} {'итераций':>9s}")
    for k, d in out.items():
        print(f"{k:6s} {d['Z']:8.4f} {d['v']*1000:10.4f} {d['it']:9d}")
    return out


# %% Задача 2.1. Водород: P = 50 атм, T = 400 К
res21 = table_volumes(["H2"], np.array([1.0]), 400.0, 50.0)

# %% Задача 2.2. CH4 25 %, C2H6 : C3H8 = 1 : 3; P = 120 атм, T = 420 К
y22 = np.array([0.25, 0.75 / 4, 0.75 * 3 / 4])
res22 = table_volumes(["CH4", "C2H6", "C3H8"], y22, 420.0, 120.0)
Tpc = sum(yi * PROPS[g][0] for yi, g in zip(y22, ["CH4", "C2H6", "C3H8"]))
Ppc = sum(yi * PROPS[g][1] for yi, g in zip(y22, ["CH4", "C2H6", "C3H8"]))
print(f"Правило Кэя: Tpc = {Tpc:.1f} К, Ppc = {Ppc:.1f} атм; Tpr = {420/Tpc:.3f}, Ppr = {120/Ppc:.3f}")

# изотерма Z(P) смеси при 420 К по SRK и PR – где газ перестаёт быть идеальным
Pg = np.linspace(1, 200, 120)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
for eos in ("SRK", "PR"):
    ax[0].plot(Pg, [molar_volume(["H2"], np.array([1.0]), 400.0, p, eos)["Z"] for p in Pg], label=eos)
    ax[1].plot(Pg, [molar_volume(["CH4", "C2H6", "C3H8"], y22, 420.0, p, eos)["Z"] for p in Pg], label=eos)
ax[0].plot(50, res21["SRK"]["Z"], "ko")
ax[1].plot(120, res22["SRK"]["Z"], "ko")
ax[0].set(xlabel="P, атм", ylabel="Z", title="Водород, 400 К")
ax[1].set(xlabel="P, атм", ylabel="Z", title="CH₄–C₂H₆–C₃H₈, 420 К")
for a_ in ax:
    a_.axhline(1, color="gray", ls=":")
    a_.legend()
draw(fig, "o2")
