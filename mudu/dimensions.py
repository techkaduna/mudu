"""
=========================
mudu.dimensions
=========================

mudu module, defines dimensions (quantities).

For more information, read the documentation using

.. code-block:: shell
    mudu --doc

in your cli
"""

from __future__ import annotations

import functools
import math
import operator
from collections import Counter, abc
from collections.abc import Callable
from typing import Any, Self

import numpy as np
import sympy as sym

from . import exceptions
from .base import (
    ABSORBED_DOSE,
    DENSITY,
    DOSE_EQUIVALENT,
    ENERGY,
    FORCE,
    GENERIC_QUANTITY,
    LENGTH,
    MASS,
    PLANE_ANGLE,
    POWER,
    PRESSURE,
    RADIOACTIVITY,
    SPEED,
    THERMODYNAMIC_TEMPERATURE,
    TIME,
    Affine,
    Linear,
    _ConversionTableType,
    _SetOnce,
    _UnitType,
)
from .units import (
    _ABSORBED_DOSE_CONVERSION_TABLE,
    _ANGLE_CONVERSION_TABLE,
    _DENSITY_CONVERSION_TABLE,
    _DOSE_EQUIVALENT_TABLE,
    _ENERGY_CONVERSION_TABLE,
    _FORCE_CONVERSION_TABLE,
    _LENGTH_CONVERSION_TABLE,
    _MASS_CONVERSION_TABLE,
    _POWER_CONVERSION_TABLE,
    _PRESSURE_CONVERSION_TABLE,
    _RADIOACTIVITY_CONVERSION_TABLE,
    _SPEED_CONVERSION_TABLE,
    _TEMPERATURE_CONVERSION_TABLE,
    _TIME_CONVERSION_TABLE,
    AMPERE,
    CANDELA,
    FARAD,
    GRAM,
    HENRY,
    KELVIN,
    LUX,
    METER,
    MOLE,
    OHMS,
    SECOND,
    SIEMENS,
    STERADIAN,
    TESLA,
    VOLT,
    WEBER,
)

__all__ = [
    "AbsorbedDose",
    "AmountOfSubstance",
    "Angle",
    "Capacitance",
    "Conductance",
    "Density",
    "DerivedQuantity",
    "DoseEquivalent",
    "ElectricCurrent",
    "Energy",
    "Force",
    "GenericUnit",
    "GenericUnit2",
    "Illuminance",
    "Inductance",
    "Length",
    "LuminousIntensity",
    "MagneticFieldStrength",
    "MagneticFlux",
    "Mass",
    "Power",
    "Pressure",
    "Radioactivity",
    "Resistance",
    "SolidAngle",
    "Speed",
    "Temperature",
    "Time",
    "Voltage",
    "_DimensionType",
    "_DimensionUnitBase",
    "audit_units",
    "custom_unit",
    "define_unit",
    "register_conversion",
]


# ============================================================================
# Shared scalar conversion helper (star topology) replaces
# what used to be a dead module-level `_unit_conversion` function, plus
# one copy each in DerivedQuantity.convert_to and _DimensionType.convert_to).
# ============================================================================
def _scalar_convert(
    value: int | float,
    from_unit: _UnitType,
    to_unit: _UnitType,
    table: _ConversionTableType,
) -> float:
    """Convert a single scalar value from `from_unit` to `to_unit`, both of
    which must belong to `table`'s dimension, via the two-hop
    from_unit -> base_unit -> to_unit path.
    """

    # Reduce `from_unit` to its prefixless equivalent (undo any KILO/MILLI/
    # etc. order multiplier), tracking the multiple applied.
    if from_unit._order is not None:
        from_multiple = from_unit._order.value
        from_base_prefixless = from_unit._base
    else:
        from_multiple = 1
        from_base_prefixless = from_unit

    if to_unit._order is not None:
        to_multiple = to_unit._order.value
        to_base_prefixless = to_unit._base
    else:
        to_multiple = 1
        to_base_prefixless = to_unit

    value_in_from_prefixless = value * from_multiple

    # Step 1: from_unit (prefixless) -> dimension's canonical base unit.
    if from_base_prefixless._unit_name == table.base_unit._unit_name:
        value_in_base = value_in_from_prefixless
    else:
        conversion = table.table.get(from_base_prefixless._unit_name)
        if conversion is None:
            raise exceptions.ConversionError(
                f"no registered conversion for unit "
                f"{from_base_prefixless._unit_name!r} in this dimension's "
                f"conversion table"
            )
        value_in_base = conversion.to_base(value_in_from_prefixless)

    # Step 2: base unit -> to_unit (prefixless).
    if to_base_prefixless._unit_name == table.base_unit._unit_name:
        value_in_to_prefixless = value_in_base
    else:
        conversion = table.table.get(to_base_prefixless._unit_name)
        if conversion is None:
            raise exceptions.ConversionError(
                f"no registered conversion for unit "
                f"{to_base_prefixless._unit_name!r} in this dimension's "
                f"conversion table"
            )
        value_in_to_prefixless = conversion.from_base(value_in_base)

    return value_in_to_prefixless / to_multiple


class _DimensionUnitBase:
    """
    Base class for all dimension models (`_DimensionType` for fundamental
    quantities, `DerivedQuantity` for derived ones).

    Attributes
    ----------
    _conversion_standards: _ConversionTableType
        Conversion table for this dimension.
    _dimension: sym.Basic
        The dimension represented by this model.
    """

    _conversion_standards: _ConversionTableType = None
    _dimension = None

    def __repr__(self):
        return ""

    def __str__(self):
        return ""

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, x):
        return self._check_and_convert(x=x, _operator=operator.add)

    def __radd__(self, x):
        return self.__add__(x)

    def __sub__(self, x):
        return self._check_and_convert(x=x, _operator=operator.sub)

    def __rsub__(self, x):
        return self.__sub__(x) * -1

    def __mul__(self, x):
        raise NotImplementedError

    def __rmul__(self, x):
        return self.__mul__(x)

    def __truediv__(self, x):
        raise NotImplementedError

    def __rtruediv__(self, x):
        raise NotImplementedError

    def __floordiv__(self, x):
        return float(math.floor(self.__truediv__(x=x)))

    def __rfloordiv__(self, x):
        return float(math.floor(self.__rtruediv__(x)))

    def __pow__(self, x):
        raise NotImplementedError

    def __round__(self, y=0):
        raise NotImplementedError

    def __lt__(self, x):
        return self._check_and_convert(x, _operator=operator.lt)

    def __gt__(self, x):
        return self._check_and_convert(x, _operator=operator.gt)

    def __le__(self, x):
        return self._check_and_convert(x, _operator=operator.le)

    def __ge__(self, x):
        return self._check_and_convert(x, _operator=operator.ge)

    def __eq__(self, x):
        if isinstance(x, _DimensionUnitBase):
            if self.dimension != x.dimension:
                return False
            try:
                other_value = x.convert_to(self.unit_type).value
            except exceptions.ConversionError:
                return False
            return bool(
                np.array_equal(
                    np.asarray(self.value, dtype=object),
                    np.asarray(other_value, dtype=object),
                )
            )
        if isinstance(x, (int, float)):
            return bool(self.value == x)
        return NotImplemented

    def __ne__(self, x):
        result = self.__eq__(x)
        if result is NotImplemented:
            return result
        return not result

    def __hash__(self):
        if self.__value_not_seq:
            value_key = self.value
        else:
            value_key = tuple(self.value)
        return hash((str(self.dimension), self.unit_type._unit_name, value_key))

    @property
    def __value_not_seq(self):
        return isinstance(self.value, (int, float))

    def _check_and_convert(
        self, x: Any, _operator: Callable
    ) -> Self | bool | (int | float):
        """Perform an arithmetic or boolean operation against another
        quantity or a plain scalar, converting units first if needed to
        guarantee homogeneity. Shared by both `DerivedQuantity` and
        `_DimensionType` -- previously duplicated with minor drift between
        the two.
        """

        if isinstance(x, _DimensionUnitBase):
            if self.dimension != x.dimension:
                raise exceptions.DimensionError(
                    f"cannot operate between quantities of dimension "
                    f"{self.dimension} and {x.dimension}"
                )

            if x.unit_type._unit_name != self.unit_type._unit_name:
                _equivalent = x.convert_to(self.unit_type).value
            else:
                _equivalent = x.value

            new_value = _operator(self.value, _equivalent)

            if isinstance(new_value, (bool, np.bool_)):
                return bool(new_value)

            return (
                self.create_unit(value=new_value, unit_definition=self.unit_type)
                if isinstance(self, DerivedQuantity)
                else self.create_unit(value=new_value, unit=self.unit_type)
            )

        elif isinstance(x, (int, float)):
            new_value = _operator(self.value, x)
            if isinstance(new_value, (bool, np.bool_)):
                return bool(new_value)
            return new_value

        else:
            raise exceptions.DimensionError(
                f"cannot operate on {self.dimension} and {type(x)}"
            )

    def convert_to(self, _to: _UnitType) -> Self:
        """Convert this quantity to another unit of the same dimension.

        Single, shared implementation (see `_scalar_convert` above) used by
        both `DerivedQuantity` and `_DimensionType`.
        """

        if self._conversion_standards is None:
            raise exceptions.ConversionError(
                "this quantity has no conversion table defined"
            )

        if not isinstance(_to, _UnitType):
            raise exceptions.ConversionError(
                "conversion can only be made to a valid unit type"
            )

        if self.dimension != _to._dimension:
            raise exceptions.DimensionError(
                f"Cannot convert {self.dimension} dimension to "
                f"{_to._dimension} dimension."
            )

        table = self._conversion_standards

        if self.__value_not_seq:
            new_value = _scalar_convert(self.value, self.unit_type, _to, table)
        else:
            new_value = [
                _scalar_convert(item.value, self.unit_type, _to, table)
                for item in iter(self.value)
            ]

        if isinstance(self, DerivedQuantity):
            return self.create_unit(value=new_value, unit_definition=_to)
        return self.create_unit(value=new_value, unit=_to)


class DerivedQuantity(_DimensionUnitBase):
    """Base class for all derived quantities (Force, Energy, Pressure, ...).

    See `mudu.dimensions.define_unit` / `register_conversion` for the
    supported way to extend mudu with new units, rather than touching
    private classes directly.
    """

    _conversion_standards: _ConversionTableType = None

    value = _SetOnce("value", (int, float, abc.Sequence, np.ndarray))
    unit_type = _SetOnce("unit_type", _UnitType)
    symbol = _SetOnce("symbol", sym.Basic)
    quantity: str = _SetOnce("quantity", str)

    @classmethod
    def create_unit(cls, **kwargs):
        return cls(**kwargs)

    def __init__(
        self,
        value: int | float,
        unit_definition: _UnitType,
        quantity: str = GENERIC_QUANTITY,
    ):

        self.unit_type = unit_definition
        self.symbol = unit_definition._unit_symbol
        self.quantity = quantity
        self.dimension = unit_definition._dimension

        if self.quantity is not GENERIC_QUANTITY:
            if self.unit_type._quantity != self.quantity:
                raise exceptions.DimensionError(
                    f"{self.unit_type._unit_name} is not a unit of {self.quantity}"
                )

        if isinstance(value, (abc.Sequence, np.ndarray)):
            self.value = np.array(
                [
                    self.create_unit(unit_definition=unit_definition, value=i)
                    for i in value
                ]
            )
        elif isinstance(value, (int, float)):
            self.value = value
        else:
            raise TypeError(
                f"value must be int, float, or a sequence thereof, got {type(value)}"
            )

    @property
    def __value_not_seq(self):
        return isinstance(self.value, (int, float))

    def __repr__(self):
        return (
            f"{self.value} {self.symbol}" if self.__value_not_seq else f"{self.value}"
        )

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return 1 if self.__value_not_seq else len(self.value)

    def __iter__(self):
        return iter([self.value]) if self.__value_not_seq else iter(self.value)

    def __round__(self, y=0):
        if self.__value_not_seq:
            value = round(self.value, y)
        else:
            value = [round(i.value, y) for i in iter(self.value)]
        return self.create_unit(value=value, unit_definition=self.unit_type)

    def __mul__(self, x):

        if isinstance(x, (DerivedQuantity, _DimensionType)):
            if self.__value_not_seq:
                value = (
                    self.value * x.value
                    if isinstance(x.value, (int, float))
                    else [i.value * self.value for i in iter(x.value)]
                )
            else:
                value = [i.value * x.value for i in iter(self.value)]
            unit_definition = self.unit_type * x.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)):
            value = (
                self.value * x
                if self.__value_not_seq
                else [i.value * x for i in iter(self.value)]
            )
            return DerivedQuantity.create_unit(
                value=value, unit_definition=self.unit_type
            )

        raise TypeError(f"cannot multiply DerivedQuantity by {type(x)}")

    def __truediv__(self, x):

        if isinstance(x, DerivedQuantity):
            same_dim = self.unit_type._dimension == x.unit_type._dimension
            same_unit = self.unit_type._unit_name == x.unit_type._unit_name

            if same_dim and same_unit:
                return (
                    self.value / x.value
                    if self.__value_not_seq
                    else np.array(
                        [
                            i.value / j.value
                            for i, j in zip(iter(self.value), iter(x.value))
                        ]
                    )
                )

            if same_dim and not same_unit:
                x_conv = x.convert_to(self.unit_type)
                return (
                    self.value / x_conv.value
                    if self.__value_not_seq
                    else np.array(
                        [
                            i.value / j.value
                            for i, j in zip(iter(self.value), iter(x_conv.value))
                        ]
                    )
                )

            value = (
                self.value / x.value
                if self.__value_not_seq
                else [i.value / x.value for i in iter(self.value)]
            )
            unit_definition = self.unit_type / x.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, _DimensionType):
            value = (
                self.value / x.value
                if self.__value_not_seq
                else [i.value / x.value for i in iter(self.value)]
            )
            unit_definition = self.unit_type / x.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)):
            value = (
                self.value / x
                if self.__value_not_seq
                else [i.value / x for i in iter(self.value)]
            )
            return DerivedQuantity.create_unit(
                value=value, unit_definition=self.unit_type
            )

        raise TypeError(f"cannot divide DerivedQuantity by {type(x)}")

    def __rtruediv__(self, x):

        if isinstance(x, DerivedQuantity):
            same_dim = self.unit_type._dimension == x.unit_type._dimension
            same_unit = self.unit_type._unit_name == x.unit_type._unit_name

            if same_dim and same_unit:
                return (
                    x.value / self.value
                    if self.__value_not_seq
                    else np.array(
                        [
                            j.value / i.value
                            for i, j in zip(iter(self.value), iter(x.value))
                        ]
                    )
                )

            value = (
                x.value / self.value
                if self.__value_not_seq
                else [x.value / i.value for i in iter(self.value)]
            )
            unit_definition = x.unit_type / self.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, _DimensionType):
            # FIX: previously referenced the nonexistent `self.__value`
            # (a typo for `self.__value_not_seq`) -- guaranteed AttributeError
            # if this branch was ever reached.
            value = (
                x.value / self.value
                if self.__value_not_seq
                else [x.value / i.value for i in iter(self.value)]
            )
            unit_definition = x.unit_type / self.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)):
            value = (
                x / self.value
                if self.__value_not_seq
                else [x / i.value for i in iter(self.value)]
            )
            return DerivedQuantity.create_unit(
                value=value, unit_definition=x / self.unit_type
            )

        raise TypeError(f"cannot divide {type(x)} by DerivedQuantity")

    def __pow__(self, x):
        if isinstance(x, (int, float)):
            value = (
                self.value**x
                if self.__value_not_seq
                else [i.value**x for i in iter(self.value)]
            )
            unit_definition = self.unit_type**x
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )
        raise exceptions.DimensionError(
            f"cannot operate on {self.unit_type._dimension} and {type(x)}"
        )


class _DimensionType(_DimensionUnitBase):
    """Base class for all fundamental quantities (Length, Mass, Time, ...)."""

    _conversion_standards: _ConversionTableType = None
    _dimension = None
    _base_unit_standard = None

    dimension = _SetOnce("dimension", sym.Basic)
    unit_type = _SetOnce("unit_type", _UnitType)
    unit = _SetOnce("unit", str)
    symbol = _SetOnce("symbol", sym.Basic)
    value = _SetOnce("value", (int, float, abc.Sequence, np.ndarray))

    @classmethod
    def create_unit(cls, **kwargs):
        return cls(**kwargs)

    def __init__(self, unit: _UnitType, value: int | float | abc.Sequence) -> None:

        self.unit_type = unit
        self.dimension = unit._dimension

        if self._dimension is not None and self._dimension != self.dimension:
            raise exceptions.DimensionError(
                f"{unit._unit_name} is not a unit of {self._dimension}"
            )

        self.unit = unit._unit_name
        self.symbol = unit._unit_symbol

        if isinstance(value, abc.Sequence):
            self.value = np.array([self.create_unit(unit=unit, value=i) for i in value])
        elif isinstance(value, (int, float)):
            self.value = value
        else:
            raise TypeError(
                f"value must be int, float, or a sequence thereof, got {type(value)}"
            )

    @property
    def __value_not_seq(self):
        return isinstance(self.value, (int, float))

    def __repr__(self):
        return (
            f"{self.value} {self.symbol}" if self.__value_not_seq else f"{self.value}"
        )

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return 1 if self.__value_not_seq else len(self.value)

    def __iter__(self):
        return iter([self.value]) if self.__value_not_seq else iter(self.value)

    def __round__(self, y=0):
        value = (
            round(self.value, y)
            if self.__value_not_seq
            else [round(i.value, y) for i in iter(self.value)]
        )
        return self.create_unit(value=value, unit=self.unit_type)

    def __mul__(self, x):

        if isinstance(x, (int, float)):
            value = (
                self.value * x
                if self.__value_not_seq
                else [i.value * x for i in iter(self.value)]
            )
            return self.create_unit(unit=self.unit_type, value=value)

        elif isinstance(x, DerivedQuantity):
            value = (
                self.value * x.value
                if self.__value_not_seq
                else [i.value * x.value for i in iter(self.value)]
            )
            unit_definition = self.unit_type * x.unit_type
            return DerivedQuantity(value=value, unit_definition=unit_definition)

        elif isinstance(x, _DimensionType):
            is_same_dimension = self.dimension == x.dimension
            is_same_unit = (
                (self.unit_type._unit_name == x.unit_type._unit_name)
                if is_same_dimension
                else False
            )
            need_conversion = is_same_dimension and (not is_same_unit)

            if need_conversion:
                equiv = x.convert_to(self.unit_type).value
                x_unit = self.unit_type
            else:
                equiv = x.value
                x_unit = x.unit_type

            if self.__value_not_seq:
                value = (
                    self.value * equiv
                    if isinstance(equiv, (int, float))
                    else [self.value * i.value for i in iter(equiv)]
                )
            else:
                value = [
                    i.value * (equiv if isinstance(equiv, (int, float)) else equiv)
                    for i in iter(self.value)
                ]

            unit_definition = self.unit_type * x_unit
            return DerivedQuantity(value=value, unit_definition=unit_definition)

        raise TypeError(f"cannot multiply quantity by {type(x)}")

    def __truediv__(self, x):

        if isinstance(x, (int, float)):
            value = (
                self.value / x
                if self.__value_not_seq
                else [i.value / x for i in iter(self.value)]
            )
            return self.create_unit(value=value, unit=self.unit_type)

        elif isinstance(x, _DimensionType):
            is_same_dimension = self.dimension == x.dimension
            is_same_unit = (
                (self.unit_type._unit_name == x.unit_type._unit_name)
                if is_same_dimension
                else False
            )

            if is_same_dimension and is_same_unit:
                if self.__value_not_seq and isinstance(x.value, (int, float)):
                    return self.value / x.value
                self_vals = (
                    [self.value]
                    if self.__value_not_seq
                    else [i.value for i in iter(self.value)]
                )
                x_vals = (
                    [x.value]
                    if isinstance(x.value, (int, float))
                    else [i.value for i in iter(x.value)]
                )
                result = np.array([a / b for a, b in zip(self_vals, x_vals)])
                return result if len(result) > 1 else float(result[0])

            if is_same_dimension and not is_same_unit:
                x_conv = x.convert_to(self.unit_type)
                if self.__value_not_seq and isinstance(x_conv.value, (int, float)):
                    return self.value / x_conv.value
                self_vals = (
                    [self.value]
                    if self.__value_not_seq
                    else [i.value for i in iter(self.value)]
                )
                x_vals = (
                    [x_conv.value]
                    if isinstance(x_conv.value, (int, float))
                    else [i.value for i in iter(x_conv.value)]
                )
                result = np.array([a / b for a, b in zip(self_vals, x_vals)])
                return result if len(result) > 1 else float(result[0])

            value = (
                self.value / x.value
                if self.__value_not_seq
                else [i.value / x.value for i in iter(self.value)]
            )
            return DerivedQuantity(
                value=value, unit_definition=self.unit_type / x.unit_type
            )

        elif isinstance(x, DerivedQuantity):
            value = (
                self.value / x.value
                if self.__value_not_seq
                else [i.value / x.value for i in iter(self.value)]
            )
            return DerivedQuantity(
                value=value, unit_definition=self.unit_type / x.unit_type
            )

        raise TypeError(f"cannot divide quantity by {type(x)}")

    def __rtruediv__(self, x):
        if isinstance(x, (int, float)):
            value = (
                x / self.value
                if self.__value_not_seq
                else [x / i.value for i in iter(self.value)]
            )
            return DerivedQuantity(value=value, unit_definition=x / self.unit_type)
        raise TypeError(f"cannot divide {type(x)} by quantity")

    def __pow__(self, x):
        if isinstance(x, (int, float)):
            value = (
                self.value**x
                if self.__value_not_seq
                else [i.value**x for i in iter(self.value)]
            )
            unit_definition = self.unit_type**x
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )
        raise exceptions.DimensionError(
            f"cannot operate on {self.unit_type._dimension} and {type(x)}"
        )


# ==========================================================================================
# Fundamental dimension classes
# ==========================================================================================
class Length(_DimensionType):
    _conversion_standards = _LENGTH_CONVERSION_TABLE
    _dimension = LENGTH
    _base_unit_standard = METER

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


class Mass(_DimensionType):
    _conversion_standards = _MASS_CONVERSION_TABLE
    _dimension = MASS
    _base_unit_standard = GRAM

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


class Time(_DimensionType):
    _conversion_standards = _TIME_CONVERSION_TABLE
    _dimension = TIME
    _base_unit_standard = SECOND

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


class Temperature(_DimensionType):
    _conversion_standards = _TEMPERATURE_CONVERSION_TABLE
    _dimension = THERMODYNAMIC_TEMPERATURE
    _base_unit_standard = KELVIN

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


class Angle(_DimensionType):
    _conversion_standards = _ANGLE_CONVERSION_TABLE
    _dimension = PLANE_ANGLE

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


class GenericUnit(_DimensionType):
    def __init__(self, value, unit):
        self._dimension = unit._dimension
        super().__init__(unit=unit, value=value)


SolidAngle = functools.partial(GenericUnit, unit=STERADIAN)
ElectricCurrent = functools.partial(GenericUnit, unit=AMPERE)
AmountOfSubstance = functools.partial(GenericUnit, unit=MOLE)
LuminousIntensity = functools.partial(GenericUnit, unit=CANDELA)


# ==========================================================================================
# Derived-quantity classes
# ==========================================================================================
class Force(DerivedQuantity):
    _conversion_standards = _FORCE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=FORCE)


class Speed(DerivedQuantity):
    _conversion_standards = _SPEED_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=SPEED)


class Pressure(DerivedQuantity):
    _conversion_standards = _PRESSURE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=PRESSURE)


class Energy(DerivedQuantity):
    _conversion_standards = _ENERGY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=ENERGY)


class Density(DerivedQuantity):
    _conversion_standards = _DENSITY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=DENSITY)


class Power(DerivedQuantity):
    _conversion_standards = _POWER_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=POWER)


class Radioactivity(DerivedQuantity):
    _conversion_standards = _RADIOACTIVITY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=RADIOACTIVITY)


class AbsorbedDose(DerivedQuantity):
    _conversion_standards = _ABSORBED_DOSE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=ABSORBED_DOSE)


class DoseEquivalent(DerivedQuantity):
    _conversion_standards = _DOSE_EQUIVALENT_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=DOSE_EQUIVALENT)


class GenericUnit2(DerivedQuantity):
    def __init__(self, value, unit_definition):
        super().__init__(
            unit_definition=unit_definition,
            value=value,
            quantity=unit_definition._quantity,
        )


Voltage = functools.partial(GenericUnit2, unit_definition=VOLT)
Capacitance = functools.partial(GenericUnit2, unit_definition=FARAD)
Inductance = functools.partial(GenericUnit2, unit_definition=HENRY)
MagneticFlux = functools.partial(GenericUnit2, unit_definition=WEBER)
Resistance = functools.partial(GenericUnit2, unit_definition=OHMS)
Conductance = functools.partial(GenericUnit2, unit_definition=SIEMENS)
MagneticFieldStrength = functools.partial(GenericUnit2, unit_definition=TESLA)
Illuminance = functools.partial(GenericUnit2, unit_definition=LUX)


class custom_unit(DerivedQuantity):
    """Custom compound units, e.g. `custom_unit(5, num=[NEWTON], per=[METER, SECOND])`.

    NOTE: experimental -- `convert_to` is not yet implemented for compound
    custom units.
    """

    def __init__(
        self,
        value: int | float,
        *,
        num: abc.Sequence,
        per: abc.Sequence = (1,),
        quantity=GENERIC_QUANTITY,
    ):
        self.__numerator = []
        self.__denominator = []

        self.__numerator_unit = self.__list2unit(num, allow_int=False)
        self.__denominator_unit = self.__list2unit(per, allow_int=True)
        self.__numerator.append(num)
        self.__denominator.append(per)
        self.__unit_definition = self.__numerator_unit / self.__denominator_unit
        super().__init__(
            value=value, unit_definition=self.__unit_definition, quantity=quantity
        )

    def __check_condition(self, _from, allow_int=False):
        if not isinstance(_from, abc.Sequence):
            raise ValueError("numerator or denominator must be a sequence of units")
        elif allow_int is False and not all(
            isinstance(x, _UnitType) for x in list(_from)
        ):
            raise ValueError("numerator sequence must contain one or more units")
        elif allow_int is True and not all(
            isinstance(x, (_UnitType, int)) for x in list(_from)
        ):
            raise ValueError("denominator sequence must contain integers or units")

    def __list2unit(self, _from, allow_int=False):
        _to = 1
        self.__check_condition(_from, allow_int)
        self.__repr_only_one_quantity(_from, is_denum=allow_int)
        for unit in _from:
            _to = _to * unit
        return _to

    def __repr_only_one_quantity(self, _from, is_denum=False):
        quantities = [x._quantity for x in _from if isinstance(x, _UnitType)]
        counts = Counter(quantities)
        duplicates = [s for s, c in counts.items() if c > 1]
        if duplicates:
            err_str = f"duplicate quantities are not allowed: {counts}"
            raise ValueError(
                "Numerator: " + err_str if not is_denum else "Denominator: " + err_str
            )

    def convert_to(self, _to=None, **kwargs):
        raise NotImplementedError(
            "custom_unit is an experimental feature; convert_to has not been "
            "implemented for compound custom units yet"
        )


# ============================================================================
# Public extension API (Phase 1.5)
#
# Previously, extending mudu with a new unit required directly
# instantiating underscore-prefixed "private" classes (_UnitType) and
# calling ._conversion_standards.extend(...) with a hand-built tuple. That
# is no longer necessary and is not the 'right' way. Instead, use the two functions
# below. Internal classes remain available for backward
# compatibility but are not the supported extension surface going forward.
# ============================================================================
def define_unit(
    dimension_class: type[_DimensionUnitBase],
    name: str,
    symbol: str,
    quantity: str | None = None,
) -> _UnitType:
    """Define a new unit belonging to an existing mudu dimension (e.g. `Length`).

    Parameters
    ----------
    dimension_class: type
        One of mudu's dimension classes (`Length`, `Mass`, `Force`, ...).
    name: str
        Unique unit name within this dimension's quantity.
    symbol: str
        Display/symbolic representation of the unit.
    quantity: str, optional
        Defaults to the dimension class's own `_quantity`/table quantity
        where inferable.

    Returns
    -------
    _UnitType
        Pass this straight into the dimension class, e.g.
        ``Length(12, my_new_unit)``. To make it convertible to/from other
        units of the same dimension, follow up with `register_conversion`.
    """

    table = dimension_class._conversion_standards
    if table is None:
        raise exceptions.ConversionError(
            f"{dimension_class.__name__} has no conversion table to attach a unit to"
        )

    inferred_quantity = quantity
    if inferred_quantity is None:
        inferred_quantity = table.base_unit._quantity

    return _UnitType(
        _dimension=(
            dimension_class._dimension
            if dimension_class._dimension is not None
            else table.dimension
        ),
        _unit_name=name,
        _unit_symbol=symbol,
        _quantity=inferred_quantity,
    )


def register_conversion(
    dimension_class: type[_DimensionUnitBase],
    unit: _UnitType,
    conversion: Linear | Affine,
) -> None:
    """Register how `unit` converts to/from `dimension_class`'s canonical
    base unit.

    - **Usage example**

        .. code-block:: python

            from mudu import Length, define_unit, register_conversion, Linear

            SMOOT = define_unit(Length, name="smoot", symbol="smoot")
            register_conversion(Length, SMOOT, Linear(1.7018))  # 1 smoot = 1.7018 m

            Length(1, SMOOT).convert_to(METER)  # -> 1.7018 m
    """

    table = dimension_class._conversion_standards
    if table is None:
        raise exceptions.ConversionError(
            f"{dimension_class.__name__} has no conversion table to register against"
        )
    table.register(unit, conversion)


def audit_units(*tables: _ConversionTableType) -> list[str]:
    """Scan one or more conversion tables for bugs
    such as duplicate unit names within a dimension's table,
    and units registered under a table whose dimension
    they do not actually match.
    Returns a list of human-readable problem descriptions;
    an empty list means the tables passed are clean.

    Intended to run in CI against every conversion table shipped with
    mudu, and against any tables a downstream project builds via
    `define_unit`/`register_conversion`.
    """

    problems: list[str] = []

    for table in tables:
        seen_names = {table.base_unit._unit_name: table.base_unit}
        for unit_name, conversion in table.table.items():
            if unit_name in seen_names and seen_names[unit_name] is not None:
                problems.append(
                    f"duplicate unit name {unit_name!r} in table for "
                    f"dimension {table.dimension}"
                )
            seen_names[unit_name] = None
            if not isinstance(conversion, (Linear, Affine)):
                problems.append(
                    f"unit {unit_name!r} has a conversion of unexpected type "
                    f"{type(conversion)}; expected Linear or Affine"
                )

    return problems
