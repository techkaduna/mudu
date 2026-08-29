# Usage Guide

This section provides a brief but comprehensive tutorial on how to use mudu and its features. The section is divided into two sub-sections:

- **Basic usage**: covers the basics of specifying units and dimensions as well as arithmetic operations using mudu
- **More usage**: which covers more advanced features such as registering new conversions and creating custom units and dimensions, etc.

## Prerequisites

To follow this tutorial and get the most out of it, it is assumed that readers have:

- Basic understanding of the Python programming language
- Secondary school (or equivalent) knowledge of dimensions and dimensional analysis

## Basic Usage

### Specifying units

To specify units, simply import the necessary dimensions and units, and create a dimension object.

```python
from mudu import Length, METER, INCH
from mudu import Time, SECOND, HOUR
from mudu import Force, NEWTON, DYNE
from mudu import Pressure, PASCAL, mmHg

# create a fundamental quantity
length = Length(12, INCH)

t0 = Time(2, HOUR)

# create a derived quantity
force = Force(1, NEWTON)

pressure = Pressure(12, PASCAL)
```

Objects like `Length`, `Mass`, `Time` are called `dimensions` while `METER`, `INCH` and `NEWTON` are called `units`. Also note that *dimensions are defined in title case*, while *units are defined in all caps*. For a more comprehensive list of dimensions and units, check the [API Reference](api.md) section.

### Unit conversion

Unit conversion is done by using the dimension `convert_to` method.

```python
length.convert_to(METER)

t0.convert_to(SECOND)

t0.convert_to(METER)    # does not make sense

# there is also support for conversion between some derived quantities
force.convert_to(DYNE)
pressure.convert_to(mmHg)

pressure.convert_to(NEWTON)     # definitely does not make sense
```

!!! note
    Converting between units representing different dimensions raises an `exceptions.DimensionError`.

The scalar value, symbol, dimension and quantity (for derived quantities) can also be accessed e.g.

```python
# for fundamental quantities
length.value    # -> 12
length.symbol   # -> in
length.dimension    # -> L

# for derived quantity
force.value # -> 1
force.quantity  # -> force
force.dimension # -> L*M/T**2
force.unit_type # -> N
```

!!! note
    `obj.dimension` returns a sympy `sympy.core` child object that represents the dimension of the unit, and in the case of derived quantities, it does a sort of dimensional analysis.

```python
velocity = length/t0
velocity.dimension  # -> L/T
```

### Operating with unit multiple prefixes

It is also possible to create units with multiples by specifying their multiple prefixes.

```python
from mudu import Length, METER, INCH, Force, NEWTON, KILO, MILLI, OrderUnit

# creating units in their multiples
KILONEWTON = OrderUnit(KILO, NEWTON)
MILLIMETER = OrderUnit(MILLI, METER)
KILOINCH = OrderUnit(KILO, INCH)    # if it makes sense to you

l = Length(1000, MILLIMETER)
F = Force(20, KILONEWTON)

area = l * l

# you can also convert units with multiples
l_in_meter = l.convert_to(METER)    # very valid
new_area = l_in_meter * l_in_meter

pressure = F / new_area
```

The `OrderUnit` is used to create units in their multiples, and supports the same operations as `_UnitType`. `KILO` and `MILLI` (and other multiple prefixes) are instances of `_OrderType`. See the [API Reference](api.md) page for more information.

## Arithmetic Operations

mudu objects also support arithmetic operations provided they are legal in the context provided. Illegal operations trigger exceptions. For example:

```python
# legal arithmetic operations
total_length = length + length  # in inches

# adding a unit object to a scalar returns a scalar
small_length = total_length + 1     # same as total_length.value + 1
large_length = 5.3 + small_length  # same as 5.3 + small_length.value
```

The subtraction operator treats data just like the addition operator would.

```python
small_length = Length(1, INCH)
total_length = length - small_length  # in inches

# subtracting a scalar from a unit object returns a scalar
smaller_length = total_length - 1     # same as total_length.value - 1
```

!!! note
    Not all addition and subtraction operations are valid, some would cause errors because they are dimensionally incompatible. For example:

```python
t = Time(12, SECOND)
l = Length(144, METER)

# an illegal arithmetic operation would look like
t_l = t + l     # adding time and length dimensions does not make sense
```

Adding time and length dimension objects does not make sense, so this operation raises a `mudu.exceptions.DimensionError`.

Multiplication and division operations follow all dimensional rules as well.

```python
# unit multiplication and division operations
area = length ** 2  # result is a DerivedQuantity object
pressure = force / area # also a DerivedQuantity object

# and you can still check the following
pressure.value
pressure.quantity
pressure.dimension
pressure.symbol

# operations like these are also allowed
p0 = 3 * pressure
p_inv = 1 / pressure
```

!!! note
    It is important to note that multiplication and division operations between two or more `_DimensionType` objects return a `DerivedQuantity` object (which is really doing dimensional analysis under the hood). In the case where the arithmetic operation is between data of the same dimension but different unit, the right-hand operand is implicitly converted to the same unit as the left operand.

```python
length_in_m = Length(2, METER)

total_length = length + length_in_m # total_length is now in INCHes

l_sqr = length_in_m * length    # l_sqr is in METERs
```

By checking the type of `length` and `force`, their types are `mudu.dimensions.Length` and `mudu.dimensions.Force` respectively, but note that arithmetic operations between two dimension objects returns the generic `DerivedQuantity` type rather than a more specific subclass:

```python
surface_tension = force * length
isinstance(surface_tension, mudu.dimensions.DerivedQuantity)    # True
isinstance(surface_tension, type(Force))                        # False
```

So it is worth noting that every derived quantity is a child class of `mudu.dimensions.DerivedQuantity` while every fundamental quantity is a child class of `mudu.dimensions._DimensionType`. Both classes inherit from `_DimensionUnitBase`.

Other operations such as `int`, `float`, `round` are also possible. For more information about possible operators and operations, check the [API Reference](api.md) section.

```python
# same as int(length.value)
int(length)

# same as float(length.value)
float(length)

# round length.value to x decimal places, the unit is preserved
round(length*0.0122, 2) # round to 2 decimal places

# floor division is also possible, and correctly floors negative
# results (this was a bug in earlier versions)
r = Length(12.23, METER)
r // 2  # -> 6.0

Length(-7, METER) // 2  # -> -4.0, not -3.0
```

Let's try something:

```python
from mudu import Length, METER, Pressure, PSI, Force, NEWTON

length = Length(12, METER)
force = Force(112, NEWTON)
pressure = Pressure(12, PSI)

area = length * length
pressure_2 = force / area

pressure == pressure_2  # is False

pressure.dimension == pressure_2.dimension  # is True
```

That example was intended to show the idea of dimensional homogeneity (and I hope it did). Quantity equality (`==`) always returns a plain `bool` and quantities are hashable, so they can be used in sets and as dict keys. For more information about available methods and functionalities, check the API reference.

## More Usage

Dimension objects like `Length`, `Time` and `Force` have some built-in conversions defined via their class attribute, `_conversion_standards`, that is why it is possible to convert between units provided the dimensions are the same. This is not always the case for all dimensions or quantities (a newly-defined custom quantity has no `_conversion_standards` by default); to make a dimension convertible to a new unit, the new unit must:

- first be defined against the dimension, via `define_unit`
- then have its conversion registered against that dimension's base unit, via `register_conversion`

This process is straightforward. So with the problem defined, let's get coding.

```python
from mudu import Length, METER, define_unit, register_conversion, Linear

# define a new LENGTH unit
NEW_UNIT = define_unit(Length, name="new_unit", symbol="nu")

# register how it converts to Length's base unit (METER):
# base_value = value * scale
register_conversion(Length, NEW_UNIT, Linear(0.001))  # 1 new_unit = 0.001 m

l1 = Length(12, NEW_UNIT)
l2 = l1.convert_to(METER) + Length(4, METER)    # l2 is in METERs
```

For conversions that involve an offset rather than a pure scale factor (as with temperature scales), use `Affine(scale, offset)` instead of `Linear(scale)`: `base_value = value * scale + offset`.

```python
from mudu import Temperature, KELVIN, define_unit, register_conversion, Affine

MY_SCALE = define_unit(Temperature, name="my_scale", symbol="ms")
register_conversion(Temperature, MY_SCALE, Affine(scale=1.0, offset=100.0))
```

Once you've registered several custom units, `mudu.audit_units()` can scan your dimension's conversion table for duplicate unit names or malformed conversion entries. This same method checks mudu's own CI runs against its built-in tables:

```python
from mudu import audit_units
from mudu.units import _LENGTH_CONVERSION_TABLE

problems = audit_units(_LENGTH_CONVERSION_TABLE)
assert problems == [], problems
```

To create a custom quantity or 'dimension' that has no existing mudu dimension to attach to at all, simply inherit from `_DimensionType` or `DerivedQuantity` directly, and construct its units with `_UnitType` (this is the one case where using the private `_UnitType` class directly is still the correct, intended pattern). The API reference has more details about the implementation of both classes.

```python
from mudu.dimensions import DerivedQuantity
from mudu.base import _UnitType
from mudu import NEWTON, METER, SECOND

class Power(DerivedQuantity):
    _conversion_standards = None

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity="power")

JOULES = _UnitType(
    _dimension=((NEWTON*METER)/SECOND)._dimension,
    _unit_name="joules",
    _unit_symbol="J",
    _quantity="power",
    _order=None,
)

power = Power(12, JOULES)
```

!!! note
    As of this current version, some derived quantities have not been implemented; other quantities and units will be implemented as soon as possible. A good practice is creating all custom-defined units in a different file and then registering them against the relevant dimension in your main file, but the decision is up to you.

As a way of ending this tutorial, I recommend trying out the following on the Python repl.

```shell
$ python
Python 3.12+
>>>
>>> from mudu import Pressure, PSI, METER, SECOND
>>>
>>> METER
m
>>>
>>> METER * METER
m^2
>>>
>>> PSI / METER
psi/m
>>>
>>> 3 * PSI
psi
>>>
>>> PSI / 3
psi
>>>
>>> PSI * 3
psi
>>>
>>> 4 / PSI
1/psi
>>>
>>> PSI + METER
Traceback (most recent call last):
File "<python-input-18>", line 1, in <module>
    PSI + METER
    ~~~~^~~~~~~
TypeError: unsupported operand type(s) for +: '_UnitType' and '_UnitType'
>>>
>>> 1 / (PSI * METER)
1/(mpsi)
>>>
>>>
```

The idea behind the above example is to illustrate the way `_UnitType` objects can perform arithmetic operations independently of any quantity wrapping them. I hope you now have a grasp of how to use `mudu` and its features. I hope you find mudu useful and beneficial to your scientific computation projects.