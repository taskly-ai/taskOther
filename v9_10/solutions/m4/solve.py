# Модуль 4. САПР (Aspen HYSYS): сепарационный блок задачи 3.2 (варианты 9, 10) — эталон на Python.
# Термодинамическая модель: уравнение Пенга–Робинсона (1976), классические правила смешения,
# k_ij = 0 (в HYSYS пакет Peng-Robinson имеет собственные k_ij ≈ 0–0.03 — отсюда малые расхождения).
# Запуск: python solutions/m4/solve.py   (печатает числа для сверки с HYSYS)
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))  # noqa
from _common import *  # noqa

NAMES = ["CH4", "C2H6", "C3H8", "i-C4H10", "n-C4H10", "n-C5H12"]
# Tc, К; Pc, атм; ω — справочник IFP, раздел A2 (PDF с. 31–33)
CR = np.array([[190.6, 45.4, 0.008], [305.4, 48.2, 0.098], [369.8, 41.9, 0.152],
               [408.1, 36.0, 0.176], [425.2, 37.5, 0.193], [469.6, 33.3, 0.251]])
Tc, Pc, W = CR[:, 0], CR[:, 1] * ATM, CR[:, 2]
Z_FEED = np.array([0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706])


def pr_params(T):
    kap = 0.37464 + 1.54226 * W - 0.26992 * W ** 2
    a = 0.45724 * R ** 2 * Tc ** 2 / Pc * (1 + kap * (1 - np.sqrt(T / Tc))) ** 2
    b = 0.07780 * R * Tc / Pc
    return a, b


def ln_phi(x, T, P, phase):
    a, b = pr_params(T)
    aij = np.sqrt(np.outer(a, a))
    am, bm = x @ aij @ x, x @ b
    A, B = am * P / (R * T) ** 2, bm * P / (R * T)
    r = np.roots([1, -(1 - B), A - 3 * B ** 2 - 2 * B, -(A * B - B ** 2 - B ** 3)])
    r = np.sort(r[np.abs(r.imag) < 1e-10].real)
    r = r[r > B]
    s2 = np.sqrt(2)

    def lnphi_z(Z):
        return (b / bm * (Z - 1) - np.log(Z - B)
                - A / (2 * s2 * B) * (2 * (aij @ x) / am - b / bm)
                * np.log((Z + (1 + s2) * B) / (Z + (1 - s2) * B)))
    if phase == "min":             # корень с минимальной энергией Гиббса смеси
        Z = min(r, key=lambda zz: float(x @ lnphi_z(zz)))
    else:
        Z = r.max() if phase == "V" else r.min()
    return lnphi_z(Z), Z


def stable(z, T, P):
    """Тест стабильности Михельсена (касательная плоскость): True — фаза стабильна."""
    d = np.log(z) + ln_phi(z, T, P, "min")[0]
    Kw = Pc / P * np.exp(5.373 * (1 + W) * (1 - Tc / T))
    for Wt in (z * Kw, z / Kw):
        for _ in range(1000):
            lnW = d - ln_phi(Wt / Wt.sum(), T, P, "min")[0]
            Wn = np.exp(lnW)
            if np.max(np.abs(Wn - Wt)) < 1e-12:
                break
            Wt = Wn
        if Wt.sum() > 1 + 1e-8:
            return False
    return True


def rr(z, K):
    f = lambda e: np.sum(z * (K - 1) / (1 + e * (K - 1)))
    if K.max() <= 1 or K.min() >= 1:
        return 0.0 if K.max() <= 1 else 1.0
    lo, hi = 1 / (1 - K.max()) + 1e-10, 1 / (1 - K.min()) - 1e-10   # отрицательный флеш
    return brentq(f, lo, hi, xtol=1e-14)


def pr_flash(z, T, P):
    K = Pc / P * np.exp(5.373 * (1 + W) * (1 - Tc / T))      # приближение Вильсона
    for it in range(500):
        e = rr(z, K)
        ec = min(max(e, 0.0), 1.0)
        x = z / (1 + ec * (K - 1)); x /= x.sum()
        y = K * x; y /= y.sum()
        lpl, _ = ln_phi(x, T, P, "L")
        lpv, _ = ln_phi(y, T, P, "V")
        Kn = np.exp(lpl - lpv)
        if np.max(np.abs(Kn - K)) < 1e-11:
            break
        K = Kn
    trivial = np.max(np.abs(np.log(K))) < 1e-4
    if trivial and not stable(z, T, P):
        raise RuntimeError("тривиальное решение при нестабильной фазе — нужен другой старт")
    if trivial or e >= 1:
        return dict(e=1.0 if not trivial else np.nan, x=x, y=z.copy(), K=K, phase="однофазно (газ/флюид)")
    if e <= 0:
        return dict(e=0.0, x=z.copy(), y=y, K=K, phase="однофазно (жидкость)")
    return dict(e=e, x=x, y=y, K=K, phase="две фазы")


def train(conds, z=Z_FEED):
    out, feed, F = [], z, 1.0
    for P, t in conds:
        if F == 0:
            out.append(dict(e=np.nan, phase="нет питания", F=0, V=0, L=0, x=z * np.nan, y=z * np.nan)); continue
        s = pr_flash(feed, t + 273.15, P)
        e = 1.0 if np.isnan(s["e"]) else s["e"]
        s.update(P=P, t=t, F=F, V=F * e, L=F * (1 - e))
        out.append(s)
        feed, F = s["y"], s["V"]
    return out


BASE = [(9.8e6, 40.8), (8.7e6, 12.8), (8.7e6, -40.8)]

if __name__ == "__main__":
    # контроль реализации: давление насыщения пропана при нормальной Tкип −42.1 °C (≈ 1 атм)
    def psat(T):
        z1 = np.array([0, 0, 1.0, 0, 0, 0])
        f = lambda P: (ln_phi(z1, T, P, "L")[0] - ln_phi(z1, T, P, "V")[0])[2]
        return brentq(f, 2e4, 3e5)
    print(f"Контроль PR: Pнас(C3H8, −42.1 °C) = {psat(231.05)/1000:.1f} кПа (опыт 101.3 кПа)")
    C1, C2, C3 = BASE
    for title, conds in (("3 сепаратора: С1 + С2 + С3 (база)", BASE),
                         ("2 сепаратора: С1 + С2", [C1, C2]),
                         ("2 сепаратора: С2 + С3", [C2, C3]),
                         ("2 сепаратора: С1 + С3", [C1, C3]),
                         ("1 сепаратор: С1", [C1]),
                         ("1 сепаратор: С3", [C3])):
        print(f"\n== {title}")
        tr = train(conds)
        for i, s in enumerate(tr, 1):
            if s["phase"].startswith("одно"):
                s["phase"] += ", стабильна" if stable(s["y"] if s["e"] != 0 else s["x"], s["t"] + 273.15, s["P"]) else ", НЕСТАБИЛЬНА"
            print(f"С{i}: {s['phase']:24s} e = {s['e']:.4f}  V = {s['V']:.4f}  L = {s['L']:.4f} моль/моль сырья")
            if s["phase"] == "две фазы":
                print("    x:", np.round(s["x"], 4), "\n    y:", np.round(s["y"], 4))
        print(f"Газ последнего сепаратора: {tr[-1]['V']:.4f} моль/моль сырья, CH4 в газе {tr[-1]['y'][0]:.4f}, "
              f"C3+ {np.sum(tr[-1]['y'][2:])*100:.3f} %")
