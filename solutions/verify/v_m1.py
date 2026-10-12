"""Independent verification, Topic 1 (empirical models / regression), variant 1."""
import numpy as np
from scipy.optimize import least_squares, curve_fit
from scipy.integrate import quad

def r2sse(y, yh):
    sse = float(np.sum((y - yh) ** 2)); sst = float(np.sum((y - y.mean()) ** 2))
    return 1 - sse / sst, sse

def lsq_poly(x, y, d):
    # normal equations via QR (not np.polyfit)
    X = np.vander(x, d + 1, increasing=True)
    Q, R = np.linalg.qr(X)
    b = np.linalg.solve(R, Q.T @ y)
    return b, X @ b

print("=== 1.1 heat capacity, degree 1 ===")
T = np.array([50,100,150,200,273.15,300,400,500,600,700,800,900,1000,1100,1200,1300.])
C = np.array([34.16,41.3,48.79,56.07,68.74,73.93,94.01,112.59,128.7,142.67,154.77,163.35,174.6,182.67,189.74,195.85])
b, Ch = lsq_poly(T, C, 1)
r2, sse = r2sse(C, Ch)
print(f"b0={b[0]:.6f} b1={b[1]:.8f} R2={r2:.6f} SSE={sse:.6f}")
I_poly, _ = quad(lambda t: b[0] + b[1] * t, 50, 1300)
Cm_poly = I_poly / 1250
# trapezoid by hand
I_trap = float(np.sum(0.5 * (C[1:] + C[:-1]) * np.diff(T)))
Cm_trap = I_trap / 1250
print(f"<C> poly = {Cm_poly:.6f}; <C> trapz = {Cm_trap:.6f}; diff = {Cm_poly-Cm_trap:.6f} ({(Cm_poly-Cm_trap)/Cm_trap*100:.4f} %)")
# for info: higher degrees
for d in (2, 3, 4, 5):
    bd, _ = lsq_poly(T, C, d)
    P = np.polynomial.Polynomial(bd).integ()
    print(f"  (info) deg {d}: <C>={(P(1300)-P(50))/1250:.4f}")

print("\n=== 1.2 stripping column y = a*(ln(x/b))^(-2/3) ===")
x = np.array([0.263,0.294,0.321,0.367,0.429,0.608,1.33,1.36])
y = np.array([0.34,0.32,0.24,0.20,0.16,0.11,0.06,0.04])
f = lambda p, x: p[0] * np.log(x / p[1]) ** (-2/3)
# Method: profile likelihood -- for fixed b, a is linear: a = sum(g y)/sum(g^2); scan b finely then refine with bounded LSQ
def prof(bb):
    g = np.log(x / bb) ** (-2/3); a = g @ y / (g @ g); return a, np.sum((y - a * g) ** 2)
bs = np.linspace(1e-4, 0.2629, 200001)
ss = np.array([prof(bb)[1] for bb in bs])
i = int(np.argmin(ss)); b0 = bs[i]
res = least_squares(lambda p: f(p, x) - y, [prof(b0)[0], b0], bounds=([0, 1e-8], [np.inf, 0.263 - 1e-12]), xtol=1e-15, ftol=1e-15, gtol=1e-15)
a12, b12 = res.x
r2, sse = r2sse(y, f(res.x, x))
print(f"grid b*={b0:.6f}; refined a={a12:.6f} b={b12:.6f} R2={r2:.6f} SSE={sse:.6e}")
# alternative forms
p, _ = curve_fit(lambda x, a, n: a * x ** (-n), x, y, p0=[0.1, 1])
print(f"power y=a x^-n: a={p[0]:.6f} n={p[1]:.6f} R2={r2sse(y, p[0]*x**(-p[1]))[0]:.6f} SSE={r2sse(y, p[0]*x**(-p[1]))[1]:.6e}")
p2, _ = curve_fit(lambda x, a, k, c: a * np.exp(-k * x) + c, x, y, p0=[1, 3, 0.04], maxfev=20000)
yh = p2[0] * np.exp(-p2[1] * x) + p2[2]
print(f"exp y=a e^-kx + c: a={p2[0]:.6f} k={p2[1]:.6f} c={p2[2]:.6f} R2={r2sse(y, yh)[0]:.6f} SSE={r2sse(y, yh)[1]:.6e}")

print("\n=== 1.3 Arrhenius ===")
R = 8.314462618
t = np.arange(100, 501, 50.); TK = t + 273.15
k = np.array([0.05,0.25,0.60,0.98,1.35,1.99,2.87,4.56,8.43])
X = np.column_stack([np.ones_like(TK), 1 / TK])
coef, *_ = np.linalg.lstsq(X, np.log(k), rcond=None)
Ea_lin = -coef[1] * R; A_lin = np.exp(coef[0])
r2ln = r2sse(np.log(k), X @ coef)[0]
r2k_lin = r2sse(k, A_lin * np.exp(-Ea_lin / (R * TK)))[0]
print(f"linear ln k: Ea={Ea_lin:.4f} J/mol A={A_lin:.6f} 1/s R2(ln k)={r2ln:.6f} R2(k)={r2k_lin:.6f}")
# nonlinear on k: parameterize as lnA, Ea/1e4 for conditioning; Levenberg-Marquardt
res = least_squares(lambda p: np.exp(p[0] - p[1] * 1e4 / (R * TK)) - k, [coef[0], Ea_lin / 1e4], method='lm', xtol=1e-15, ftol=1e-15)
A_nl = np.exp(res.x[0]); Ea_nl = res.x[1] * 1e4
kh = A_nl * np.exp(-Ea_nl / (R * TK))
r2k, ssek = r2sse(k, kh)
print(f"nonlinear k: Ea={Ea_nl:.4f} J/mol A={A_nl:.6f} 1/s R2(k)={r2k:.6f} SSE={ssek:.6f}")

print("\n=== 1.4 acetone viscosity ===")
Tv = np.array([250,260,270,280,290,300,310,320,330,350,370,390.])
mu = np.array([0.500,0.442,0.395,0.356,0.322,0.293,0.268,0.246,0.230,0.200,0.170,0.150])
n = len(Tv)
for d in (1, 2, 3):
    # scaled variable for conditioning, then convert back to raw T coefficients
    s = (Tv - 300) / 100
    bs_, _ = lsq_poly(s, mu, d)
    Praw = np.polynomial.Polynomial(bs_)(np.polynomial.Polynomial([-3, 0.01]))
    braw = Praw.coef
    yh = Praw(Tv)
    r2, sse = r2sse(mu, yh)
    adj = 1 - (1 - r2) * (n - 1) / (n - d - 1)
    print(f"deg {d}: coefs b0..b{d} = " + ", ".join(f"{c:.9e}" for c in braw) + f"\n        R2={r2:.6f} SSE={sse:.6e} adjR2={adj:.6f}")
