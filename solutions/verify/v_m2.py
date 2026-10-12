"""Independent verification, Topic 2 (equations of state), variant 1.
Volume found by Newton iteration on the pressure-explicit residual P(v) - P = 0
starting from the ideal-gas volume (vapour root), cross-checked by brentq."""
import numpy as np
from scipy.optimize import brentq
R = 8.314462618; atm = 101325.0

def params(Tc, Pc, w, T, kind):
    Tr = T / Tc
    b = 0.08664 * R * Tc / Pc
    if kind == 'RK':
        a = 0.42748 * R**2 * Tc**2 / Pc * Tr**-0.5
    else:
        m = 0.480 + 1.574 * w - 0.176 * w**2
        a = 0.42748 * R**2 * Tc**2 / Pc * (1 + m * (1 - np.sqrt(Tr)))**2
    return a, b

def solve_v(a, b, T, P):
    Pf = lambda v: R * T / (v - b) - a / (v * (v + b)) - P
    dP = lambda v: -R * T / (v - b)**2 + a * (2 * v + b) / (v * (v + b))**2
    v = R * T / P
    for _ in range(200):
        dv = Pf(v) / dP(v); v -= dv
        if abs(dv) < 1e-16 * abs(v): break
    vb = brentq(Pf, b * 1.0001, 10 * R * T / P, xtol=1e-18)
    return v, vb

def report(name, a, b, T, P):
    v, vb = solve_v(a, b, T, P)
    print(f"  {name:4s}: v = {v*1e3:.6f} L/mol (brentq {vb*1e3:.6f})  Z = {P*v/(R*T):.6f}   a={a:.6e} b={b:.6e}")

print("=== 2.1 methane, 40 atm, 350 K ===")
T, P = 350.0, 40 * atm
vig = R * T / P
print(f"  IG  : v = {vig*1e3:.6f} L/mol  Z = 1")
for kind in ('RK', 'SRK'):
    a, b = params(190.6, 45.4 * atm, 0.008, T, kind)
    report(kind, a, b, T, P)

print("\n=== 2.2 25% NH3 + N2:H2=1:3, 250 atm, 520 K ===")
comp = {'NH3': (405.6, 111.3, 0.250), 'N2': (126.2, 33.5, 0.040), 'H2': (33.2, 12.8, -0.22)}
y = np.array([0.25, 0.75 / 4, 0.75 * 3 / 4])
print("  y =", y)
T, P = 520.0, 250 * atm
print(f"  IG  : v = {R*T/P*1e3:.6f} L/mol  Z = 1")
for kind in ('RK', 'SRK'):
    ab = np.array([params(Tc, Pc * atm, w, T, kind) for Tc, Pc, w in comp.values()])
    sa = np.sqrt(ab[:, 0])
    a = float((y @ sa)**2)   # = sum_i sum_j yi yj sqrt(ai aj)
    b = float(y @ ab[:, 1])
    report(kind, a, b, T, P)
