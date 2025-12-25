![mudu Logo](https://raw.githubusercontent.com/techkaduna/mudu/main/logo.png)

# WELCOME TO `mudu`

`mudu` is a package for units and dimension handling, unit conversion
and unit arithemtic, with support for custom units definition.

`mudu` was created as part of a larger project (my final year
project), `flightperformance`, a Python package for
analyzing aircraft (fixed wing) performance. As it is standard in
engineering to specify the units of data so as to ensure dimensional
homogeniety and reproducability, the `flightperformance`
package required a means of specifying the units of data, the quantity
they represents, convert between units and do arithemtic operations
efforlessly with emphasis on flexibiliy and readability, this is what
`mudu` does.

`mudu` provides a set of classes and methods, while retaining
Python\'s expressiveness, to add unit signatures to numeric data,
convert between units and perform valid arithemtic operations on
dimension (or quantities) and unit objects. At its core, mudu creates
dimensions using the `DimensionUnitBase` base class while
units are all instances or child classes of the `_UnitType`
class, both these classes are composed of other classes.

## Why use **mudu**

> -   It provides an simple and expressive way of specifying units
> -   Capability to perform conversion from one unit to another while
>     ensuring dimensional homogeniety as it applies in mathematics
> -   Supports valid arithemtic operations
> -   It provides interfaces to define custom units, dimensions (or quantities) and define relationships between custom and existing units

This documentation, contains information about the general structure of
mudu, a quick tutorial that captures almost all the important
functionalities of mudu and some selected examples to give to an easy
start on the usage of the package.

## Installation

To install using pip, run:

> ``` shell
> $ pip install mudu
> ```

You can view a better documentation of this project on
<https://mudu.readthedocs.io>

## Usage Guide

This section provides a brief but comprehensive tutorial on how to use
mudu and its features. The section is divided into two sub-sections:

-   Basic usage: covers the basics of specifying units and dimensions as
    well as arithemetic operations using mudu
-   More usage: which covers more advanced features such as extending
    conversion standards, creating custom unit and dimensions e.t.c

## Preresquisites

To follow this tutorial and get the most out of it, it is assumed that
readers have:

-   Basic understanding of Python programming language
-   Secondary school (or equivalent) knowledge of dimensions and
    dimensional analysis

## Basic Usage

## Specifying units

To specify units, simply import the neccesary dimensions and units, and
create a dimension object.

``` python
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

Objects like `Length`, `Mass`, 
`Time` are called `dimensions` while `METER`,
`INCH` and `NEWTON` are called `units`. Also note
that *dimensions are defined in title case*, while *units
are defined in all caps*. For a more comprehensive list of
dimensions and unit, check the *API Reference* section.

## Unit conversion

Unit conversion is done by using the dimension [convert_to]
method.

``` python
length.convert_to(METER)

t0.convert_to(SECOND)

t0.convert_to(METER)    # does not make sense

# there is also support for conversion between some derived quantities
force.convert_to(DYNE)
pressure.convert_to(mmHg)

pressure.convert_to(NEWTON)     # definitely does not make sense
```

**NOTE** Converting between units representing different dimensions
raises an *exceptions.ConversionError*.

The scalar value, symbol, dimension and quantity (for derived
quantities) can also be accessed e.g.

``` python
# for fundamental quantites
length.value    # -> 12
length.symbol   # -> in
length.dimension    # -> L

# for derived quantity
force.value # -> 1
force.quantity  # -> Force
force.dimension # -> L*M/T**2
force.unit_type # -> N
```

**NOTE** *obj.dimension* returns a sympy *sympy.core* child
object that represents the dimension of the unit, and in the case of
derived quantities, it does some sort dimensional analysis.

``` python
velocity = length/t0
velocity.dimension  # -> L/T
```

## Operating with units multiple prefix

It is also possible to create units with multiples by specifying their
multiple prefixes.

``` python
from mudu import Length, METER, INCH, Force, KILO, MILLI, OrderUnit

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

# Note
err_area = area.convert_to(METER)   # throws an error

pressure = F / new_area
```

The `OrderUnit` is subclass of `_UnitType` used
to create units in their multiples, and supports the same operations as
`_UnitType`. `KILO` and `MILLI`
(and other multiple prefixes) are instances of
`_OrderType`. See the API Reference page for more
information.

## Arithemetic Operations

mudu objects also support arithemetic operations provided they are legal
in the context provided. Illegal operations trigger exceptions. For
example:

``` python
# legal arthemetic operations
total_length = length + length  # in inches

# adding a unit object to a scalar returns a scalar
small_length = total_length + 1     # same as total_length.value + 1
large_length = 5.3 + small_length  # same as 5.3 + small_length.value
```

Subraction operator treats data just like the addition operator would.

``` python
small_length = Length(1, INCH)
total_length = length - small_length  # in inches

# adding a unit object to a scalar returns a scalar
smaller_length = total_length - 1     # same as total_length.value - 1
```

**NOTE** Not all addition and subtraction operations are valid, some
would cause errors because they are dimensionally incompatible. For
example:

``` python
t = Time(12, SECOND)
l = Length(144, METER)

# an illegal arithemetic would look like
t_l = t + l     # adding time and length dimensions does not make sense
```

adding time and length dimension objects does not make sense, so this
operation raises an [exceptions.DimensionError].

Multiplication and division operation follow all dimensional rules as
well.

``` python
# unit multiplication and division operation
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

**NOTE** It is important to note that, multiplication and division
operations between two or more `_DimensionType` objects
return a `DerivedQuantity` object, its mathematics really.
In the case where the arithemetic operation is between data of the same
dimension but different unit, the right hand operand is implicity
converted to the same unit as the left operand.

``` python
length_in_m = Length(2, METER)

total_length = length + length_in_m # total_length is now in INCHes

l_sqr = length_in_m * length    # l_sqr is in METERs
```

By checking the type of `length` and `force`,
their types are `mudu.dimensions.Length` and
`mudu.dimensions.Force` respectively, but if you try:

``` python
surface_tension = force * length
isinstance(force, type(surface_tension))    # the result is True
```

So it is worthy to note that every derived quantity is a child class of
`mudu.dimensions.DerivedQuantity` while every fundamental
quantity is a child class of
`mudu.dimensions.\_DimensionType`. Both classes inherit from
`_DimensionUnitBase`.

Other operations such as `int`, `float`,
`round` are also possible. For more information about
possible operators and operations, check the `API Reference`
section.

``` python
# same as int(length.value)
int(length)

# same as float(length.value)
float(length)

# round length.value to x decimal place, the unit is preserved
round(length*0.0122, 2) # round to 2 decimal places

# floor division is also possible
r = Length(12.23, METER)
r // 2  # -> 6.0
```

Lets try something

``` python
from mudu import Length, METER, Pressure, PSI, Force, NEWTON

length = Length(12, METER)
force = Force(112, NEWTON)
pressure = Pressure(12, PSI)

area = length * length
pressure_2 = force / area

pressure == pressure_2  # is False

pressure.dimension == pressure_2.dimension  # is True
```

That example was intended to show the idea of dimensional homogeniety -
I hope it did. For more information about available methods and
functionalities, check the API reference.

## More Usage

Dimension objects like `Length`, `Time` and
`Force` have some built-in conversion standards defined as
the class attribute, `_conversion_standards`, that is why
it is possible to convert between units provided the dimensions are the
same. This is not always the case for all dimensions or quantites,
hence, to convert a dimension objects with an empty
`_conversion_standards` attribute to a new unit, the new
unit must:

-   first be created
-   then the conversion standard is defined
-   then the `Dimension._conversion_standards` is extended

This process, though it seems like a lot, is actually very simple and
straightforward. This topic will be the main course of this tutorial
section.

So with the problem defined, lets get coding.

``` python
from mudu import Pressure, PSI
from mudu.base import _UnitType
from mudu.units import _basic_unit_converter

# define a new unit type
NEW_UNIT = _UnitType(
    _dimension=LENGTH,
    _unit_name="new_unit",
    _unit_symbol="nu",
    )

# create a conversion standard with METER
seq = ((NEW_UNIT, PSI), functools.partial(_basic_unit_converter, y=0.001))

# extend the conversion table
Pressure._conversion_standards.extend(seq)

p1 = Pressure(12, PSI)
p2 = p1.convert_to(NEW_UNIT) + 4    # p2 is in units of NEW_UNIT
```

To create a custom quantity or \'dimension\', simply inherit from
`_DimensionType` class or `DerivedQuantity`
class. The API reference has more details about the implementation of
both classes.

``` python
from mudu.dimensions import DerivedQuantity

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

**NOTE** As of this current version, some derived quantites have not
been implemented, other quantites and units will be implemented as soon
as possible. A good practice will be creating all custom defined units
in a different file and then extending the dimension in the main file,
but then, the decision is up to you.

As a way of ending this tutorial, I recommend trying out the following
on Python repl.

``` shell
C:\Users\USER\Desktop\mudu>python
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
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

The idea behind the above example is to illustrate the way
`_UnitType` objects can perform arithemetic operations. I
hope you now have a grasp on how to use `mudu` and its features. I
hope you find mudu useful and beneficial to your scientific computation
projects.
