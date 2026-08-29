# What's Changed in mudu 2.0.0

This page summarizes the correctness fixes and API changes made during the project's first "D-Check" review pass. Full line-by-line detail is in `CHANGELOG.md` in the repository root; this page focuses on what a user of the *previous* version needs to know before upgrading.

## If you were working around a bug

If you previously worked around any of the following, **remove the workaround** — it is now fixed at the source and your workaround may now double-apply or silently overwrite the correct behavior:

- `Mass(1, SLUG).convert_to(GRAM)` now correctly returns `14593.903` (previously `14.593903`).
- `Length(x, INCH).convert_to(FEET)` (and the reverse) now correctly scales by 1/12 (previously inverted by 144x).
- `Pressure(x, PSI)` no longer silently collides with `Pressure(y, PASCAL)` in arithmetic. If you were manually re-wrapping or re-converting PSI values to work around wrong results, that's no longer necessary.
- `Radioactivity` values in `BECQUEREL` and `CURIE` can now be converted between each other; this previously raised `DimensionError` incorrectly.
- `Angle` and `Temperature` (and `SolidAngle`) are now correctly distinct dimensions; arithmetic between them now correctly raises `DimensionError` instead of silently succeeding.

## New public extension API

Previously, extending mudu with a new unit on an *existing* dimension required touching private classes directly:

```python
# OLD -- do not use this pattern anymore for existing dimensions
from mudu.base import _UnitType
from mudu.units import _basic_unit_converter
import functools

NEW_UNIT = _UnitType(_dimension=LENGTH, _unit_name="new_unit", _unit_symbol="nu")
seq = ((NEW_UNIT, METER), functools.partial(_basic_unit_converter, y=0.001))
Length._conversion_standards.extend(seq)
```

This is replaced by two public functions:

```python
from mudu import Length, METER, define_unit, register_conversion, Linear

NEW_UNIT = define_unit(Length, name="new_unit", symbol="nu")
register_conversion(Length, NEW_UNIT, Linear(0.001))  # 1 new_unit = 0.001 m
# meter is the base unit for the Length dimension

Length(5, NEW_UNIT).convert_to(METER)  # -> 0.005 m
```

For conversions that involve an offset rather than a pure scale factor (temperature-style), use `Affine` instead of `Linear`:

```python
from mudu import Temperature, KELVIN, define_unit, register_conversion, Affine

MY_SCALE = define_unit(Temperature, name="my_scale", symbol="ms")
# base_value = value * scale + offset
register_conversion(Temperature, MY_SCALE, Affine(scale=1.0, offset=100.0))
```

!!! note "When you still need the private classes directly"
    If you're defining an entirely new *quantity* that has no existing dimension to attach to (mudu has no built-in notion of, say, "Luminous Flux" yet), you still subclass `DerivedQuantity` and instantiate `_UnitType` directly for that new quantity's units — there's no existing table to register against. See the `Power` example in [Examples](examples.md).

## Renamed / corrected names

- `mudu.exceptions.SequenceOperationErrorr` (typo, extra "r") is renamed to `SequenceOperationError`. The old name has been removed for this version.
- `mudu.dimensions.MageneticFieldStrength` (typo) is renamed to `MagneticFieldStrength`, with no deprecated alias.
- `mudu.OUNCE` is now actually importable (`from mudu import OUNCE`); it existed internally before but was never exported.

## Updated symbols

`mudu.base.PLANE_ANGLE`, `mudu.base.SOLID_ANGLE`, and `mudu.base.THERMODYNAMIC_TEMPERATURE` previously shared the same symbol, Ɵ. Now:

- `mudu.base.PLANE_ANGLE` is represented with lower case theta, θ
- `mudu.base.SOLID_ANGLE` is represented with lower case omega, ω
- `mudu.base.THERMODYNAMIC_TEMPERATURE` is now represented using capital theta, Ɵ

## Other things worth knowing

- `__eq__` on quantity objects now always returns a plain `bool` (previously it could, in some cases, return a whole new quantity object). If you were relying on the old behavior anywhere, that code needs to be revisited.
- Quantity objects (`Length`, `Force`, etc.) are now hashable and can be used in sets and as dict keys.
- `mudu.audit_units()` is a new utility that scans conversion tables for duplicate/malformed entries — useful if you've registered your own units via `register_conversion` and want a sanity check.
- `mudu.base._ConversionTableType.extend` has been replaced with `mudu.base._ConversionTableType.register`. `.extend(...)` is still kept for backward compatibility.