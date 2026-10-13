# Модуль 1. Эмпирические модели и регрессия (тема 1, задачи 1.1–1.4), варианты 9 и 10.
# Запуск: python solutions/m1/solve.py   (в Colab — ячейки ниже после ячейки 0)
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

import atexit; atexit.register(show_results)  # noqa: консольный запуск — вывод в конце

# %% Задача 1.1. Полином 5-й степени C(T) и средняя теплоёмкость пропана
task("t11", "Задача 1.1")
T11 = np.array([50, 100, 150, 200, 273.15, 300, 400, 500, 600, 700,
                800, 900, 1000, 1100, 1200, 1300])                      # К
C11 = np.array([34.16, 41.3, 48.79, 56.07, 68.74, 73.93, 94.01, 112.59,
                128.7, 142.67, 154.77, 163.35, 174.6, 182.67, 189.74, 195.85])
deg = 5                                     # степень полинома
T0, Tk = 50.0, 1300.0                       # пределы интегрирования, К

# МНК с масштабированием аргумента (без него матрица для T^5 плохо обусловлена)
P11 = np.polynomial.Polynomial.fit(T11, C11, deg)
a11 = P11.convert().coef                    # a0, a1, ..., a5 для T в К
C_fit = P11(T11)
P_int = P11.integ()                         # первообразная полинома
I_poly = P_int(Tk) - P_int(T0)
trap = getattr(np, "trapezoid", None) or np.trapz   # NumPy 2.x / 1.x
I_trap = trap(C11, T11)                     # интеграл по таблице (трапеции)
Cm_poly = I_poly / (Tk - T0)
Cm_trap = I_trap / (Tk - T0)
res11 = dict(a=a11, R2=r2(C11, C_fit), SSE=sse(C11, C_fit),
             I_poly=I_poly, I_trap=I_trap, Cm_poly=Cm_poly, Cm_trap=Cm_trap,
             d_rel=abs(Cm_poly - Cm_trap) / Cm_trap * 100, resid=C11 - C_fit,
             s=np.sqrt(sse(C11, C_fit) / (len(C11) - deg - 1)))
for j, c in enumerate(a11):
    out(f"a{j} = {c: .6e}")
out(f"R2 = {res11['R2']:.6f};  SSE = {res11['SSE']:.3f};  s = {res11['s']:.3f}")
out(f"Интеграл: полином {I_poly:.1f}, трапеции {I_trap:.1f}")
out(f"<C>(1300 K): полином {Cm_poly:.3f}, трапеции {Cm_trap:.3f}, "
    f"расхождение {res11['d_rel']:.3f} %")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
Tg = np.linspace(T0, Tk, 200)
ax[0].plot(T11, C11, "o", label="эксперимент")
ax[0].plot(Tg, P11(Tg), "-", label="полином 5-й степени")
ax[0].set(xlabel="T, К", ylabel="C, Дж/(моль∙К)")
ax[0].legend()
ax[1].bar(T11, res11["resid"], width=25)
ax[1].axhline(0, color="k", lw=0.8)
ax[1].set(xlabel="T, К", ylabel="Остаток C − Cрасч, Дж/(моль∙К)")
for a in ax:
    style_axes(a)
show(fig, "t11")

# %% Задача 1.2. Модель y = a·(ln(x/b))^(-2/3) для отпарной колонны
task("t12", "Задача 1.2")
x12 = np.array([0.263, 0.294, 0.321, 0.367, 0.429, 0.608, 1.33, 1.36])   # кг/с
y12 = np.array([0.34, 0.32, 0.24, 0.20, 0.16, 0.11, 0.06, 0.04])


def model_given(x, a, b):
    return a * np.log(x / b) ** (-2 / 3)


def model_power(x, a, n):                   # альтернатива: степенная
    return a * x ** (-n)


def model_exp(x, a, k, c):                  # альтернатива: экспонента
    return a * np.exp(-k * x) + c


# Ограничение модели: ln(x/b) > 0 при всех x, т.е. 0 < b < x_min = 0.263 кг/с.
# Линеаризация y^(-3/2) = a^(-3/2)·(ln x − ln b) даёт b > x_min (проверка ниже),
# поэтому параметры ищутся нелинейным МНК с границами.
k_lin, m_lin = np.polyfit(np.log(x12), y12 ** -1.5, 1)
b_linearized = np.exp(-m_lin / k_lin)
out(f"b по линеаризации = {b_linearized:.4f} кг/с > x_min = {x12.min()}"
    " -> недопустимо")
models = {"заданная": (model_given, [0.1, 0.2], ([0, 1e-4], [np.inf, 0.2629])),
          "степенная": (model_power, [0.05, 1.0], (-np.inf, np.inf)),
          "экспоненциальная": (model_exp, [1.0, 3.0, 0.05], (-np.inf, np.inf))}
res12 = {"b_linearized": b_linearized}
for name, (fn, p0, bnd) in models.items():
    p, cov = curve_fit(fn, x12, y12, p0=p0, bounds=bnd, maxfev=20000)
    yc = fn(x12, *p)
    n, k = len(y12), len(p)
    res12[name] = dict(p=p, R2=r2(y12, yc), SSE=sse(y12, yc), k=k, yc=yc,
                       R2adj=1 - (1 - r2(y12, yc)) * (n - 1) / (n - k),
                       max_abs=np.max(np.abs(y12 - yc)))
    out(f"{name:17s} p = {np.round(p, 5)}  R2 = {res12[name]['R2']:.4f}  "
        f"R2adj = {res12[name]['R2adj']:.4f}  SSE = {res12[name]['SSE']:.5f}")

fig, ax = plt.subplots(figsize=(6, 3.8))
xg = np.linspace(0.263, 1.4, 300)
ax.plot(x12, y12, "ko", label="эксперимент")
for name, (fn, _, _) in models.items():
    ax.plot(xg, fn(xg, *res12[name]["p"]), label=f"{name} модель")
ax.set(xlabel="Расход пара x, кг/с", ylabel="Содержание воды y, доли")
ax.legend()
style_axes(ax)
show(fig, "t12")

# %% Задача 1.3. Уравнение Аррениуса
task("t13", "Задача 1.3")
t13 = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500.0])        # °C
k13 = np.array([0.10, 0.56, 1.76, 3.54, 9.53, 15.98, 25.04, 60.74, 143.60])  # 1/с
T13 = t13 + 273.15                                                       # К

# 1) линеаризация: ln k = ln A − (Ea/R)·(1/T)
slope, intercept = np.polyfit(1 / T13, np.log(k13), 1)
Ea_lin, A_lin = -slope * R, np.exp(intercept)
lnk_calc = intercept + slope / T13
# 2) нелинейный МНК по самим k (начальное приближение — из линеаризации)
(A_nl, Ea_nl), _ = curve_fit(lambda T, A, Ea: A * np.exp(-Ea / (R * T)),
                             T13, k13, p0=[A_lin, Ea_lin], maxfev=20000)
k_lin = A_lin * np.exp(-Ea_lin / (R * T13))
k_nl = A_nl * np.exp(-Ea_nl / (R * T13))
res13 = dict(Ea_lin=Ea_lin, A_lin=A_lin, Ea_nl=Ea_nl, A_nl=A_nl,
             R2_ln=r2(np.log(k13), lnk_calc), R2_k_lin=r2(k13, k_lin),
             R2_k_nl=r2(k13, k_nl), R2_ln_nl=r2(np.log(k13), np.log(k_nl)),
             resid_ln=np.log(k13) - lnk_calc, k_lin=k_lin, k_nl=k_nl)
out(f"Линеаризация: Ea = {Ea_lin/1000:.2f} кДж/моль, A = {A_lin:.4e} 1/с, "
    f"R2(ln k) = {res13['R2_ln']:.4f}, R2(k) = {res13['R2_k_lin']:.4f}")
out(f"Нелинейный МНК: Ea = {Ea_nl/1000:.2f} кДж/моль, A = {A_nl:.4e} 1/с, "
    f"R2(k) = {res13['R2_k_nl']:.4f}")
out("Остатки ln k:", np.round(res13["resid_ln"], 3))
# проверка постоянства Ea: «локальная» энергия активации по соседним точкам
Ea_loc = -R * np.diff(np.log(k13)) / np.diff(1 / T13)
res13["Ea_loc"] = Ea_loc
out("Ea по соседним точкам, кДж/моль:", np.round(Ea_loc / 1000, 1))

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].plot(1000 / T13, np.log(k13), "ko", label="эксперимент")
ax[0].plot(1000 / T13, lnk_calc, "-", label="линеаризация")
ax[0].set(xlabel="1000/T, 1/К", ylabel="ln k (k в 1/с)")
ax[0].legend()
Tg = np.linspace(T13[0], T13[-1], 200)
ax[1].plot(T13, k13, "ko", label="эксперимент")
ax[1].plot(Tg, A_lin * np.exp(-Ea_lin / (R * Tg)), "-", label="линеаризация")
ax[1].plot(Tg, A_nl * np.exp(-Ea_nl / (R * Tg)), "--", label="нелинейный МНК")
ax[1].set(xlabel="T, К", ylabel="k, 1/с")
ax[1].legend()
for a in ax:
    style_axes(a)
show(fig, "t13")

# %% Задача 1.4. Вязкость глицерина: полиномы 1–3 степени
task("t14", "Задача 1.4")
# при 250 и 260 К данных нет («-» в таблице задания)
T14 = np.array([270, 280, 290, 300, 310, 320, 330, 350, 370, 390.0])            # К
mu14 = np.array([12.00, 8.500, 6.050, 4.250, 3.500, 2.600, 2.000, 1.200,
                 0.730, 0.450])                                                # мПа∙с
res14 = {}
for d in (1, 2, 3):
    p = np.polynomial.Polynomial.fit(T14, mu14, d).convert().coef   # b0, b1, ...
    mc = np.polynomial.polynomial.polyval(T14, p)
    n = len(mu14)
    res14[d] = dict(b=p, mu_calc=mc, R2=r2(mu14, mc), SSE=sse(mu14, mc),
                    R2adj=1 - (1 - r2(mu14, mc)) * (n - 1) / (n - d - 1),
                    s=np.sqrt(sse(mu14, mc) / (n - d - 1)),
                    max_err=np.max(np.abs(mu14 - mc) / mu14) * 100)
    out(f"степень {d}: b = {np.array2string(p, precision=6)}")
    out(f"   R2 = {res14[d]['R2']:.5f}, R2adj = {res14[d]['R2adj']:.5f}, "
        f"SSE = {res14[d]['SSE']:.3e}, s = {res14[d]['s']:.4f} мПа∙с, "
        f"макс. отн. ошибка = {res14[d]['max_err']:.2f} %")

# для сравнения: уравнение Андраде ln μ = A + B/T (линейный МНК по ln μ)
B_and, A_and = np.polyfit(1 / T14, np.log(mu14), 1)
mu_and = np.exp(A_and + B_and / T14)
res14["andrade"] = dict(A=A_and, B=B_and, mu_calc=mu_and, R2=r2(mu14, mu_and),
                        SSE=sse(mu14, mu_and),
                        max_err=np.max(np.abs(mu14 - mu_and) / mu14) * 100)
out(f"Андраде: ln mu = {A_and:.4f} + {B_and:.1f}/T; R2 = {res14['andrade']['R2']:.5f}, "
    f"SSE = {res14['andrade']['SSE']:.3e}, "
    f"макс. отн. ошибка = {res14['andrade']['max_err']:.2f} %")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
Tg = np.linspace(270, 390, 200)
ax[0].plot(T14, mu14, "ko", label="эксперимент")
for d in (1, 2, 3):
    ax[0].plot(Tg, np.polynomial.polynomial.polyval(Tg, res14[d]["b"]),
               label=f"полином {d}-й степени")
    ax[1].plot(T14, mu14 - res14[d]["mu_calc"], "o-", label=f"{d}-я степень")
ax[0].plot(Tg, np.exp(A_and + B_and / Tg), "k--", label="уравнение Андраде")
ax[0].set(xlabel="T, К", ylabel="μ, мПа∙с")
ax[1].axhline(0, color="k", lw=0.8)
ax[1].set(xlabel="T, К", ylabel="Остаток μ − μрасч, мПа∙с")
for a in ax:
    a.legend()
    style_axes(a)
show(fig, "t14")
