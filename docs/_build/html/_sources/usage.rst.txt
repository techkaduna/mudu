===========
Usage Guide
===========

This section provides a structured tutorial on the usage of **mudu**. It introduces the fundamental concepts required to work with unit-aware numerical data and progressively moves toward advanced usage patterns such as custom units, custom dimensions, and extension of conversion standards.

The guide is divided into two main parts:

- **Basic usage**: specification of units and dimensions, unit conversion, and arithmetic operations
- **Advanced usage**: extension of conversion standards, creation of custom units, and definition of custom quantities

Prerequisites
"""""""""""""

To follow this guide effectively, the reader is expected to have:

- Basic proficiency in Python programming
- Secondary school–level understanding of physical dimensions and dimensional analysis

Basic Usage
-----------

Specifying Dimensions and Units
"""""""""""""""""""""""""""""""

In **mudu**, numerical values are associated with physical meaning through *dimensions* and *units*. A dimension represents a physical quantity (e.g. length, time, force), while a unit represents a particular scale or measurement standard for that dimension.

To create a quantity, import the required dimension class and unit, then instantiate the dimension with a numerical value and unit definition.

.. code-block:: python

    from mudu import Length, METER, INCH
    from mudu import Time, SECOND, HOUR
    from mudu import Force, NEWTON, DYNE
    from mudu import Pressure, PASCAL, mmHg

    length = Length(12, INCH)
    t0 = Time(2, HOUR)

    force = Force(1, NEWTON)
    pressure = Pressure(12, PASCAL)

Here, `Length`, `Time`, `Force`, and `Pressure` are *dimension classes*, while `INCH`, `METER`, and `NEWTON` are *unit definitions*.

By convention:
- Dimension classes are defined in *TitleCase*
- Unit definitions are defined in *UPPERCASE*

A complete list of available dimensions and units is provided in the API Reference.

Unit Conversion
"""""""""""""""

Unit conversion is performed using the `convert_to` method of a dimension instance.

.. code-block:: python

    length.convert_to(METER)
    t0.convert_to(SECOND)

Attempting to convert between incompatible dimensions raises an exception.

.. code-block:: python

    t0.convert_to(METER)      # invalid
    pressure.convert_to(NEWTON)  # invalid

Conversions between compatible derived units are supported when conversion standards exist.

.. code-block:: python

    force.convert_to(DYNE)
    pressure.convert_to(mmHg)

**Note:** Converting between units of different dimensions raises `exceptions.ConversionError`.

Inspecting Quantity Attributes
""""""""""""""""""""""""""""""

Each dimension object exposes several useful attributes.

.. code-block:: python

    length.value        # numerical value
    length.symbol       # unit symbol
    length.dimension    # symbolic dimension (e.g. L)

For derived quantities:

.. code-block:: python

    force.value
    force.quantity
    force.dimension     # e.g. L*M/T**2
    force.unit_type

The `dimension` attribute returns a SymPy symbolic expression representing the dimensional form of the quantity. This enables automatic dimensional analysis during arithmetic operations.

Example:

.. code-block:: python

    velocity = length / t0
    velocity.dimension   # -> L/T

Units with Order Prefixes
"""""""""""""""""""""""""

**mudu** supports the construction of units with metric order prefixes such as kilo-, milli-, etc.

.. code-block:: python

    from mudu import OrderUnit, KILO, MILLI

    KILONEWTON = OrderUnit(KILO, NEWTON)
    MILLIMETER = OrderUnit(MILLI, METER)

    l = Length(1000, MILLIMETER)
    F = Force(20, KILONEWTON)

These prefixed units behave identically to base units and support conversion and arithmetic.

.. code-block:: python

    l.convert_to(METER)

Attempting to convert quantities with incompatible dimensions still raises errors.

Arithmetic Operations
"""""""""""""""""""""

Dimension objects support arithmetic operations where mathematically valid.

Addition and subtraction are permitted only between quantities of the same dimension.

.. code-block:: python

    total_length = length + length
    reduced_length = length - Length(1, INCH)

Adding or subtracting scalars returns a scalar value.

.. code-block:: python

    total_length + 1
    5.3 + total_length

Illegal operations raise `exceptions.DimensionError`.

.. code-block:: python

    t = Time(12, SECOND)
    l = Length(144, METER)

    t + l   # invalid

Multiplication and division follow dimensional rules and typically produce derived quantities.

.. code-block:: python

    area = length ** 2
    pressure = force / area

These derived quantities retain accessible attributes.

.. code-block:: python

    pressure.value
    pressure.quantity
    pressure.dimension
    pressure.symbol

Scalar interactions are also supported.

.. code-block:: python

    3 * pressure
    1 / pressure

When operating on quantities of the same dimension but different units, the right-hand operand is implicitly converted to the unit of the left-hand operand.

.. code-block:: python

    length_in_m = Length(2, METER)
    total_length = length + length_in_m

Type Hierarchy
""""""""""""""

Fundamental quantities (e.g. `Length`, `Time`) inherit from `_DimensionType`, while derived quantities inherit from `DerivedQuantity`. Both derive from `_DimensionUnitBase`.

Example:

.. code-block:: python

    surface_tension = force * length
    isinstance(surface_tension, force.__class__)  # False

All derived quantities are instances of `DerivedQuantity`.

Other Supported Operations
""""""""""""""""""""""""""

Built-in numerical operations are supported.

.. code-block:: python

    int(length)
    float(length)
    round(length * 0.0122, 2)

Floor division is also defined.

.. code-block:: python

    r = Length(12.23, METER)
    r // 2

Dimensional Homogeneity Example
""""""""""""""""""""""""""""""

.. code-block:: python

    from mudu import Length, METER, Pressure, PSI, Force, NEWTON

    length = Length(12, METER)
    force = Force(112, NEWTON)

    area = length * length
    pressure_2 = force / area

    pressure = Pressure(12, PSI)

    pressure == pressure_2               # False
    pressure.dimension == pressure_2.dimension  # True

This illustrates dimensional homogeneity: quantities may differ numerically yet share the same dimension.

Advanced Usage
--------------

Generic Quantities
""""""""""""""""""

Some quantities are defined using `GenericUnit`, such as electric current and solid angle.

.. code-block:: python

    import functools
    from mudu import GenericUnit, AMPERE, STERADIAN

    ElectricCurrent = functools.partial(GenericUnit, unit=AMPERE)
    SolidAngle = functools.partial(GenericUnit, unit=STERADIAN)

Usage:

.. code-block:: python

    a = ElectricCurrent(10)
    s = SolidAngle(1)

Derived Generic Quantities
"""""""""""""""""""""""""

For derived quantities without explicit dimension classes, `GenericUnit2` is provided.

.. code-block:: python

    import functools
    from mudu import GenericUnit2, VOLT

    Voltage = functools.partial(GenericUnit2, unit_definition=VOLT)

Extending Conversion Standards
"""""""""""""""""""""""""""""

Dimension classes store conversion logic in `_conversion_standards`. To extend conversion support:

1. Define a new unit
2. Define a conversion function
3. Extend the dimension’s conversion table

.. code-block:: python

    from mudu import Pressure, PSI
    from mudu.base import _UnitType
    from mudu.units import _basic_unit_converter
    import functools

    NEW_UNIT = _UnitType(
        _dimension=Pressure._dimension,
        _unit_name="new_unit",
        _unit_symbol="nu",
    )

    seq = ((NEW_UNIT, PSI),
           functools.partial(_basic_unit_converter, y=0.001))

    Pressure._conversion_standards.extend(seq)

Custom Dimensions
"""""""""""""""""

Custom quantities can be defined by subclassing `DerivedQuantity` or `_DimensionType`.

.. code-block:: python

    from mudu.dimensions import DerivedQuantity

    class Power(DerivedQuantity):
        _conversion_standards = None

        def __init__(self, value, unit_definition):
            super().__init__(value, unit_definition, quantity="power")

**Note:** Some quantities are not yet implemented in the current version. Users are encouraged to define custom units and quantities as needed.

Interactive Exploration
"""""""""""""""""""""""

The Python REPL is a useful environment for exploring unit arithmetic.

.. code-block:: shell

    >>> from mudu import PSI, METER
    >>> PSI * METER
    psi·m
    >>> 1 / PSI
    1/psi
    >>> PSI + METER
    TypeError

Vectorized Quantities (Experimental)
====================================

In addition to scalar-valued quantities, **mudu** provides *experimental* support for **vectorized quantities**, where the numerical magnitude of a dimension object is an array-like structure (e.g. list or iterable). This enables element-wise arithmetic, unit conversion, and dimensional analysis over collections of values while preserving unit safety and dimensional correctness.

This feature is intended to support lightweight batch computations and exploratory numerical analysis without requiring explicit NumPy arrays or external vectorization frameworks.

Conceptually, a vectorized quantity in **mudu** is:

- a *single physical quantity*,
- with a *uniform unit definition*,
- and an *array-valued magnitude*.

This is distinct from an array of independent quantity objects.

Creating Vectorized Quantities
-------------------------------

A vectorized quantity is created by passing an iterable as the value argument when instantiating a dimension object.

.. code-block:: python

    from mudu import Length, METER

    l = Length([i for i in range(12)], METER)
    l

    # Output:
    # [0 m 1 m 2 m 3 m 4 m 5 m 6 m 7 m 8 m 9 m 10 m 11 m]

Here, `l` represents a vectorized length quantity whose magnitude is a sequence of values, all expressed in meters.

Element-wise Arithmetic
-----------------------

Arithmetic operations involving vectorized quantities are applied **element-wise** to the underlying magnitude, provided the operation is dimensionally valid.

Scalar operations:

.. code-block:: python

    l / 2

    # Output:
    # [0.0 m 0.5 m 1.0 m 1.5 m 2.0 m 2.5 m 3.0 m 3.5 m 4.0 m 4.5 m 5.0 m 5.5 m]

Division by a scalar preserves the unit and applies the operation to each element independently.

Operations with Other Quantities
--------------------------------

Vectorized quantities may participate in arithmetic with scalar-valued quantities of compatible dimensions.

.. code-block:: python

    from mudu import Time, SECOND

    t = Time(12, SECOND)
    speed = l / t
    speed

    # Output:
    # [0 m/s 12 m/s 24 m/s 36 m/s 48 m/s 60 m/s
    #  72 m/s 84 m/s 96 m/s 108 m/s 120 m/s 132 m/s]

In this example, division is performed element-wise, producing a vectorized derived quantity with dimension L/T.

Vectorized Derived Quantities
-----------------------------

Derived quantities may also be vectorized.

.. code-block:: python

    from mudu import Force, NEWTON

    f = Force([12, 24, 45], NEWTON)
    f

    # Output:
    # [12 N 24 N 45 N]

Unit conversion remains fully supported.

.. code-block:: python

    from mudu import DYNE

    f.convert_to(DYNE)

    # Output:
    # [1200000.0 dyn 2400000.0 dyn 4500000.0 dyn]

Conversion is applied element-wise while enforcing dimensional compatibility.

Dimensional Semantics
---------------------

Vectorized quantities in **mudu** obey the same dimensional rules as scalar quantities:

- All arithmetic operations are checked for dimensional validity.
- Illegal operations raise the same exceptions (`DimensionError`, `ConversionError`).
- The resulting object retains a well-defined dimension and unit.

The `dimension` attribute of a vectorized quantity represents the *symbolic dimension* of the quantity, not the shape or size of the underlying data.

Design Notes and Limitations
----------------------------

This feature is currently **experimental** and subject to change. In particular:

- Broadcasting rules are minimal and intentionally conservative.
- Mixed-shape vector operations are not guaranteed to behave consistently.
- Performance is not optimized for large numerical arrays.
- NumPy interoperability is not yet formalized.

Vectorized quantities are best suited for:
- small to medium-sized datasets,
- exploratory analysis,
- pedagogical demonstrations of dimensional analysis.

For large-scale numerical computation, explicit NumPy-based workflows may be more appropriate.

Terminology
-----------

Within the **mudu** documentation and codebase, this feature is referred to as:

- *vectorized quantities*, or
- *vectorized unit-aware computation*.

This terminology emphasizes that vectorization applies to the numerical magnitude, while the unit and dimension remain single, coherent entities.

Future Work
-----------

Planned improvements may include:

- explicit NumPy array support,
- clearer broadcasting semantics,
- optional strict shape validation,
- performance optimizations.

Users are encouraged to treat this feature as provisional and to report issues or edge cases encountered during use.

Custom Units (Experimental)
==================================

**mudu** provides experimental support for *ad-hoc custom units* via the `custom_unit` interface. This feature allows users to construct a physical quantity directly from a numerator–denominator unit specification without defining a formal dimension or derived quantity class.

The primary intent of this feature is to support rapid prototyping, exploratory calculations, and situations where defining a full dimension class would be unnecessarily heavy.

Unlike standard dimension objects (e.g. `Length`, `Force`), a `custom_unit` instance represents a **generic physical quantity** with:

- a scalar numerical value,
- an explicitly defined unit expression,
- and an automatically inferred symbolic dimension.

Creating a Custom Unit
----------------------

A custom unit is created by providing:
- a numerical value, and
- a numerator (`num`) and denominator (`per`) tuple describing the unit composition.

.. code-block:: python

    from mudu import custom_unit, METER, SECOND

    c = custom_unit(20, num=(METER,), per=(SECOND,))
    c

    # Output:
    # 20 m/s

Here, the unit expression `m/s` is constructed dynamically, and the dimension is inferred as L/T.

Inspecting Attributes
---------------------

A `custom_unit` object exposes a limited but well-defined interface.

.. code-block:: python

    c.value        # numerical magnitude
    c.unit_type    # unit expression
    c.dimension    # symbolic dimension
    c.quantity     # generic quantity label

Example:

.. code-block:: python

    c.value        # 20
    c.unit_type    # m/s
    c.dimension    # L/T
    c.quantity     # 'generic_quantity'

Note that `custom_unit` does not expose a `unit` attribute. Instead, the unit expression is accessible via `unit_type`.

Arithmetic and Comparison Semantics
-----------------------------------

`custom_unit` objects support limited arithmetic and comparison operations with scalars.

Scalar arithmetic:

.. code-block:: python

    c + 10     # returns a scalar
    c * 2
    c / 4

Comparison operations compare the underlying numerical value:

.. code-block:: python

    c == 20        # True
    c > 20         # False
    c < 20         # False

This behavior is equivalent to comparing `c.value` directly.

.. code-block:: python

    c.value == 20  # True

**Important:** Arithmetic or comparison with other dimensioned objects is intentionally restricted in the current implementation.

Dimensional Semantics
---------------------

Although `custom_unit` instances do not correspond to a named dimension class, they still participate in symbolic dimensional analysis.

.. code-block:: python

    c.dimension   # L/T

The dimension is inferred from the unit composition (`num` and `per`) using the same symbolic machinery as standard derived quantities.

Conversion Limitations
----------------------

Unit conversion is **not yet implemented** for `custom_unit`.

Attempting to convert a custom unit raises a `NotImplementedError`.

.. code-block:: python

    c.convert_to(num=(METER,), per=(SECOND,))

    # NotImplementedError:
    # custom_unit is an experimental feature and has not been completely implemented yet

Users requiring full conversion support should define a proper derived quantity or extend conversion standards explicitly.

Design Rationale
----------------

The `custom_unit` feature exists to fill a gap between:

- fully defined dimension classes (rigorous but verbose), and
- raw numerical computation (flexible but dimensionally unsafe).

It enables quick expression of physically meaningful values without requiring:
- subclassing `DerivedQuantity`,
- defining conversion standards,
- or registering units globally.

This makes it particularly useful for:
- interactive exploration,
- prototyping new physical models,
- temporary or one-off unit expressions.

Limitations and Experimental Status
-----------------------------------

This feature is **experimental** and subject to change. Known limitations include:

- No unit conversion support
- Restricted arithmetic with other quantities
- Generic (unnamed) quantity semantics
- Potential API changes in future releases

Users should avoid relying on `custom_unit` in production-critical code.

Future Directions
-----------------

Potential future enhancements include:

- full conversion support,
- interoperability with vectorized quantities,
- optional promotion to formal derived quantities,
- stricter arithmetic rules.

Feedback on usage patterns and edge cases is encouraged.

