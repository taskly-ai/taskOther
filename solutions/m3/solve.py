# Модуль 3. Расчёт фазовых равновесий (тема 3, задачи 3.1–3.2), вариант 1.
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

# %% Задачи 3.1–3.2. Общая часть: константы фазового равновесия K(T, P)
# ln K = −A/T^2 + B − C·ln P + D/P^2 (форма 1) или + D/P (форма 2); T в °R, P в psia
KCOEF = {"CH4":   (292860.0, 8.2445, 0.8951, 59.8465, 1),
         "C2H6":  (687248.2, 7.90694, 0.866, 49.02654, 1),
         "C3H8":  (970688.6, 7.15059, 0.76984, 6.90224, 2),
         "i-C4":  (1166846.0, 7.72668, 0.92213, 0.0, 1),
         "n-C4":  (1280557.0, 7.94986, 0.96455, 0.0, 1),
         "n-C5":  (1524891.0, 7.33129, 0.89143, 0.0, 1)}


def K_values(names, T, P):
    """T в К, P в Па -> массив K_i (внутри перевод в °R и psia)."""
    TR, Pp = 1.8 * T, P / PSI
    K = []
    for n in names:
        A, B, C, D, form = KCOEF[n]
        last = D / Pp ** 2 if form == 1 else D / Pp
        K.append(np.exp(-A / TR ** 2 + B - C * np.log(Pp) + last))
    return np.array(K)


# %% Задача 3.1. ТНК и ТКК смеси (вариант 1) при 14 атм
names31 = ["CH4", "C2H6", "C3H8", "n-C4"]
z31 = np.array([0.20, 0.25, 0.35, 0.20])
P31 = 14 * ATM                                   # 14 атм = 1,4186 МПа = 205,7 psia
f_bub = lambda T: np.sum(K_values(names31, T, P31) * z31) - 1      # Σ Ki·xi = 1
f_dew = lambda T: np.sum(z31 / K_values(names31, T, P31)) - 1      # Σ yi/Ki = 1
Tb = brentq(f_bub, 100.0, 500.0)
Td = brentq(f_dew, 100.0, 500.0)
Kb, Kd = K_values(names31, Tb, P31), K_values(names31, Td, P31)
res31 = dict(P=P31, Ppsia=P31 / PSI, Tb=Tb, Td=Td, tb=Tb - 273.15, td=Td - 273.15,
             Kb=Kb, Kd=Kd, y_b=Kb * z31, x_d=z31 / Kd)
print(f"P = {P31/1e6:.4f} МПа = {P31/PSI:.2f} psia")
print(f"ТНК = {Tb:.2f} К = {Tb-273.15:.2f} °C; ТКК = {Td:.2f} К = {Td-273.15:.2f} °C")
print("K при ТНК:", np.round(Kb, 4))
print("   состав первого пузырька y:", np.round(Kb * z31, 4))
print("K при ТКК:", np.round(Kd, 4))
print("   состав первой капли x:", np.round(z31 / Kd, 4))

Tg = np.linspace(180, 380, 300)
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(Tg - 273.15, [f_bub(T) for T in Tg], label="Σ Ki∙xi − 1 (ТНК)")
ax.plot(Tg - 273.15, [f_dew(T) for T in Tg], label="Σ yi/Ki − 1 (ТКК)")
ax.plot([Tb - 273.15, Td - 273.15], [0, 0], "ko")
ax.axhline(0, color="k", lw=0.8)
ax.set(xlabel="t, °C", ylabel="Невязка", ylim=(-1.5, 3))
ax.legend()
style_axes(ax)
show(fig, "t31")

# %% Задача 3.2. Сепарационный блок С1 -> С2 -> С3: базовый расчёт
names32 = ["CH4", "C2H6", "C3H8", "i-C4", "n-C4", "n-C5"]
z32 = np.array([0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706])
BASE = [(9.8e6, 40.8), (8.7e6, 12.8), (8.7e6, -40.8)]       # (P, Па; t, °C) для С1–С3


def flash(z, T, P):
    """Однократное испарение: уравнение Рачфорда–Райса Σ zi(Ki−1)/(1+e(Ki−1)) = 0."""
    K = K_values(names32, T, P)
    if np.sum(z * K) <= 1:                  # ниже ТНК — только жидкость
        return dict(e=0.0, x=z.copy(), y=np.full_like(z, np.nan), K=K,
                    phase="жидкость")
    if np.sum(z / K) <= 1:                  # выше ТКК — только газ
        return dict(e=1.0, x=np.full_like(z, np.nan), y=z.copy(), K=K, phase="газ")
    rr = lambda e: np.sum(z * (K - 1) / (1 + e * (K - 1)))
    e = brentq(rr, 0.0, 1.0, xtol=1e-14)
    x = z / (1 + e * (K - 1))
    return dict(e=e, x=x, y=K * x, K=K, phase="две фазы")


def train(conds, z=z32, F=1.0):
    """Газ сепаратора i — сырьё сепаратора i+1. F — расход сырья, моль/с."""
    out, feed, Fi = [], z, F
    for P, t in conds:
        if Fi == 0:                         # газа из предыдущего сепаратора нет
            nan = np.full_like(z, np.nan)
            out.append(dict(e=np.nan, x=nan, y=nan, K=nan, phase="нет сырья",
                            P=P, t=t, F=0.0, V=0.0, L=0.0))
            continue
        s = flash(feed, t + 273.15, P)
        s.update(P=P, t=t, F=Fi, V=Fi * s["e"], L=Fi * (1 - s["e"]))
        out.append(s)
        feed, Fi = s["y"], s["V"]
    return out


def summary(tr, z=z32):
    """Выход газа С3, C3+ в газе, извлечение C3H8 в жидкость, потери CH4."""
    V, y = tr[-1]["V"], tr[-1]["y"]
    liq = sum(s["L"] * np.nan_to_num(s["x"]) for s in tr)          # Σ жидкостей, моль
    yC3p = np.sum(y[2:]) if V > 0 else np.nan
    return dict(V_out=V, y_out=y, yC3p=yC3p, rec_C3=liq[2] / z[2],
                loss_CH4=liq[0] / z[0], rec_C3p=np.sum(liq[2:]) / np.sum(z[2:]))


base = train(BASE)
res32 = dict(base=base, sum=summary(base))
for i, s in enumerate(base, 1):
    print(f"С{i}: P = {s['P']/1e6} МПа, t = {s['t']} °C, фаза: {s['phase']}, "
          f"e = {s['e']:.5f}, V = {s['V']:.5f}, L = {s['L']:.5f} моль")
    print("    K =", np.round(s["K"], 4))
    print("    x =", np.round(s["x"], 5), " y =", np.round(s["y"], 5))
sb = res32["sum"]
print(f"Газ С3: {sb['V_out']:.4f} моль/моль сырья, C3+ в газе {sb['yC3p']*100:.3f} %")
print(f"Извлечение C3H8 в жидкость {sb['rec_C3']*100:.2f} %; "
      f"CH4 в жидкость {sb['loss_CH4']*100:.2f} %")

# %% Задача 3.2. Исследование влияния температуры в первом сепараторе (вариант 1)
t1_grid = np.round(np.arange(-30.0, 90.01, 1.0), 1)
study = []
for t1 in t1_grid:
    tr = train([(BASE[0][0], t1), BASE[1], BASE[2]])
    s = summary(tr)
    study.append(dict(t1=t1, e=[x["e"] for x in tr], ph=[x["phase"] for x in tr],
                      L=[x["L"] for x in tr], **s))
V_arr = np.array([s["V_out"] for s in study])
# эффективный режим: максимум выхода газа С3 при t1 >= 30 °C (охлаждение воздухом,
# без холодильного цикла), состав газа (C3+) практически не зависит от t1
ok = t1_grid >= 30
t1_best = t1_grid[ok][np.argmax(V_arr[ok])]
t1_cold = t1_grid[np.argmax(V_arr)]       # глобальный максимум (с захолаживанием)
res32.update(study=study, t1_best=t1_best, t1_cold=t1_cold,
             best=train([(BASE[0][0], t1_best), BASE[1], BASE[2]]))
print(" t1,°C   e1      e2      e3     V(С3)   C3+,%  изв.C3H8,%  CH4 в жидк.,%")
for s in study:
    if s["t1"] % 10 == 0 or s["t1"] in (t1_best, t1_cold):
        e = ["  —   " if np.isnan(v) else f"{v:.4f}" for v in s["e"]]
        print(f"{s['t1']:6.1f}  {'  '.join(e)}  {s['V_out']:.4f}"
              f"  {s['yC3p']*100:6.3f}"
              f"  {s['rec_C3']*100:8.2f}  {s['loss_CH4']*100:8.2f}")
print(f"Максимум газа при t1 >= 30 °C: t1 = {t1_best} °C, V = {V_arr[ok].max():.4f};"
      f" глобальный максимум: t1 = {t1_cold} °C, V = {V_arr.max():.4f}")

fig, ax = plt.subplots(1, 3, figsize=(11, 3.4))
for j, lab in enumerate(("С1", "С2", "С3")):
    ax[0].plot(t1_grid, [s["e"][j] for s in study], label=lab)
    ax[1].plot(t1_grid, [s["L"][j] for s in study], label=f"жидкость {lab}")
ax[0].set(xlabel="t1, °C", ylabel="Доля отгона e")
ax[1].set(xlabel="t1, °C", ylabel="Расход жидкости, моль/моль сырья")
ax[2].plot(t1_grid, V_arr, label="газ С3")
ax[2].axvline(40.8, color="gray", ls=":", label="базовый режим")
ax[2].axvline(t1_best, color="r", ls="--", label="выбранный режим")
ax[2].set(xlabel="t1, °C", ylabel="Выход газа С3, моль/моль сырья")
for a in ax:
    a.legend(fontsize=8)
    style_axes(a)
show(fig, "t32_study")
