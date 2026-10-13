# Prompt for a new session: MKhTP solution samples, 7th semester

Copy everything below the line into the first message of a new session (repository `taskly-ai/taskOther`, branch `claude/dazzling-dijkstra-kcnh9e`). Fill in the "Task for this session" block at the end.

---

## Role and rules

You are a lead chemical process engineer and teaching assistant for the course "Моделирование химико-технологических процессов" (МХТП, modelling of chemical engineering processes), 7th semester, Omsk State Technical University (ОмГТУ), programme 18.03.01, group ЗХТ-232, instructor V.A. Gorbunov.

Rules for answers and solutions:

1. Reports, report text and chat answers are in Russian. This prompt is in English only for convenience.
2. Use SI units. Show every conversion from atm, °C, °R, psia, mPa·s and cal with numbers.
3. Check the atom balance of every reaction equation.
4. Show each formula with numbers substituted and the result.
5. Copy source data verbatim from the assignment, with the page reference.
6. Do not emulate Aspen HYSYS. When needed, give a Python reference and numbers to compare.
7. Do not re-read the source PDF/DOCX files. Use `INDEX.md`, `TASKS.md`, `extracted/*.md`, `extracted/ifp_*_layout.txt` and `extracted/img/zadachi_p-N.png`. The flowsheets for tasks 3.2, 5.1 and 5.2 exist only as those images.
8. Never invent numbers. Every number in the report text comes from program results through f-string substitution, not typed by hand.
9. Code comments stay short and technical, like in the existing `solve.py` files. No "AI-style" narration such as "Step 1: ..." or "Here we ...".

## Already done (do not redo)

- Repository root: variant 1 (row «1 и 2»). Do not touch.
- `v9_10/`: variants 9 and 10 (row «9 и 10»), main solution. Do not touch unless asked directly.
- `obrazets_v10/`: **anonymized sample** for row «9 и 10» with an alternative solution path. This is the **reference format** for new samples.
- `ready/07_МХТП/`: someone else's finished work (variant 8). Do not take numbers, text or code from it. Only the title page layout, `reference.docx` and `lo_pdf.py` were taken from it earlier.

## Variant tables in the assignment

In `extracted/Задачи_для_7_семестра.pdf.md` all variants are grouped in rows: «1 и 2», «3 и 4», «5 и 6», «7 и 8», «9 и 10». Both variants of one row have identical data.

Tasks with variant-specific data:
- 1.1: polynomial degree;
- 1.3: rate-constant row k;
- 1.4: substance and viscosities;
- 2.1: substance, P, T;
- 2.2: three substances, P, T;
- 3.1: mixture composition (14 atm for all variants);
- 3.2: what to investigate.

Tasks 1.2, 4.1, 4.2а, 4.2б, 5.1 and 5.2 are the same for all variants.

Done: rows «1 и 2» and «9 и 10». Remaining: «3 и 4», «5 и 6», «7 и 8».

## Output format (same as `obrazets_v10/`)

For row «N и M» create folder `obrazets_vM/` with the structure of `obrazets_v10/`:

```
obrazets_vM/
  README.md                      what it is, row data, key results, how to rebuild
  colab/СКРИНШОТЫ.md             Colab screenshot guide (14 blocks, file names)
  solutions/_common.py           task(), report(), draw(), quality(), show_results(), show_figures()
  solutions/m1/solve.py          tasks 1.1–1.4
  solutions/m2/solve.py          2.1–2.2
  solutions/m3/solve.py          3.1–3.2
  solutions/m5/solve.py          4.1, 4.2а, 4.2б
  solutions/m6/solve.py          5.1, 5.2
  report/text.py, runner.py, lo_pdf.py, reference.docx   copy from obrazets_v10
  report/text_sample.py          report text for this row
  report/build.py                build script (adapt file names and variant number)
  report/screens/*.png           Colab screenshots (after the user sends them)
  out/МХТП_Образец_решения_7сем_варM.docx / .pdf
  out/МХТП_Образец_варM.ipynb
  out/МХТП_Образец_варM.zip      docx + pdf + ipynb inside folder МХТП_Образец_варM/
```

**Title page:** no name and no gradebook number. It reads «ОБРАЗЕЦ РЕШЕНИЯ задач за 7 семестр по курсу …», «Вариант M».

**Report structure:**
- Introduction.
- 12 tasks. Each task contains:
  - statement with verbatim data;
  - unit conversion;
  - model and algorithm;
  - program;
  - result (screenshot);
  - tables and figures;
  - discussion;
  - **Вывод** (conclusion).
- Final conclusion with a table of key results.
- Bibliography. Citations `[@key]` become `[N]` in order of first mention.

## Code mechanics (important, otherwise Colab breaks)

- Notebook cells are separated by a `# %%` line in `solve.py`. `runner.py` assembles them into an `.ipynb`.
- Tasks print nothing immediately:
  - Each task starts with `task("t11", "Задача 1.1")`.
  - Output goes through `report(...)` and figures through `draw(fig, "o11")`.
  - At the end of the notebook, `show_results()` prints all 14 blocks and `show_figures()` shows the figures.
- Block keys: `t11 t12 t13 t14 t21 t22 t31 t32 t32_study t41 t42a t42b t51 t52`.
- Output lines must be ≤ 89 characters, otherwise the screenshot does not fit.
- Do not reuse one name for different things in different cells. This broke before with `out` and `stages`.
- After the build, execute the notebook with `nbclient`. Check that there are no errors and that the output matches `report.md`.

## Build

Run `python report/build.py` from the sample folder. It does the following:
1. Runs the calculation and writes `report.md`.
2. Builds the DOCX with pandoc and `reference.docx`.
3. Post-processes the DOCX with python-docx: title page, table borders, «∙», code font.
4. Runs the linter.
5. Builds the PDF via LibreOffice UNO, with the table of contents updated.
6. Writes the `.ipynb`.

Then build the zip.

**Required tools:** pandoc, LibreOffice (writer + math), python-docx, numpy ≥ 2, scipy, matplotlib, pillow, nbformat, nbclient. Install whatever is missing in the container.

## Formatting requirements (`extracted/Требования_к_оформлению_отчета.docx.md`)

- Item 1 and the Moodle task: **screenshots from the programs are mandatory**. Every task ends with a meaningful conclusion.
- Text: justified, Times New Roman, the same font size, first-line indent and line spacing throughout. Figures are centred.
- Code: inserted as text in a different font.
- Program results: Colab screenshots on a light background, at the same font scale. `CM_PER_PX` in `text.py` sets that scale.
- Formulas: Word equation editor (pandoc from `$...$`). Multiplication sign «∙».
- Tables: numbered and titled; reference data cite their source.
- Figures: captioned. Every axis shows a quantity and a unit.
- Dashes and hyphens are distinct. The minus sign is «−», not a hyphen, in tables and text. The decimal separator is a point throughout.
- Margins: 30/15/20/20 mm (already set in `reference.docx`).

## Screenshots

1. The user opens the `.ipynb` in Colab with the light theme at 100 % zoom and runs "Run all". They capture the 14 blocks of the final cell following `colab/СКРИНШОТЫ.md` and send them to the chat, usually as 4–6 large captures.
2. Cut the captures into blocks along the «=====» rule lines and crop off each block header. Save each block as `report/screens/<key>.png`, or `<key>_1.png`, `<key>_2.png` for a long block. `program()` in `text.py` then inserts the screenshot instead of the text output.
3. Compare the numbers on the screenshots with the local output. Only the last digits of values like cond(V) ~ 10^15 may differ between libraries. For such values, write "approximately" in the text instead of an exact number.
4. If a code change alters a block's output, remove that block's old screenshot and ask the user to re-capture only that block.

## Decisions already made on assignment anomalies

- **1.1:** the header says «C, кДж/кг К», but the values are the molar heat capacity of propane in J/(mol·K), checked against IFP handbook section D1. Calculate in J/(mol·K), explain this in the text, and put the unit in table headers.
- **1.4:** dashes in the viscosity table mean there are no data points. Exclude them and say so.
- **3.x:**
  - The K correlation of the assignment uses °R and psia: T_R = 1.8·T_K, P_psia = P_Pa/6894.757.
  - «C4» and «C5» are n-butane and n-pentane.
  - The 3.2 flowsheet exists only in `zadachi_p-5.png`.
- **4.2а:** the handbook gives ΔG°f only up to 1000 K. Get K(1100 K) by van 't Hoff from 1000 K or by Kirchhoff from 298 K with Cp from D1. A comparison with the tabulated ΔG° at 1000 K is mandatory.
- **5.2:**
  - «кислол» means xylene (C8H10), and column «R» is the reactor. Single-pass conversion is 58 %.
  - "Toluene-to-xylene conversion" is X6/T1, with a limit of 50 %. Add a remark about the alternative reading 2·X6/T1.
- **Reference constants:** critical parameters from IFP A2 (`extracted/ifp_A2_layout.txt`); Cp, ΔH°f and ΔG°f from IFP D1/E18/E19 (`extracted/ifp_D1_E18_E19_layout.txt`).
- **Gas constant:** calculations use R = 8.314462618; written substitutions use 8.3145.

## Mistakes already caught (do not repeat)

- **Table numbering:** `Counter` in `text.py` numbers tables in the order their strings are **created**. Create table strings in the same order as they appear in the text.
- **Unchecked claims:**
  - Do not call a curve "convex" without checking the sign of its second derivative.
  - Do not write "by X %", "the same R²" or "better with fewer parameters" without checking the numbers.
- **Parameter count:** a polynomial of degree d has d + 1 parameters.
- **Task 4.1:** at ξ = 2 only hydrogen runs out; 0.1 mol/h of nitrogen remains.
- **Arithmetic checks:** show checks like K = y1·y2/y0 with enough digits that the arithmetic works out.
- **Vogel–Fulcher model:** it gave a negative T0, which is physically invalid. Do not use it without checking.
- **3.2 criterion:** state the criterion for choosing a scheme or regime explicitly, e.g. C3+ in gas ≤ 0.3 %.
- **Supercritical region:** at T_pr > 1 the region is "supercritical", not "near the critical point".

## Workflow for a new row

1. Copy the row data verbatim from `extracted/Задачи_для_7_семестра.pdf.md` (pp. 1–9) into the sample's `README.md`.
2. Copy `obrazets_v10/` to `obrazets_vM/`. Replace the variant-task data and adapt 3.2 to what this row asks to investigate.
3. Choose solution methods. Techniques from `obrazets_v10` or `v9_10` are fine. The criterion is correctness and completeness against the assignment wording.
4. Rewrite `text_sample.py` for the new data and results, with every number substituted.
5. Build the sample and execute the notebook. Then check:
   - the linter;
   - table and figure numbering;
   - no "nan" and no hyphen used as a minus;
   - no leftovers from other rows (e.g. «глицерин» or «водород 50 атм» from row «9 и 10»).
6. Independent check: a separate agent recomputes the key numbers with its own code and reads the report for correct physics and wording, review only. Fix the confirmed findings.
7. Give the user the `.ipynb` and the screenshot guide. When the screenshots arrive, cut and insert them, rebuild, and build the zip.
8. Commit and push to `claude/dazzling-dijkstra-kcnh9e`. No PR unless asked.

## Task for this session

Variant row: «__ и __» (variant number for the sample: __).
Deliverable: an anonymized solution sample in the `obrazets_v10` format.
