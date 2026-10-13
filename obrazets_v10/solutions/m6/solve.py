# Модуль 6. Материальные балансы, вариант 10 (образец, альтернативное решение).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задача 5.1. Три колонны: метод Гаусса с выбором главного элемента (собственная реализация)
task("t51", "Задача 5.1")
def gauss(A, b):
    A, b = np.array(A, float), np.array(b, float)
    n = len(b)
    for i in range(n):                                   # прямой ход
        p_ = i + np.argmax(np.abs(A[i:, i]))
        A[[i, p_]], b[[i, p_]] = A[[p_, i]], b[[p_, i]]
        for j in range(i + 1, n):
            f = A[j, i] / A[i, i]
            A[j, i:] -= f * A[i, i:]
            b[j] -= f * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):                       # обратный ход
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x


comps = ["ксилол", "стирол", "толуол", "бензол"]
F = 1000.0
xF = np.array([15, 25, 40, 20]) / 100
xD1, xB1 = np.array([7, 4, 54, 35]) / 100, np.array([18, 24, 42, 16]) / 100
xD2, xB2 = np.array([15, 10, 54, 21]) / 100, np.array([24, 65, 10, 1]) / 100
D1, B1, D2, B2 = gauss(np.column_stack([xD1, xB1, xD2, xB2]), F * xF)
D, B = D1 + B1, D2 + B2
xD, xB = (D1 * xD1 + B1 * xB1) / D, (D2 * xD2 + B2 * xB2) / B
# степень извлечения компонента колонной №1 в дистиллят: D·xD,i / (F·xF,i)
rec1 = D * xD / (F * xF) * 100
streams = {"F": (F, xF), "D": (D, xD), "B": (B, xB), "D1": (D1, xD1), "B1": (B1, xB1),
           "D2": (D2, xD2), "B2": (B2, xB2)}
report("поток   расход, моль/ч   " + "  ".join(f"{c:>7s}" for c in comps))
for k, (Fl, xx) in streams.items():
    report(f"{k:5s} {Fl:12.2f}       " + "  ".join(f"{v:7.4f}" for v in xx))
report("извлечение в D колонны №1, %:", "  ".join(f"{c} {v:.1f}" for c, v in zip(comps, rec1)))
report(f"проверка общего баланса: F - (D1 + B1 + D2 + B2) = {F - D1 - B1 - D2 - B2:.2e} моль/ч")
res51 = dict(streams=streams, rec1=rec1)

# %% Задача 5.2. Процесс Toray: последовательный модульный расчёт, разрыв по рециклу (поток 7)
task("t52", "Задача 5.2")
F1, conv = 100.0, 0.58          # свежий толуол, моль/ч; конверсия толуола за проход
# компоненты: [толуол, бензол, ксилол]


def flowsheet(s7):
    """Один проход по схеме при заданном рецикле s7; возвращает все потоки."""
    s1 = np.array([F1, 0, 0])
    s2 = s1 + s7                                        # смеситель M
    xi = conv * s2[0] / 2                               # реактор R: 2 C7H8 -> C6H6 + C8H10
    sR = np.array([-2 * xi, xi, xi])
    s3 = s2 + sR
    s4 = np.array([0.001 * s3[0], 0.995 * s3[1], 0.0])  # S1: бензольная фракция
    s5 = s3 - s4
    s7_new = np.array([0.995 * s5[0], s5[1], 0.001 * s5[2]])   # S2: рецикл
    s6 = s5 - s7_new
    return dict(s1=s1, s2=s2, R=sR, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7_new, xi=xi)


def solve_recycle(method, tol=1e-10, maxit=500):
    s7, hist = np.zeros(3), []
    g_prev = x_prev = None
    for it in range(1, maxit + 1):
        g = flowsheet(s7)["s7"]                          # g(x): новое значение рецикла
        err = np.max(np.abs(g - s7))
        hist.append((it, s7[0], err))
        if err < tol:
            return flowsheet(s7), hist
        if method == "Вегстейн" and g_prev is not None:  # ускорение по каждому компоненту
            dx = s7 - x_prev
            sl = np.divide(g - g_prev, dx, out=np.zeros(3), where=np.abs(dx) > 1e-14)
            q = np.clip(sl / (sl - 1), -5, 0)
            x_new = q * s7 + (1 - q) * g
        else:
            x_new = g                                    # простая итерация
        x_prev, g_prev, s7 = s7, g, x_new
    raise RuntimeError("нет сходимости")


sol = {}
for meth in ("простая итерация", "Вегстейн"):
    sol[meth] = solve_recycle(meth)
    report(f"{meth}: {len(sol[meth][1])} итераций")
S = sol["Вегстейн"][0]
report(f"{'':8s}" + "".join(f"{k:>9s}" for k in ("1", "2", "R", "3", "4", "5", "6", "7")))
for i, c in enumerate(("Толуол", "Бензол", "Ксилол")):
    report(f"{c:8s}" + "".join(f"{S[k][i]:9.3f}" for k in ("s1", "s2", "R", "s3", "s4", "s5", "s6", "s7")))
report(f"{'Всего':8s}" + "".join(f"{S[k].sum():9.3f}" for k in ("s1", "s2", "R", "s3", "s4", "s5", "s6", "s7")))
X_xyl = S["s6"][2] / F1
X_tot = 1 - (S["s4"][0] + S["s6"][0]) / F1
Y_benz = S["s4"][1] / F1                                 # выход бензола на свежий толуол
report(f"конверсия толуола в ксилол {X_xyl*100:.2f} %, общая конверсия толуола {X_tot*100:.2f} %")
report(f"выход бензола {Y_benz*100:.2f} % (моль на моль свежего толуола)")
res52 = dict(S=S, hist={m: h for m, (_, h) in sol.items()}, X_xyl=X_xyl, X_tot=X_tot, Y_benz=Y_benz)

fig, ax = plt.subplots(figsize=(6, 3.4))
for meth, (_, h) in sol.items():
    h = np.array(h)
    ax.semilogy(h[:, 0], h[:, 2], "o-", ms=3, label=meth)
ax.set(xlabel="Номер итерации", ylabel="Невязка рецикла, моль/ч")
ax.legend()
draw(fig, "o52")
