# Модуль 6. Расчёт материальных балансов (тема 5, задачи 5.1 и 5.2).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

import atexit; atexit.register(show_results)  # noqa: консольный запуск — вывод в конце

# %% Задача 5.1. Схема из трёх колонн: ксилол, стирол, толуол, бензол
task("t51", "Задача 5.1")
F = 1000.0                                           # моль/ч
zF = np.array([0.15, 0.25, 0.40, 0.20])              # ксилол, стирол, толуол, бензол
xD1 = np.array([0.07, 0.04, 0.54, 0.35])
xB1 = np.array([0.18, 0.24, 0.42, 0.16])
xD2 = np.array([0.15, 0.10, 0.54, 0.21])
xB2 = np.array([0.24, 0.65, 0.10, 0.01])
# покомпонентный баланс всей схемы: xD1·D1 + xB1·B1 + xD2·D2 + xB2·B2 = zF·F
A = np.column_stack([xD1, xB1, xD2, xB2])
D1, B1, D2, B2 = np.linalg.solve(A, zF * F)
D, B = D1 + B1, D2 + B2
flows = {"F": F, "D": D, "B": B, "D1": D1, "B1": B1, "D2": D2, "B2": B2}
comp = {"F": zF, "D": (xD1 * D1 + xB1 * B1) / D, "B": (xD2 * D2 + xB2 * B2) / B,
        "D1": xD1, "B1": xB1, "D2": xD2, "B2": xB2}
res51 = dict(flows=flows, comp=comp, cond=np.linalg.cond(A), det=np.linalg.det(A),
             err=np.max(np.abs(A @ [D1, B1, D2, B2] - zF * F)))
out(f"{'':8s}" + "".join(f"{k:>9s}" for k in flows))
for i, nm in enumerate(("Ксилол", "Стирол", "Толуол", "Бензол")):
    out(f"{nm:8s}" + "".join(f"{flows[k]*comp[k][i]:9.2f}" for k in flows))
out(f"{'Всего':8s}" + "".join(f"{flows[k]:9.2f}" for k in flows))
for i, nm in enumerate(("Ксилол", "Стирол", "Толуол", "Бензол")):
    out(f"{nm:8s}" + "".join(f"{comp[k][i]:9.4f}" for k in flows))
out(f"Невязка баланса {res51['err']:.1e} моль/ч; "
    f"число обусловленности {res51['cond']:.1f}")

# %% Задача 5.2. Процесс Toray: 2 C7H8 <=> C6H6 + C8H10 с рециклом толуола
task("t52", "Задача 5.2")
F1, X = 100.0, 0.58                  # свежий толуол, моль/ч; конверсия за проход
# неизвестные: [T2, B2, X2, xi, T4, B4, T5, B5, X5, T7, B7, X7, T6, X6] (T — толуол,
# B — бензол, X — ксилол; xi — число пробегов реакции, моль/ч)
M = np.zeros((14, 14)); rhs = np.zeros(14)
iT2, iB2, iX2, ixi, iT4, iB4, iT5, iB5, iX5, iT7, iB7, iX7, iT6, iX6 = range(14)
eqs = [({iT2: 1, iT7: -1}, F1),                 # смеситель: T2 = F1 + T7
       ({iB2: 1, iB7: -1}, 0), ({iX2: 1, iX7: -1}, 0),
       ({ixi: 1, iT2: -X / 2}, 0),              # реактор: xi = X·T2/2
       ({iB4: 1, iB2: -0.995, ixi: -0.995}, 0),  # S1: 99,5 % бензола потока 3
       ({iT4: 1, iT2: -0.001 * (1 - X)}, 0),     # S1: 0,1 % толуола потока 3
       ({iT5: 1, iT2: -(1 - X), iT4: 1}, 0),    # поток 5 = поток 3 − поток 4
       ({iB5: 1, iB2: -1, ixi: -1, iB4: 1}, 0),
       ({iX5: 1, iX2: -1, ixi: -1}, 0),          # ксилол в поток 4 не уходит
       ({iT7: 1, iT5: -0.995}, 0),              # S2: 99,5 % толуола -> рецикл
       ({iB7: 1, iB5: -1}, 0),                  # S2: весь бензол -> рецикл
       ({iX7: 1, iX5: -0.001}, 0),              # S2: 0,1 % ксилола -> рецикл
       ({iT6: 1, iT5: -1, iT7: 1}, 0),
       ({iX6: 1, iX5: -1, iX7: 1}, 0)]
for r_, (coef, b) in enumerate(eqs):
    for j, c in coef.items():
        M[r_, j] = c
    rhs[r_] = b
u = np.linalg.solve(M, rhs)
xi = u[ixi]
S = {"1": np.array([F1, 0, 0]),
     "2": u[[iT2, iB2, iX2]],
     "R": np.array([-2 * xi, xi, xi]),           # изменение в реакторе, моль/ч
     "3": u[[iT2, iB2, iX2]] + np.array([-2 * xi, xi, xi]),
     "4": np.array([u[iT4], u[iB4], 0.0]),
     "5": u[[iT5, iB5, iX5]],
     "6": np.array([u[iT6], 0.0, u[iX6]]),
     "7": u[[iT7, iB7, iX7]]}
T_out = S["4"][0] + S["6"][0]               # толуол, ушедший с продуктами
res52 = dict(S=S, xi=xi, conv_X=S["6"][2] / F1, conv_total=1 - T_out / F1,
             yield_B=S["4"][1] / F1,
             check_C=7 * F1 - (7 * T_out + 6 * S["4"][1] + 8 * S["6"][2]))
out(f"{'':8s}" + "".join(f"{k:>9s}" for k in S))
for i, nm in enumerate(("Толуол", "Бензол", "Ксилол")):
    out(f"{nm:8s}" + "".join(f"{S[k][i]:9.3f}" for k in S))
out(f"{'Всего':8s}" + "".join(f"{S[k].sum():9.3f}" for k in S))
out(f"xi = {xi:.4f} моль/ч; конверсия толуола в ксилол {res52['conv_X']*100:.2f} %;"
    f" общая конверсия толуола {res52['conv_total']*100:.2f} %")
out(f"Баланс атомов C: {res52['check_C']:.2e} моль/ч")
