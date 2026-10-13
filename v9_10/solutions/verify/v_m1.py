"""Independent verification, Topic 1 (empirical models / regression), variants 9 & 10.

Methods (deliberately different from a plain numpy.polyfit / curve_fit call):
  1.1  exact rational normal equations (fractions.Fraction + Gauss-Jordan) -> exact LSQ
       coefficients; cross-check with Householder QR on a scaled variable u=(T-675)/625.
       Integral of the polynomial done analytically (exact antiderivative); trapezoid by hand.
  1.2  variable projection: for a fixed nonlinear parameter the linear one is closed form,
       then 1-D golden-section search (own implementation) on the reduced SSE.
  1.3  (a) closed-form simple linear regression; (b) variable projection + golden section.
  1.4  exact rational normal equations for degree 1..3; Andrade by closed-form regression.
"""
from fractions import Fraction as Fr
import math
import numpy as np

R = 8.314462618


# ---------------------------------------------------------------- helpers
def exact_polyfit(xs, ys, deg):
    """Exact LSQ via rational normal equations (Gauss-Jordan in Fractions)."""
    X = [Fr(str(x)) for x in xs]
    Y = [Fr(str(y)) for y in ys]
    n = deg + 1
    M = [[sum(x ** (i + j) for x in X) for j in range(n)] + [sum(y * x ** i for x, y in zip(X, Y))]
         for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [v / piv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]  # a0..adeg (exact)


def peval(coef, x):
    return sum(c * x ** k for k, c in enumerate(coef))


def stats(y, yh, p=None):
    y = np.asarray(y, float); yh = np.asarray(yh, float)
    sse = float(np.sum((y - yh) ** 2)); sst = float(np.sum((y - y.mean()) ** 2))
    r2 = 1 - sse / sst
    out = dict(SSE=sse, R2=r2, maxrel=float(np.max(np.abs((yh - y) / y)) * 100))
    if p is not None:
        n = len(y)
        out["R2adj"] = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    return out


def golden(f, a, b, tol=1e-14, it=500):
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(it):
        if abs(b - a) < tol * (1 + abs(a) + abs(b)):
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a); fd = f(d)
    return (a + b) / 2


def grid_then_golden(f, lo, hi, n=4000):
    xs = np.linspace(lo, hi, n)
    vals = [f(x) for x in xs]
    i = int(np.argmin(vals))
    a = xs[max(i - 1, 0)]; b = xs[min(i + 1, n - 1)]
    return golden(f, a, b)


# ---------------------------------------------------------------- 1.1
T = [50, 100, 150, 200, 273.15, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
C = [34.16, 41.3, 48.79, 56.07, 68.74, 73.93, 94.01, 112.59, 128.7, 142.67, 154.77, 163.35,
     174.6, 182.67, 189.74, 195.85]
print("=== 1.1 degree-5 polynomial C(T) ===")
cx = exact_polyfit(T, C, 5)
cf = [float(c) for c in cx]
for k, c in enumerate(cf):
    print(f"  a{k} = {c:.10e}")
# QR cross-check on scaled variable, then expand back to powers of T
Ta = np.array(T, float); Ca = np.array(C, float)
u = (Ta - 675.0) / 625.0
V = np.vander(u, 6, increasing=True)
Q, Rm = np.linalg.qr(V)
bu = np.linalg.solve(Rm, Q.T @ Ca)
# expand sum b_k ((T-675)/625)^k
poly_T = np.zeros(6)
for k, bk in enumerate(bu):
    # (T-675)^k / 625^k
    pk = np.array([1.0])
    for _ in range(k):
        pk = np.convolve(pk, [-675.0, 1.0])
    poly_T[:len(pk)] += bk * pk / 625.0 ** k
print("  QR(scaled) max rel diff of coeffs vs exact:",
      max(abs(poly_T[k] - cf[k]) / abs(cf[k]) for k in range(6)))
Ch = [float(peval(cx, Fr(str(t)))) for t in T]
s = stats(C, Ch, p=5)
print(f"  R2 = {s['R2']:.10f}  SSE = {s['SSE']:.8f}  R2adj = {s['R2adj']:.10f}  maxrel% = {s['maxrel']:.5f}")
# exact integral
t0, t1 = Fr(50), Fr(1300)
I = sum(c * (t1 ** (k + 1) - t0 ** (k + 1)) / (k + 1) for k, c in enumerate(cx))
Cmean_poly = float(I / 1250)
# trapezoid by hand
Itr = sum((T[i + 1] - T[i]) * (C[i + 1] + C[i]) / 2 for i in range(len(T) - 1))
Cmean_tr = Itr / 1250
print(f"  integral(poly) = {float(I):.6f}   <C>_poly = {Cmean_poly:.8f}")
print(f"  integral(trap) = {Itr:.6f}   <C>_trap = {Cmean_tr:.8f}")
print(f"  difference trap-poly = {Cmean_tr - Cmean_poly:.6f} ({(Cmean_tr - Cmean_poly) / Cmean_poly * 100:.5f} %)")

# ---------------------------------------------------------------- 1.2
x = np.array([0.263, 0.294, 0.321, 0.367, 0.429, 0.608, 1.33, 1.36])
y = np.array([0.34, 0.32, 0.24, 0.20, 0.16, 0.11, 0.06, 0.04])
print("\n=== 1.2 y = a (ln(x/b))^(-2/3) ===")


def a_of_b(b):
    f = np.log(x / b) ** (-2.0 / 3.0)
    return float(f @ y / (f @ f)), f


def sse_b(b):
    a, f = a_of_b(b)
    return float(np.sum((y - a * f) ** 2))


bopt = grid_then_golden(sse_b, 1e-6, 0.263 - 1e-9, n=20000)
aopt, f = a_of_b(bopt)
s = stats(y, aopt * f)
print(f"  a = {aopt:.8f}  b = {bopt:.8f}  SSE = {s['SSE']:.8e}  R2 = {s['R2']:.8f}")

print("=== 1.2 alt y = a x^(-n) ===")


def a_of_n(n):
    g = x ** (-n)
    return float(g @ y / (g @ g)), g


def sse_n(n):
    a, g = a_of_n(n)
    return float(np.sum((y - a * g) ** 2))


nopt = grid_then_golden(sse_n, 0.01, 5.0)
apw, g = a_of_n(nopt)
s = stats(y, apw * g)
print(f"  nonlinear LSQ on y: a = {apw:.8f}  n = {nopt:.8f}  SSE = {s['SSE']:.8e}  R2 = {s['R2']:.8f}")
# log-linear variant
lx, ly = np.log(x), np.log(y)
sl = np.sum((lx - lx.mean()) * (ly - ly.mean())) / np.sum((lx - lx.mean()) ** 2)
ic = ly.mean() - sl * lx.mean()
a_ll, n_ll = math.exp(ic), -sl
s2 = stats(y, a_ll * x ** (-n_ll))
r2log = 1 - np.sum((ly - (ic + sl * lx)) ** 2) / np.sum((ly - ly.mean()) ** 2)
print(f"  log-linear fit: a = {a_ll:.8f}  n = {n_ll:.8f}  R2(on y) = {s2['R2']:.8f}  R2(on ln y) = {r2log:.8f}")

# ---------------------------------------------------------------- 1.3
print("\n=== 1.3 Arrhenius ===")
t = np.arange(100, 501, 50, dtype=float)
k = np.array([0.10, 0.56, 1.76, 3.54, 9.53, 15.98, 25.04, 60.74, 143.60])
TK = t + 273.15
X = 1 / TK; Yl = np.log(k)
sl = np.sum((X - X.mean()) * (Yl - Yl.mean())) / np.sum((X - X.mean()) ** 2)
ic = Yl.mean() - sl * X.mean()
Ea_a, A_a = -sl * R, math.exp(ic)
r2_ln = 1 - np.sum((Yl - (ic + sl * X)) ** 2) / np.sum((Yl - Yl.mean()) ** 2)
s_a = stats(k, A_a * np.exp(-Ea_a / (R * TK)))
print(f"  (a) linear ln k vs 1/T: Ea = {Ea_a:.4f} J/mol  A = {A_a:.6f} 1/s  R2(ln k) = {r2_ln:.8f}  R2(k) = {s_a['R2']:.8f}")


def A_of_E(E):
    e = np.exp(-E / (R * TK))
    return float(e @ k / (e @ e)), e


def sse_E(E):
    A, e = A_of_E(E)
    return float(np.sum((k - A * e) ** 2))


Eb = grid_then_golden(sse_E, 1e4, 2e5, n=20000)
Ab, e = A_of_E(Eb)
s_b = stats(k, Ab * e)
r2b_ln = 1 - np.sum((Yl - np.log(Ab * e)) ** 2) / np.sum((Yl - Yl.mean()) ** 2)
print(f"  (b) nonlinear on k:     Ea = {Eb:.4f} J/mol  A = {Ab:.6f} 1/s  R2(k) = {s_b['R2']:.8f}  SSE = {s_b['SSE']:.6f}  R2(ln k) = {r2b_ln:.8f}")

# ---------------------------------------------------------------- 1.4
print("\n=== 1.4 glycerin viscosity ===")
Tv = [270, 280, 290, 300, 310, 320, 330, 350, 370, 390]
mu = [12.00, 8.500, 6.050, 4.250, 3.500, 2.600, 2.000, 1.200, 0.730, 0.450]
for d in (1, 2, 3):
    cx = exact_polyfit(Tv, mu, d)
    mh = [float(peval(cx, Fr(t))) for t in Tv]
    s = stats(mu, mh, p=d)
    print(f"  deg {d}: coefs a0..a{d} = " + ", ".join(f"{float(c):.10e}" for c in cx))
    print(f"         R2 = {s['R2']:.8f}  SSE = {s['SSE']:.8f}  R2adj = {s['R2adj']:.8f}  max rel err = {s['maxrel']:.5f} %")
Tva = np.array(Tv, float); mua = np.array(mu)
X = 1 / Tva; Yl = np.log(mua)
B = np.sum((X - X.mean()) * (Yl - Yl.mean())) / np.sum((X - X.mean()) ** 2)
A = Yl.mean() - B * X.mean()
s = stats(mu, np.exp(A + B * X))
r2l = 1 - np.sum((Yl - A - B * X) ** 2) / np.sum((Yl - Yl.mean()) ** 2)
print(f"  Andrade ln mu = A + B/T: A = {A:.8f}  B = {B:.6f} K  R2(mu) = {s['R2']:.8f}  SSE(mu) = {s['SSE']:.8f}  "
      f"max rel err = {s['maxrel']:.5f} %  R2(ln mu) = {r2l:.8f}")
