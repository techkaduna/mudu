"""
===================
mudu.base
===================

base module for mudu.
"""

from typing import Self, Sequence
from dataclasses import dataclass
import math

import sympy as sym

# ==================
# Fundamental units
# ==================
LENGTH = sym.Symbol("L")
MASS = sym.Symbol("M")
TIME = sym.Symbol("T")
PLANE_ANGLE = sym.Symbol("Ɵ")
SOLID_ANGLE = sym.Symbol("Ɵ")
THERMODYNAMIC_TEMPERATURE = sym.Symbol("Ɵ")
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
SPEED = "speed"  # also doubles for velocity vector
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


@dataclass
class _ConversionTableType:
    """Internal base class definition for conversion table for dimension objects.

    Attributes
    ----------
    dimension: str
        Conversion table contains units of dimension. Dimension could be `LENGTH TIME MASS` e.t.c.
    conversion_table: Sequence
        `tuple` containing the conversion units and a lambda calculating the conversion. e.g.
        `((INCH, METER), functools.partial(_basic_unit_converter, y=0.0254))`
    extend: None
        Extend an existing conversion table with more conversion standards.

    """

    dimension: str
    conversion_table: Sequence

    def extend(self, seq: Sequence) -> None:
        """Convieniece method to extend the built-in conversion standard to
        accomodate other user defined units.

        Parameters
        ----------
        seq: Sequence
            tuple that contains:
                a tuple of the units
                and a callable that defines the conversion operation.
        - **Usage example**

            .. code-block:: python

                import functools

                from mudu import Length, METER
                from mudu.base import _UnitType
                from mudu.units import _basic_unit_converter

                # define a new unit type
                ME_UNIT = _UnitType(
                    _dimension=LENGTH,
                    _unit_name="me_unit",
                    _unit_symbol="m_u",
                    )

                # create a conversion standard with METER
                seq = ((ME_UNIT, METER), functools.partial(_basic_unit_converter, y=0.001))

                # extend the conversion table
                Length._conversion_standards.extend(seq)
        """

        self.conversion_table.extend((seq,))


@dataclass
class _UnitType:
    """Internal base class for units definition.

    Attributes
    ----------
    _dimension: str
        The unit dimension, say, `LENGTH`, `MASS`, `TIME `
    _unit_name: str
        The unit name e.g.  `meter`
    _unit_symbol: str
        Symbolic representation of the unit, usually passed as a
        string, then converted to a `sympy.Symbol` object
    _order: _OrderType
        Multiple prefix, if unit is a multiple prefix
        of a  `_UnitType`.
    _base: _UnitType
        If a unit is a multiple prefix, then it has a base unit. e.g.
        `CENTIMETER` is composed of the multiple prefix `CENTI` and the base
        unit `METER`.
    _quantity: str
        The quantity the unit represents, say Force, Energy.
    create_unit: _UnitType
        Class method to create a `_UnitType` object.
    is_unit_type: bool
        Internal method to validate that an object is an instance of `_UnitType`

    - **Usage example**

        .. code-block:: python

            from mudu import Length, METER
            from mudu.base import _UnitType

            # define a new unit type
            ME_UNIT = _UnitType(
                _dimension=LENGTH,
                _unit_name="me_unit",
                _unit_symbol="m_u",
                )

            some_length = Length(12, ME_UNIT)

    To create a conversion standard with another unit, read the documentation
    on _ConversionTableType or read the full documentation at <https://github.com/techkaduna/mudu>_.
    """

    _dimension: str
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
            raise TypeError(f"operand must be type _UnitType or {type(1)}")

    def __rmul__(self, x: Self):

        if isinstance(x, int | float):
            return self
        else:
            raise TypeError(f"operand must be type _UnitType or {type(1)}")

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
            raise TypeError(f"operand must be type _UnitType or {type(1)}")

    def __rtruediv__(self, x):

        if isinstance(x, (int, float)) is True:
            return _UnitType.create_unit(
                _dimension=self._dimension**-1,
                _unit_name=GENERIC_DIMENSION,
                _unit_symbol=1 / self._unit_symbol,
            )

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


class _OrderUnitType:
    """Intenal class for creating a multiple prefix unit.

    - **Usage example**

        .. code-block:: python

            from mudu import Length, METER, OrderUnit, KILO

            # define an OrderUnit
            KILOMETER = OrderUnit(KILO, METER)

            some_length = Length(12, KILOMETER)

    **NOTE** `_OrderUnit` was not used to create the multiple prefix unit,
    `OrderUnit`, which is an instance of `_OrderUnit`, was used instead.
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
    """Internal base class descriptor for setting attributes only once.

    Attributes
    ----------
    name: str
        Attribute identifier
    expected_types: obj | Sequence
        Attribute expected type(s)

    """

    def __init__(self, name: str, expected_types) -> None:
        self.name = name
        self.expected_types = expected_types

    def __get__(self, instance, cls):

        if instance is None:
            return self

        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):

        try:
            getattr(instance, self.name)
            raise ValueError(f"cannot set {self.name} after it has been set")

        except KeyError:
            # attribute does not exist; now set attribute
            if isinstance(value, self.expected_types) is False:
                raise TypeError(f"{self.name} must be of type {self.expected_types}")
            instance.__dict__[self.name] = value
