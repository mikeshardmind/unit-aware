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
from typing import Generic, NamedTuple, Protocol, Self, TypeVar

"""
s	second	time
m	metre	length
kg	kilogram	mass
A	ampere	electric current
K	kelvin	thermodynamic temperature
mol	mole	amount of substance
cd	candela	luminous intensity
"""

class UnitsVector(NamedTuple):
    time: int = 0
    length: int = 0
    mass: int = 0
    current: int = 0
    temperature: int = 0
    luminous_intensity: int = 0
    amount_of_substance: int = 0

class Units:

    @classmethod
    @property
    def scalar_value(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def acceleration(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 1, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def amount_of_substance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 0, 1)

    @classmethod
    @property
    def angular_momentum(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-1, 2, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def area(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 2, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def capacitance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(4, -2, -1, 2, 0, 0, 0)

    @classmethod
    @property
    def charge(cls: type[Self]) -> UnitsVector:
        return UnitsVector(1, 0, 0, 1, 0, 0, 0)

    @classmethod
    @property
    def conductance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(3, -2, -1, 2, 0, 0, 0)

    @classmethod
    @property
    def conductivity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(3, -3, -1, 2, 0, 0, 0)

    @classmethod
    @property
    def current(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 0, 1, 0, 0, 0)

    @classmethod
    @property
    def density(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, -3, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def electric_field_strength(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 1, 1, -1, 0, 0, 0)

    @classmethod
    @property
    def energy(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 2, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def entropy(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 2, 1, 0, -1, 0, 0)

    @classmethod
    @property
    def force(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 1, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def frequency(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-1, 0, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def gravitation(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 3, -1, 0, 0, 0, 0)

    @classmethod
    @property
    def illuminance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, -2, 0, 0, 0, 1, 0)

    @classmethod
    @property
    def inductance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 2, 1, -2, 0, 0, 0)

    @classmethod
    @property
    def length(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 1, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def luminous_intensity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 0, 1, 0)

    @classmethod
    @property
    def magnetic_flux(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 2, 1, -1, 0, 0, 0)

    @classmethod
    @property
    def magnetic_flux_density(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 0, 1, -1, 0, 0, 0)

    @classmethod
    @property
    def magnetic_permeability(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 1, 1, -2, 0, 0, 0)

    @classmethod
    @property
    def mass(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def molar_mass(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 1, 0, 0, 0, -1)

    @classmethod
    @property
    def molar_volume(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 3, 0, 0, 0, 0, -1)

    @classmethod
    @property
    def momentum(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-1, 1, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def permittivity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(4, -3, -1, 2, 0, 0, 0)

    @classmethod
    @property
    def power(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 2, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def pressure(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, -1, 1, 0, 0, 0, 0)

    @classmethod
    @property
    def resistance(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 2, 1, -2, 0, 0, 0)

    @classmethod
    @property
    def resistivity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 3, 1, -2, 0, 0, 0)

    @classmethod
    @property
    def specific_heat_capacity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-2, 2, 0, 0, -1, 0, 0)

    @classmethod
    @property
    def temperature(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 0, 0, 0, 1, 0, 0)

    @classmethod
    @property
    def thermal_conductivity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 1, 1, 0, -1, 0, 0)

    @classmethod
    @property
    def time(cls: type[Self]) -> UnitsVector:
        return UnitsVector(1, 0, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def velocity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-1, 1, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def voltage(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-3, 2, 1, -1, 0, 0, 0)

    @classmethod
    @property
    def volume(cls: type[Self]) -> UnitsVector:
        return UnitsVector(0, 3, 0, 0, 0, 0, 0)

    @classmethod
    @property
    def catalytic_activity(cls: type[Self]) -> UnitsVector:
        return UnitsVector(-1, 0, 0, 0, 0, 0, 1)


class SupportsBasicArithmetic(Protocol):
    
    def __add__(self: Self, other: Self) -> Self:
        ...
    
    def __sub__(self: Self, other: Self) -> Self:
        ...
    
    def __mul__(self: Self, other: Self) -> Self:
        ...
    
    def __truediv__(self: Self, other: Self) -> Self:
        ...

    def __eq__(self: Self, other: Self) -> bool:
        ...

T = TypeVar("T", bound=SupportsBasicArithmetic)


class UnitMismatch(Exception):
    def __init__(self: Self, *args: object) -> None:
        super().__init__("Can't add/subtract values with different units")


class UnitAwareValue(Generic[T]):

    __slots__ = ("value", "units")

    def __init__(self: Self, value: T, units: UnitsVector) -> None:
        self.value: T = value
        self.units: UnitsVector = units

    def __repr__(self: Self) -> str:
        return f"UnitAwareValue(value={self.value!r}, units={self.units!r})"

    def __add__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)):
            if self.units == other.units:
                return type(self)(self.value + other.value, self.units)
            raise UnitMismatch
        return NotImplemented

    def __sub__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)):
            if self.units == other.units:
                return type(self)(self.value - other.value, self.units)
            raise UnitMismatch
        return NotImplemented
    
    def __mul__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)):
            new_units = UnitsVector(*map(operator.add, self.units, other.units))
            return type(self)(self.value * other.value, new_units)
        return NotImplemented
    
    def __truediv__(self: Self, other: object) -> Self:
        if isinstance(other, type(self)):
            new_units = UnitsVector(*map(operator.sub, self.units, other.units))
            return type(self)(self.value / other.value, new_units)
        return NotImplemented
    
    def __eq__(self: Self, other: object) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value and self.units == other.units
        return False


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
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079",
    0: "\u2070",
}


def format_unitsvector_as_si(vec: UnitsVector) -> str:
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
        "length", "mass", "time", "current", "temperature", "amount_of_substance", "luminous_intensity",
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


class SIUnitAwareValue(UnitAwareValue[T]):

    def __repr__(self: Self) -> str:
        si_repr = format_unitsvector_as_si(self.units)
        # done this way in case of dimensionless values
        return " ".join(filter(None, (f"{self.value}", si_repr)))