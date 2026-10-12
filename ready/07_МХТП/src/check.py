"""Проверка расчётов МХТП (вариант 8). Запуск: python check.py  (exit 0 — всё сходится).

Проверяется:
  * Т1: R² воспроизводится независимым расчётом; <C> двумя способами отличается < 2 %;
  * Т2: корень кубического уравнения в форме v и в форме Z совпадает; реализация Ли–Кеслера
        воспроизводит табличные Z0 справочника IFP (I4, 3/6) и Zcorr (I6, 4/6);
  * Т3: Σx = Σy = 1 в каждом сепараторе, невязки Рачфорда–Райса и условий кипения < 1e-8,
        покомпонентный МБ блока сепараторов, ручной пересчёт одной K по McWilliams;
  * Т4: невязки уравнений равновесия < 1e-8, единственность физичного решения;
  * Т5: невязки МБ < 1e-6 (компоненты, узлы, атомы C и H, масса), известное решение Т5 З1;
  * reactions.txt — все уравнения уравнены (через _lib.chem);
  * PR-ориентир для HYSYS (pr_flash.py): давление насыщения пропана, однофазность сырья при 40,8 °C,
    равенство фугитивностей и МБ в двухфазных сепараторах;
  * числа для сверки в HYSYS_инструкция.md и PR-сравнение в ЗАЩИТА.md совпадают с расчётом;
  * в report.md (если собран) присутствуют ключевые числа в том же виде, что и в расчёте.
"""
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1]))           # корень репозитория для _lib

import mhtp_v8 as m  # noqa: E402

FAILS = []


def ok(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        FAILS.append(msg)


res = m.run_all(plots=False, verbose=False)

# ---------------------------------------------------------------- Тема 1
r = res["t1z1"]
p = np.polyfit(m.T1_T, m.T1_C, 4)
yf = sum(c * m.T1_T ** k for k, c in enumerate(p[::-1]))
r2 = 1 - np.sum((m.T1_C - yf) ** 2) / np.sum((m.T1_C - m.T1_C.mean()) ** 2)
ok(abs(r2 - r["R2"]) < 1e-12, f"Т1З1 R² полинома 4-й степени воспроизводится: {r2:.6f}")
# интеграл полинома аналитически вручную
I = sum(c / (k + 1) * (1300.0 ** (k + 1) - 50.0 ** (k + 1)) for k, c in enumerate(p[::-1]))
ok(abs(I / 1250 - r["C_poly"]) < 1e-9, f"Т1З1 <C> по полиному = {I/1250:.3f} Дж/(моль·К)")
Itr = sum((m.T1_T[i + 1] - m.T1_T[i]) * (m.T1_C[i + 1] + m.T1_C[i]) / 2 for i in range(len(m.T1_T) - 1))
ok(abs(Itr / 1250 - r["C_trap"]) < 1e-9, f"Т1З1 <C> трапециями (цикл) = {Itr/1250:.3f} Дж/(моль·К)")
ok(r["delta_rel"] < 2.0, f"Т1З1 расхождение двух способов {r['delta_rel']:.3f} % < 2 %")
ok(abs(r["err_trap_rule"] + r["err_model"] - (r["C_trap"] - r["C_poly"])) < 1e-9,
   "Т1З1 разложение расхождения (метод трапеций + остатки модели) замыкается")
# справочная теплоёмкость IFP D1 (кал/(моль·К)) при 300 и 1000 К — проверка единиц Дж/(моль·К)
cp_ifp = lambda T: (-0.966 + 7.279e-2 * T - 3.755e-5 * T ** 2 + 7.58e-9 * T ** 3) * 4.184
ok(abs(cp_ifp(300) - 73.93) / 73.93 < 0.01 and abs(cp_ifp(1000) - 174.6) / 174.6 < 0.01,
   f"Т1З1 единицы: IFP D1 даёт {cp_ifp(300):.2f} и {cp_ifp(1000):.2f} Дж/(моль·К) (табл. 73,93 и 174,6)")

r = res["t1z2"]
for name, f in r["fits"].items():
    func = {"given": m.m_given, "power": m.m_power, "hyper": m.m_hyper, "exp": m.m_exp}[name]
    yv = func(m.X2, *f["p"])
    r2 = 1 - np.sum((m.Y2 - yv) ** 2) / np.sum((m.Y2 - m.Y2.mean()) ** 2)
    ok(abs(r2 - f["R2"]) < 1e-12, f"Т1З2 R² модели {name} = {r2:.4f}")
ok(r["fits"]["given"]["p"][1] < m.X2.min(), "Т1З2 параметр b заданной модели меньше min(x)")
ok(r["b_lin"] > m.X2.min(), "Т1З2 линеаризация действительно даёт недопустимое b > min(x)")
# оптимальность: градиент SSE заданной модели ≈ 0 (численно)
a, b = r["fits"]["given"]["p"]
S = lambda a, b: np.sum((m.Y2 - m.m_given(m.X2, a, b)) ** 2)
g = [(S(a + 1e-7, b) - S(a - 1e-7, b)) / 2e-7, (S(a, b + 1e-7) - S(a, b - 1e-7)) / 2e-7]
ok(max(abs(g[0]) * a, abs(g[1]) * b) / S(a, b) < 1e-4,
   f"Т1З2 минимум SSE заданной модели (градиент {g[0]:.1e}, {g[1]:.1e})")

r = res["t1z3"]
x, y = 1 / (m.T3_t + 273.15), np.log(m.T3_k)
slope = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
ok(abs(-slope * m.R - r["Ea"]) < 1e-6, f"Т1З3 Ea по формулам МНК = {-slope*m.R/1000:.3f} кДж/моль")
ok(abs(r["R2_ln"] - np.corrcoef(x, y)[0, 1] ** 2) < 1e-12, f"Т1З3 R²(ln k) = {r['R2_ln']:.4f}")

r = res["t1z4"]
for deg, d in r["models"].items():
    A = np.vander(m.T4_T, deg + 1)
    coef = np.linalg.lstsq(A, m.T4_mu, rcond=None)[0]
    s = np.sum((m.T4_mu - A @ coef) ** 2)
    ok(abs(s - d["SSE"]) / d["SSE"] < 1e-6, f"Т1З4 SSE степени {deg} = {s:.3e} (lstsq)")
ok(r["models"][3]["R2"] > r["models"][2]["R2"] > r["models"][1]["R2"], "Т1З4 R² растёт со степенью")
ok(r["F"] > r["Fcrit"], f"Т1З4 F = {r['F']:.2f} > Fкрит = {r['Fcrit']:.2f}: кубический член значим")

# ---------------------------------------------------------------- Тема 2
for key in ("t2z1", "t2z2"):
    r = res[key]
    for eos in ("RK", "SRK"):
        d = r["res"][eos]
        A = d["a"] * r["P"] / (m.R * r["T"]) ** 2
        B = d["b"] * r["P"] / (m.R * r["T"])
        zr = np.roots([1, -1, A - B - B * B, -A * B])
        zr = zr[np.abs(zr.imag) < 1e-10].real.max()
        ok(abs(zr - d["Z"]) < 1e-9, f"Т2 {key} {eos}: Z из формы v и формы Z совпадают ({zr:.5f})")
        pv = m.R * r["T"] / (d["v"] - d["b"]) - d["a"] / (d["v"] * (d["v"] + d["b"]))
        ok(abs(pv - r["P"]) / r["P"] < 1e-9, f"Т2 {key} {eos}: подстановка v в уравнение даёт P")
        ok(len(d["real"]) == 1, f"Т2 {key} {eos}: один действительный корень (сверхкритика)")
# Ли–Кеслер против таблиц справочника IFP (I4 3/6 — Z0; I6 4/6 — Zcorr при Tr=4, Pr=10)
for Tr, Pr, z0t in [(1.1, 0.6, 0.8324), (1.1, 0.8, 0.7649), (1.5, 2.0, 0.8328), (2.4, 3.0, 1.0012),
                    (2.0, 5.0, 0.9773), (1.1, 3.0, 0.4771)]:
    z0 = m._lk_z(Tr, Pr, m.LK_SIMPLE)
    ok(abs(z0 - z0t) < 2e-4, f"Т2 Ли–Кеслер Z0(Tr={Tr}, Pr={Pr}) = {z0:.4f} (табл. {z0t})")
_, _, zc = m.lee_kesler_z(4.0, 10.0, 0.0)
ok(abs(zc - 0.2992392) < 5e-4, f"Т2 Ли–Кеслер Zcorr(4; 10) = {zc:.4f} (табл. 0,2992)")
ok(abs(res["t2z2"]["y"].sum() - 1) < 1e-12 and abs(res["t2z2"]["y"][1] / res["t2z2"]["y"][2] - 1 / 3) < 1e-12,
   "Т2З2 состав смеси: Σy = 1, O2 : N2 = 1 : 3")

# ---------------------------------------------------------------- Тема 3
r = res["t3z1"]
ok(abs(r["res_b"]) < 1e-8 and abs(r["res_d"]) < 1e-8, "Т3З1 невязки условий начала и конца кипения < 1e-8")
ok(abs(r["y_bubble"].sum() - 1) < 1e-8 and abs(r["x_dew"].sum() - 1) < 1e-8, "Т3З1 Σy пузырька = Σx капли = 1")
ok(r["tb"] < r["td"], f"Т3З1 t_нк = {r['tb']:.2f} °C < t_кк = {r['td']:.2f} °C")
# ручной пересчёт K метана при 9,8 МПа и 40,8 °C
TR, PP = (40.8 + 273.15) * 1.8, 9.8e6 / 6894.757293168
K_hand = math.exp(-292860 / TR ** 2 + 8.2445 - 0.8951 * math.log(PP) + 59.8465 / PP ** 2)
ok(abs(K_hand - res["t3z2_base"]["train"][0]["K"][0]) < 1e-12, f"Т3З2 K(CH4, С1) вручную = {K_hand:.4f}")
z = m.SEP_Z
ok(abs(z.sum() - 1) < 1e-12, "Т3З2 сумма мольных долей сырья = 1")
for j, s in enumerate(res["t3z2_base"]["train"], 1):
    ok(abs(np.sum(s["x"]) - 1) < 1e-8 and abs(np.sum(s["y"]) - 1) < 1e-8,
       f"Т3З2 С{j}: Σx = {np.sum(s['x']):.10f}, Σy = {np.sum(s['y']):.10f}")
    ok(abs(s["rr"]) < 1e-8 and 0 < s["e"] < 1, f"Т3З2 С{j}: невязка РР {s['rr']:.1e}, 0 < e = {s['e']:.4f} < 1")
    bal = s["F"] * s["z"] - s["V"] * s["y"] - s["L"] * s["x"]
    ok(np.max(np.abs(bal)) < 1e-12, f"Т3З2 С{j}: покомпонентный МБ сепаратора")
ok(res["t3z2_base"]["summary"]["closure"] < 1e-12, "Т3З2 МБ блока: жидкости + газ С3 = сырьё")
for s in res["t3z2_study"]["rows"]:
    if s["closure"] > 1e-10:
        ok(False, f"Т3З2 МБ блока при P2 = {s['P2']}")
        break
else:
    ok(True, f"Т3З2 МБ блока сходится во всех {len(res['t3z2_study']['rows'])} точках исследования P2")
rows = {round(s["P2"], 1): s for s in res["t3z2_study"]["rows"]}
ok(rows[4.0]["states"][1] == "газ" and rows[6.0]["states"][1] == "двухфазная",
   "Т3З2 при P2 = 4 МПа С2 однофазен (газ), при 6 МПа — двухфазен")
ok(abs(np.sum(m.separator_train(m.SEP_BASE[:1])[0]["y"] / m.k_mcw(m.SEP_NAMES, m.SEP_BASE[1][1],
       res["t3z2_study"]["P2_dew"] * m.MPA)) - 1) < 1e-8, "Т3З2 давление начала конденсации газа С1 при 12,8 °C")

# ---------------------------------------------------------------- Тема 4
r = res["t4z1"]
y = r["y"]
ok(abs(y[2] / (y[0] ** 0.5 * y[1] ** 1.5) / 220 - 0.05) < 1e-8, "Т4З1 невязка уравнения равновесия < 1e-8")
ok(np.allclose(r["n0"] @ [2, 0, 1], r["n"] @ [2, 0, 1]) and np.allclose(r["n0"] @ [0, 2, 3], r["n"] @ [0, 2, 3]),
   "Т4З1 баланс атомов N и H")
ok(r["n_roots"] == 1 and np.all(r["n"] > 0), "Т4З1 единственный физичный корень, все n > 0")
r = res["t4z2a"]
ok(abs(r["residual"]) < 1e-8, f"Т4З2а невязка равновесия {r['residual']:.1e}")
ok(abs(r["ke"]["dG_lin"] - (-1106.5)) < 1e-6, "Т4З2а ΔG°r(1100) = 2119 + (2119 − 8570)/2 = −1106,5 кал/моль")
ok(abs(r["K2_1367"][1] - 0.769) / 0.769 < 0.02 and abs(r["K1_1367"][1] - 37.6) / 37.6 < 0.05,
   "Т4З2 заданные Kp при 1367 К согласуются со справочником (±5 %)")
r = res["t4z2b"]
ok(np.max(np.abs(r["residual"])) < 1e-8, "Т4З2б невязки системы < 1e-8")
ok(len(r["unique"]) == 1 and np.all(r["n"] > 0), "Т4З2б физичное решение единственно, все n > 0")
ok(abs((r["n"] @ [2, 2, 0, 2]) - 2) < 1e-12 and abs((r["n"] @ [6, 4, 2, 2]) - 6) < 1e-12,
   "Т4З2б баланс атомов C и H")

# ---------------------------------------------------------------- Тема 5
r = res["t5z1"]
ok(np.allclose([r["flows"][k] for k in ("D1", "B1", "D2", "B2")], [375, 250, 125, 250], atol=1e-9),
   "Т5З1 D1 = 375, B1 = 250, D2 = 125, B2 = 250 моль/ч")
ok(np.max(np.abs(r["residual"])) < 1e-6, f"Т5З1 невязка балансов колонн {np.max(np.abs(r['residual'])):.1e}")
ok(all(v > 0 for v in r["flows"].values()), "Т5З1 все расходы положительны")
ok(all(abs(c.sum() - 1) < 1e-12 for c in r["comp"].values()), "Т5З1 сумма долей в каждом потоке = 1")
r = res["t5z2"]
a = 0.995 * 0.999 * 0.42
ok(abs(r["streams"]["7"][0] - 100 * a / (1 - a)) < 1e-9, f"Т5З2 толуол рецикла аналитически = {100*a/(1-a):.4f}")
for name in ("bal", "nodes"):
    ok(np.max(np.abs(r[name])) < 1e-6, f"Т5З2 МБ ({name}) |Δ| = {np.max(np.abs(r[name])):.1e} < 1e-6")
ok(abs(r["dC"]) < 1e-6 and abs(r["dH"]) < 1e-6 and abs(r["dm"]) < 1e-6, "Т5З2 баланс атомов C, H и массы")
ok(r["n7_diff"] < 1e-8, "Т5З2 простая итерация сходится к прямому решению")
ok(abs(r["conv_to_xylene"] + r["conv_to_benzene"] + (1 - r["conv_total"]) - 1) < 1e-9,
   "Т5З2 распределение свежего толуола: в ксилол + в бензол + потери = 100 %")
try:
    from _lib.chem import molar_mass
    ok(abs(molar_mass("C7H8") - m.MW["C7H8"]) < 1e-9, "Т5З2 молярные массы совпадают с _lib.chem")
except ImportError:
    print("SKIP _lib.chem недоступна")

# ---------------------------------------------------------------- реакции
try:
    from _lib.chem import check_file
    bad = [str(x) for x in check_file(HERE / "reactions.txt") if not x.ok]
    ok(not bad, "reactions.txt: все уравнения уравнены" + ("" if not bad else ": " + "; ".join(bad)))
except ImportError:
    print("SKIP _lib.chem недоступна")

# ---------------------------------------------------------------- PR-ориентир для HYSYS (pr_flash.py)
import pr_flash as pr  # noqa: E402

prr = pr.run_all(verbose=False, plots=False)
ok(abs(prr["psat_c3_tb"] / 101325.0 - 1) < 0.02,
   f"PR: давление насыщения пропана при t_кип (−42,1 °C, IFP A2) = {prr['psat_c3_tb']/1000:.1f} кПа ≈ 101,3")
T1 = m.SEP_BASE[0][1]
stable_all = all(pr.stability(m.SEP_Z, T1, P * m.MPA) is None for P in (0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9.8, 12))
ok(stable_all, "PR: сырьё при 40,8 °C однофазно во всём интервале 0,5–12 МПа")
(Pcdt, tcdt), _ = prr["cdt"]
ok(tcdt < 40.8 and prr["mcw_dew98"] > 40.8,
   f"PR: крикондентерма {tcdt:.1f} °C < 40,8 °C; McWilliams: точка росы при 9,8 МПа {prr['mcw_dew98']:.1f} °C")
for key, states in (("base", ["одна фаза", "двухфазная", "одна фаза"]),
                    ("choice", ["одна фаза", "двухфазная", "двухфазная"])):
    tr = prr[key]
    ok([s["state"] for s in tr] == states, f"PR {key}: состояния сепараторов {states}")
    for j, s in enumerate(tr, 1):
        if s["state"] != "двухфазная":
            continue
        ok(s["res"] < 1e-8 and abs(s["x"].sum() - 1) < 1e-12 and abs(s["y"].sum() - 1) < 1e-12,
           f"PR {key} С{j}: равенство фугитивностей (невязка {s['res']:.1e}), Σx = Σy = 1")
        bal = s["F"] * s["z"] - s["V"] * s["y"] - s["L"] * s["x"]
        ok(np.max(np.abs(bal)) < 1e-10, f"PR {key} С{j}: покомпонентный МБ сепаратора")
    ok(pr.train_closure(tr) < 1e-10, f"PR {key}: МБ блока (жидкости + газ = сырьё)")
st = {r["P2"]: r for r in prr["study"]}
ok(st[7.5]["states"][2] == "двухфазная" and all(st[P]["states"][2] == "одна фаза" for P in (8.0, 8.5, 9.0, 9.5)),
   "PR: С3 двухфазен при P2 ≤ 7,5 МПа и однофазен при 8,0–9,5 МПа")

# ---------------------------------------------------------------- числа инструкции HYSYS и ЗАЩИТЫ
fc = lambda v, nd: f"{v:.{nd}f}".replace(".", ",").replace("-", "−")
ins = (HERE / "HYSYS_инструкция.md").read_text(encoding="utf-8").replace("{,}", ",")
tb, rows3 = res["t3z2_base"]["train"], {round(s["P2"], 1): s for s in res["t3z2_study"]["rows"]}
ch = rows3[m.P2_CHOICE]
need = [fc(s["e"], 4) for s in tb] + [fc(100 * tb[0]["L"], 2), fc(100 * tb[1]["L"], 2), fc(100 * tb[2]["V"], 2),
        fc(tb[2]["y"][0], 5), fc(ch["e"][1], 4), fc(ch["e"][2], 4), fc(100 * ch["V_out"], 2),
        fc(ch["y_out"][0], 5), fc(ch["y_out"][2], 5), fc(res["t3z2_study"]["P2_dew"], 2)]
b2, c2, c3 = prr["base"][1], prr["choice"][1], prr["choice"][2]
need += [fc(b2["e"], 4), fc(100 * b2["L"], 2), fc(100 * b2["V"], 2), fc(prr["base"][2]["Z"], 3),
         fc(c2["e"], 4), fc(c3["e"], 4), fc(100 * c3["V"], 2), fc(c3["y"][0], 5), fc(c3["y"][2], 5),
         fc(tcdt, 1), fc(Pcdt, 1), fc(prr["mcw_dew98"], 1), fc(100 * st[4.0]["V3"], 1), fc(100 * st[7.5]["V3"], 1)]
r41, r42 = res["t4z1"], res["t4z2a"]
need += [fc(v, 4) for v in r41["n"]] + [fc(r41["n"].sum(), 4), fc(r41["y"][2], 4), fc(r41["xi"], 4),
                                        fc(100 * r41["conv_N2"], 2)]
need += [fc(r42["x"], 4), fc(r42["y"][0], 4), fc(r42["y"][1], 4), fc(r42["n"].sum(), 4), fc(r42["K"], 3)]
miss = [k for k in need if k not in ins]
ok(not miss, "HYSYS_инструкция.md: все числа для сверки совпадают с расчётом" + (f" (нет: {miss})" if miss else ""))
zas = (HERE.parent / "ЗАЩИТА.md").read_text(encoding="utf-8").replace("{,}", ",")
need_z = [fc(100 * c3["V"] / 100, 3), fc(ch["V_out"], 3), fc(prr["mcw_dew98"], 1)]
miss = [k for k in need_z if k not in zas]
ok(not miss, "ЗАЩИТА.md: числа PR-сравнения совпадают с расчётом" + (f" (нет: {miss})" if miss else ""))

# ---------------------------------------------------------------- согласование с отчётом
rep = HERE / "report.md"
if rep.exists():
    text = rep.read_text(encoding="utf-8")
    f = lambda v, nd: f"{v:.{nd}f}".replace(".", ",").replace("-", "−")
    keys = [f(res["t1z1"]["C_poly"], 2), f(res["t1z1"]["C_trap"], 2), f(res["t1z3"]["Ea"] / 1000, 1),
            f(res["t2z1"]["res"]["SRK"]["v_L"], 4), f(res["t2z2"]["res"]["SRK"]["Z"], 4),
            f(res["t3z1"]["tb"], 1), f(res["t3z1"]["td"], 1), f(res["t3z2_base"]["train"][2]["e"], 4),
            f(res["t4z1"]["xi"], 4), f(res["t4z2a"]["x"], 4), f(res["t4z2b"]["x1"], 4),
            f(res["t5z2"]["streams"]["7"][0], 4), f(res["t5z2"]["conv_to_xylene"] * 100, 2)]
    missing = [k for k in keys if k not in text]
    ok(not missing, "report.md содержит ключевые числа расчёта" + (f" (нет: {missing})" if missing else ""))

print("\nИТОГ:", "ВСЁ СХОДИТСЯ" if not FAILS else f"ОШИБОК {len(FAILS)}")
sys.exit(1 if FAILS else 0)
