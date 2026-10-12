# Independent verification — variant 1 (rows "1 и 2")

Scripts (run with `python3 <script>` from this folder): `v_m1.py` (topic 1), `v_m2.py` (topic 2),
`v_m3.py` (topic 3), `v_m5.py` (topic 4, chemical equilibrium), `v_m6.py` (topic 5, material balances).
Constants: R = 8.314462618 J/(mol·K), 1 atm = 101325 Pa, 1 psi = 6894.757 Pa, T(°R) = 1.8·T(K), 1 cal = 4.184 J.

## 1.1 Mean heat capacity, linear polynomial (16 points)

| Quantity | Value |
|---|---|
| b0 (intercept) | 34.40799 |
| b1 (slope, per K) | 0.1369886 |
| R² | 0.977251 |
| SSE | 1119.073 |
| ⟨C⟩ 50→1300 K, integral of polynomial | 126.8753 |
| ⟨C⟩ 50→1300 K, trapezoid on table | 128.8316 |
| Difference (poly − trapz) | −1.9563 (−1.519 %) |

Method: QR least squares (not polyfit); the integral by `scipy.integrate.quad`; the trapezoid rule written out by hand.
For reference only: degree 2 to 5 polynomials give ⟨C⟩ = 128.87 / 128.92 / 128.80 / 128.87. The linear model's lack of fit is what causes the ~1.5 % gap.
Ambiguity: the table header says кДж/кг·К, but the values are typical of propane in J/(mol·K). The units do not change any number.

## 1.2 Stripping column y = a·(ln(x/b))^(−2/3)

| Model | Parameters | R² | SSE |
|---|---|---|---|
| a·(ln(x/b))^(−2/3) | a = 0.126391, b = 0.214441 | 0.935513 | 5.6998e−3 |
| a·x^(−n) | a = 0.053228, n = 1.388607 | 0.976010 | 2.1204e−3 |
| a·e^(−kx) + c | a = 1.385520, k = 5.952818, c = 0.054127 | 0.980694 | 1.7064e−3 |

Method: profile least squares (a is linear for fixed b). A 200 001-point scan of b in (0, 0.263) was then refined by bounded `least_squares`.
Ambiguity: the model needs x > b, so 0 < b < 0.263. The fit is unweighted and done on y, not on a linearised form.

## 1.3 Arrhenius (T = t + 273.15)

| Fit | Ea, J/mol | A, 1/s | R² |
|---|---|---|---|
| (a) linear regression of ln k on 1/T | 27 483.57 | 480.9608 | 0.978785 (on ln k); 0.932893 (on k) |
| (b) nonlinear LSQ on k (Levenberg–Marquardt, params lnA, Ea) | 39 895.39 | 3 971.236 | 0.974268 (on k), SSE = 1.48962 |

Ambiguity: the two criteria minimise different errors and so give quite different Ea. When comparing R², check which variable it was computed on.

## 1.4 Acetone viscosity, polynomials in T (K), n = 12

| Degree | Coefficients b0, b1, … | R² | SSE | adj R² |
|---|---|---|---|---|
| 1 | 1.038888, −2.391038e−3 | 0.924973 | 9.83096e−3 | 0.917471 |
| 2 | 2.635241, −1.260060e−2, 1.602804e−5 | 0.995227 | 6.25413e−4 | 0.994166 |
| 3 | 6.163025, −4.656951e−2, 1.237971e−4, −1.126502e−7 | 0.999727 | 3.57374e−5 | 0.999625 |

Method: QR least squares in the scaled variable s = (T − 300)/100, then converted exactly back to raw-T coefficients.

## 2.1 Methane, 40 atm, 350 K

| EOS | v, L/mol | Z |
|---|---|---|
| Ideal gas | 0.718002 | 1 |
| RK | 0.691484 | 0.963067 |
| SRK | 0.696172 | 0.969596 |

Method: Newton iteration on P(v) = RT/(v−b) − a/(v(v+b)) starting from the ideal-gas volume, cross-checked with `brentq`. T > Tc, so there is only one real root.
RK: a = 0.172221 Pa·m⁶/mol², b = 2.98472e−5 m³/mol. SRK: a = 0.158874 Pa·m⁶/mol².

## 2.2 25 % NH3 + N2:H2 = 1:3 (y = 0.25 / 0.1875 / 0.5625), 250 atm, 520 K

| EOS | v, L/mol | Z |
|---|---|---|
| Ideal gas | 0.170679 | 1 |
| RK | 0.182069 | 1.066734 |
| SRK | 0.183407 | 1.074570 |

Mixing: a = (Σ yᵢ√aᵢ)² (identical to the double sum with √(aᵢaⱼ)), b = Σ yᵢbᵢ.
Mixture RK: a_m = 0.0615399, b_m = 2.18714e−5. SRK: a_m = 0.0539855.
Z > 1 (repulsion dominates, mostly from H2), so the gas is not ideal (deviation about 7 %). Ambiguity: H2 uses the given ω = −0.22 with no quantum correction.

## 3.1 Bubble and dew T, 14 atm (205.74 psia), CH4/C2H6/C3H8/n-C4 = 0.20/0.25/0.35/0.20

| Quantity | Value |
|---|---|
| T bubble (Σ zK = 1) | −58.04 °C (215.109 K) |
| T dew (Σ z/K = 1) | 44.82 °C (317.971 K) |

Method: `brentq` on ln Σ zK and ln Σ z/K. Propane uses form (2) (D/P); the others use form (1) (D/P²).

## 3.2 Separator train, base case (basis 1 mol feed)

| | C1 x | C1 y | C2 x | C2 y | C3 x | C3 y |
|---|---|---|---|---|---|---|
| CH4 | 0.370059 | 0.848331 | 0.429626 | 0.907521 | 0.829861 | 0.992485 |
| C2H6 | 0.051806 | 0.030442 | 0.062040 | 0.025975 | 0.045168 | 0.004977 |
| C3H8 | 0.516824 | 0.118511 | 0.490005 | 0.065995 | 0.124000 | 0.002534 |
| i-C4 | 0.020351 | 0.001480 | 0.009400 | 0.000360 | 0.000687 | 0.000003 |
| n-C4 | 0.015619 | 0.000731 | 0.005074 | 0.000117 | 0.000223 | 4.27e−7 |
| n-C5 | 0.025342 | 0.000505 | 0.003854 | 0.000032 | 0.000061 | 2.6e−8 |
| Vapour fraction e | 0.736090 | | 0.876144 | | 0.477541 | |
| Feed to separator, mol | 1.000000 | | 0.736090 | | 0.644921 | |

Final gas from C3 = **0.307976 mol per mol feed**. C3+ in that gas = **0.2538 mol %** (CH4 99.2485 %).
Method: Rachford–Rice solved by bisection, with the single-phase checks Σ zK ≤ 1 (all liquid) and Σ z/K ≤ 1 (all vapour).

T1 sweep (C2, C3 at base conditions):

| T1, °C | 0 | 7 | 10 | 20 | 30 | 40.8 | 55 | 60 | 80 |
|---|---|---|---|---|---|---|---|---|---|
| final gas, mol | 0.315345 | 0.327066 | 0.324600 | 0.294594 | 0.301117 | 0.307976 | 0.311135 | 0.310753 | 0.306700 |
| e1 | 0.414490 | 0.483154 | 0.509332 | 0.588143 | 0.660160 | 0.736090 | 0.837259 | 0.872665 | 0.990280 |

- Global maximum (1 °C grid): T1 = 7 °C, gas = 0.327066. On a 0.01 °C grid: T1 = 6.76 °C, gas = 0.327080.
- Maximum for T1 ≥ 30 °C (1 °C grid): T1 = 55 °C, gas = 0.311135. On a 0.01 °C grid: 54.75 °C, gas = 0.311136.
- Feed at 9.8 MPa has a bubble T of −22.33 °C and a dew T of 82.34 °C:
  - Below −22.33 °C, C1 is all liquid and the final gas is 0.
  - Above 82.34 °C, C1 is all vapour and the final gas is constant at 0.306481.
  - For T1 in [−22.3, 18.6] °C the C1 gas is above its own dew point at C2 conditions, so C2 is single-phase vapour (e2 = 1). This is what causes the kink near 18–20 °C and the local minimum around 20 °C.

Ambiguity: "C4" and "C5" in the p.6 table are taken as n-butane and n-pentane, using the n-C4 and n-C5 constants. The extrapolated K-correlation (for example methane K at −40.8 °C, 8.7 MPa = 1.196) is used as given.

## 4.1 NH3 synthesis, Kp = 0.05 atm⁻¹, P = 220 atm (Kp·P = 11)

| | In, mol/h | Out, mol/h | y |
|---|---|---|---|
| N2 | 1.1 | 0.365433 | 0.129089 |
| H2 | 3.0 | 0.796299 | 0.281292 |
| NH3 | 0.2 | 1.669134 | 0.589620 |
| Total | 4.3 | 2.830866 | 1 |

Extent = 1.469134 mol/h (for NH3 formed). Solved by `brentq` on the extent. T = 589 K does not enter, because Kp is given.

## 4.2a C2H6 ⇌ C2H4 + H2, 1100 K, 1 atm (data only up to 1000 K)

At 1000 K: ΔG° = 8.8659 kJ/mol, K = 0.344272, ΔH° = 144.285 kJ/mol.

| Method of extrapolating to 1100 K | K(1100) | X (conversion) | y C2H6 | y C2H4 = y H2 |
|---|---|---|---|---|
| van 't Hoff with constant ΔH(1000) | 1.667409 | 0.790635 | 0.116922 | 0.441539 |
| Linear extrapolation of ΔG° (800 and 1000 K) | 1.658964 | 0.789882 | 0.117392 | 0.441304 |
| van 't Hoff with constant ΔCp (800 to 1000 K) | 1.671014 | 0.790955 | 0.116722 | 0.441639 |
| van 't Hoff with ΔH quadratic (600 to 1000 K) | 1.668374 | 0.790721 | 0.116868 | 0.441566 |
| LSQ fit ΔG = a + bT + cT lnT (5 points) | 1.711708 | 0.794499 | 0.114517 | 0.442741 |

Conversion X = √(K/(K + P)). Moles out: C2H6 = 1 − X, C2H4 = H2 = X, total = 1 + X.
The estimates agree within about 3 % in K: **K(1100) ≈ 1.66–1.71, X ≈ 0.79**.

## 4.2b Two reactions, 1367 K, 1 atm, K1 = 37.6, K2 = 0.769, 1 mol C2H6

| | n, mol | y |
|---|---|---|
| C2H6 | 0.007080 | 0.002779 |
| C2H4 | 0.438204 | 0.172004 |
| H2 | 1.547637 | 0.607479 |
| C2H2 | 0.554716 | 0.217738 |
| Total | 2.547637 | 1 |

Extents: ξ1 = 0.992920, ξ2 = 0.554716. Solved by nested 1-D `brentq` (an outer solve on ξ1 and an inner solve on ξ2). Both K are reproduced exactly.

## 5.1 Column train, F = 1000 mol/h

| Stream | Total | Xylene | Styrene | Toluene | Benzene |
|---|---|---|---|---|---|
| F | 1000 | 150 (15 %) | 250 (25 %) | 400 (40 %) | 200 (20 %) |
| D | 625 | 71.25 (11.40 %) | 75.00 (12.00 %) | 307.50 (49.20 %) | 171.25 (27.40 %) |
| B | 375 | 78.75 (21.00 %) | 175.00 (46.667 %) | 92.50 (24.667 %) | 28.75 (7.667 %) |
| D1 | 375 | 26.25 | 15.00 | 202.50 | 131.25 |
| B1 | 250 | 45.00 | 60.00 | 105.00 | 40.00 |
| D2 | 125 | 18.75 | 12.50 | 67.50 | 26.25 |
| B2 | 250 | 60.00 | 162.50 | 25.00 | 2.50 |

Method: exact rational Gauss–Jordan elimination on the 4 component balances, cross-checked with `lstsq`. The flows come out as exact integers.

## 5.2 Toray process (successive substitution on the recycle, converged in 40 iterations to 1e−13)

| Stream | Toluene | Benzene | Xylene | Total |
|---|---|---|---|---|
| 1 (fresh) | 100.00000 | 0 | 0 | 100.00000 |
| 2 (reactor in) | 171.66854 | 0.25017 | 0.04983 | 171.96855 |
| R (change in reactor) | −99.56776 | +49.78388 | +49.78388 | 0 |
| 3 (reactor out) | 72.10079 | 50.03405 | 49.83371 | 171.96855 |
| 4 (benzene) | 0.07210 | 49.78388 | 0 | 49.85598 |
| 5 | 72.02869 | 0.25017 | 49.83371 | 122.11257 |
| 6 (xylene) | 0.36014 | 0 | 49.78388 | 50.14402 |
| 7 (recycle) | 71.66854 | 0.25017 | 0.04983 | 71.96855 |

| Quantity | Value |
|---|---|
| Xylene product / fresh toluene (X6/T1) | 49.7839 % (0.497839 mol/mol) |
| Toluene consumed to make xylene, 2·X6/T1 | 99.5678 % |
| Overall toluene conversion, 1 − (T4 + T6)/T1 | 99.5678 % |
| Purity of stream 4 (benzene) | 99.8554 % |
| Purity of stream 6 (xylene) | 99.2818 % |

Ambiguities:
- The "R" column in the results table is not defined. It is shown here as the reactor's generation term; the recycle itself is stream 7.
- "Conversion of toluene into xylene" can be read two ways. Read as yield (mol xylene per mol fresh toluene) it is 0.4978. Read stoichiometrically (2 mol toluene per mol xylene) it is 99.57 %, which equals the overall toluene conversion.
