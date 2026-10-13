# Модуль 1. Эмпирические модели и регрессия, вариант 10 (образец, альтернативное решение).
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задача 1.1. Теплоёмкость пропана: полином 5-й степени по τ = T/1000
task("t11", "Задача 1.1")
T = np.array([50, 100, 150, 200, 273.15, 300, 400, 500, 600, 700,
              800, 900, 1000, 1100, 1200, 1300])
C = np.array([34.16, 41.3, 48.79, 56.07, 68.74, 73.93, 94.01, 112.59,
              128.7, 142.67, 154.77, 163.35, 174.6, 182.67, 189.74, 195.85])
deg, T0, T1 = 5, 50.0, 1300.0
tau = T / 1000                               # безразмерная температура
V = np.vander(tau, deg + 1, increasing=True)  # столбцы 1, τ, τ^2, ..., τ^5
c, *_ = np.linalg.lstsq(V, C, rcond=None)     # МНК через QR/SVD
cond_tau = np.linalg.cond(V)
cond_T = np.linalg.cond(np.vander(T, deg + 1, increasing=True))
C_mod = V @ c
q11 = quality(C, C_mod, deg + 1)
# интеграл полинома: ∫C dT = 1000·Σ c_j·τ^(j+1)/(j+1)
F = lambda t: 1000 * sum(cj * t ** (j + 1) / (j + 1) for j, cj in enumerate(c))
I_mod = F(T1 / 1000) - F(T0 / 1000)
I_trap = float(np.sum((C[1:] + C[:-1]) / 2 * np.diff(T)))   # трапеции вручную
I_simp = float(integrate.simpson(C, x=T))                    # Симпсон (неравном. сетка)
Cm = {k: v / (T1 - T0) for k, v in (("модель", I_mod), ("трапеции", I_trap), ("Симпсон", I_simp))}
for j, cj in enumerate(c):
    report(f"c{j} = {cj:10.4f} Дж/(моль·К)")
report(f"cond(V): по τ = {cond_tau:.3e}, по T = {cond_T:.3e}")
report(f"R2 = {q11['R2']:.6f}, s = {q11['s']:.3f} Дж/(моль·К), max δ = {q11['dmax']:.2f} %")
for k, v in Cm.items():
    report(f"<C>({k:9s}) = {v:.3f} Дж/(моль·К)")
res11 = dict(c=c, q=q11, I=dict(модель=I_mod, трапеции=I_trap, Симпсон=I_simp), Cm=Cm,
             cond_tau=cond_tau, cond_T=cond_T, e=C - C_mod, T=T.copy(), C=C.copy())

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
tg = np.linspace(T0, T1, 300) / 1000
ax[0].plot(T, C, "s", ms=4, label="таблица")
ax[0].plot(tg * 1000, np.vander(tg, deg + 1, increasing=True) @ c, label="полином 5-й степени")
ax[0].set(xlabel="T, К", ylabel="C, Дж/(моль∙К)")
ax[0].legend()
ax[1].stem(T, C - C_mod)
ax[1].set(xlabel="T, К", ylabel="Остаток, Дж/(моль∙К)")
draw(fig, "o11")

# %% Задача 1.2. Модель y = a·(ln(x/b))^(-2/3): least_squares и две альтернативы
task("t12", "Задача 1.2")
x = np.array([0.263, 0.294, 0.321, 0.367, 0.429, 0.608, 1.33, 1.36])
y = np.array([0.34, 0.32, 0.24, 0.20, 0.16, 0.11, 0.06, 0.04])
f_given = lambda p, x: p[0] * np.log(x / p[1]) ** (-2 / 3)
sol = optimize.least_squares(lambda p: f_given(p, x) - y, x0=[0.1, 0.2],
                             bounds=([0, 1e-4], [np.inf, 0.2629]))
a, b = sol.x
q_given = quality(y, f_given(sol.x, x), 2)
# альтернатива 1: гипербола y = A/x + B (линейна по 1/x)
M = np.column_stack([1 / x, np.ones_like(x)])
(Ah, Bh), *_ = np.linalg.lstsq(M, y, rcond=None)
q_hyp = quality(y, Ah / x + Bh, 2)
# альтернатива 2: степенная y = K·x^(-n), МНК в логарифмах: ln y = ln K - n·ln x
slope, ln_K = np.polyfit(np.log(x), np.log(y), 1)
K_p, n_p = np.exp(ln_K), -slope
q_pow = quality(y, K_p * x ** (-n_p), 2)
report(f"заданная:  a = {a:.4f}, b = {b:.4f} кг/с; R2 = {q_given['R2']:.4f}, SSE = {q_given['SSE']:.5f}")
report(f"гипербола: A = {Ah:.4f} кг/с, B = {Bh:.4f}; R2 = {q_hyp['R2']:.4f}, SSE = {q_hyp['SSE']:.5f}")
report(f"степенная: K = {K_p:.4f}, n = {n_p:.4f}; R2 = {q_pow['R2']:.4f}, SSE = {q_pow['SSE']:.5f}")
res12 = dict(a=a, b=b, q=q_given, hyp=(Ah, Bh, q_hyp), pow=(K_p, n_p, q_pow),
             y_given=f_given(sol.x, x), x=x.copy(), y=y.copy())

fig, ax = plt.subplots(figsize=(6, 3.6))
xg = np.linspace(0.27, 1.4, 300)
ax.plot(x, y, "ko", label="опыт")
ax.plot(xg, f_given(sol.x, xg), label="заданная модель")
ax.plot(xg, Ah / xg + Bh, "--", label="гипербола")
ax.plot(xg, K_p * xg ** (-n_p), ":", label="степенная (МНК в логарифмах)")
ax.set(xlabel="x, кг/с", ylabel="y, доли")
ax.legend()
draw(fig, "o12")

# %% Задача 1.3. Аррениус: линеаризация, МНК по относительным ошибкам, два участка
task("t13", "Задача 1.3")
t = np.arange(100, 501, 50.0)
k = np.array([0.10, 0.56, 1.76, 3.54, 9.53, 15.98, 25.04, 60.74, 143.60])
TK = t + 273.15
X = np.column_stack([np.ones_like(TK), -1 / (R * TK)])     # ln k = ln A - Ea/(R·T)
(lnA, Ea), *_ = np.linalg.lstsq(X, np.log(k), rcond=None)
q_ln = quality(np.log(k), X @ [lnA, Ea], 2)
# МНК по относительным отклонениям: (k_расч - k)/k -> min
rel = optimize.least_squares(lambda p: (np.exp(p[0] - p[1] / (R * TK)) - k) / k, x0=[lnA, Ea])
lnA_r, Ea_r = rel.x
q_rel = quality(k, np.exp(lnA_r - Ea_r / (R * TK)), 2)
# два участка: 100-300 °C и 300-500 °C
seg = {}
for name, msk in (("100–300 °C", t <= 300), ("300–500 °C", t >= 300)):
    (l_A, E), *_ = np.linalg.lstsq(X[msk], np.log(k[msk]), rcond=None)
    seg[name] = (E, np.exp(l_A), quality(np.log(k[msk]), X[msk] @ [l_A, E], 2)["R2"])
report(f"линеаризация: Ea = {Ea/1000:.2f} кДж/моль, A = {np.exp(lnA):.4e} 1/с, R2(ln k) = {q_ln['R2']:.4f}")
report(f"МНК по отн. ошибкам: Ea = {Ea_r/1000:.2f} кДж/моль, A = {np.exp(lnA_r):.4e} 1/с, "
       f"max δ = {q_rel['dmax']:.1f} %")
for name, (E, A_, r2_) in seg.items():
    report(f"участок {name}: Ea = {E/1000:.2f} кДж/моль, A = {A_:.4e} 1/с, R2(ln k) = {r2_:.4f}")
res13 = dict(Ea=Ea, A=np.exp(lnA), q_ln=q_ln, Ea_r=Ea_r, A_r=np.exp(lnA_r), q_rel=q_rel, seg=seg,
             e_ln=np.log(k) - X @ [lnA, Ea], t=t.copy(), k=k.copy())

fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(1000 / TK, np.log(k), "ko", label="опыт")
ax.plot(1000 / TK, X @ [lnA, Ea], label="один участок")
for name, msk in (("100–300 °C", t <= 300), ("300–500 °C", t >= 300)):
    E, A_, _ = seg[name]
    ax.plot(1000 / TK[msk], np.log(A_) - E / (R * TK[msk]), "--", label=f"участок {name}")
ax.set(xlabel="1000/T, 1/К", ylabel="ln k (k в 1/с)")
ax.legend()
draw(fig, "o13")

# %% Задача 1.4. Вязкость глицерина: полиномы по z = (T - 330)/60, F-критерий, ln μ(1/T)
task("t14", "Задача 1.4")
from scipy import stats
Tv = np.array([270, 280, 290, 300, 310, 320, 330, 350, 370, 390.0])   # при 250, 260 К данных нет
mu = np.array([12.00, 8.500, 6.050, 4.250, 3.500, 2.600, 2.000, 1.200, 0.730, 0.450])
z = (Tv - 330) / 60
fits, n = {}, len(mu)
for d in (1, 2, 3):
    Vd = np.vander(z, d + 1, increasing=True)
    bd, *_ = np.linalg.lstsq(Vd, mu, rcond=None)
    fits[d] = dict(b=bd, mu=Vd @ bd, q=quality(mu, Vd @ bd, d + 1))
for d in (2, 3):                              # нужен ли следующий член полинома?
    s1, s2 = fits[d - 1]["q"]["SSE"], fits[d]["q"]["SSE"]
    fits[d]["F"] = (s1 - s2) / (s2 / (n - d - 1))
    fits[d]["Fcr"] = stats.f.ppf(0.95, 1, n - d - 1)
# сравнение: ln μ = A + B/T + C/T^2 (уравнение Андраде с поправкой; линейный МНК по ln μ)
W = np.column_stack([np.ones_like(Tv), 1 / Tv, 1 / Tv ** 2])
pa, *_ = np.linalg.lstsq(W, np.log(mu), rcond=None)
q_and = quality(mu, np.exp(W @ pa), 3)
for d, f_ in fits.items():
    report(f"степень {d}: b = {np.round(f_['b'], 4)}")
    extra = f"; F = {f_['F']:.1f} (Fкр = {f_['Fcr']:.2f})" if "F" in f_ else ""
    report(f"   R2 = {f_['q']['R2']:.4f}, SSE = {f_['q']['SSE']:.3f}, "
           f"max δ = {f_['q']['dmax']:.1f} %{extra}")
report(f"ln mu = {pa[0]:.4f} + {pa[1]:.1f}/T + ({pa[2]:.4e})/T^2; R2 = {q_and['R2']:.5f}, "
       f"max δ = {q_and['dmax']:.2f} %")
res14 = dict(fits=fits, lnmu=(pa, q_and), T=Tv.copy(), mu=mu.copy())

fig, ax = plt.subplots(figsize=(6, 3.6))
Tg = np.linspace(270, 390, 300)
ax.semilogy(Tv, mu, "ko", label="опыт")
for d in (1, 2, 3):
    mg = np.vander((Tg - 330) / 60, d + 1, increasing=True) @ fits[d]["b"]
    ax.semilogy(Tg[mg > 0], mg[mg > 0], label=f"полином {d}-й степени")
ax.semilogy(Tg, np.exp(pa[0] + pa[1] / Tg + pa[2] / Tg ** 2), "k--", label="ln μ = A + B/T + C/T²")
ax.set(xlabel="T, К", ylabel="μ, мПа∙с (лог. шкала)")
ax.legend(fontsize=8)
draw(fig, "o14")
