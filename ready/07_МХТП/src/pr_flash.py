"""Ориентир для перекрёстной проверки задачи 3.2 в Aspen HYSYS: однократное испарение
по уравнению Пенга–Робинсона (тот же пакет свойств, что выбирается в HYSYS).

    python pr_flash.py        (печатает результаты и строит fig/hysys_s1_*.png)

Зачем: в отчёте K считаются по корреляции McWilliams (так требует задание), а HYSYS
считает фазовое равновесие по уравнению состояния. Скрипт показывает, что увидит
студент в компьютерном классе, и позволяет объяснить расхождение.

Модель: PR, правило смешения ван-дер-Ваальса, kij = 0 (HYSYS подставляет свои небольшие
kij для пар углеводородов — отличия в 2–3-м знаке, сильнее вблизи критической области).
Tc, Pc, ω — справочник Refining & Chemicals (IFP Training), табл. A2 (тот же источник,
что для задач 2.1–2.2). Алгоритм: тест стабильности Михельсена (две пробные фазы,
начальные K по Вильсону) -> если смесь неустойчива, метод последовательных подстановок
K = φL/φV с решением уравнения Рачфорда–Райса на каждом шаге.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mhtp_v8 as m  # noqa: E402

R, ATM, MPA = m.R, m.ATM, m.MPA

# Tc, К; Pc, атм; ω — справочник IFP, табл. A2 (порядок как m.SEP_NAMES)
PR_CRIT = {
    "CH4": (190.6, 45.4, 0.008),
    "C2H6": (305.4, 48.2, 0.098),
    "C3H8": (369.8, 41.9, 0.152),
    "i-C4H10": (408.1, 36.0, 0.176),
    "n-C4H10": (425.2, 37.5, 0.193),
    "n-C5H12": (469.6, 33.3, 0.251),
}
TC = np.array([PR_CRIT[n][0] for n in m.SEP_NAMES])
PC = np.array([PR_CRIT[n][1] for n in m.SEP_NAMES]) * ATM
W = np.array([PR_CRIT[n][2] for n in m.SEP_NAMES])
SQ2 = np.sqrt(2.0)


def pr_ab(T):
    """Параметры PR чистых компонентов: a, Па·м6/моль2; b, м3/моль."""
    mm = 0.37464 + 1.54226 * W - 0.26992 * W ** 2
    a = 0.45724 * R ** 2 * TC ** 2 / PC * (1 + mm * (1 - np.sqrt(T / TC))) ** 2
    return a, 0.07780 * R * TC / PC


def pr_roots(x, T, P):
    """Все корни Z > B для состава x; каждый — (Z, ln φ_i, приведённая энергия Гиббса)."""
    a, b = pr_ab(T)
    aij = np.sqrt(np.outer(a, a))                  # kij = 0
    am, bm = x @ aij @ x, x @ b
    A, B = am * P / (R * T) ** 2, bm * P / (R * T)
    zr = np.roots([1.0, -(1 - B), A - 3 * B ** 2 - 2 * B, -(A * B - B ** 2 - B ** 3)])
    zr = sorted({round(z.real, 13) for z in zr if abs(z.imag) < 1e-9 and z.real > B})
    s = aij @ x
    out = []
    for Z in zr:
        lnphi = (b / bm * (Z - 1) - np.log(Z - B) - A / (2 * SQ2 * B) * (2 * s / am - b / bm)
                 * np.log((Z + (1 + SQ2) * B) / (Z + (1 - SQ2) * B)))
        g = float(np.sum(x * (np.log(np.where(x > 0, x, 1.0)) + lnphi)))
        out.append((Z, lnphi, g))
    return out


def pr_phase(x, T, P):
    """Устойчивый корень (минимум энергии Гиббса): (Z, ln φ)."""
    Z, lnphi, _ = min(pr_roots(x, T, P), key=lambda t: t[2])
    return Z, lnphi


def k_wilson(T, P):
    return PC / P * np.exp(5.373 * (1 + W) * (1 - TC / T))


def stability(z, T, P):
    """Тест Михельсена. Возвращает (S, W) неустойчивой пробной фазы или None (смесь устойчива)."""
    _, lnz = pr_phase(z, T, P)
    d = np.log(z) + lnz
    K, best = k_wilson(T, P), None
    for Wt in (z * K, z / K):                      # пробная фаза «газ» и «жидкость»
        for _ in range(5000):
            _, lnw = pr_phase(Wt / Wt.sum(), T, P)
            Wn = np.exp(d - lnw)
            done = np.max(np.abs(np.log(Wn / Wt))) < 1e-10
            Wt = Wn
            if done:
                break
        S, Wnorm = Wt.sum(), Wt / Wt.sum()
        if np.max(np.abs(Wnorm - z)) > 1e-4 and S > 1 + 1e-8 and (best is None or S > best[0]):
            best = (S, Wnorm)
    return best


def pr_flash(z, T, P):
    """Изотермический флеш PR. state: «двухфазная» или «одна фаза» (смесь устойчива)."""
    st = stability(z, T, P)
    if st is None:
        Z, _ = pr_phase(z, T, P)
        return dict(state="одна фаза", e=np.nan, Z=Z, x=None, y=None, K=None, res=0.0)
    _, Wt = st
    K = Wt / z if Wt @ TC < z @ TC else z / Wt     # пробная фаза легче питания -> это газ
    for it in range(20000):
        f = lambda e: np.sum(z * (K - 1) / (1 + e * (K - 1)))
        lo, hi = 1 / (1 - K.max()), 1 / (1 - K.min())
        e = brentq(f, lo + 1e-14 * (hi - lo), hi - 1e-14 * (hi - lo), xtol=1e-15)
        x = z / (1 + e * (K - 1))
        x, y = x / x.sum(), K * x / np.sum(K * x)
        Zl, lnl = pr_phase(x, T, P)
        Zv, lnv = pr_phase(y, T, P)
        Kn = np.exp(lnl - lnv)
        done = np.max(np.abs(np.log(Kn / K))) < 1e-11
        K = Kn
        if done:
            break
    x = z / (1 + e * (K - 1))
    x, y = x / x.sum(), K * x / np.sum(K * x)
    Zl, lnl = pr_phase(x, T, P)
    Zv, lnv = pr_phase(y, T, P)
    res = float(np.max(np.abs(np.log(x) + lnl - np.log(y) - lnv)))   # равенство фугитивностей
    return dict(state="двухфазная", e=e, x=x, y=y, K=K, Zl=Zl, Zv=Zv, it=it, res=res)


@lru_cache(maxsize=None)
def pr_train(P2_MPa, P3_MPa=None):
    """Блок С1–С3 (условия С1 и температуры — базовые). Однофазный сепаратор пропускает
    весь поток дальше (в HYSYS он уйдёт в один из выходов целиком)."""
    P3_MPa = P2_MPa if P3_MPa is None else P3_MPa
    conds = [(m.SEP_BASE[0][0], m.SEP_BASE[0][1]), (P2_MPa * MPA, m.SEP_BASE[1][1]),
             (P3_MPa * MPA, m.SEP_BASE[2][1])]
    z, F, out = m.SEP_Z.copy(), 1.0, []
    for P, T in conds:
        r = pr_flash(z, T, P)
        r.update(P=P, T=T, F=F, z=z)
        if r["state"] == "одна фаза":
            r.update(V=F, L=0.0)
        else:
            r.update(V=F * r["e"], L=F * (1 - r["e"]))
            F, z = r["V"], r["y"]
        out.append(r)
    return out


def train_closure(tr):
    """Покомпонентный МБ блока: Σ L·x + газ последнего двухфазного = сырьё (на 1 моль)."""
    liq = sum(s["L"] * s["x"] for s in tr if s["state"] == "двухфазная")
    last = [s for s in tr if s["state"] == "двухфазная"][-1]
    return float(np.max(np.abs(liq + last["V"] * last["y"] - m.SEP_Z)))


def psat_pure(i, T):
    """Давление насыщения чистого компонента i по PR (равенство фугитивностей), Па."""
    x = np.zeros(len(TC))
    x[i] = 1.0

    def g(P):
        rr = pr_roots(x, T, P)
        return np.nan if len(rr) < 2 else rr[0][1][i] - rr[-1][1][i]
    Ps = np.linspace(0.02, 0.999, 300) * PC[i]
    v = [g(P) for P in Ps]
    for k in range(len(Ps) - 1):
        if np.isfinite(v[k]) and np.isfinite(v[k + 1]) and v[k] * v[k + 1] < 0:
            return brentq(g, Ps[k], Ps[k + 1], xtol=1e-6)
    raise ValueError("нет давления насыщения")


def dew_T_upper(P, z=None, t_lo=-60.0, t_hi=60.0):
    """Наибольшая температура двухфазной области при давлении P (бисекция по тесту
    стабильности), °C; None — при этом давлении смесь однофазна во всём интервале."""
    z = m.SEP_Z if z is None else z
    ts = np.arange(t_lo, t_hi + 1e-9, 5.0)
    unstable = [stability(z, t + 273.15, P) is not None for t in ts]
    if not any(unstable):
        return None
    k = max(i for i, u in enumerate(unstable) if u)
    if k == len(ts) - 1:
        return t_hi
    a, b = ts[k], ts[k + 1]
    for _ in range(30):
        c = (a + b) / 2
        a, b = (c, b) if stability(z, c + 273.15, P) is not None else (a, c)
    return (a + b) / 2


def cricondentherm(P_grid=np.arange(3.0, 9.01, 0.5)):
    vals = [(P, dew_T_upper(P * MPA)) for P in P_grid]
    vals = [(P, t) for P, t in vals if t is not None]
    return max(vals, key=lambda v: v[1]), vals


def mcw_dew_T(P_MPa):
    """Температура начала конденсации сырья по McWilliams (для сравнения), °C."""
    f = lambda T: np.sum(m.SEP_Z / m.k_mcw(m.SEP_NAMES, T, P_MPa * MPA)) - 1
    return brentq(f, 200.0, 500.0) - 273.15


def study(P2_grid=np.round(np.arange(4.0, 9.51, 0.5), 2)):
    rows = []
    for P2 in P2_grid:
        tr = pr_train(float(P2))
        rows.append(dict(P2=float(P2), states=[s["state"] for s in tr],
                         e=[s["e"] for s in tr], V3=tr[2]["V"]))
    return rows


def run_all(verbose=True, plots=True):
    res = dict(base=pr_train(8.7), choice=pr_train(m.P2_CHOICE),
               psat_c3_tb=psat_pure(2, 273.15 - 42.1), study=study(),
               cdt=cricondentherm(), mcw_dew98=mcw_dew_T(9.8))
    res["stab_C1"] = stability(m.SEP_Z, m.SEP_BASE[0][1], m.SEP_BASE[0][0])
    if verbose:
        print_all(res)
    if plots:
        plot_scheme()
        plot_study(res)
    return res


def _fmt_train(tr):
    lines = []
    for j, s in enumerate(tr, 1):
        head = f"С{j}: P = {s['P']/MPA:.1f} МПа, t = {s['T']-273.15:.1f} °C, питание {s['F']:.4f}: "
        if s["state"] == "одна фаза":
            lines.append(head + f"одна фаза (Z = {s['Z']:.3f}), весь поток проходит дальше")
        else:
            lines.append(head + f"e = {s['e']:.4f}, V = {s['V']:.4f}, L = {s['L']:.4f}, "
                         f"невязка фугитивностей {s['res']:.1e}")
            lines.append("    K = " + np.array2string(s["K"], precision=4))
            lines.append("    y = " + np.array2string(s["y"], precision=5))
    return "\n".join(lines)


def print_all(res):
    print("PR: давление насыщения пропана при t_кип = −42,1 °C:", f"{res['psat_c3_tb']/1000:.1f} кПа")
    print("PR: сырьё при 40,8 °C и 9,8 МПа —", "устойчиво (одна фаза)" if res["stab_C1"] is None else "неустойчиво")
    (Pc_, tc_), vals = res["cdt"]
    print(f"PR: крикондентерма сырья ≈ {tc_:.1f} °C (при ≈ {Pc_:.1f} МПа); "
          f"McWilliams: точка росы при 9,8 МПа = {res['mcw_dew98']:.1f} °C")
    print("=== Базовый режим (P2 = P3 = 8,7 МПа)\n" + _fmt_train(res["base"]))
    print(f"=== Рекомендуемый режим (P2 = P3 = {m.P2_CHOICE} МПа)\n" + _fmt_train(res["choice"]))
    print(" P2   С1      С2      С3      V3")
    for r in res["study"]:
        cells = ["1ф    " if s == "одна фаза" else f"{e:.4f}" for s, e in zip(r["states"], r["e"])]
        print(f" {r['P2']:.1f}  " + "  ".join(cells) + f"  {r['V3']:.4f}")


def plot_scheme():
    """Схема сценария 1 в HYSYS: сепараторы V-100…V-102 и холодильники E-100, E-101."""
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9.8, 3.4))
    ax.set_xlim(0, 14.0)
    ax.set_ylim(0, 5)
    ax.axis("off")
    xs_v, xs_e = [2.0, 6.7, 11.4], [4.1, 8.8]
    labels = ["V-100\n(С1)", "V-101\n(С2)", "V-102\n(С3)"]
    conds = ["9800 кПа\n40,8 °C", "8700 кПа\n12,8 °C", "8700 кПа\n−40,8 °C"]
    for j, x in enumerate(xs_v):
        m._box(ax, x, 2.4, 1.0, 1.8, labels[j])
        ax.text(x + 0.62, 1.0, conds[j], fontsize=7.5, ha="left", va="center", color="#52514e")
        m._arrow(ax, [(x, 1.5), (x, 0.45)], f"Ж{j+1}", (x - 0.12, 0.6), ha="right")
    for j, x in enumerate(xs_e):
        m._box(ax, x, 3.8, 0.9, 0.8, f"E-10{j}", fc="#eef4fb")
        m._arrow(ax, [(x, 4.75), (x, 4.2)], f"Q-10{j}", (x + 0.1, 4.75), ha="left")
        # газ сепаратора -> холодильник -> следующий сепаратор
        m._arrow(ax, [(xs_v[j], 3.3), (xs_v[j], 3.8), (x - 0.45, 3.8)],
                 f"Газ С{j+1}", ((xs_v[j] + x) / 2 - 0.2, 4.05), fs=7.5)
        m._arrow(ax, [(x + 0.45, 3.8), (x + 0.8, 3.8), (x + 0.8, 2.4), (xs_v[j + 1] - 0.5, 2.4)],
                 f"Пит. С{j+2}", ((x + 0.8 + xs_v[j + 1] - 0.5) / 2, 2.65), fs=7.5)
    m._arrow(ax, [(0.2, 2.4), (xs_v[0] - 0.5, 2.4)], "Сырьё", (0.85, 2.7), fs=8)
    m._arrow(ax, [(xs_v[2], 3.3), (xs_v[2], 3.8), (13.8, 3.8)], "Газ С3", (12.9, 4.1), fs=8)
    ax.text(0.2, 0.15, "Голубые прямоугольники — Cooler (Heat Transfer); Q — энергетические потоки",
            fontsize=7.5, color="#52514e")
    return m.finish(fig, "hysys_s1_scheme.png")


def plot_study(res):
    """Выход газа С3 и доля отгона С3 в зависимости от P2 = P3: McWilliams и PR."""
    import matplotlib.pyplot as plt
    mcw = m.t3z2_study(P2_grid=np.round(np.arange(4.0, 9.81, 0.1), 2))
    P_m = [r["P2"] for r in mcw["rows"]]
    fig, ax = plt.subplots(1, 2, figsize=(9.6, 3.8))
    ax[0].plot(P_m, [r["V_out"] for r in mcw["rows"]], color=m.COLORS[0], label="McWilliams (отчёт)")
    ax[1].plot(P_m, [r["e"][2] for r in mcw["rows"]], color=m.COLORS[0], label="McWilliams (отчёт)")
    st = [r for r in res["study"]]
    two = [r for r in st if r["states"][2] == "двухфазная"]
    ax[0].plot([r["P2"] for r in two], [r["V3"] for r in two], ls="--", marker="o", ms=4,
               color=m.COLORS[1], label="PR, kij = 0 (ориентир для HYSYS)")
    ax[1].plot([r["P2"] for r in two], [r["e"][2] for r in two], ls="--", marker="o", ms=4,
               color=m.COLORS[1], label="PR, kij = 0 (ориентир для HYSYS)")
    one = [r["P2"] for r in st if r["states"][2] == "одна фаза"]
    if one:
        for a in ax:
            a.axvspan(min(one) - 0.25, max(one) + 0.25, color="#eda100", alpha=0.15)
        ax[1].text(min(one) - 0.2, 0.05, "PR: С3\nоднофазен", fontsize=8, color="#7a5a00")
    ax[0].set_xlabel("Давление P2 = P3, МПа")
    ax[0].set_ylabel("Выход газа С3, моль/моль сырья")
    ax[1].set_xlabel("Давление P2 = P3, МПа")
    ax[1].set_ylabel("Доля отгона в С3, моль/моль")
    ax[1].set_ylim(0, 1)
    ax[0].legend(fontsize=8)
    return m.finish(fig, "hysys_s1_study.png")


if __name__ == "__main__":
    run_all()
