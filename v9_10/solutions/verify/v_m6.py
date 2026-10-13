"""Independent verification, Topic 5 (material balances), variants 9 & 10.

5.1  4x4 component balances solved EXACTLY by Cramer's rule in rational arithmetic
     (fractions.Fraction, Leibniz-expansion determinants).
5.2  Toray process: successive substitution on the recycle (stream 7) plus an
     independent closed-form solution of the linear recycle balance.
"""
from fractions import Fraction as Fr
from itertools import permutations

# ---------------------------------------------------------------- 5.1
print("=== 5.1 three-column train ===")
comps = ["xylene", "styrene", "toluene", "benzene"]
F = 1000
zF = [Fr(15, 100), Fr(25, 100), Fr(40, 100), Fr(20, 100)]
cols = {"D1": [7, 4, 54, 35], "B1": [18, 24, 42, 16], "D2": [15, 10, 54, 21], "B2": [24, 65, 10, 1]}
keys = list(cols)
M = [[Fr(cols[k][i], 100) for k in keys] for i in range(4)]
rhs = [F * z for z in zF]


def det(A):
    n = len(A)
    tot = Fr(0)
    for p in permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        prod = Fr(1)
        for i in range(n):
            prod *= A[i][p[i]]
        tot += -prod if inv % 2 else prod
    return tot


D0 = det(M)
sol = {}
for j, k in enumerate(keys):
    Mj = [row[:j] + [rhs[i]] + row[j + 1:] for i, row in enumerate(M)]
    sol[k] = det(Mj) / D0
D = sol["D1"] + sol["B1"]
B = sol["D2"] + sol["B2"]
for k in keys:
    print(f"  {k} = {float(sol[k]):.8f} mol/h  (exact {sol[k]})")
print(f"  D = D1+B1 = {float(D):.8f}   B = D2+B2 = {float(B):.8f}   D+B = {float(D + B):.8f}")
for nm, parts in (("D", ["D1", "B1"]), ("B", ["D2", "B2"])):
    fl = [sum(sol[p] * Fr(cols[p][i], 100) for p in parts) for i in range(4)]
    tot = sum(fl)
    print(f"  {nm}: flows " + ", ".join(f"{c}={float(f):.6f}" for c, f in zip(comps, fl)) +
          " | fractions " + ", ".join(f"{float(f / tot):.6f}" for f in fl))

# ---------------------------------------------------------------- 5.2
print("\n=== 5.2 Toray process ===")
FRESH = 100.0
X = 0.58


def flowsheet(rec):
    """rec = (T, B, X) of recycle stream 7; returns all streams and new recycle."""
    s1 = (FRESH, 0.0, 0.0)
    s2 = tuple(a + b for a, b in zip(s1, rec))
    rT = X * s2[0]
    react = (-rT, rT / 2, rT / 2)
    s3 = tuple(a + b for a, b in zip(s2, react))
    s4 = (0.001 * s3[0], 0.995 * s3[1], 0.0)
    s5 = tuple(a - b for a, b in zip(s3, s4))
    s7 = (0.995 * s5[0], s5[1], 0.001 * s5[2])
    s6 = tuple(a - b for a, b in zip(s5, s7))
    return dict(s1=s1, s2=s2, R=react, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7)


rec = (0.0, 0.0, 0.0)
for it in range(1, 10000):
    st = flowsheet(rec)
    new = st["s7"]
    err = max(abs(a - b) for a, b in zip(new, rec))
    rec = new
    if err < 1e-13:
        break
st = flowsheet(rec)
print(f"  successive substitution converged in {it} iterations")
print("  stream : toluene      benzene      xylene       total")
for k in ["s1", "s2", "R", "s3", "s4", "s5", "s6", "s7"]:
    v = st[k]
    print(f"  {k:6s} : {v[0]:11.6f}  {v[1]:11.6f}  {v[2]:11.6f}  {sum(v):11.6f}")

# closed-form: let T2 = toluene into reactor.
# T7 = 0.995*(0.999*(1-X)*T2), T2 = 100 + T7  -> T2 = 100/(1 - 0.995*0.999*(1-X))
aT = 0.995 * 0.999 * (1 - X)
T2 = FRESH / (1 - aT)
# benzene: B7 = 0.005*(B2 + X T2/2), B2 = B7 -> B7 = 0.005 X T2/2 / 0.995
B7 = 0.005 * X * T2 / 2 / (1 - 0.005)
# xylene: X7 = 0.001*(X2 + X T2/2) -> X7 = 0.001 X T2/2 / 0.999
X7 = 0.001 * X * T2 / 2 / (1 - 0.001)
print(f"  closed form recycle: T7 = {aT * T2:.8f}  B7 = {B7:.8f}  X7 = {X7:.8f}  (SS: {rec[0]:.8f} {rec[1]:.8f} {rec[2]:.8f})")
x6 = st["s6"][2]
t_out = st["s4"][0] + st["s6"][0]
print(f"  xylene product (stream 6) = {x6:.8f} mol/h; xylene / fresh toluene = {x6 / FRESH:.8f}")
print(f"  toluene stoichiometrically converted into xylene = 2*X6 = {2 * x6:.8f} mol/h ({2 * x6 / FRESH * 100:.6f} % of fresh)")
print(f"  benzene product (stream 4) = {st['s4'][1]:.8f} mol/h; benzene/fresh toluene = {st['s4'][1] / FRESH:.8f}")
print(f"  toluene leaving in products = {t_out:.8f}; overall toluene conversion = {(FRESH - t_out) / FRESH * 100:.6f} %")
print(f"  reactor toluene conversion per pass check: {-st['R'][0] / st['s2'][0]:.4f}")
