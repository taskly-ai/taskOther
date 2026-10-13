"""Independent verification, Topic 2 (cubic EOS), variants 9 & 10.

Method: Newton iteration on the pressure-explicit form F(V) = RT/(V-b) - a/(V(V+b)) - P = 0
starting from the ideal-gas volume (vapor root), with an independent cross-check by
Cardano's trigonometric/closed-form solution of the cubic in Z:
    Z^3 - Z^2 + (A - B - B^2) Z - A B = 0,  A = aP/(RT)^2, B = bP/(RT).
"""
import math

R = 8.314462618               # J/(mol K)
ATM = 101325.0
RL = R / ATM * 1000.0         # L atm / (mol K)


def ab_rk(Tc, Pc, T):
    Tr = T / Tc
    a = 0.42748 * RL ** 2 * Tc ** 2 / Pc * Tr ** -0.5
    b = 0.08664 * RL * Tc / Pc
    return a, b


def ab_srk(Tc, Pc, w, T):
    Tr = T / Tc
    m = 0.480 + 1.574 * w - 0.176 * w ** 2
    alpha = (1 + m * (1 - math.sqrt(Tr))) ** 2
    a = 0.42748 * RL ** 2 * Tc ** 2 / Pc * alpha
    b = 0.08664 * RL * Tc / Pc
    return a, b, m, alpha


def newton_V(a, b, P, T):
    V = RL * T / P
    for _ in range(200):
        F = RL * T / (V - b) - a / (V * (V + b)) - P
        dF = -RL * T / (V - b) ** 2 + a * (2 * V + b) / (V * (V + b)) ** 2
        dV = -F / dF
        V += dV
        if abs(dV) < 1e-15 * V:
            break
    return V


def cardano_Z(a, b, P, T):
    A = a * P / (RL * T) ** 2
    B = b * P / (RL * T)
    # Z^3 + c2 Z^2 + c1 Z + c0
    c2, c1, c0 = -1.0, A - B - B * B, -A * B
    p = c1 - c2 ** 2 / 3
    q = 2 * c2 ** 3 / 27 - c2 * c1 / 3 + c0
    disc = (q / 2) ** 2 + (p / 3) ** 3
    if disc > 0:
        s = math.sqrt(disc)
        u = math.copysign(abs(-q / 2 + s) ** (1 / 3), -q / 2 + s)
        v = math.copysign(abs(-q / 2 - s) ** (1 / 3), -q / 2 - s)
        roots = [u + v - c2 / 3]
    else:
        r = math.sqrt(-p / 3)
        phi = math.acos(max(-1, min(1, -q / (2 * r ** 3))))
        roots = [2 * r * math.cos((phi - 2 * math.pi * kk) / 3) - c2 / 3 for kk in range(3)]
    return max(roots), roots, A, B


def report(label, a, b, P, T):
    V = newton_V(a, b, P, T)
    Z = P * V / (RL * T)
    Zc, roots, A, B = cardano_Z(a, b, P, T)
    print(f"  {label:4s}: V = {V:.8f} L/mol  Z = {Z:.8f}   (Cardano Zmax = {Zc:.8f}, n_real = {len(roots)}; "
          f"a = {a:.6g} L2 atm/mol2, b = {b:.6g} L/mol)")
    return V, Z


print(f"R = {RL:.9f} L atm/(mol K)")
# ---------------------------------------------------------------- 2.1 hydrogen
print("=== 2.1 hydrogen, 50 atm, 400 K ===")
P, T = 50.0, 400.0
Tc, Pc, w = 33.2, 12.8, -0.22
Vig = RL * T / P
print(f"  IG  : V = {Vig:.8f} L/mol  Z = 1")
report("RK", *ab_rk(Tc, Pc, T), P, T)
a, b, m, al = ab_srk(Tc, Pc, w, T)
print(f"        SRK m = {m:.6f}, alpha = {al:.6f}, Tr = {T / Tc:.6f}")
report("SRK", a, b, P, T)

# ---------------------------------------------------------------- 2.2 mixture
print("=== 2.2 CH4/C2H6/C3H8 = 0.25/0.1875/0.5625, 120 atm, 420 K ===")
P, T = 120.0, 420.0
y = [0.25, 0.75 / 4, 0.75 * 3 / 4]
crit = [(190.6, 45.4, 0.008), (305.4, 48.2, 0.098), (369.8, 41.9, 0.152)]
Vig = RL * T / P
print(f"  IG  : V = {Vig:.8f} L/mol  Z = 1")


def mix(ab_list):
    a = sum(y[i] * y[j] * math.sqrt(ab_list[i][0] * ab_list[j][0]) for i in range(3) for j in range(3))
    b = sum(y[i] * ab_list[i][1] for i in range(3))
    return a, b


report("RK", *mix([ab_rk(Tc, Pc, T) for Tc, Pc, w in crit]), P, T)
report("SRK", *mix([ab_srk(Tc, Pc, w, T)[:2] for Tc, Pc, w in crit]), P, T)
