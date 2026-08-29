"""
===================
mudu.base
===================

base module for mudu.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Self

import sympy as sym

__all__ = [
    "ABSORBED_DOSE",
    "AMOUNT_OF_SUBSTANCE",
    "ATTO",
    "CAPACITANCE",
    "CENTI",
    "CONDUCTANCE",
    "DENSITY",
    "DIMENSIONLESS",
    "DIMENSIONLESS_UNIT",
    "DOSE_EQUIVALENT",
    "ELECTRIC_CURRENT",
    "ENERGY",
    "FEMTO",
    "FORCE",
    "GENERIC_DIMENSION",
    "GENERIC_QUANTITY",
    "GENERIC_UNIT",
    "GIGA",
    "ILLUMINANCE",
    "INDUCTANCE",
    "KILO",
    "LENGTH",
    "LUMINOUS_INTENSITY",
    "MAGNETIC_FIELD_STRENGTH",
    "MAGNETIC_FLUX",
    "MASS",
    "MEGA",
    "MICRO",
    "MILLI",
    "NANO",
    "PICO",
    "PLANE_ANGLE",
    "POWER",
    "PRESSURE",
    "RADIOACTIVITY",
    "RESISTANCE",
    "SOLID_ANGLE",
    "SPEED",
    "THERMODYNAMIC_TEMPERATURE",
    "TIME",
    "VOLTAGE",
    "Affine",
    "Linear",
    "OrderUnit",
    "_ConversionTableType",
    "_UnitType",
]

# ==================
# Fundamental units
# ==================
LENGTH = sym.Symbol("L")
MASS = sym.Symbol("M")
TIME = sym.Symbol("T")
PLANE_ANGLE = sym.Symbol("θ")
SOLID_ANGLE = sym.Symbol("ω")
THERMODYNAMIC_TEMPERATURE = sym.Symbol("Θ")
ELECTRIC_CURRENT = sym.Symbol("I")
AMOUNT_OF_SUBSTANCE = sym.Symbol("N")
LUMINOUS_INTENSITY = sym.Symbol("J")

# ==============
# Derived units
# ==============
FORCE = "force"
PRESSURE = "pressure"  # same unit as stress
ENERGY = "energy"  # same as heat and work
DENSITY = "density"
POWER = "power"
SPEED = "speed"  # same as velocity vector
ILLUMINANCE = "illuminance"  # physics -> optics
# === Electrical Derived Units ======
VOLTAGE = "voltage"  # Electromotive Force or Potential Difference
CAPACITANCE = "capacitance"
RESISTANCE = "resistance"
CONDUCTANCE = "conductance"
MAGNETIC_FLUX = "magnetic_flux"
MAGNETIC_FIELD_STRENGTH = "magnetic_field_strength"
INDUCTANCE = "inductance"
# === Derived Units in Chemistry =====
RADIOACTIVITY = "radioactivity"
ABSORBED_DOSE = "absorbed_dose"
DOSE_EQUIVALENT = "dose_equivalent"


# Generic unit
GENERIC_UNIT = "generic_unit"
GENERIC_DIMENSION = "generic_dimension"

# Generic quantity
GENERIC_QUANTITY = "generic_quantity"

# Dimensionless quantity
DIMENSIONLESS = "dimensionless"
DIMENSIONLESS_UNIT = "dimensionless_unit"


@dataclass
class _OrderType:
    """Internal base class for defining multiple prefix (order).

    Attributes
    ----------
    name: str
        name of the multiple prefix e.g. `kilo`
    symbol: str
        symbol of the multiple prefix e.g. `k`
    value: float
        multiple value the _OrderType represents `kilo represents 1000 `
    """

    name: str
    symbol: str
    value: float

@dataclass(frozen=True)
class Linear:
    """A purely multiplicative conversion: base_value = value * scale.

    Use for any conversion that passes through zero unchanged (nearly all
    physical units: length, mass, force, energy, ...).
    """

    scale: float

    def to_base(self, x):
        return x * self.scale

    def from_base(self, x):
        return x / self.scale


@dataclass(frozen=True)
class Affine:
    """An offset (non-multiplicative) conversion:
    base_value = value * scale + offset.

    Use for conversions that do NOT pass through zero unchanged. A
    canonical example is temperature (Celsius/Fahrenheit <-> Kelvin).
    """

    scale: float
    offset: float

    def to_base(self, x):
        return x * self.scale + self.offset

    def from_base(self, x):
        return (x - self.offset) / self.scale


Conversion = Linear | Affine


@dataclass
class _ConversionTableType:
    """Internal base class definition for a *star-topology* conversion table.

    Every non-base unit of a dimension stores exactly one `Conversion`
    (Linear or Affine) that maps it to and from the dimension's single
    canonical base unit (e.g. METER for LENGTH, GRAM for MASS). Converting
    between any two units of the same dimension is always a two-hop
    `from_unit -> base -> to_unit` operation.
    
    Attributes
    ----------
    dimension: sym.Basic
        The physical dimension this table serves (e.g. LENGTH).
    base_unit: _UnitType
        The canonical unit that every other unit converts through.
    table: dict[str, Conversion]
        Maps a unit's `_unit_name` to its Conversion relative to base_unit.
    """

    dimension: sym.Basic
    base_unit: _UnitType
    table: dict = field(default_factory=dict)

    def register(self, unit: _UnitType, conversion: Conversion) -> None:
        """Register (or overwrite, with a warning) a unit's conversion to
        the dimension's base unit.

        Parameters
        ----------
        unit: _UnitType
            The unit being registered. Must belong to this table's dimension.
        conversion: Linear | Affine
            The conversion between `unit` and `self.base_unit`.
        """

        if unit._dimension != self.dimension:
            raise ValueError(
                f"cannot register {unit._unit_name!r}: its dimension does not "
                f"match this table's dimension"
            )

        if unit._unit_name in self.table:
            import warnings

            warnings.warn(
                f"overwriting existing conversion for unit "
                f"{unit._unit_name!r} in this table",
                stacklevel=2,
            )

        self.table[unit._unit_name] = conversion

    # Backward-compatible alias for the old public-facing `.extend(...)`
    # convenience method referenced in earlier docs/examples. Prefer
    # `register()` for new code -- this method now expects the same
    # (unit, conversion) pair rather than a legacy pairwise-table tuple.
    def extend(self, unit: _UnitType, conversion: Conversion) -> None:
        self.register(unit, conversion)


# ============================ ORDERS ==========================================================================
# Non time order
GIGA = _OrderType(name="giga", symbol="G", value=math.pow(10, 9))
MEGA = _OrderType(name="mega", symbol="M", value=math.pow(10, 6))
KILO = _OrderType(name="kilo", symbol="k", value=math.pow(10, 3))
CENTI = _OrderType(name="centi", symbol="c", value=math.pow(10, -2))
MILLI = _OrderType(name="milli", symbol="m", value=math.pow(10, -3))
MICRO = _OrderType(name="micro", symbol="u", value=math.pow(10, -6))
NANO = _OrderType(name="nano", symbol="n", value=math.pow(10, -9))
PICO = _OrderType(name="pico", symbol="p", value=math.pow(10, -12))
FEMTO = _OrderType(name="femto", symbol="f", value=math.pow(10, -15))
ATTO = _OrderType(name="atto", symbol="a", value=math.pow(10, -18))
# ==============================================================================================================


@dataclass
class _UnitType:
    """Internal base class for units definition.

    Attributes
    ----------
    _dimension: sym.Basic
        The unit dimension, say, `LENGTH`, `MASS`, `TIME`
    _unit_name: str
        The unit name e.g. `meter`. Must be unique within a `_quantity`
        (enforced by `audit_units()` in `mudu.dimensions`).
    _unit_symbol: str
        Symbolic representation of the unit, passed as a
        string, then converted to a `sympy.Symbol` object
    _order: _OrderType
        Multiple prefix, if unit is a multiple prefix
        of a `_UnitType`.
    _base: _UnitType
        If a unit is a multiple prefix, then it has a base unit. e.g.
        `KILOMETER` is composed of the multiple prefix `KILO` and the base
        unit `METER`.
    _quantity: str
        The quantity the unit represents, say Force, Energy.
    create_unit: _UnitType
        Class method to create a `_UnitType` object.

    - **Usage example**

        .. code-block:: python

            from mudu import Length, define_unit

            # define a new unit type through the public API (preferred —
            # see mudu.dimensions.define_unit / register_conversion; this
            # avoids touching private classes directly).
            ME_UNIT = define_unit(
                dimension=Length,
                name="me_unit",
                symbol="m_u",
            )

            some_length = Length(12, ME_UNIT)

    To create a conversion standard with another unit, read the documentation
    on `mudu.dimensions.register_conversion`, or the full documentation at
    <https://github.com/techkaduna/mudu>_.
    """

    _dimension: sym.Basic
    _unit_name: str
    _unit_symbol: str | sym.Symbol
    _quantity: str = GENERIC_QUANTITY
    _order: _OrderType = None
    _base: Self = None

    @classmethod
    def create_unit(cls, **kwargs):
        """Internal alternate `_UnitType` constructor.

        Parameters
        ----------
        `create_unit` takes same parameters as the `_UnitType` `__init__`.
        """

        return cls(**kwargs)

    def __post_init__(self):
        if isinstance(self._unit_symbol, str) is True:
            self._unit_symbol = sym.Symbol(self._unit_symbol)

    def __repr__(self):
        return str(self._unit_symbol).replace("**", "^").replace("*", "")  # sorry :)

    def __hash__(self):
        # _UnitType is a value object once constructed (fields are set at
        # __post_init__ and not intended to be mutated afterwards). A
        # consistent hash lets units be used as dict keys / in sets, e.g.
        # in the conversion-table lookups above.
        return hash((str(self._dimension), self._unit_name, str(self._unit_symbol)))

    def __mul__(self, x: Self):

        if isinstance(x, _UnitType) is True:
            return _UnitType.create_unit(
                _dimension=self._dimension * x._dimension,
                _unit_name=GENERIC_DIMENSION,
                _unit_symbol=self._unit_symbol * x._unit_symbol,
            )

        elif isinstance(x, int | float):
            return self

        else:
            raise TypeError(f"operand must be type _UnitType or {int}")

    def __rmul__(self, x: Self):

        if isinstance(x, int | float):
            return self
        else:
            raise TypeError(f"operand must be type _UnitType or {int}")

    def __truediv__(self, x):

        if isinstance(x, _UnitType) is True:
            return _UnitType.create_unit(
                _dimension=self._dimension / x._dimension,
                _unit_name=GENERIC_DIMENSION,
                _unit_symbol=self._unit_symbol / x._unit_symbol,
            )

        elif isinstance(x, int | float):
            return self

        else:
            raise TypeError(f"operand must be type _UnitType or {int}")

    def __rtruediv__(self, x):

        if isinstance(x, (int, float)) is True:
            return _UnitType.create_unit(
                _dimension=self._dimension**-1,
                _unit_name=GENERIC_DIMENSION,
                _unit_symbol=1 / self._unit_symbol,
            )
        raise TypeError(f"operand must be type int or float, got {type(x)}")

    def __pow__(self, x):

        if isinstance(x, (int, float)) is False:
            raise TypeError(
                "_UnitType can only be raise to the power of an integer (or float)"
            )
        return _UnitType.create_unit(
            _dimension=self._dimension**x,
            _unit_name=GENERIC_DIMENSION,
            _unit_symbol=self._unit_symbol**x,
        )


class _OrderUnitType:
    """Internal class for creating a multiple prefix unit.

    - **Usage example**

        .. code-block:: python

            from mudu import Length, METER, OrderUnit, KILO

            # define a multiple-prefix unit
            KILOMETER = OrderUnit(KILO, METER)

            some_length = Length(12, KILOMETER)

    **NOTE** `_OrderUnitType` itself is internal; `OrderUnit`, the module-level
    instance of it, is the public callable used to build prefixed units.
    """

    def __call__(self, _order: _OrderType, unit: _UnitType):
        return _UnitType(
            _dimension=unit._dimension,
            _quantity=unit._quantity,
            _unit_name=f"{_order.name}{unit._unit_name}",
            _unit_symbol=f"{_order.symbol}{unit._unit_symbol}",
            _order=_order,
            _base=unit,
        )


OrderUnit = _OrderUnitType()


class _SetOnce:
    """Internal descriptor for setting attributes only once.

    Attributes
    ----------
    name: str
        Attribute identifier
    expected_types: obj | tuple
        Attribute expected type(s)
    """

    def __init__(self, name: str, expected_types) -> None:
        self.name = name
        self.expected_types = expected_types

    def __get__(self, instance, cls):

        if instance is None:
            return self

        try:
            return instance.__dict__[self.name]
        except KeyError:
            raise AttributeError(
                f"{self.name!r} has not been set on {instance!r}"
            ) from None

    def __set__(self, instance, value):

        if self.name in instance.__dict__:
            raise ValueError(f"cannot set {self.name} after it has been set")

        if isinstance(value, self.expected_types) is False:
            raise TypeError(f"{self.name} must be of type {self.expected_types}")
        instance.__dict__[self.name] = value
