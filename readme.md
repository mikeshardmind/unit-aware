# Math and physics preserving and checking units

### quick example

```py
>>> from unit_aware import Units, UnitAwareValue, UnitsVector
>>> UnitAwareValue(120, Units.velocity) * UnitAwareValue(60, Units.time)
UnitAwareValue(value=7200, units=UnitsVector(time=0, length=1, mass=0, current=0, temperature=0, luminous_intensity=0, amount_of_substance=0))
```

UnitsVector holds info about units of measurement as a 7 dimensional vector
Units contains shortcuts to these based on what you are measuring.
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


### Todo list

Formatting based on units.
Parsing from string for SI units.
Conversion matrices for other coherent systems.
Display in terms of equivalent specified units with error on units not being compatible