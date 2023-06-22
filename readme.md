# Math and physics preserving and checking units

### quick example

```py
>>> from unit_aware import Units, UnitAwareValue, UnitsVector
>>> UnitAwareValue(120, Units.velocity) * UnitAwareValue(60, Units.time)
UnitAwareValue(value=7200, units=UnitsVector(time=0, length=1, mass=0, current=0, temperature=0, luminous_intensity=0, amount_of_substance=0))
```

`UnitsVector` holds info about units of measurement as a 7 dimensional vector

`Units` contains shortcuts to these based on what you are measuring.

You can use this to check that the units you are using make sense

```py
>>> Units.area  # SI: m^2
UnitsVector(time=0, length=2, mass=0, current=0, temperature=0, luminous_intensity=0, amount_of_substance=0)
>>> Units.acceleration  # SI: m/s^2
UnitsVector(time=-2, length=1, mass=0, current=0, temperature=0, luminous_intensity=0, amount_of_substance=0)
```

UnitAwareValue prevents addition and subtraction with mismatched units, the below raises informing you of the mismatch
```py
>>> UnitAwareValue(120, Units.area) + UnitAwareValue(120, Units.volume)
```

### Already using SI units like you should be?

`SIUnitAwareValue` has a repr which displays the SI units, including basic support for derived units.
```py
from unit_aware import Units, SIUnitAwareValue as SIV
>>> SIV(1, Units.scalar_value) / SIV(1, Units.time) 
1.0 Hz
>>> SIV(1, Units.velocity) * SIV(1, Units.time) 
1 m
>>> SIV(1, Units.velocity) + SIV(1, Units.acceleration) * SIV(1, Units.time) 
2 m/s
>>> SIV(1, Units.power) / SIV(1, Units.current)
1.0 V
```

If it can't determine an equivalent derived unit appears to make sense:
```py
>>> SIV(1, Units.power) / SIV(1, Units.time) * SIV(1, Units.area) / SIV(1, Units.time)  
1.0 m⁴kg/s⁵
```

Not all SI recognized derived units are supported. 
- Radians, and steradians are dimensionless. You can insert them as appropriate without other modification to what is displayed.
- Celcius is not supported by this at this time. This may not change (needs consideration of impact)
- becquerel, gray, sievert, and katal are all excluded for now, with a potential to add support later

### Arbitray Precision

`UnitAwareValue` and `SIUnitAwareValue` both accept any type which support additon, subtraction, multiplcation, division, and equality comparison for a value.

You can use the builtin `fractions.Fraction` or `decimal.Decimal` if specific precision is required

```py
>>> from fractions import Fraction
>>> from unit_aware import Units, SIUnitAwareValue as SIV
>>> SIV(Fraction("5/4"), Units.length) / SIV(Fraction("3"), Units.time)   
5/12 m/s
```

### Other systems of measurement?

While the base units here correspond to the SI base units, nothing here prevents using these with any coherent system of measurement

consider, the [7 Cs](https://www.youtube.com/watch?v=KmfdeWd0RMk) A system of measurement based around

- Velocity (the speed of light)
- Energy (calorie)
- Frequency (middle c)
- Temperature (degrees celcius)
- Luminous Intensity (candela)
- Charge (coulomb)
- Amount of Substance (100, roman numeral C)

In this system of measurement, derived units still work just fine

Current is measured in "middle C coulombs", which to anyone used to working in more standard units is absurd.

but units vectors don't care about the units, only the coherence of the units, so

```py
>>> midc_coulomb = UnitAwareValue(1, Units.frequency) * UnitAwareValue(1, Units.charge)
>>> midc_coulomb.units == Units.current
True
```

This doesn't mean the *values* are equivalent to those of the SI, you still need to scale based on the base units 
in this case, scaling by a factor of 220 * (2**(1/4)), as charge is the same in both systems,
and the seven cs uses middle C (c4), assuming A4 is 440hz and 12-tone equal temperament


### Todo list

- Parsing from string for SI units.
- Conversion matrices for other coherent systems.
- Display in terms of equivalent specified units with error on units not being compatible
- Possible extended form for units that allows defining in terms of relation to SI for non-coherent units?