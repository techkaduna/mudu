# Changelog - Mudu 2.0.0 (the D-Check Release)

### Added
- `mudu.define_unit()` — public, supported way to define a new unit against
  an existing dimension (`Length`, `Mass`, `Force`, ...), replacing the
  previous documented workflow of instantiating the private `_UnitType`
  class directly.
- `mudu.register_conversion()` — public, supported way to register how a
  custom unit converts to/from its dimension's base unit, using the new
  `Linear`/`Affine` conversion types. Replaces the previous
  `_conversion_standards.extend(...)` pattern that required touching
  internals.
- `mudu.Linear` and `mudu.Affine` — explicit, first-class conversion types.
  `Linear(scale)` for ordinary multiplicative conversions; `Affine(scale,
  offset)` for offset conversions (currently used for Celsius/Fahrenheit).
  Previously this distinction existed only implicitly, as differently
  shaped anonymous lambdas.
- `mudu.audit_units()` — scans one or more conversion tables for duplicate
  unit names and malformed conversion entries. Intended to run in CI
  against every shipped table (see `test/test_suite.py`); would have
  caught the PSI and Becquerel defects below automatically had it existed
  at the time.
- `OUNCE` is now exported from the package root (`from mudu import OUNCE`).
  It was previously defined and used internally in the mass conversion
  table but never added to `mudu/__init__.py`'s public exports.
- `test/test_suite.py`: full pytest + Hypothesis test suite, including a
  permanent regression test for every bug fixed below, known-value
  conversion checks against standard reference constants, data-model
  contract tests (`__eq__`/`__hash__`/`__floordiv__`), and property-based
  round-trip tests run across every shipped conversion table.

### Changed
- **Conversion architecture reworked to a star topology.** Every dimension
  now has exactly one canonical base unit (e.g. `METER` for `Length`,
  `KELVIN` for `Temperature`), and every other unit registers exactly one
  `Linear`/`Affine` conversion relative to that base unit. Converting
  between any two units is always a two-hop
  `from_unit -> base_unit -> to_unit` operation.
  This replaces the previous pairwise-entry design, which required a
  hand-written table row for every combination of units needing direct
  conversion, offered no way to detect an inverted or duplicate entry, and
  in practice shipped with at least one inverted entry (see `INCH -> FEET`
  below). This is the same approach used internally by `pint` and
  `astropy.units`.
- **`convert_to` consolidated into a single implementation.** Previously
  duplicated across three near-identical ~70-line blocks: a dead
  module-level `_unit_conversion()` function, `DerivedQuantity.convert_to`,
  and `_DimensionType.convert_to`. All three are replaced by one shared
  implementation on `_DimensionUnitBase` (via the internal
  `_scalar_convert` helper), used by both quantity classes.
- `_check_and_convert` (the shared arithmetic/comparison path for `+`,
  `-`, `<`, `>`, `<=`, `>=`, `==`) is likewise now a single implementation
  on `_DimensionUnitBase`, rather than two separately maintained copies.
- `SequenceOperationErrorr` renamed to `SequenceOperationError` (the
  original name had a stray trailing "r"). The old name has been removed
  in this version.
- `MageneticFieldStrength` renamed to `MagneticFieldStrength` (typo fix).
- `AMPERE`'s `_unit_name` corrected from `"current"` to `"ampere"` for
  consistency with every other base-unit naming convention in the module.
- Every module now declares `__all__`, making the intended public surface
  explicit rather than implicit in `mudu/__init__.py`'s import list alone.
- `_SetOnce.__get__` now raises `AttributeError` (via a proper `KeyError`
  catch translated at the descriptor boundary) instead of leaking a raw
  `KeyError`, matching normal Python attribute-access conventions.

### Fixed
- **`PLANE_ANGLE`, `SOLID_ANGLE`, and `THERMODYNAMIC_TEMPERATURE` no longer
  share a sympy symbol.** All three previously used the identical symbol
  `"Ɵ"`, which — because sympy `Symbol`s compare and hash by name — made
  them the *same dimension* as far as every homogeneity check in the
  library was concerned. Arithmetic between, e.g., an `Angle` and a
  `Temperature` did not raise `DimensionError` as it should have. Each
  dimension now has its own distinct symbol.
- **`BECQUEREL`'s dimension corrected.** It previously reused `LUX`'s
  (illuminance) dimension formula via a copy-paste error, instead of
  1/TIME like `CURIE` (both units of `RADIOACTIVITY`). Converting between
  `Becquerel` and `Curie` previously raised a spurious `DimensionError`
  despite both being valid activity units.
- **`PSI`'s `_unit_name` corrected from `"pascal"` to `"psi"`.** The
  duplicate name (copy-pasted from `PASCAL`) was not merely cosmetic: the
  `is_same_unit` check in the multiplication/division operators compares
  units by `_unit_name`, so a `Pressure` in Pascals and a `Pressure` in
  PSI could be misidentified as "the same unit," silently skipping a
  needed conversion and producing a numerically wrong result with no
  exception raised.
- **`SLUG -> GRAM` conversion factor corrected**, from `14.593903` to
  `14593.903`. The old value was off by exactly 1000x — a kilogram/gram
  unit mixup (1 slug is 14.593903 *kilograms*, i.e. 14593.903 grams).
- **`INCH -> FEET` conversion corrected.** The old pairwise table entry
  used `y=12` as a forward multiply (`inches * 12 = feet`), which is
  backwards by a factor of 144 (1 inch is 1/12 foot, not 12 feet). This
  entry no longer exists as a hand-written row at all — see "Conversion
  architecture reworked" above; both `INCH` and `FEET` now convert
  correctly and automatically via `METER`.
- **`_DimensionType.__len__` no longer crashes on ordinary scalar
  quantities.** It previously computed `1 if self.value is True else
  len(self.value)` — an identity check against the literal boolean
  `True`, which is essentially never satisfied by a real numeric value,
  so `len()` on e.g. `Length(12, METER)` raised `TypeError`.
- **`DerivedQuantity.__rtruediv__` no longer references a nonexistent
  attribute.** The `_DimensionType` branch referenced `self.__value` (a
  typo for `self.__value_not_seq`), guaranteed to raise `AttributeError`
  if that code path was ever reached.
- **`custom_unit` no longer leaks state across instances.** `
  __numerator`/`__denominator` were previously declared as class-level
  mutable lists, so every `custom_unit` instance appended into the same
  shared list process-wide rather than its own. They are now correctly
  initialized as instance attributes in `__init__`.
- **`__eq__` now always returns `bool`.** Previously, in some branches it
  could return a whole new quantity object instead of a boolean, breaking
  Python's data model contract for equality (affecting `assertEqual`,
  `set`/`dict` membership, `in`, and any code doing a plain `if a == b`).
- **Quantities are now hashable.** Defining `__eq__` without `__hash__`
  implicitly set `__hash__ = None` on the whole hierarchy, making
  quantities unusable as dict keys or set members. A `__hash__` consistent
  with the fixed `__eq__` (based on dimension, unit, and value) has been
  added.
- **`__floordiv__` now floors correctly for negative results.** Previously
  `float(int(self.__truediv__(x=x)))`, which truncates toward zero rather
  than flooring — e.g. it returned `-3.0` instead of the correct `-4.0`
  for an underlying true-division result of `-3.5`.
- **`GRAM_PER_CUBIC_MILLILITER` no longer shares its `_unit_name` and
  `_unit_symbol` with `GRAM_PER_CUBIC_CENTIMETER`.** Numerically harmless
  (1 mL == 1 cm³, so the conversion factor was coincidentally correct
  either way) but the duplicate metadata is exactly the class of
  copy-paste error `audit_units()` now catches.
- **`POUND_FORCE`, `POUND_PER_SQUARE_FOOT`, and several other force/energy
  constants tightened to more precise standard values** (e.g.
  `POUND_FORCE -> NEWTON` from `4.44822` to `4.4482216153`;
  `ELECTRON_VOLT -> JOULE` to the 2019 SI-exact value
  `1.602176634e-19`; `BRITISH_THERMAL_UNIT -> JOULE` to the IT-BTU value
  `1055.05585262`) during the constant-by-constant review that
  accompanied this release. None of the previous values were wrong by an
  order of magnitude — they were reasonable roundings — but this release
  tightens precision as a matter of course while every constant was
  already being re-derived.
- Removed dead code: the unused module-level `_unit_conversion()` function
  in `dimensions.py`, superseded by (and redundant with) the consolidated
  `convert_to` described above.

### Known limitations (not addressed in this release)
- Sequence/array-valued quantities remain represented as `numpy.ndarray`s
  *of individually wrapped scalar quantity objects*, not true vectorized
  arrays of raw floats. This is the primary source of the performance
  overhead in array operations and is tracked as its own architecture
  change, deliberately scoped out of this
  release to avoid combining a large architecture change with a
  correctness-focused fix pass.
- No `numpy`/`pandas`/`matplotlib` interoperability, no serialization
  support, and no expansion of derived-quantity/SI coverage in this
  release.
