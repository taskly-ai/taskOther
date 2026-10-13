# Independent verification: variants 9 and 10

Scripts in this folder (run with `python3 v_mX.py`):
- `v_m1.py`: Topic 1 (regression)
- `v_m2.py`: Topic 2 (EOS)
- `v_m3.py`: Topic 3 (phase equilibria)
- `v_m5.py`: Topic 4 (chemical equilibrium)
- `v_m6.py`: Topic 5 (material balances)

Constants: R = 8.314462618 J/(mol K) = 0.082057366 L atm/(mol K) = 1.987204 cal/(mol K); 1 atm = 101325 Pa; 1 psi = 6894.757 Pa; T(°R) = 1.8 T(K).

## 1.1 Degree-5 polynomial C(T)
Method: exact rational normal equations (Fraction, Gauss-Jordan). Cross-checked with Householder QR on the scaled variable u = (T-675)/625, expanded back to powers of T (max relative coefficient difference 6e-14).

| coef | value |
|---|---|
| a0 | 3.1725774711e+01 |
| a1 | 3.8728769410e-02 |
| a2 | 5.8013962625e-04 |
| a3 | -9.4084946785e-07 |
| a4 | 6.1090644019e-10 |
| a5 | -1.4660876036e-13 |

- R² = 0.99985640, SSE = 7.0643750, adj. R² = 0.99978459, max relative error 2.4553 % (at T = 50 K)
- ∫50→1300 of the polynomial = 161085.912, so ⟨C⟩_poly = 128.86873
- Trapezoid rule on the table: ∫ = 161039.5205, so ⟨C⟩_trap = 128.83162 (−0.03711, −0.0288 % vs the polynomial)

## 1.2 Stripper model
Method: variable projection (a in closed form for fixed b, or for fixed n) plus a dense grid and golden-section search. Cross-checked with scipy curve_fit.
- y = a (ln(x/b))^(-2/3): **a = 0.126391, b = 0.214441**, SSE = 5.69982e-3, **R² = 0.935513**
- y = a x^(-n), nonlinear LSQ on y: **a = 0.0532283, n = 1.388608**, SSE = 2.12043e-3, **R² = 0.976010**
- y = a x^(-n), log-linear fit: a = 0.0663989, n = 1.168808, R²(y) = 0.962860, R²(ln y) = 0.970362

## 1.3 Arrhenius (T = t + 273.15)
- (a) Closed-form regression of ln k on 1/T: **Ea = 40832.15 J/mol, A = 51752.35 s⁻¹, R²(ln k) = 0.989426** (R² on k = 0.832540)
- (b) Nonlinear LSQ on k (variable projection plus golden section; scipy agrees to 1e-6 relative): **Ea = 73150.1 J/mol, A = 1.24376e7 s⁻¹, R²(k) = 0.993010**, SSE = 123.994

## 1.4 Glycerin viscosity (n = 10, T in K, μ in mPa·s)
Method: exact rational normal equations.

| deg | coefficients a0..ad | R² | SSE | adj R² | max rel err % |
|---|---|---|---|---|---|
| 1 | 30.907581, −0.083425486 | 0.769089 | 29.02478 | 0.740225 | 461.857 |
| 2 | 161.32809, −0.88643507, 1.2194347e-3 | 0.967720 | 4.057469 | 0.958497 | 143.207 |
| 3 | 665.96829, −5.5659307, 1.5566217e-2, −1.4541363e-5 | 0.995665 | 0.5449539 | 0.993497 | 40.4591 |
| Andrade ln μ = A + B/T | A = −7.966388, B = 2835.908 K | 0.995355 (on μ) | 0.5839209 | n/a | 10.9244 |

For Andrade, R² on ln μ = 0.996949.

## 2.1 Hydrogen, 50 atm, 400 K
Method: Newton on P(V) starting from the ideal-gas V, checked by the Cardano cubic in Z (largest root).
- IG: V = 0.65645893 L/mol, Z = 1
- RK: a = 0.0714095 L²atm/mol², b = 0.0184401 L/mol, **V = 0.67288982 L/mol, Z = 1.0250296** (the other two roots are negative)
- SRK: m = 0.125202, α = 0.476957 (Tr = 12.0482), a = 0.118221, **V = 0.67156648 L/mol, Z = 1.0230137**

## 2.2 Mixture CH4/C2H6/C3H8 = 0.25/0.1875/0.5625, 120 atm, 420 K
- IG: V = 0.28720078 L/mol, Z = 1
- RK: a_mix = 5.71265, b_mix = 0.0512028, **V = 0.19619923 L/mol, Z = 0.68314309** (single real root)
- SRK: a_mix = 5.41070, **V = 0.20695948 L/mol, Z = 0.72060905** (single real root)

## 3.1 Bubble and dew T, 14 atm (205.7433 psia)
Method: bisection on ln Σ(zK) and ln Σ(z/K), with a Newton cross-check.
- **Bubble T = 293.0461 K = 19.8961 °C**
- **Dew T = 339.3816 K = 66.2316 °C**

## 3.2 Separator train (feed 1 mol, Σz = 1.00000)
Method: bisection on Rachford–Rice, with single-phase checks before each flash.

Base case stage details (C1 → C2 → C3):

| stage | V/F | K (CH4, C2, C3, iC4, nC4, C5) |
|---|---|---|
| C1 | 0.73608976 | 2.29242, 0.587616, 0.229307, 0.0727132, 0.0467909, 0.0199419 |
| C2 | 0.87614441 | 2.11235, 0.418678, 0.134682, 0.0383103, 0.0230298, 0.00831489 |
| C3 | 0.47754057 | 1.19597, 0.110189, 0.0204395, 0.00397194, 0.00191449, 0.000430039 |

Gas compositions:
- y(C1) = 0.848331, 0.030442, 0.118511, 0.001480, 0.000731, 0.000505
- y(C3) = 0.992485, 0.004977, 0.002534, 3e-6, ~0, ~0

| scheme | stage V/F | final gas, mol | CH4 % in gas | C3+ % in gas | C3 recovery to liquids % | CH4 lost to liquids % |
|---|---|---|---|---|---|---|
| C1 | 0.7360898 | 0.7360898 | 84.8331 | 12.1227 | 60.9914 | 13.5246 |
| C3 | 0 (Σ zK = 0.87220 < 1, all liquid) | 0 | n/a | n/a | 100 | 100 |
| C1+C2 | 0.7360898, 0.8761444 | 0.6449209 | 90.7521 | 6.65042 | 80.9678 | 18.9487 |
| C1+C3 | 0.7360898, 0.1078642 | 0.0793977 | 99.3573 | 0.27169 | 99.9038 | 89.0754 |
| C2+C3 | 0.6034506, 0.5078816 | 0.3064815 | 99.2752 | 0.25698 | 99.6486 | 57.8651 |
| C1+C2+C3 | 0.7360898, 0.8761444, 0.4775406 | 0.3079759 | 99.2485 | 0.25377 | 99.6510 | 57.6711 |

## 4.1 NH3 synthesis (Kp·P = 11)
Method: bisection on the log-equilibrium residual.
- **Extent ξ = 1.4691342 mol/h**
- Outlet: N2 = 0.3654329, H2 = 0.7962987, NH3 = 1.6691342, total = 2.8308658 mol/h
- y: N2 = 0.1290887, H2 = 0.2812916, NH3 = 0.5896197
- N2 conversion = 66.7788 %

## 4.2a C2H6 ⇌ C2H4 + H2, 1100 K, 1 atm
- ΔH_r: 34290 (800 K), 34485 (1000 K) cal/mol, slope 0.975 cal/(mol K), giving ΔH_r(1100) = 34582.5
- ΔG_r: 8570 (800 K), 2119 (1000 K) cal/mol
- K(1000) = 0.34427236
- **van 't Hoff with linear ΔH**, integrated analytically and by Simpson (they agree): ln(K1100/K1000) = 1.57975258, so **K(1100) = 1.6710136**
  - **conversion = 0.7909553**; y_C2H6 = 0.1167225, y_C2H4 = y_H2 = 0.4416388; total moles = 1.7909553
- **Linear extrapolation of ΔG**: ΔG_r(1100) = −1106.5 cal/mol, so **K = 1.6589637**
  - conversion = 0.7898820; y_C2H6 = 0.1173921, y_C2H4 = y_H2 = 0.4413040
- For reference, van 't Hoff with constant ΔH(1000) gives K = 1.6674092.

## 4.2b Two reactions, 1367 K, 1 atm, K1 = 37.6, K2 = 0.769
Method: nested bisection, cross-checked with damped Newton.
- **ξ1 = 0.99292022, ξ2 = 0.55471639**, total = 2.5476366 mol
- Moles: C2H6 = 0.0070798, C2H4 = 0.4382038, H2 = 1.5476366, C2H2 = 0.5547164
- **y: C2H6 = 0.0027790, C2H4 = 0.1720041, H2 = 0.6074793, C2H2 = 0.2177376**

## 5.1 Column train (exact Cramer's rule in rationals)
- **D1 = 375, B1 = 250, D2 = 125, B2 = 250, D = 625, B = 375 mol/h** (all exact)
- D composition (xylene/styrene/toluene/benzene): 0.114 / 0.120 / 0.492 / 0.274
- B composition: 0.210 / 0.466667 / 0.246667 / 0.076667

## 5.2 Toray process (successive substitution, 40 iterations to 1e-13; closed-form linear solution agrees)

| stream | toluene | benzene | xylene | total |
|---|---|---|---|---|
| 1 | 100 | 0 | 0 | 100 |
| 2 | 171.66854 | 0.25017 | 0.04983 | 171.96855 |
| R (reaction change) | −99.56776 | +49.78388 | +49.78388 | 0 |
| 3 | 72.10079 | 50.03405 | 49.83371 | 171.96855 |
| 4 | 0.07210 | 49.78388 | 0 | 49.85598 |
| 5 | 72.02869 | 0.25017 | 49.83371 | 122.11257 |
| 6 | 0.36014 | 0 | 49.78388 | 50.14402 |
| 7 (recycle) | 71.66854 | 0.25017 | 0.04983 | 71.96855 |

- Xylene product = 49.783878 mol/h. **Xylene / fresh toluene = 0.49783878** (49.7839 %)
- Toluene converted into xylene stoichiometrically (2·X6) = 99.5678 % of the fresh toluene
- **Overall toluene conversion = 99.567756 %**
- Benzene product = 49.783878 mol/h
