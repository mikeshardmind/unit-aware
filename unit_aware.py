#   Copyright 2023-present Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from __future__ import annotations

import operator
from fractions import Fraction
from typing import Any, NamedTuple, Protocol, Self

__all__ = ["SIUnitAwareValue", "UnitAwareValue", "Units", "UnitsVector"]

"""
s	second	time
m	metre	length
kg	kilogram	mass
A	ampere	electric current
K	kelvin	thermodynamic temperature
mol	mole	amount of substance
cd	candela	luminous intensity
"""

type _VTs = int | float | Fraction
type UnitsLike = tuple[_VTs, _VTs, _VTs, _VTs, _VTs, _VTs, _VTs]


class UnitsVector(NamedTuple):
    time: _VTs = 0
    length: _VTs = 0
    mass: _VTs = 0
    current: _VTs = 0
    temperature: _VTs = 0
    luminous_intensity: _VTs = 0
    amount_of_substance: _VTs = 0


class UnitsMeta(type):
    @property
    def scalar_value(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 0, 0)

    @property
    def acceleration(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 1, 0, 0, 0, 0, 0)

    @property
    def amount_of_substance(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 0, 1)

    @property
    def angular_momentum(cls: Any) -> UnitsVector:
        return UnitsVector(-1, 2, 1, 0, 0, 0, 0)

    @property
    def area(cls: Any) -> UnitsVector:
        return UnitsVector(0, 2, 0, 0, 0, 0, 0)

    @property
    def capacitance(cls: Any) -> UnitsVector:
        return UnitsVector(4, -2, -1, 2, 0, 0, 0)

    @property
    def charge(cls: Any) -> UnitsVector:
        return UnitsVector(1, 0, 0, 1, 0, 0, 0)

    @property
    def conductance(cls: Any) -> UnitsVector:
        return UnitsVector(3, -2, -1, 2, 0, 0, 0)

    @property
    def conductivity(cls: Any) -> UnitsVector:
        return UnitsVector(3, -3, -1, 2, 0, 0, 0)

    @property
    def current(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 0, 1, 0, 0, 0)

    @property
    def density(cls: Any) -> UnitsVector:
        return UnitsVector(0, -3, 1, 0, 0, 0, 0)

    @property
    def electric_field_strength(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 1, 1, -1, 0, 0, 0)

    @property
    def energy(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 2, 1, 0, 0, 0, 0)

    @property
    def entropy(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 2, 1, 0, -1, 0, 0)

    @property
    def force(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 1, 1, 0, 0, 0, 0)

    @property
    def frequency(cls: Any) -> UnitsVector:
        return UnitsVector(-1, 0, 0, 0, 0, 0, 0)

    @property
    def gravitation(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 3, -1, 0, 0, 0, 0)

    @property
    def illuminance(cls: Any) -> UnitsVector:
        return UnitsVector(0, -2, 0, 0, 0, 1, 0)

    @property
    def inductance(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 2, 1, -2, 0, 0, 0)

    @property
    def length(cls: Any) -> UnitsVector:
        return UnitsVector(0, 1, 0, 0, 0, 0, 0)

    @property
    def luminous_intensity(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 1, 0)

    @property
    def magnetic_flux(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 2, 1, -1, 0, 0, 0)

    @property
    def magnetic_flux_density(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 0, 1, -1, 0, 0, 0)

    @property
    def magnetic_permeability(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 1, 1, -2, 0, 0, 0)

    @property
    def mass(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 1, 0, 0, 0, 0)

    @property
    def molar_mass(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 1, 0, 0, 0, -1)

    @property
    def molar_volume(cls: Any) -> UnitsVector:
        return UnitsVector(0, 3, 0, 0, 0, 0, -1)

    @property
    def momentum(cls: Any) -> UnitsVector:
        return UnitsVector(-1, 1, 1, 0, 0, 0, 0)

    @property
    def permittivity(cls: Any) -> UnitsVector:
        return UnitsVector(4, -3, -1, 2, 0, 0, 0)

    @property
    def power(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 2, 1, 0, 0, 0, 0)

    @property
    def pressure(cls: Any) -> UnitsVector:
        return UnitsVector(-2, -1, 1, 0, 0, 0, 0)

    @property
    def resistance(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 2, 1, -2, 0, 0, 0)

    @property
    def resistivity(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 3, 1, -2, 0, 0, 0)

    @property
    def specific_heat_capacity(cls: Any) -> UnitsVector:
        return UnitsVector(-2, 2, 0, 0, -1, 0, 0)

    @property
    def temperature(cls: Any) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 1, 0, 0)

    @property
    def thermal_conductivity(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 1, 1, 0, -1, 0, 0)

    @property
    def time(cls: Any) -> UnitsVector:
        return UnitsVector(1, 0, 0, 0, 0, 0, 0)

    @property
    def velocity(cls: Any) -> UnitsVector:
        return UnitsVector(-1, 1, 0, 0, 0, 0, 0)

    @property
    def voltage(cls: Any) -> UnitsVector:
        return UnitsVector(-3, 2, 1, -1, 0, 0, 0)

    @property
    def volume(cls: Any) -> UnitsVector:
        return UnitsVector(0, 3, 0, 0, 0, 0, 0)

    @property
    def catalytic_activity(cls: Any) -> UnitsVector:
        return UnitsVector(-1, 0, 0, 0, 0, 0, 1)


class Units(metaclass=UnitsMeta): ...


class SupportsOps(Protocol):
    def __add__(self: Self, other: Self) -> Self: ...

    def __sub__(self: Self, other: Self) -> Self: ...

    def __mul__(self: Self, other: Self) -> Self: ...

    def __truediv__(self: Self, other: Self) -> Self: ...

    def __eq__(self: object, other: object) -> bool: ...

    def __hash__(self) -> int: ...


class UnitMismatch(Exception):
    def __init__(self: Self, *args: object) -> None:
        super().__init__("Can't add/subtract values with different units")


class UnitAwareValue[V: SupportsOps, U: UnitsLike]:
    __slots__ = ("_units", "_value")

    def __new__(cls, value: V, units: U, /) -> Self:
        obj = super().__new__(cls)
        obj._value, obj._units = value, units
        return obj

    @property
    def value(self) -> V:
        return self._value

    @property
    def units(self) -> U:
        return self._units

    def __repr__(self: Self) -> str:
        return f"UnitAwareValue(value={self.value!r}, units={self.units!r})"

    def __add__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)) and isinstance(other.units, type(self.units)):
            if self.units == other.units:
                return type(self)(self.value + other.value, self.units)
            raise UnitMismatch
        return NotImplemented

    def __sub__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)) and isinstance(other.units, type(self.units)):
            if self.units == other.units:
                return type(self)(self.value - other.value, self.units)
            raise UnitMismatch
        return NotImplemented

    def __mul__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)) and isinstance(other.units, type(self.units)):
            new_units = type(self.units)(*map(operator.add, self.units, other.units))
            return type(self)(self.value * other.value, new_units)
        return NotImplemented

    def __truediv__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)) and isinstance(other.units, type(self.units)):
            new_units = type(self.units)(*map(operator.sub, self.units, other.units))
            return type(self)(self.value / other.value, new_units)
        return NotImplemented

    def __eq__(self: Self, other: object) -> bool:
        if isinstance(other, type(self)) and isinstance(other.units, type(self.units)):
            return self.value == other.value and self.units == other.units
        return False

    def __hash__(self) -> int:
        return hash(("!%^", type(self), self.value, self.units))


SI_BASE_UNIT_LOOKUP_DICT: dict[UnitsVector, str] = {
    Units.time: "s",
    Units.length: "m",
    Units.mass: "kg",
    Units.current: "A",
    Units.temperature: "K",
    Units.amount_of_substance: "mol",
    Units.luminous_intensity: "cd",
}

SI_NAMED_DERIVED_UNIT_LOOKUP_DICT: dict[UnitsVector, str] = {
    Units.frequency: "Hz",
    Units.force: "N",
    Units.pressure: "Pa",
    Units.energy: "J",
    Units.power: "W",
    Units.charge: "C",
    Units.voltage: "V",
    Units.capacitance: "F",
    Units.resistance: "Ω",
    Units.conductance: "S",
    Units.magnetic_flux: "Wb",
    Units.magnetic_flux_density: "T",
    Units.inductance: "H",
    Units.illuminance: "lx",
    Units.catalytic_activity: "Kat",
}

SUPERSCRIPTS: dict[int, str] = {
    1: "\u00b9",
    2: "\u00b2",
    3: "\u00b3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079",
    0: "\u2070",
}


def format_unitsvector_as_si(vec: UnitsLike, /) -> str:
    if not isinstance(vec, UnitsVector):
        vec = UnitsVector(*vec)
    try:
        return SI_BASE_UNIT_LOOKUP_DICT[vec]
    except KeyError:
        try:
            return SI_NAMED_DERIVED_UNIT_LOOKUP_DICT[vec]
        except KeyError:
            pass

    this: list[str] = []
    per_that: list[str] = []

    for name in (
        "length",
        "mass",
        "time",
        "current",
        "temperature",
        "amount_of_substance",
        "luminous_intensity",
    ):
        val: int = getattr(vec, name, 0)
        if not val:
            continue

        arr = this
        if val < 0:
            arr = per_that
            val = abs(val)

        arr.append(SI_BASE_UNIT_LOOKUP_DICT[getattr(Units, name)])
        if val > 1:
            # just in case, but are we really having units like this?
            while val >= 10:
                n, val = divmod(val, 10)
                arr.append(SUPERSCRIPTS[n])
            arr.append(SUPERSCRIPTS[val])

    return "/".join(filter(None, ("".join(this), "".join(per_that))))


class SIUnitAwareValue[V: SupportsOps, U: UnitsLike](UnitAwareValue[V, U]):
    def __repr__(self: Self) -> str:
        si_repr = format_unitsvector_as_si(self.units)
        # done this way in case of dimensionless values
        return " ".join(filter(None, (f"{self.value}", si_repr)))
