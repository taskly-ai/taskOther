"""Independent verification, Topic 3 (phase equilibria with K-correlation), variants 9 & 10.

K-correlation: ln K = -A/T^2 + B - C ln P + D/P^2 (form 1) or + D/P (form 2), T in degR, P in psia.
3.1: bubble point sum(z K) = 1 and dew point sum(z/K) = 1 solved by bisection on T
     (ln of the sums is monotone in T), cross-checked by Newton on ln sum.
3.2: Rachford-Rice solved by bisection (no library), single-phase checks first,
     separators in series (vapor of one stage is the feed of the next).
"""
import math

ATM = 101325.0
PSI = 6894.757


def lnK(c, T_K, P_Pa):
    A, B, C, D, form = c
    TR = 1.8 * T_K
    P = P_Pa / PSI
    return -A / TR ** 2 + B - C * math.log(P) + (D / P ** 2 if form == 1 else D / P)


def bisect(f, a, b, tol=1e-13, it=300):
    fa = f(a)
    for _ in range(it):
        m = 0.5 * (a + b)
        fm = f(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
        if b - a < tol:
            break
    return 0.5 * (a + b)


# ---------------------------------------------------------------- 3.1
print("=== 3.1 bubble/dew T, 14 atm ===")
comp31 = {
    "ethylene": ((600076.9, 7.90595, 0.84677, 42.94594, 1), 0.20),
    "propane": ((970688.6, 7.15059, 0.76984, 6.90224, 2), 0.30),
    "isobutane": ((1166846, 7.72668, 0.92213, 0, 1), 0.30),
    "n-butane": ((1280557, 7.94986, 0.96455, 0, 1), 0.20),
}
P = 14 * ATM
print(f"  P = {P / PSI:.6f} psia")
bub = lambda T: math.log(sum(z * math.exp(lnK(c, T, P)) for c, z in comp31.values()))
dew = lambda T: math.log(sum(z / math.exp(lnK(c, T, P)) for c, z in comp31.values()))
Tb = bisect(bub, 150, 600)
Td = bisect(lambda T: -dew(T), 150, 600)


def newton(f, x):
    for _ in range(100):
        h = 1e-6
        d = (f(x + h) - f(x - h)) / (2 * h)
        dx = -f(x) / d
        x += dx
        if abs(dx) < 1e-12:
            break
    return x


print(f"  bubble: T = {Tb:.6f} K = {Tb - 273.15:.6f} C  (Newton: {newton(bub, 300) - 273.15:.6f} C)")
print(f"  dew   : T = {Td:.6f} K = {Td - 273.15:.6f} C  (Newton: {newton(dew, 300) - 273.15:.6f} C)")
for nm, (c, z) in comp31.items():
    print(f"     K_{nm} at bubble = {math.exp(lnK(c, Tb, P)):.6f}, at dew = {math.exp(lnK(c, Td, P)):.6f}")

# ---------------------------------------------------------------- 3.2
print("\n=== 3.2 separator train ===")
names = ["CH4", "C2H6", "C3H8", "i-C4", "n-C4", "n-C5"]
z0 = [0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706]
cc = [(292860, 8.2445, 0.8951, 59.8465, 1), (687248.2, 7.90694, 0.866, 49.02654, 1),
      (970688.6, 7.15059, 0.76984, 6.90224, 2), (1166846, 7.72668, 0.92213, 0, 1),
      (1280557, 7.94986, 0.96455, 0, 1), (1524891, 7.33129, 0.89143, 0, 1)]
print(f"  sum feed = {sum(z0):.5f} (normalised below)")
stages = {"C1": (9.8e6, 40.8 + 273.15), "C2": (8.7e6, 12.8 + 273.15), "C3": (8.7e6, -40.8 + 273.15)}


def flash(n, P, T):
    """n: component mol amounts. Returns V (fraction), vapor moles, liquid moles, K."""
    F = sum(n)
    z = [v / F for v in n]
    K = [math.exp(lnK(c, T, P)) for c in cc]
    if sum(zi * Ki for zi, Ki in zip(z, K)) <= 1:
        return 0.0, [0.0] * len(n), list(n), K
    if sum(zi / Ki for zi, Ki in zip(z, K)) <= 1:
        return 1.0, list(n), [0.0] * len(n), K
    rr = lambda V: sum(zi * (Ki - 1) / (1 + V * (Ki - 1)) for zi, Ki in zip(z, K))
    # rr is decreasing in V
    a, b = 0.0, 1.0
    for _ in range(300):
        m = 0.5 * (a + b)
        if rr(m) > 0:
            a = m
        else:
            b = m
    V = 0.5 * (a + b)
    y = [zi * Ki / (1 + V * (Ki - 1)) for zi, Ki in zip(z, K)]
    x = [zi / (1 + V * (Ki - 1)) for zi, Ki in zip(z, K)]
    vap = [V * F * yi for yi in y]
    liq = [(1 - V) * F * xi for xi in x]
    return V, vap, liq, K


s0 = sum(z0)
feed = [v / s0 for v in z0]
# base case details
print("  Base case (C1->C2->C3) stage compositions:")
gas = list(feed)
for st in ["C1", "C2", "C3"]:
    P, T = stages[st]
    V, vap, liq, K = flash(gas, P, T)
    sv, sl = sum(vap), sum(liq)
    print(f"   {st}: V/F = {V:.8f}  feed = {sum(gas):.8f}  gas = {sv:.8f}  liq = {sl:.8f}")
    print("       K  = " + " ".join(f"{k:.6g}" for k in K))
    print("       x  = " + " ".join(f"{(l / sl if sl else 0):.6f}" for l in liq))
    print("       y  = " + " ".join(f"{(v / sv if sv else 0):.6f}" for v in vap))
    gas = vap

schemes = [["C1"], ["C3"], ["C1", "C2"], ["C1", "C3"], ["C2", "C3"], ["C1", "C2", "C3"]]
print("\n  scheme      | stage V/F                         | gas mol   | CH4 %    | C3+ %   | C3 rec % | CH4 lost %")
for sch in schemes:
    gas = list(feed)
    liqtot = [0.0] * 6
    Vs = []
    for st in sch:
        P, T = stages[st]
        V, vap, liq, K = flash(gas, P, T)
        if st == sch[0]:
            Sk = sum(n * k for n, k in zip(gas, K)) / sum(gas)
            Sd = sum(n / k for n, k in zip(gas, K)) / sum(gas)
        Vs.append(V)
        liqtot = [a + b for a, b in zip(liqtot, liq)]
        gas = vap
    G = sum(gas)
    ch4 = gas[0] / G * 100 if G > 0 else float('nan')
    c3p = sum(gas[2:]) / G * 100 if G > 0 else float('nan')
    c3rec = liqtot[2] / feed[2] * 100
    ch4lost = liqtot[0] / feed[0] * 100
    print(f"  {'+'.join(sch):11s} | " + ", ".join(f"{v:.7f}" for v in Vs).ljust(33) +
          f" | {G:.7f} | {ch4:.5f} | {c3p:.5f} | {c3rec:.5f} | {ch4lost:.6f}"
          f"   (1st stage sum zK = {Sk:.5f}, sum z/K = {Sd:.5f})")
