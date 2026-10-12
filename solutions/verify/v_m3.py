"""Independent verification, Topic 3 (phase equilibria), variant 1.
Bubble/dew T by bisection-type root finding (brentq) on ln(sum zK) and ln(sum z/K).
Flash: Rachford-Rice solved by plain bisection (not Newton), with explicit single-phase checks."""
import numpy as np
from scipy.optimize import brentq

PSI = 6894.757; ATM = 101325.0
DATA = {  # A, B, C, D, form
    'CH4':  (292860, 8.2445, 0.8951, 59.8465, 1),
    'C2H4': (600076.9, 7.90595, 0.84677, 42.94594, 1),
    'C2H6': (687248.2, 7.90694, 0.866, 49.02654, 1),
    'C3H8': (970688.6, 7.15059, 0.76984, 6.90224, 2),
    'nC4':  (1280557, 7.94986, 0.96455, 0, 1),
    'iC4':  (1166846, 7.72668, 0.92213, 0, 1),
    'nC5':  (1524891, 7.33129, 0.89143, 0, 1),
}
def K(name, T_K, P_Pa):
    A, B, C, D, form = DATA[name]
    TR = 1.8 * T_K; Pp = P_Pa / PSI
    return np.exp(-A / TR**2 + B - C * np.log(Pp) + (D / Pp**2 if form == 1 else D / Pp))
def Kvec(names, T_K, P): return np.array([K(n, T_K, P) for n in names])

print("=== 3.1 bubble/dew T, 14 atm ===")
names = ['CH4', 'C2H6', 'C3H8', 'nC4']; z = np.array([0.20, 0.25, 0.35, 0.20]); P = 14 * ATM
Tb = brentq(lambda T: np.log(z @ Kvec(names, T, P)), 100, 600, xtol=1e-12)
Td = brentq(lambda T: np.log(np.sum(z / Kvec(names, T, P))), 100, 600, xtol=1e-12)
print(f"  T_bubble = {Tb-273.15:.4f} C ({Tb:.4f} K)   K at Tb: {np.round(Kvec(names,Tb,P),5)}")
print(f"  T_dew    = {Td-273.15:.4f} C ({Td:.4f} K)   K at Td: {np.round(Kvec(names,Td,P),5)}")
# check: incipient phase composition sums
print(f"  check sum zK(Tb)={z@Kvec(names,Tb,P):.10f}  sum z/K(Td)={np.sum(z/Kvec(names,Td,P)):.10f}")

print("\n=== 3.2 three separators in series ===")
names = ['CH4', 'C2H6', 'C3H8', 'iC4', 'nC4', 'nC5']
z0 = np.array([0.72211, 0.03608, 0.22363, 0.00646, 0.00466, 0.00706])
print(f"  sum z0 = {z0.sum():.5f}")

def flash(z, T_K, P):
    k = Kvec(names, T_K, P)
    if z @ k <= 1:   # subcooled / at bubble point -> all liquid
        return 0.0, z.copy(), z * k / (z @ k), k
    if np.sum(z / k) <= 1:  # superheated -> all vapour
        return 1.0, (z / k) / np.sum(z / k), z.copy(), k
    g = lambda e: np.sum(z * (k - 1) / (1 + e * (k - 1)))
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if g(mid) > 0: lo = mid
        else: hi = mid
    e = 0.5 * (lo + hi)
    x = z / (1 + e * (k - 1)); y = k * x
    return e, x, y, k

def train(T1, P1=9.8e6, T2=12.8, P2=8.7e6, T3=-40.8, P3=8.7e6, verbose=False):
    F = 1.0; z = z0.copy(); out = []
    for i, (Tc, Pp) in enumerate([(T1, P1), (T2, P2), (T3, P3)]):
        e, x, y, k = flash(z, Tc + 273.15, Pp)
        V = F * e; L = F - V
        out.append((e, x, y, k, F, V, L))
        if verbose:
            print(f"  Separator C{i+1}: T={Tc} C P={Pp/1e6} MPa  feed={F:.6f}  e={e:.6f}  V={V:.6f}  L={L:.6f}")
            for n, xi, yi, ki in zip(names, x, y, k):
                print(f"     {n:5s} K={ki:10.5f}  x={xi:.6f}  y={yi:.6f}")
            print(f"     sums x={x.sum():.6f} y={y.sum():.6f}")
        F = V; z = y
        if F <= 0:
            while len(out) < 3:
                out.append((0.0, np.zeros(6), np.zeros(6), None, 0.0, 0.0, 0.0))
            break
    return out

out = train(40.8, verbose=True)
gas = out[-1][5]; ygas = out[-1][2]
print(f"  Final gas from C3 = {gas:.6f} mol per mol feed;  C3+ in final gas = {100*ygas[2:].sum():.4f} mol%")
print(f"  Overall liquid = {1-gas:.6f}; methane recovery to gas = {gas*ygas[0]/z0[0]*100:.4f} %")

print("\n  Sweep of T1 (C2, C3 at base):")
def final_gas(T1):
    o = train(T1); return o[-1][5], o[-1][2], [r[0] for r in o]
for T1 in [-30, -20, -10, 0, 5, 7, 10, 15, 20, 30, 40.8, 50, 55, 60, 70, 80, 90]:
    g, yy, es = final_gas(T1)
    print(f"   T1={T1:6.1f}  e1={es[0]:.6f} e2={es[1]:.6f} e3={es[2]:.6f}  gas={g:.6f}  C3+={100*yy[2:].sum():.4f}%  CH4={100*yy[0]:.4f}%")
grid = np.arange(-30, 91, 1.0)
gv = np.array([final_gas(t)[0] for t in grid])
i = int(np.argmax(gv)); print(f"  global max on 1C grid: T1={grid[i]} C gas={gv[i]:.6f}")
m = grid >= 30; j = int(np.argmax(gv[m])); print(f"  max for T1>=30 on 1C grid: T1={grid[m][j]} C gas={gv[m][j]:.6f}")
fine = np.arange(-30, 90.001, 0.01); FG = [final_gas(t) for t in fine]; gf = np.array([r[0] for r in FG])
i = int(np.argmax(gf)); print(f"  global max on 0.01C grid: T1={fine[i]:.2f} C gas={gf[i]:.6f}")
# where does C1 become single-phase?
e1 = np.array([r[2][0] for r in FG])
print(f"  C1 all-vapour for T1 >= {fine[np.argmax(e1>=1)]:.2f} C (first grid point with e1=1)")
print(f"  gas at T1=90 C: {final_gas(90)[0]:.6f}")
mf = fine >= 30; j = int(np.argmax(gf[mf])); print(f"  max for T1>=30 on 0.01C grid: T1={fine[mf][j]:.2f} C gas={gf[mf][j]:.6f}")
Tbub1 = brentq(lambda T: np.log(z0 @ Kvec(names, T, 9.8e6)), 150, 400, xtol=1e-12)
Tdew1 = brentq(lambda T: np.log(np.sum(z0 / Kvec(names, T, 9.8e6))), 150, 400, xtol=1e-12)
print(f"  Feed at 9.8 MPa: bubble T = {Tbub1-273.15:.3f} C, dew T = {Tdew1-273.15:.3f} C")
e2 = np.array([r[2][1] for r in FG]); v2 = fine[(e2 >= 1) & (gf > 0)]
print(f"  C2 is single-phase vapour for T1 in [{v2.min():.2f}, {v2.max():.2f}] C (0.01 C grid)")
