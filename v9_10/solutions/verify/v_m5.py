"""Independent verification, Topic 4 (chemical equilibrium), variants 9 & 10.

4.1  extent solved by bisection on ln(Ky_calc) - ln(Kp P) (monotone in extent).
4.2a K(1000) from dG_r; van 't Hoff integrated 1000 -> 1100 K with dH_r(T) linear
     (through the 800 and 1000 K points): analytic integral + composite Simpson cross-check.
     Alternative: dG_r linearly extrapolated. Conversion closed form x = sqrt(K/(K+P)).
4.2b two extents by nested bisection (outer xi1, inner xi2), cross-checked by Newton.
"""
import math

R = 8.314462618
Rcal = R / 4.184


def bisect(f, a, b, tol=1e-15, it=400):
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


# ---------------------------------------------------------------- 4.1
print("=== 4.1 ammonia synthesis ===")
n0 = {"N2": 1.1, "H2": 3.0, "NH3": 0.2}
Kp, P = 0.05, 220.0


def g41(xi):
    N2, H2, NH3 = 1.1 - 0.5 * xi, 3.0 - 1.5 * xi, 0.2 + xi
    nt = N2 + H2 + NH3
    return math.log(NH3 / nt) - 0.5 * math.log(N2 / nt) - 1.5 * math.log(H2 / nt) - math.log(Kp * P)


xi = bisect(g41, -0.2 + 1e-12, 2.0 - 1e-12)
N2, H2, NH3 = 1.1 - 0.5 * xi, 3.0 - 1.5 * xi, 0.2 + xi
nt = N2 + H2 + NH3
print(f"  extent = {xi:.10f} mol/h")
print(f"  out: N2 = {N2:.8f}  H2 = {H2:.8f}  NH3 = {NH3:.8f}  total = {nt:.8f}")
print(f"  y:   N2 = {N2 / nt:.8f}  H2 = {H2 / nt:.8f}  NH3 = {NH3 / nt:.8f}")
print(f"  N2 conversion = {0.5 * xi / 1.1 * 100:.6f} %")
print(f"  check Ky = {NH3 / nt / ((N2 / nt) ** 0.5 * (H2 / nt) ** 1.5):.8f} vs Kp*P = {Kp * P}")

# ---------------------------------------------------------------- 4.2a
print("\n=== 4.2a ethane dehydrogenation, 1100 K, 1 atm ===")
Tt = [298, 400, 600, 800, 1000]
dHf_e = [-20236, -21419, -23280, -24530, -25280]
dHf_y = [12496, 11766, 10600, 9760, 9205]
dGf_e = [-7860, -3447, 5970, 15920, 26130]
dGf_y = [16282, 17675, 20918, 24490, 28249]
dHr = [b - a for a, b in zip(dHf_e, dHf_y)]
dGr = [b - a for a, b in zip(dGf_e, dGf_y)]
for T, h, g in zip(Tt, dHr, dGr):
    print(f"  T={T:5d}: dH_r = {h:7d} cal/mol  dG_r = {g:7d} cal/mol  K = {math.exp(-g / (Rcal * T)):.6e}")
K1000 = math.exp(-dGr[4] / (Rcal * 1000))
s = (dHr[4] - dHr[3]) / 200.0
H0 = dHr[4] - s * 1000.0          # dH(T) = H0 + s T
T1, T2 = 1000.0, 1100.0
# analytic: int (H0 + sT)/(R T^2) dT = (H0 (1/T1 - 1/T2) + s ln(T2/T1)) / R
lnratio = (H0 * (1 / T1 - 1 / T2) + s * math.log(T2 / T1)) / Rcal
# Simpson cross-check
N = 1000
h = (T2 - T1) / N
f = lambda T: (H0 + s * T) / (Rcal * T * T)
simp = f(T1) + f(T2) + sum((4 if i % 2 else 2) * f(T1 + i * h) for i in range(1, N))
simp *= h / 3
K_vh = K1000 * math.exp(lnratio)
dH1100 = H0 + s * 1100
print(f"  K(1000) = {K1000:.8f}   dH_r(1100, extrapolated) = {dH1100:.2f} cal/mol, slope = {s:.4f} cal/mol/K")
print(f"  van 't Hoff: ln(K1100/K1000) = {lnratio:.10f} (Simpson {simp:.10f})  K(1100) = {K_vh:.8f}")
# constant dH(1000) variant for info
K_const = K1000 * math.exp(dHr[4] / Rcal * (1 / T1 - 1 / T2))
print(f"  (info) van 't Hoff with constant dH(1000): K(1100) = {K_const:.8f}")
dG1100 = dGr[4] + (dGr[4] - dGr[3]) / 200.0 * 100.0
K_dG = math.exp(-dG1100 / (Rcal * 1100))
print(f"  dG linear extrapolation: dG_r(1100) = {dG1100:.2f} cal/mol  K(1100) = {K_dG:.8f}")
Ptot = 1.0
for lab, K in (("van 't Hoff", K_vh), ("dG extrap.", K_dG)):
    x = math.sqrt(K / (K + Ptot))
    nt = 1 + x
    print(f"  [{lab}] conversion = {x:.8f}  y_C2H6 = {(1 - x) / nt:.8f}  y_C2H4 = y_H2 = {x / nt:.8f}  total = {nt:.8f}")

# ---------------------------------------------------------------- 4.2b
print("\n=== 4.2b two reactions, 1367 K, 1 atm ===")
K1, K2 = 37.6, 0.769


def inner(x1):
    # given xi1 solve xi2 in (0, xi1): K2 = xi2 (x1 + xi2) / ((x1 - xi2)(1 + x1 + xi2)) at P = 1
    g = lambda x2: math.log(x2 * (x1 + x2)) - math.log((x1 - x2) * (1 + x1 + x2)) - math.log(K2 / Ptot)
    return bisect(g, 1e-300 if x1 > 0 else 0, x1 * (1 - 1e-16))


def outer(x1):
    x2 = inner(x1)
    nt = 1 + x1 + x2
    return math.log((x1 - x2) * (x1 + x2)) - math.log((1 - x1) * nt) - math.log(K1 / Ptot)


x1 = bisect(outer, 1e-9, 1 - 1e-15)
x2 = inner(x1)
# Newton cross-check
import numpy as np


def Fv(v):
    a, b = v
    nt = 1 + a + b
    return np.array([math.log((a - b) * (a + b)) - math.log((1 - a) * nt) - math.log(K1),
                     math.log(b * (a + b)) - math.log((a - b) * nt) - math.log(K2)])


v = np.array([0.9, 0.3])
for _ in range(60):
    F0 = Fv(v)
    J = np.zeros((2, 2))
    for j in range(2):
        d = np.zeros(2); d[j] = 1e-8
        J[:, j] = (Fv(v + d) - Fv(v - d)) / 2e-8
    step = np.linalg.solve(J, F0)
    lam = 1.0
    while True:  # damped: keep 0 < xi2 < xi1 < 1
        w = v - lam * step
        if 0 < w[1] < w[0] < 1:
            break
        lam /= 2
    v = w
nt = 1 + x1 + x2
n = {"C2H6": 1 - x1, "C2H4": x1 - x2, "H2": x1 + x2, "C2H2": x2}
print(f"  xi1 = {x1:.10f}  xi2 = {x2:.10f}   (Newton: {v[0]:.10f}, {v[1]:.10f})  total = {nt:.8f}")
for k_, val in n.items():
    print(f"   {k_:5s}: n = {val:.8f}  y = {val / nt:.8f}")
print(f"  ethane conversion = {x1 * 100:.6f} %")
