"""Independent verification, Topic 4 (chemical equilibrium), variant 1.
(Module numbering: v_m5 = topic 4 of the task sheet.)
Equilibria solved by bracketing (brentq) on reaction extents; 2-reaction case by a nested 1-D solve."""
import numpy as np
from scipy.optimize import brentq
R = 8.314462618; CAL = 4.184

print("=== 4.1 NH3 synthesis, Kp=0.05 atm^-1, P=220 atm ===")
n0 = np.array([1.1, 3.0, 0.2]); nu = np.array([-0.5, -1.5, 1.0]); KP = 0.05 * 220
def comp(xi): n = n0 + nu * xi; return n, n / n.sum()
def f41(xi):
    n, y = comp(xi); return np.log(y[2]) - 0.5 * np.log(y[0]) - 1.5 * np.log(y[1]) - np.log(KP)
xi = brentq(f41, -0.2 + 1e-12, 2.0 - 1e-12, xtol=1e-15)
n, y = comp(xi)
print(f"  extent = {xi:.6f} mol/h")
for s, a, b, c in zip(['N2', 'H2', 'NH3'], n0, n, y): print(f"  {s:4s} in={a:.4f} out={b:.6f} y={c:.6f}")
print(f"  total out = {n.sum():.6f};  check KpP = {y[2]/(y[0]**.5*y[1]**1.5):.6f};  H2 conversion = {(3-n[1])/3*100:.4f} %, N2 conv = {(1.1-n[0])/1.1*100:.4f} %")

print("\n=== 4.2a C2H6 = C2H4 + H2 at 1100 K, 1 atm ===")
Tt = np.array([298., 400, 600, 800, 1000])
dHf6 = np.array([-20236, -21419, -23280, -24530, -25280.]); dHf4 = np.array([12496, 11766, 10600, 9760, 9205.])
dGf6 = np.array([-7860, -3447, 5970, 15920, 26130.]); dGf4 = np.array([16282, 17675, 20918, 24490, 28249.])
dH = (dHf4 - dHf6) * CAL; dG = (dGf4 - dGf6) * CAL
lnK = -dG / (R * Tt)
for T_, h, g, l in zip(Tt, dH, dG, lnK): print(f"   T={T_:6.0f}  dH={h/1000:9.4f} kJ  dG={g/1000:9.4f} kJ  K={np.exp(l):.6e}")
T = 1100.0
est = {}
# M1: van 't Hoff, dH constant = dH(1000)
est['M1 vant Hoff, dH(1000) const'] = lnK[-1] - dH[-1] / R * (1 / T - 1 / 1000)
# M2: linear extrapolation of dG from 800,1000
g1100 = dG[-1] + (dG[-1] - dG[-2]) / 200 * 100
est['M2 linear extrap dG (800-1000)'] = -g1100 / (R * T)
# M3: dH linear in T (const dCp) from 800/1000 points, integrated Gibbs-Helmholtz from 1000 K
dCp = (dH[-1] - dH[-2]) / 200; H0 = dH[-1] - dCp * 1000   # dH(T) = H0 + dCp*T
est['M3 vant Hoff, const dCp (800-1000)'] = lnK[-1] + (-H0 / R * (1 / T - 1 / 1000) + dCp / R * np.log(T / 1000))
# M4: LSQ fit dG = a + b T + c T lnT to all 5 points, extrapolate
X = np.column_stack([np.ones(5), Tt, Tt * np.log(Tt)]); c, *_ = np.linalg.lstsq(X, dG, rcond=None)
est['M4 LSQ dG=a+bT+cTlnT (5 pts)'] = -(c[0] + c[1] * T + c[2] * T * np.log(T)) / (R * T)
# M5: Gibbs-Helmholtz with dH(T) from quadratic fit over 600..1000
pq = np.polyfit(Tt[2:], dH[2:], 2)
from scipy.integrate import quad
est['M5 vant Hoff, dH quad fit (600-1000)'] = lnK[-1] + quad(lambda t: np.polyval(pq, t) / (R * t**2), 1000, T)[0]
def conv(K, P=1.0): return np.sqrt(K / (K + P))
for k_, l in est.items():
    K = np.exp(l); x = conv(K)
    print(f"  {k_:38s} K(1100)={K:.6f} dG={-l*R*T/1000:8.4f} kJ  X={x:.6f}  y: C2H6={(1-x)/(1+x):.6f} C2H4=H2={x/(1+x):.6f}")

print("\n=== 4.2b two reactions at 1367 K, 1 atm, K1=37.6, K2=0.769 ===")
K1, K2, P = 37.6, 0.769, 1.0
def inner(x1):
    # given x1, solve reaction 2: K2 = x2 (x1+x2) / ((x1-x2)(1+x1+x2)) * P
    f = lambda x2: x2 * (x1 + x2) * P - K2 * (x1 - x2) * (1 + x1 + x2)
    return brentq(f, 0.0, x1, xtol=1e-16)
def outer(x1):
    x2 = inner(x1)
    return (x1 - x2) * (x1 + x2) * P - K1 * (1 - x1) * (1 + x1 + x2)
x1 = brentq(outer, 1e-9, 1 - 1e-14, xtol=1e-16); x2 = inner(x1)
n = np.array([1 - x1, x1 - x2, x1 + x2, x2]); y = n / n.sum()
print(f"  extents xi1={x1:.6f} xi2={x2:.6f}; total={n.sum():.6f}")
for s, a, b in zip(['C2H6', 'C2H4', 'H2', 'C2H2'], n, y): print(f"  {s:5s} n={a:.6f} y={b:.6f}")
print(f"  checks: K1={y[1]*y[2]/y[0]*P:.6f} K2={y[3]*y[2]/y[1]*P:.6f}; ethane conversion={x1*100:.4f} %, ethylene selectivity={(x1-x2)/x1*100:.4f} %")
