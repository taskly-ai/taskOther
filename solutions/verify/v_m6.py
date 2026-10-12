"""Independent verification, Topic 5 (material balances), variant 1.
(Module numbering: v_m6 = topic 5 of the task sheet.)"""
import numpy as np
from fractions import Fraction as Fr

print("=== 5.1 column train (xylene, styrene, toluene, benzene) ===")
F = 1000
zF = [15, 25, 40, 20]
cols = {'D1': [7, 4, 54, 35], 'B1': [18, 24, 42, 16], 'D2': [15, 10, 54, 21], 'B2': [24, 65, 10, 1]}
# exact rational Gauss-Jordan elimination (different from a float linear solve)
M = [[Fr(cols[k][i], 100) for k in cols] + [Fr(F * zF[i], 100)] for i in range(4)]
for c in range(4):
    p = next(r for r in range(c, 4) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
    M[c] = [v / M[c][c] for v in M[c]]
    for r in range(4):
        if r != c and M[r][c] != 0:
            M[r] = [a - M[r][c] * b for a, b in zip(M[r], M[c])]
flows = {k: M[i][4] for i, k in enumerate(cols)}
# float cross-check with lstsq
A = np.array([cols[k] for k in cols]).T / 100; sol = np.linalg.lstsq(A, F * np.array(zF) / 100, rcond=None)[0]
names = ['xylene', 'styrene', 'toluene', 'benzene']
streams = {}
for k in cols: streams[k] = np.array([float(flows[k]) * c / 100 for c in cols[k]])
streams['D'] = streams['D1'] + streams['B1']; streams['B'] = streams['D2'] + streams['B2']
streams['F'] = F * np.array(zF) / 100
print("  exact flows:", {k: f"{float(v):.6f} ({v})" for k, v in flows.items()}, " lstsq:", np.round(sol, 6))
for k in ['F', 'D', 'B', 'D1', 'B1', 'D2', 'B2']:
    s = streams[k]; print(f"  {k:3s} total={s.sum():10.4f}  " + "  ".join(f"{n}={v:9.4f} ({v/s.sum()*100:7.4f}%)" for n, v in zip(names, s)))

print("\n=== 5.2 Toray process, successive substitution on recycle ===")
X = 0.58
T1 = 100.0
r = np.zeros(3)  # recycle stream 7: [toluene, benzene, xylene]
for it in range(1, 1000):
    s1 = np.array([T1, 0, 0]); s2 = s1 + r
    ext = X * s2[0] / 2                       # extent of 2T -> B + X
    rxn = np.array([-2 * ext, ext, ext])
    s3 = s2 + rxn
    s4 = np.array([0.001 * s3[0], 0.995 * s3[1], 0.0]); s5 = s3 - s4
    s7 = np.array([0.995 * s5[0], s5[1], 0.001 * s5[2]]); s6 = s5 - s7
    if np.max(np.abs(s7 - r)) < 1e-13: break
    r = s7
print(f"  converged in {it} iterations")
S = {'1': s1, '2': s2, 'R(reaction)': rxn, '3': s3, '4': s4, '5': s5, '6': s6, '7': s7}
print("  stream      toluene      benzene       xylene        total")
for k, s in S.items(): print(f"  {k:11s} {s[0]:11.5f} {s[1]:12.5f} {s[2]:12.5f} {s.sum():12.5f}")
print(f"  balance check (in - out - reacted toluene): {T1 - s4[0] - s6[0] + rxn[0]:.2e}")
print(f"  xylene product / fresh toluene = {s6[2]/T1*100:.4f} %  (mol xylene per mol toluene)")
print(f"  toluene converted to xylene (2*X6/T1, stoichiometric) = {2*s6[2]/T1*100:.4f} %")
print(f"  overall toluene conversion (1 - (T4+T6)/T1) = {(1-(s4[0]+s6[0])/T1)*100:.4f} %")
print(f"  benzene product (stream 4) = {s4[1]:.5f}; purity of 4 = {s4[1]/s4.sum()*100:.4f} %; xylene purity of 6 = {s6[2]/s6.sum()*100:.4f} %")
print(f"  recycle ratio 7/1 = {s7.sum()/T1:.5f}")
