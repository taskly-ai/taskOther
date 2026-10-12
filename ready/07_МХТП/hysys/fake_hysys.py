"""Эмулятор подмножества COM-интерфейса Aspen HYSYS для `hysys_auto.py selftest`.

Нужен только чтобы проверить логику скрипта без HYSYS. Сепараторы считаются нашим
флешем Пенга–Робинсона (07_МХТП/src/pr_flash.py), равновесный реактор — по Kp
(идеальный газ), реактор Гиббса — по K = 1,659. Это НЕ HYSYS: числа эмулятора
совпадают с ориентиром PR и отчётом по построению.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


class _Var:
    def __init__(self, unit_to_internal=None):
        self.v = None
        self.k = unit_to_internal or {}

    def SetValue(self, value, unit=""):
        self.v = float(value) * self.k.get(unit, 1.0)

    def GetValue(self, unit=""):
        if self.v is None:
            return -32767.0
        return self.v / self.k.get(unit, 1.0)


class _Arr:
    def __init__(self):
        self.Values = None

    def GetValues(self, unit=""):
        return tuple(self.Values) if self.Values is not None else ()


class Stream:
    def __init__(self, name):
        self.Name = name
        self.Temperature = _Var()
        self.Pressure = _Var()
        self.MolarFlow = _Var({"kgmole/h": 1 / 3600.0})  # внутренние единицы kgmole/s
        self.VapourFraction = _Var()
        self.ComponentMolarFraction = _Arr()
        self.spec_T = self.spec_P = None


class Energy:
    def __init__(self, name):
        self.Name = name


class _Coll(list):
    def __init__(self, factory=None):
        super().__init__()
        self.factory = factory

    def Add(self, *a):
        obj = self.factory(*a) if self.factory else a[0]
        self.append(obj)
        return obj

    def Item(self, key):
        if isinstance(key, int):
            return self[key]
        for o in self:
            if o.Name == key:
                return o
        raise KeyError(key)

    @property
    def Count(self):
        return len(self)

    @property
    def Names(self):
        return tuple(o if isinstance(o, str) else o.Name for o in self)


class Op:
    def __init__(self, name, typ):
        known = {"flashtank", "coolerop", "eqmreactorop", "gibbsreactorop"}
        if typ not in known:
            raise ValueError(f"неизвестный тип {typ}")
        self.Name, self.TypeName = name, typ
        self.FeedStreams = _Coll()
        self.VapourProduct = self.LiquidProduct = None
        self.FeedStream = self.ProductStream = self.EnergyStream = None
        self.ReactionSet = None


class FluidPackage:
    def __init__(self, name):
        self.Name = name
        self.PropertyPackageName = ""
        self.Components = _Coll(lambda n: n)
        self.ReactionSets = _Coll()


class BasisManager:
    def __init__(self):
        self.FluidPackages = _Coll(FluidPackage)

    def StartBasisChange(self):
        pass

    def EndBasisChange(self):
        pass


class Flowsheet:
    def __init__(self):
        self.MaterialStreams = _Coll(Stream)
        self.EnergyStreams = _Coll(Energy)
        self.Operations = _Coll(Op)
        self.FluidPackage = None


class Solver:
    def __init__(self, case):
        self._case, self._can = case, True
        self.IsSolving = False

    @property
    def CanSolve(self):
        return self._can

    @CanSolve.setter
    def CanSolve(self, v):
        self._can = bool(v)
        if v:
            self._case._solve()


class Case:
    def __init__(self):
        self.BasisManager = BasisManager()
        self.Flowsheet = Flowsheet()
        self.Solver = Solver(self)
        self.Visible = False

    def SaveAs(self, path):
        Path(path).write_text("эмулятор HYSYS: файл-заглушка\n", encoding="utf-8")

    # --- «расчёт»
    def _solve(self):
        fs = self.Flowsheet
        if fs.FluidPackage is None:
            return
        names = list(fs.FluidPackage.Components)
        for _ in range(len(fs.Operations) + 1):  # проходы до сходимости, как решатель HYSYS
            for op in fs.Operations:
                if op.TypeName == "flashtank":
                    self._flash(op, names)
                elif op.TypeName == "coolerop":
                    f, p = op.FeedStream, op.ProductStream
                    p.MolarFlow.v = f.MolarFlow.v
                    p.ComponentMolarFraction.Values = f.ComponentMolarFraction.Values
                elif op.TypeName == "eqmreactorop":
                    self._eqm(op, names)
                elif op.TypeName == "gibbsreactorop":
                    self._gibbs(op, names)

    def _flash(self, op, names):
        import pr_flash as prf
        f = op.FeedStreams[0]
        if f.MolarFlow.v is None or f.ComponentMolarFraction.Values is None or f.Temperature.v is None:
            return
        z = np.array(f.ComponentMolarFraction.Values, float)
        r = prf.pr_flash(z, f.Temperature.v + 273.15, f.Pressure.v * 1e3)
        F = f.MolarFlow.v
        if r["state"] == "одна фаза":
            e, y, x = 1.0, z, z
        else:
            e, y, x = r["e"], r["y"], r["x"]
        f.VapourFraction.v = e
        for s, frac, comp in ((op.VapourProduct, e, y), (op.LiquidProduct, 1 - e, x)):
            s.MolarFlow.v = F * frac
            s.ComponentMolarFraction.Values = tuple(comp)
            s.Temperature.v, s.Pressure.v = f.Temperature.v, f.Pressure.v
            s.VapourFraction.v = 1.0 if s is op.VapourProduct else 0.0

    def _eqm(self, op, names):
        f, v, l = op.FeedStreams[0], op.VapourProduct, op.LiquidProduct
        n0 = np.array(f.ComponentMolarFraction.Values) * f.MolarFlow.v * 3600
        iN, iH, iA = names.index("Nitrogen"), names.index("Hydrogen"), names.index("Ammonia")
        P = f.Pressure.v / 101.325

        def g(x):
            n = n0.copy()
            n[iN] -= 0.5 * x
            n[iH] -= 1.5 * x
            n[iA] += x
            y = n / n.sum()
            return y[iA] / (y[iN] ** 0.5 * y[iH] ** 1.5) / P - 0.05
        x = brentq(g, 0, min(2 * n0[iN], n0[iH] / 1.5) * (1 - 1e-12))
        n = n0.copy()
        n[iN] -= 0.5 * x
        n[iH] -= 1.5 * x
        n[iA] += x
        v.MolarFlow.v = n.sum() / 3600
        v.ComponentMolarFraction.Values = tuple(n / n.sum())
        l.MolarFlow.v = 0.0
        l.ComponentMolarFraction.Values = tuple(n / n.sum())

    def _gibbs(self, op, names):
        f, v, l = op.FeedStreams[0], op.VapourProduct, op.LiquidProduct
        F0 = f.MolarFlow.v * 3600
        K = 1.659
        x = (K / (1 + K)) ** 0.5
        n = np.zeros(len(names))
        n[names.index("Ethane")] = F0 * (1 - x)
        n[names.index("Ethylene")] = F0 * x
        n[names.index("Hydrogen")] = F0 * x
        v.MolarFlow.v = n.sum() / 3600
        v.ComponentMolarFraction.Values = tuple(n / n.sum())
        l.MolarFlow.v = 0.0


class SimulationCases(_Coll):
    def __init__(self):
        super().__init__(lambda *a: Case())


class Application:
    def __init__(self):
        self.SimulationCases = SimulationCases()
        self.Visible = False
        self.Version = "эмулятор"
