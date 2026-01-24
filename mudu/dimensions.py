"""
=========================
mudu.dimensions
=========================

mudu module, defines dimensions (quantities).

For more information, read the documenation using

.. code-block:: shell
    mudu --doc
    
in your cli

"""

import operator
from collections import abc, Counter
from typing import Any, Callable, Self
import functools

import sympy as sym
import numpy as np

from .base import (
    GENERIC_QUANTITY,
    _SetOnce,
    _UnitType,
    _ConversionTableType,
    LENGTH,
    MASS,
    TIME,
    THERMODYNAMIC_TEMPERATURE,
    PLANE_ANGLE,
    SPEED,
    FORCE,
    PRESSURE,
    ENERGY,
    DENSITY,
    POWER,
    RADIOACTIVITY,
    ABSORBED_DOSE,
    DOSE_EQUIVALENT,
)

from .units import (
    METER,
    GRAM,
    KELVIN,
    SECOND,
    STERADIAN,
    AMPERE,
    MOLE,
    CANDELA,
    VOLT,
    FARAD,
    HENRY,
    WEBER,
    OHMS,
    SIEMENS,
    TESLA,
    LUX,
    _LENGTH_CONVERSION_TABLE,
    _MASS_CONVERSION_TABLE,
    _TIME_CONVERSION_TABLE,
    _ANGLE_CONVERSION_TABLE,
    _TEMPERATURE_CONVERSION_TABLE,
    _FORCE_CONVERSION_TABLE,
    _PRESSURE_CONVERSION_TABLE,
    _ENERGY_CONVERSION_TABLE,
    _DENSITY_CONVERSION_TABLE,
    _POWER_CONVERSION_TABLE,
    _RADIOACTIVITY_CONVERSION_TABLE,
    _ABSORBED_DOSE_CONVERSION_TABLE,
    _DOSE_EQUIVALENT_TABLE,
    _SPEED_CONVERSION_TABLE,
)
from . import exceptions

def _unit_conversion(self, _to):
    """Converts from one unit to another, provided that there is a conversion standard
    defined for the units involved.

    Parameters
    ----------
    unit_type: _UnitType
        The _UnitType instance to be converted to.

    return: _DimensionType object with the `unit_type` as the unit.
    """
    
    @property
    def __value_not_seq(self):
        """ value is not a sequence"""
        return isinstance(self.value, (int, float))

    if self._conversion_standards is None:
        raise exceptions.ConversionError("this quantity has no conversion unit defined")

    if isinstance(_to, _UnitType) is True:

        new_value = object()
        try:
            if self.dimension != _to._dimension:
                raise exceptions.DimensionError(
                    f"Cannot convert {self.dimension} dimension to {_to._dimension} dimension."
                )

            elif self.dimension == _to._dimension:
                # check conversion table and do the needful
                _from, to, value = None, None, None

                # check if self a derived (quantity) unit
                base_unit = self.unit_type._base
                if base_unit is not None:
                    base_unit = base_unit
                else:
                    base_unit = self.unit_type

                # check if to is also a derived (quantity) unit
                to_base_unit = _to._base
                if to_base_unit is not None:
                    to_base_unit = to_base_unit
                else:
                    to_base_unit = _to

                # check if self is a multiple of other unit
                _order = self.unit_type._order
                if _order is None:
                    _multiple = 1
                else:
                    _multiple = _order.value

                # check if to is a multiple of other unit
                to_order = _to._order
                if to_order is None:
                    to_multiple = 1
                else:
                    to_multiple = to_order.value

                # converting between the same unit and multiple prefix
                if _to == self.unit_type:
                    return self.create_unit(unit=self.unit_type, value=self.value)
                    
                # converting between the same unit but different multiple prefix
                elif to_base_unit == base_unit:
                    if __value_not_seq is True: value = (self.value * _multiple) / to_multiple
                    else:
                        value = [
                            (i.value * _multiple) / to_multiple \
                            for i in iter(self.value)
                        ]
                    return self.create_unit(unit=base_unit, value=value)
                
                # conversion between different units with or without
                for _conv_std in self._conversion_standards.conversion_table:
                    (_from, to), value = _conv_std

                    if (base_unit, to_base_unit) == (
                        _from,
                        to,
                    ):
                        if __value_not_seq is True:
                            new_value = value(x=(self.value * _multiple)) / to_multiple
                        else:
                            new_value = [
                                value(x=(i.value * _multiple)) / to_multiple \
                                for i in iter(self.value)
                            ]

                    elif (base_unit, to_base_unit) == (
                        to,
                        _from,
                    ):
                        if __value_not_seq is True:
                            new_value = (
                                value(x=(_multiple * self.value), invert=True)
                                / to_multiple
                            )
                        else:
                            new_value = [
                                value(x=(_multiple * i.value), invert=True)
                                / to_multiple \
                                for i in iter(self.value)
                            ]

                    continue

                return self.create_unit(unit=_to, value=new_value)

        except Exception as e:
            raise exceptions.ConversionError(str(e))
    else:
        raise exceptions.ConversionError(
            f"conversion can only be made to a valid unit type"
        )


class _DimensionUnitBase:
    """
    Base class for all dimensions model.

    Attributes
    ----------
    _conversion_standards: _ConversionTableType
        Conversion table definition of conversion standards for converting
        from one unit to another provided that the units are of the same dimension.
    _dimension: str
        The dimension represented by the dimension model e.g. `METER`, `LENGTH`, `TIME`
    _check_and_convert: _DimensionUnitBase | int | float | bool
        Performs an arithemetic or boolean operation on a `_DimensionUnitBase` child object.
        Makes sure of unit homogeniety by implicitly converting units where required before
        performing the operation.
    convert_to: _DimensionUnitBase | bool
        Converts from one unit to another, provided that there is a conversion standard
        defined for the units involved.
    """

    _conversion_standards: _ConversionTableType = None
    _dimension: str = None

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
        pass

    def __rmul__(self, x):
        return self.__mul__(x)

    def __truediv__(self, x):
        pass

    def __rtruediv__(self, x):
        pass

    def __floordiv__(self, x):
        return float(int(self.__truediv__(x=x)))

    def __rfloordiv__(self, x):
        return float(int(self.__rtruediv__(x)))

    def __pow__(self, x):
        pass

    def __round__(self, y=0):
        pass

    def __lt__(self, x):
        return self._check_and_convert(x, _operator=operator.lt)

    def __gt__(self, x):
        return self._check_and_convert(x, _operator=operator.gt)

    def __le__(self, x):
        return self._check_and_convert(x, _operator=operator.le)

    def __ge__(self, x):
        return self._check_and_convert(x, _operator=operator.ge)

    def __eq__(self, x):
        return self._check_and_convert(x, _operator=operator.eq)

    def _check_and_convert(
        self, x: Any, _operator: Callable
    ) -> Self | bool | (int | float):
        """Performs an arithemetic or boolean operation on a `_DimensionUnitBase` child object.
        Makes sure of unit homogeniety by implicitly converting units where required before
        performing the operation.

        Parameters
        ----------
        x: Any
            Object to perform operation on.
        _operator: Callable
            Operator representing operation to be performed

        return: _DimensionUnitBase | bool | int | float
        """

        pass

    def convert_to(self, _to: _UnitType):
        """Converts from one unit to another, provided that there is a conversion standard
        defined for the units involved.

        Parameters
        ----------
        unit_type: _UnitType
            The _UnitType instance to be converted to.

        return: _DimensionUnitBase object with the `unit_type` as the unit.
        """

        pass


class DerivedQuantity(_DimensionUnitBase):
    """Base class for all derived quantities.  As an example,
    `Force` class is a child class of `DerivedQuantity`. Check
    the documenation at by running `mudu --doc` on the cli
    on how to extend this class.

    Attributes
    ----------
    _conversion_standards: _ConversionTableType
        Same as in `_DimensionUnitBase`
    _dimension: str
        Same as in  `DimensionUnitBase`
    value: _SetOnce[int | float]
        Scalar value of the quantity
    unit_type: _UnitType
        unit definition of the quantity
    symbol: sympy.Symbol
        Symbolic representation of the quantity unit
    create_unit: DerivedQuantity
        Internal class method for creating a new DerivedQuantity object instance
        with the same argument signature as init.
    _check_and_convert: x: Any, operator: Callable
        same as the base class  ((_DimensionUnitBase))
    convert_to: _to
        same as the base class (_DimensionUnitBase)
    """

    _conversion_standards: _ConversionTableType = None

    value = _SetOnce(
        "value",
        (
            int,
            float,
            abc.Sequence,
            np.ndarray,
        ),
    )
    unit_type = _SetOnce("unit_type", _UnitType)
    symbol = _SetOnce("symbol", sym.Basic)
    quantity: str = _SetOnce("quantity", str)

    @classmethod
    def create_unit(cls, **kwargs):
        """Internal class method to create a new DerivedQuantity object,
        the same argument signature as init.
        """

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
                    f"{self.unit_type._unit_name} is not a unit of {self._dimension}"
                )
            
        if isinstance(value, (abc.Sequence, np.ndarray)):
            self.value = np.array(
                [
                    self.create_unit(
                        unit_definition=unit_definition, value=i
                    ) for i in value
                ]
            )
        elif isinstance(value, (int, float)):
            self.value = value

    @property
    def __value_not_seq(self):
        """value is not a sequence"""
        return isinstance(self.value, (int, float))

    def __repr__(self):

        return f"{self.value} {self.symbol}" if self.__value_not_seq is True \
        else f"{self.value}"

    def __str__(self):

        if self.__value_not_seq is True:
            return f"{self.value} {self.symbol}"
        else:
            return f"{self.value}"
        
    def __len__(self):

        if self.__value_not_seq is False: return len(self.value)
        return 1

    def __iter__(self):
        if self.__value_not_seq is False: 
            return iter(self.value)
        else:
            return iter([self.value])
        #raise exceptions.NotIterableError(f"Iteration is only supported for sequence value entries")

    def __round__(self, y=0):

        if self.__value_not_seq is True:
            value = round(self.value, y)
        else:
            value = [
                round(i, y).value for i in iter(self.value)
            ]

        return self.create_unit(
            value=value, unit_definition=self.unit_type
        )

    def __mul__(self, x):

        if (
            isinstance(x, (DerivedQuantity, _DimensionType)) is True
        ):  

            if self.__value_not_seq is True:
                if isinstance(x.value, (int, float)):
                    value = self.value * x.value
                else:   # x is a sequence
                    value = [
                        i.value * self.value for i in iter(x.value)
                        ]
            else: # self.value is sequence
                value = [
                    i.value * x.value for i in iter(self.value)
                    ]

            unit_definition = self.unit_type * x.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)) is True:
            value = self.value * x if self.__value_not_seq else [i.value * x for i in iter(self.value)]

            return DerivedQuantity.create_unit(
                value=value, unit_definition=self.unit_type
            )

    def __truediv__(self, x):

        if isinstance(x, DerivedQuantity) is True:

            if self.unit_type._dimension == x.unit_type._dimension:  # e.g Force / Force

                if self.unit_type == x.unit_type:
                    if self.__value_not_seq is True: return self.value / x.value  # return a scalar
                    else:
                        return np.array([
                            i.value / x.value for i in iter(self.value)
                        ])
                    
                else:
                    if self.__value_not_seq is True: value = self.value / x.value
                    else:
                        value = [
                            i.value / x.value for i in iter(self.value)
                        ]
                        
                    unit_definition = self.unit_type / x.unit_type
                    return DerivedQuantity.create_unit(
                        value=value, unit_definition=unit_definition
                    )
            else:
                
                if self.__value_not_seq is True: value = self.value / x.value
                else:
                    value = [
                        i.value / x.value for i in iter(self.value)
                    ]

                unit_definition = self.unit_type / x.unit_type
                return DerivedQuantity.create_unit(
                    value=value, unit_definition=unit_definition
                )

        elif isinstance(x, _DimensionType) is True:
            
            if self.__value_not_seq is True: value = self.value / x.value
            else:
                value = [
                    i.value / x.value for i in iter(self.value)
                ]
            
            unit_definition = self.unit_type / x.unit_type
            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)) is True:

            value = [
                i.value / x for i in iter(self.value)
            ] if self.__value_not_seq is False else self.value / x

            return DerivedQuantity.create_unit(
                value=value, unit_definition=self.unit_type
            )

    def __rtruediv__(self, x):

        if isinstance(x, DerivedQuantity) is True:

            if self.unit_type._dimension == x.unit_type._dimension:  # e.g Force / Force

                if self.unit_type != x.unit_type:
                    # e.g. Newton * Dyne -> coerce to Newton
                    pass
                elif self.unit_type == x.unit_type:
                    return [
                        x.value / i.value for i in iter(self.value)
                    ] if self.__value_not_seq is False else x.value / self.value  # return a scalar
                else:
                    value = x.value / self.value if self.__value_not_seq is True else [
                        x.value / i.value for i in iter(self.value)
                    ]
                    unit_definition = x.unit_type / self.unit_type

                    return DerivedQuantity.create_unit(
                        value=value, unit_definition=unit_definition
                    )
            else:
                # e.g. Force * Area
                value = x.value / self.value if self.__value_not_seq is True else [
                    x.value / i.value for i in iter(self.value)
                ]
                unit_definition = x.unit_type / self.unit_type

                return DerivedQuantity.create_unit(
                    value=value, unit_definition=unit_definition
                )

        elif isinstance(x, _DimensionType) is True:

            value = x.value / self.value if self.__value is True else [
                x.value / i.value for i in iter(self.value)
            ]
            unit_definition = x.unit_type / self.unit_type

            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )

        elif isinstance(x, (int, float)) is True:
            value = x / self.value if self.__value_not_seq is True else [
                x / i.value for i in iter(self.value)
            ]
            return DerivedQuantity.create_unit(
                value=value, unit_definition=x / self.unit_type
            )

    def __pow__(self, x):

        if isinstance(x, (int, float)) is True:
            value = self.value**x if self.__value_not_seq is True else [
                i.value**x for i in iter(self.value)
            ]
            unit_definition = self.unit_type**x

            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )
        else:
            raise exceptions.DimensionError(
                f"cannot operate on {self.unit_type._dimension} and {type(x)}"
            )

    def _check_and_convert(self, x, _operator: Callable) -> Self:
        """Performs an arithemetic or boolean operation on a DerivedQuantity child object.
        Makes sure of unit homogeniety by implicitly converting units where required before
        performing the operation.

        Parameters
        ----------
        x: Any
            Object to perform operation on.
        _operator: Callable
            Operator representing operation to be performed

        return: DerivedQuantity | bool | int | float
        """

        if isinstance(x, DerivedQuantity):

            if self.unit_type._dimension != x.unit_type._dimension:
                # operation between different quantities, not accepted
                raise exceptions.DimensionError(
                    f"cannot operate between quantities of {self.unit_type._dimension} and {x.unit_type._dimension}"
                )

            elif self.unit_type._dimension == x.unit_type._dimension:
                # the operand represent the same quantity say Force and Force

                if self.unit_type != x.unit_type:
                    # the operands have rep same quantity but are of different units, e.g. Newton and Dyne

                    _equivalent_obj = x.convert_to(self.unit_type)
                    _value = _equivalent_obj.value
                    del _equivalent_obj
                else:
                    _value = x.value

                new_value = _operator(self.value, _value)

                if isinstance(new_value, bool) is True:
                    return new_value

                else:
                    return DerivedQuantity.create_unit(
                        value=new_value,
                        unit_definition=self.unit_type,
                    )

        elif isinstance(x, (int, float)) is True:
            # explicit is better than implicit afterall
            new_value = _operator(self.value, x)

            if isinstance(new_value, bool) is True:
                return new_value

            else:
                return new_value  # should be scalar or dimensionless

        else:
            # all sort of dimensional inhomogeniety
            raise exceptions.DimensionError(
                f"cannot operate on {self.unit_type._dimension} and {x.unit_type._dimension} dimensions."
            )

    def convert_to(self, _to) -> Self | None:
        """Converts from one unit to another, provided that there is a conversion standard
        defined for the units involved.

        Parameters
        ----------
        unit_type: _UnitType
            The _UnitType instance to be converted to.

        return: _DimensionType object with the `unit_type` as the unit.
        """
        
        if self._conversion_standards is None:
            raise exceptions.ConversionError("this quantity has no conversion unit defined")

        if isinstance(_to, _UnitType) is True:

            new_value = object()
            try:
                if self.dimension != _to._dimension:
                    raise exceptions.DimensionError(
                        f"Cannot convert {self.dimension} dimension to {_to._dimension} dimension."
                    )

                elif self.dimension == _to._dimension:
                    # check conversion table and do the needful
                    _from, to, value = None, None, None

                    # check if self a derived (quantity) unit
                    base_unit = self.unit_type._base
                    if base_unit is not None:
                        base_unit = base_unit
                    else:
                        base_unit = self.unit_type

                    # check if to is also a derived (quantity) unit
                    to_base_unit = _to._base
                    if to_base_unit is not None:
                        to_base_unit = to_base_unit
                    else:
                        to_base_unit = _to

                    # check if self is a multiple of other unit
                    _order = self.unit_type._order
                    if _order is None:
                        _multiple = 1
                    else:
                        _multiple = _order.value

                    # check if to is a multiple of other unit
                    to_order = _to._order
                    if to_order is None:
                        to_multiple = 1
                    else:
                        to_multiple = to_order.value

                    # converting between the same unit and multiple prefix
                    if _to == self.unit_type:
                        return self.create_unit(unit_definition=self.unit_type, value=self.value)
                        
                    # converting between the same unit but different multiple prefix
                    elif to_base_unit == base_unit:
                        if self.__value_not_seq is True: value = (self.value * _multiple) / to_multiple
                        else:
                            value = [
                                (i.value * _multiple) / to_multiple \
                                for i in iter(self.value)
                            ]
                        return self.create_unit(unit_definition=base_unit, value=value)
                    
                    # conversion between different units with or without
                    for _conv_std in self._conversion_standards.conversion_table:
                        (_from, to), value = _conv_std

                        if (base_unit, to_base_unit) == (
                            _from,
                            to,
                        ):
                            if self.__value_not_seq is True:
                                new_value = value(x=(self.value * _multiple)) / to_multiple
                            else:
                                new_value = [
                                    value(x=(i.value * _multiple)) / to_multiple \
                                    for i in iter(self.value)
                                ]

                        elif (base_unit, to_base_unit) == (
                            to,
                            _from,
                        ):
                            if self.__value_not_seq is True:
                                new_value = (
                                    value(x=(_multiple * self.value), invert=True)
                                    / to_multiple
                                )
                            else:
                                new_value = [
                                    value(x=(_multiple * i.value), invert=True)
                                    / to_multiple \
                                    for i in iter(self.value)
                                ]

                        continue

                    return self.create_unit(unit_definition=_to, value=new_value)

            except Exception as e:
                raise exceptions.ConversionError(str(e))
        else:
            raise exceptions.ConversionError(
                f"conversion can only be made to a valid unit type"
            )


# _DimensionType for fundamental quantities
class _DimensionType(_DimensionUnitBase):
    """Base class for all fundamental quantities.  As an example,
    `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
    the documenation at by running `mudu --doc` on the cli
    on how to extend this class.

    Attributes
    ----------
    _conversion_standards: _ConversionTableType
        Same as in `_DimensionUnitBase`
    _dimension: str
        Same as in  `DimensionUnitBase`
    value: _SetOnce[int | float]
        Scalar value of the quantity
    unit_type: _UnitType
        unit definition of the quantity
    symbol: sympy.Symbol
        Symbolic representation of the quantity unit
    create_unit: _DimensiionType
        Internal class method for creating a new DerivedQuantity object instance
        with the same argument signature as init.
    _check_and_convert: x: Any, operator: Callable
        same as the base class  (_DimensionUnitBase)
    convert_to: _to
        same as the base class (_DimensionUnitBase)
    """

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

    def __init__(
        self,
        unit: _UnitType,
        value: int | float | abc.Sequence,
    ) -> None:

        self.unit_type = unit
        self.dimension = unit._dimension

        if self._dimension != self.dimension:
            raise exceptions.DimensionError(
                f"{unit._unit_name} is not a unit of {self._dimension}"
            )

        self.unit = unit._unit_name
        self.symbol = unit._unit_symbol

        if isinstance(value, abc.Sequence):
            self.value = np.array(
                [
                    self.create_unit(
                        unit=unit, value=i
                    ) for i in value
                ]
            )
        elif isinstance(value, (int, float)):
            self.value = value

    @property
    def __value_not_seq(self):
        """ value is not a sequence"""
        return isinstance(self.value, (int, float))

    def __repr__(self):

        return f"{self.value} {self.symbol}" if self.__value_not_seq is True \
        else f"{self.value}"
    
    def __str__(self):
            
        return f"{self.value} {self.symbol}" if self.__value_not_seq is True \
        else f"{self.value}"
        
    def __len__(self):

        return 1 if self.value is True else len(self.value)
    
    def __iter__(self):
        if self.__value_not_seq is False:
            return iter(self.value)
        else:
            return iter([self.value])
        
        # raise exceptions.NotItera(f"Iteration is only supported for sequence value entries")

    def __round__(self, y=0):

        value = round(self.value, y) if self.__value_not_seq is True \
        else [round(i, y).value for i in iter(self.value)]

        return self.create_unit(value=value, unit=self.unit_type)

    def __mul__(self, x):

        # multiplication of unit by a non-unit (scalar)
        if isinstance(x, (int, float)) is True:

            value = value = self.value * x if self.__value_not_seq is True \
            else [(i.__mul__(x)).value for i in iter(self.value)]

            return self.create_unit(unit=self.unit_type, value=value)
        
        # multiplication by a derived quantity
        elif isinstance(x, DerivedQuantity) is True:

            value = self.value * x.value if self.__value_not_seq is True \
            else [
                (i.value) * (x.value) for i in iter(self.value)
                ]
            unit_definition = self.unit_type * x.unit_type

            return DerivedQuantity(value=value, unit_definition=unit_definition)

        elif isinstance(x, _DimensionType) is True:
            # multiplication by _DimensionType

            # if self.unit_type._dimension == x.unit_type._dimension:
                # they are of the same dimension, e.g. LENGTH * LENGTH

            # are they of the same dimension
            is_same_dimension = self.dimension == x.dimension
            
            # are they of the same unit or not?
            # if they are of different dimensions, always return True
            is_same_unit = (self.unit_type._unit_name == x.unit_type._unit_name) if is_same_dimension else True

            # only is conversion is needed
            need_conversion = is_same_dimension and (not is_same_unit)
            equiv, x_unit = (x.convert_to(self.unit_type).value, self.unit_type) if need_conversion else (x.value, x.unit_type)

            if self.__value_not_seq is True:
                # self.value is an int | float
                if isinstance(x.value, (int, float)):
                    # x is an int or float
                    value = self.value * equiv
                else:
                    # assumes that self.value is not a sequence
                    value = [
                        i.value * self.value for i in iter(equiv)
                    ]
            else:
                # self.value is a sequence
                # assuming equiv is not an sequence which can be untrue
                value = [
                    i.value * equiv for i in iter(self.value)
                ]

            unit_definition = self.unit_type * x_unit
            return DerivedQuantity(value=value, unit_definition=unit_definition)

    def __truediv__(self, x):

        # unit divided by a scalar return an instance of _DimensionType
        if isinstance(x, (int, float)) is True:

            value = self.value / x if self.__value_not_seq is True \
            else [
                    i.value / x for i in iter(self.value)
                ]
            
            return self.create_unit(value=value, unit=self.unit_type)

        # unit divided by another unit (or same unit object)
        elif isinstance(x, _DimensionType) is True:

            # return dimensionless number (float) if they have the same dimension ( e.g. length/length)
            is_same_dimension = self.dimension == x.dimension

            is_same_unit =(self.unit_type._unit_name == x.unit_type._unit_name) if is_same_dimension else True

            need_conversion = is_same_dimension and (not is_same_unit)
            equiv, x_unit = (x.convert_to(self.unit_type).value, None) if need_conversion else (x.value, x.unit_type)

            if self.__value_not_seq is True:
                # self.value is int | float
                if isinstance(x.value, (int, float)):
                    value = self.value / x.value
                else:
                    value = [
                        i.value / self.value for i in iter(equiv)
                    ]
            else:
                value = [
                    i.value * equiv for i in iter(self.value)
                ]
                
            if x_unit  in (self.unit_type, None):
                return value if isinstance(value, (int, float)) else np.array(value)
            else:
                return DerivedQuantity(value=value, unit_definition=self.unit_type / x_unit)
        
        elif isinstance(x, DerivedQuantity):

            value = self.value / x.value if self.__value_not_seq is True \
            else [
                    i.value / x.value for i in iter(self.value)
                ]
            unit_definition = self.unit_type / x.unit_type

            return DerivedQuantity(value=value, unit_definition=unit_definition)

    def __rtruediv__(self, x):

        # scalar is divided by unit return an instance of derived quantity
        if isinstance(x, (int, float)) is True:
            value = x / self.value if self.__value_not_seq is True \
            else [
                    x / i.value for i in iter(self.value)
                ]
            
            return DerivedQuantity(value=value, unit_definition=x / self.unit_type)

    def __pow__(self, x):

        if isinstance(x, (int, float)) is True:
            value = self.value**x if self.__value_not_seq is True \
            else [
                    i.value**x for i in iter(self.value)
                ]
            unit_definition = self.unit_type**x

            return DerivedQuantity.create_unit(
                value=value, unit_definition=unit_definition
            )
        else:
            raise exceptions.DimensionError(
                f"cannot operate on {self.unit_type._dimension} and {type(x)}"
            )

    def _check_and_convert(
        self,
        x,
        _operator: Callable,
    ) -> Self | bool:
        """Performs an arithemetic or boolean operation on a _DimensionType object.
        Makes sure of unit homogeniety by implicitly converting units where required before
        performing the operation.

        Parameters
        ----------
        x: Any
            Object to perform operation on.
        _operator: Callable
            Operator representing operation to be performed

        return: _DimensionType | bool | int | float
        """

        if isinstance(x, _DimensionType) is True and self.dimension == x.dimension:
            # If its a fundamental quantity and they are of the same dimension
            # explicit is better than implicit afterall
            if x.unit_type != self.unit_type:
                _equivalent = x.convert_to(self.unit_type).value
                value = _operator(self.value, _equivalent)
                del _equivalent
                
            elif x.unit_type == self.unit_type:
                value = _operator(self.value, x.value)

            if isinstance(value, np.ndarray) is True:
                if value.dtype == bool: return value
                else: 
                    value = [int(i) for i in iter(value)]
                    return self.create_unit(value=value, unit=self.unit_type)
            else: return value
            

        elif isinstance(x, (int, float)):
            value = _operator(self.value, x)
            
            return value
        else:
            raise exceptions.DimensionError(
                f"cannot operate on {self.dimension} and {x.unit_type._dimension} dimensions."
            )

    def convert_to(self, _to) -> Self | None:
        """Converts from one unit to another, provided that there is a conversion standard
        defined for the units involved.

        Parameters
        ----------
        unit_type: _UnitType
            The _UnitType instance to be converted to.

        return: _DimensionType object with the `unit_type` as the unit.
        """
        
        if self._conversion_standards is None:
            raise exceptions.ConversionError("this quantity has no conversion unit defined")

        if isinstance(_to, _UnitType) is True:

            new_value = object()
            try:
                if self.dimension != _to._dimension:
                    raise exceptions.DimensionError(
                        f"Cannot convert {self.dimension} dimension to {_to._dimension} dimension."
                    )

                elif self.dimension == _to._dimension:
                    # check conversion table and do the needful
                    _from, to, value = None, None, None

                    # check if self a derived (quantity) unit
                    base_unit = self.unit_type._base
                    if base_unit is not None:
                        base_unit = base_unit
                    else:
                        base_unit = self.unit_type

                    # check if to is also a derived (quantity) unit
                    to_base_unit = _to._base
                    if to_base_unit is not None:
                        to_base_unit = to_base_unit
                    else:
                        to_base_unit = _to

                    # check if self is a multiple of other unit
                    _order = self.unit_type._order
                    if _order is None:
                        _multiple = 1
                    else:
                        _multiple = _order.value

                    # check if to is a multiple of other unit
                    to_order = _to._order
                    if to_order is None:
                        to_multiple = 1
                    else:
                        to_multiple = to_order.value

                    # converting between the same unit and multiple prefix
                    if _to == self.unit_type:
                        return self.create_unit(unit=self.unit_type, value=self.value)
                        
                    # converting between the same unit but different multiple prefix
                    elif to_base_unit == base_unit:
                        if self.__value_not_seq is True: value = (self.value * _multiple) / to_multiple
                        else:
                            value = [
                                (i.value * _multiple) / to_multiple \
                                for i in iter(self.value)
                            ]
                        return self.create_unit(unit=base_unit, value=value)
                    
                    # conversion between different units with or without
                    for _conv_std in self._conversion_standards.conversion_table:
                        (_from, to), value = _conv_std

                        if (base_unit, to_base_unit) == (
                            _from,
                            to,
                        ):
                            if self.__value_not_seq is True:
                                new_value = value(x=(self.value * _multiple)) / to_multiple
                            else:
                                new_value = [
                                    value(x=(i.value * _multiple)) / to_multiple \
                                    for i in iter(self.value)
                                ]

                        elif (base_unit, to_base_unit) == (
                            to,
                            _from,
                        ):
                            if self.__value_not_seq is True:
                                new_value = (
                                    value(x=(_multiple * self.value), invert=True)
                                    / to_multiple
                                )
                            else:
                                new_value = [
                                    value(x=(_multiple * i.value), invert=True)
                                    / to_multiple \
                                    for i in iter(self.value)
                                ]

                        continue

                    return self.create_unit(unit=_to, value=new_value)

            except Exception as e:
                raise exceptions.ConversionError(str(e))
        else:
            raise exceptions.ConversionError(
                f"conversion can only be made to a valid unit type"
            )


# ==========================================================================================
# Length dimension class
class Length(_DimensionType):
    _conversion_standards = _LENGTH_CONVERSION_TABLE
    _dimension = LENGTH
    _base_unit_standard = METER

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


# =========================================================================================
# Mass dimension class
class Mass(_DimensionType):
    _conversion_standards = _MASS_CONVERSION_TABLE
    _dimension = MASS
    _base_unit_standard = GRAM

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


# ========================================================================================
# Time dimension class
class Time(_DimensionType):
    _conversion_standards = _TIME_CONVERSION_TABLE
    _dimension = TIME
    _base_unit_standard = SECOND

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


# ========================================================================================
# Thermodynamic units
class Temperature(_DimensionType):
    _conversion_standards = _TEMPERATURE_CONVERSION_TABLE
    _dimension = THERMODYNAMIC_TEMPERATURE
    _base_unit_standard = KELVIN

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


# ========================================================================================
# Angle unit
class Angle(_DimensionType):
    _conversion_standards = _ANGLE_CONVERSION_TABLE
    _dimension = PLANE_ANGLE

    def __init__(self, value, unit):
        super().__init__(unit=unit, value=value)


# ====== Generic Unit Class========================================================
class GenericUnit(_DimensionType):
    def __init__(self, value, unit):
        self._dimension = unit._dimension
        super().__init__(unit=unit, value=value)
        

# Solid Angle in steradian
SolidAngle = functools.partial(GenericUnit, unit=STERADIAN)

# Electric Current
ElectricCurrent = functools.partial(GenericUnit, unit=AMPERE)

# Amount of Substance
AmountOfSubstance = functools.partial(GenericUnit, unit=MOLE)

# Luminous Intensity
LuminousIntensity = functools.partial(GenericUnit, CANDELA)
# =====================================================================================

# =========================================================================================
# Force
class Force(DerivedQuantity):
    _conversion_standards = _FORCE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=FORCE)


# ============================================================================================
# Speed and Velocity
class Speed(DerivedQuantity):
    _conversion_standards = _SPEED_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=SPEED)


# ============================================================================================
# Pressure
class Pressure(DerivedQuantity):
    _conversion_standards = _PRESSURE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=PRESSURE)


# ============================================================================================
# Energy
class Energy(DerivedQuantity):
    _conversion_standards = _ENERGY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=ENERGY)

# ============================================================================================
# Density
class Density(DerivedQuantity):
    _conversion_standards = _DENSITY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=DENSITY)


# ============================================================================================
# Power
class Power(DerivedQuantity):
    _conversion_standards = _POWER_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=POWER)


# ============================================================================================
# Radioactivity
class Radioactivity(DerivedQuantity):
    _conversion_standards = _RADIOACTIVITY_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=RADIOACTIVITY)


# ============================================================================================
# Absorbeddose
class AbsorbedDose(DerivedQuantity):
    _conversion_standards = _ABSORBED_DOSE_CONVERSION_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=ABSORBED_DOSE)


# ============================================================================================
# Dose Equivalent
class DoseEquivalent(DerivedQuantity):
    _conversion_standards = _DOSE_EQUIVALENT_TABLE

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity=DOSE_EQUIVALENT)


# ======================Generic Unit 2 =======================================================
class GenericUnit2(DerivedQuantity):
    def __init__(self, value, unit_definition):
        super().__init__(unit_definition=unit_definition, value=value, quantity=unit_definition._quantity)


# Voltage and Potential Difference
Voltage = functools.partial(GenericUnit2, unit_definition=VOLT)

# Capacitance
Capacitance = functools.partial(GenericUnit2, unit_definition=FARAD)

# Inductance
Inductance = functools.partial(GenericUnit2, unit_definition=HENRY)

# Magenetic Flux
MagneticFlux = functools.partial(GenericUnit2, unit_definition=WEBER)

# Resistance
Resistance = functools.partial(GenericUnit2, unit_definition=OHMS)

# Conductance
Conductance = functools.partial(GenericUnit2, unit_definition=SIEMENS)

# Magentic Field Strength
MageneticFieldStrength = functools.partial(GenericUnit2, unit_definition=TESLA)

# Illuminance
Illuminance = functools.partial(GenericUnit2, unit_definition=LUX)

# How about inheritance?
class custom_unit(DerivedQuantity):
    """Custom units"""
    
    __numerator_unit = 1
    __denominator_unit = 1
    __numerator = []
    __denominator = []

    def __init__(self,
                 value:(int|float),
                 *, 
                 num:abc.Sequence[_UnitType], # numerator (even a single numerator) must be passed as a sequence
                 per:(abc.Sequence[int] | abc.Sequence[_UnitType], )=(1, ), # denominator (even a single denominator) must be passed as a sequence
                 quantity=GENERIC_QUANTITY,
                 ):
        
        self.__numerator_unit = self.__list2unit(num, allow_int=False)
        self.__denominator_unit = self.__list2unit(per, allow_int=True)
        self.__numerator.append(num)
        self.__denominator.append(per)
        self.__unit_definition = self.__numerator_unit / self.__denominator_unit
        super().__init__(value=value, unit_definition=self.__unit_definition, quantity=quantity)

    def __check_condition(self, _from, allow_int=False):
        # there will be only two conditons:
        # there must be at least one unit each 
        # at the numerator and at the denominator (denominator could be an integer)
        if not isinstance(_from, abc.Sequence) is True:
            raise ValueError("numerator or denominator must be a sequence of units")
        elif allow_int is False and (not all([isinstance(x, _UnitType) for x in list(_from)])):
            # not all the input are units
            raise ValueError("numerator sequence must contain one or more units")
        elif allow_int is True and (not all([isinstance(x, (_UnitType, int)) for x in list(_from)])):
            # not all the units in the denominator are ints or unit
            raise ValueError("denominator sequence must contain intergers or units")

    def __list2unit(self, _from: int | abc.Sequence[_UnitType], 
                        allow_int=False):
        _to = 1
        self.__check_condition(_from, allow_int)
        self.__repr_only_one_quantity(_from, is_denum=allow_int)
        for unit in _from:
            _to = _to * unit
        
        return _to
    
    def __repr_only_one_quantity(self, _from: abc.Sequence, is_denum=False):
        """Ensure that each unit represent exclusively only one quanitity"""
        quantities = [x._quantity for x in _from]
        counts = Counter(quantities)
        duplicates = [s for s, c in counts.items() if c > 1]

        if duplicates:
            err_str = f"duplicate quantities are not allowed: {counts}"
            raise ValueError("Numerator: " + err_str if not is_denum else "Denonimator: "+ err_str)
    
    def convert_to(self, num:abc.Sequence, per:abc.Sequence):
        # first, map units with matching quantities
        # convert each unit first by multiplications or division
        # return output

        # check if the input are correct
        numerator_unit = self.__list2unit(num)
        denominator_unit = self.__list2unit(per, allow_int=True)

        # is the conversion operation to the right dimension
        if not (numerator_unit / denominator_unit)._dimension == self.__unit_definition._dimension:
            raise ValueError("conversion is only legal where the dimensions are legal")
        
        # map which units are affected
        print(self.__numerator)
        print(self.__denominator)

        



# make custom units from unit_config
# i.e make unit_config a class
# derived units can operated on by unit_config
# e.g class unit_config
# newton_per_meter = unit_config(num=newton, per=meter)
# dyne_per_inch = newton_per_meter.config(num=dyne, denum=inch)

# add other units and quantities to make it more robust
# make sure unit_config.config be the first method called before using any mudu object.
