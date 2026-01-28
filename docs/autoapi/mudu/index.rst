mudu
====

.. py:module:: mudu

.. autoapi-nested-parse::

   ====
   mudu
   ====

   A Python package for unit and dimension handling, unit conversion, units arithemtic, with \
   support for custom units definition.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/mudu/base/index
   /autoapi/mudu/dimensions/index
   /autoapi/mudu/exceptions/index
   /autoapi/mudu/units/index


Attributes
----------

.. autoapisummary::

   mudu.LENGTH
   mudu.MASS
   mudu.TIME
   mudu.PLANE_ANGLE
   mudu.SOLID_ANGLE
   mudu.THERMODYNAMIC_TEMPERATURE
   mudu.ELECTRIC_CURRENT
   mudu.AMOUNT_OF_SUBSTANCE
   mudu.LUMINOUS_INTENSITY
   mudu.FORCE
   mudu.SPEED
   mudu.ENERGY
   mudu.DENSITY
   mudu.GENERIC_DIMENSION
   mudu.GENERIC_QUANTITY
   mudu.GENERIC_UNIT
   mudu.DIMENSIONLESS
   mudu.DIMENSIONLESS_UNIT
   mudu.GIGA
   mudu.MEGA
   mudu.KILO
   mudu.CENTI
   mudu.MILLI
   mudu.MICRO
   mudu.NANO
   mudu.PICO
   mudu.FEMTO
   mudu.ATTO
   mudu.OrderUnit
   mudu.INCH
   mudu.METER
   mudu.KILOMETER
   mudu.FEET
   mudu.YARD
   mudu.MILE
   mudu.NAUTICAL_MILE
   mudu.GRAM
   mudu.KILOGRAM
   mudu.POUND
   mudu.SLUG
   mudu.SHORT_TON
   mudu.LONG_TON
   mudu.METRIC_TON
   mudu.SECOND
   mudu.MINUTE
   mudu.HOUR
   mudu.KELVIN
   mudu.RANKINE
   mudu.CELSIUS
   mudu.FARENHEIT
   mudu.DEGREE
   mudu.RADIAN
   mudu.STERADIAN
   mudu.AMPERE
   mudu.MOLE
   mudu.CANDELA
   mudu.NEWTON
   mudu.POUND_FORCE
   mudu.POUNDAL
   mudu.DYNE
   mudu.PASCAL
   mudu.PSI
   mudu.mmHg
   mudu.inHg
   mudu.BAR
   mudu.ATM
   mudu.POUND_PER_SQUARE_FOOT
   mudu.JOULE
   mudu.BRITISH_THERMAL_UNIT
   mudu.CALORIE
   mudu.WATT_HOUR
   mudu.ELECTRON_VOLT
   mudu.KILOGRAM_PER_CUBIC_METER
   mudu.GRAM_PER_CUBIC_CENTIMETER
   mudu.GRAM_PER_CUBIC_MILLILITER
   mudu.POUND_PER_CUBIC_FOOT
   mudu.POUND_PER_CUBIC_INCH
   mudu.SLUG_PER_CUBIC_FOOT
   mudu.WATT
   mudu.HORSEPOWER
   mudu.BTU_PER_HOUR
   mudu.VOLT
   mudu.FARAD
   mudu.HENRY
   mudu.WEBER
   mudu.OHMS
   mudu.TESLA
   mudu.SIEMENS
   mudu.LUX
   mudu.BECQUEREL
   mudu.CURIE
   mudu.GRAY
   mudu.RAD
   mudu.SIEVERT
   mudu.REM
   mudu.METER_PER_SECOND
   mudu.MILE_PER_HOUR
   mudu.KM_PER_HOUR
   mudu.FOOT_PER_SECOND
   mudu.KNOT
   mudu.SolidAngle
   mudu.ElectricCurrent
   mudu.AmountOfSubstance
   mudu.LuminousIntensity
   mudu.Voltage
   mudu.Capacitance
   mudu.Inductance
   mudu.MagneticFlux
   mudu.Resistance
   mudu.Conductance
   mudu.MageneticFieldStrength
   mudu.Illuminance


Exceptions
----------

.. autoapisummary::

   mudu.DimensionError
   mudu.ConversionError
   mudu.NotIterableError
   mudu.SequenceOperationErrorr
   mudu.OperationNotAvailable


Classes
-------

.. autoapisummary::

   mudu._UnitType
   mudu._DimensionUnitBase
   mudu._DimensionType
   mudu.DerivedQuantity
   mudu.GenericUnit
   mudu.GenericUnit2
   mudu.custom_unit
   mudu.Length
   mudu.Mass
   mudu.Time
   mudu.Temperature
   mudu.Angle
   mudu.Force
   mudu.Pressure
   mudu.Energy
   mudu.Density
   mudu.Power
   mudu.Radioactivity
   mudu.AbsorbedDose
   mudu.DoseEquivalent
   mudu.Speed


Package Contents
----------------

.. py:data:: LENGTH

.. py:data:: MASS

.. py:data:: TIME

.. py:data:: PLANE_ANGLE

.. py:data:: SOLID_ANGLE

.. py:data:: THERMODYNAMIC_TEMPERATURE

.. py:data:: ELECTRIC_CURRENT

.. py:data:: AMOUNT_OF_SUBSTANCE

.. py:data:: LUMINOUS_INTENSITY

.. py:data:: FORCE
   :value: 'force'


.. py:data:: SPEED
   :value: 'speed'


.. py:data:: ENERGY
   :value: 'energy'


.. py:data:: DENSITY
   :value: 'density'


.. py:data:: GENERIC_DIMENSION
   :value: 'generic_dimension'


.. py:data:: GENERIC_QUANTITY
   :value: 'generic_quantity'


.. py:data:: GENERIC_UNIT
   :value: 'generic_unit'


.. py:data:: DIMENSIONLESS
   :value: 'dimensionless'


.. py:data:: DIMENSIONLESS_UNIT
   :value: 'dimensionless_unit'


.. py:data:: GIGA

.. py:data:: MEGA

.. py:data:: KILO

.. py:data:: CENTI

.. py:data:: MILLI

.. py:data:: MICRO

.. py:data:: NANO

.. py:data:: PICO

.. py:data:: FEMTO

.. py:data:: ATTO

.. py:class:: _UnitType

   Internal base class for units definition.

   .. attribute:: _dimension

      The unit dimension, say, `LENGTH`, `MASS`, `TIME `

      :type: str

   .. attribute:: _unit_name

      The unit name e.g.  `meter`

      :type: str

   .. attribute:: _unit_symbol

      Symbolic representation of the unit, usually passed as a
      string, then converted to a `sympy.Symbol` object

      :type: str

   .. attribute:: _order

      Multiple prefix, if unit is a multiple prefix
      of a  `_UnitType`.

      :type: _OrderType

   .. attribute:: _base

      If a unit is a multiple prefix, then it has a base unit. e.g.
      `CENTIMETER` is composed of the multiple prefix `CENTI` and the base
      unit `METER`.

      :type: _UnitType

   .. attribute:: _quantity

      The quantity the unit represents, say Force, Energy.

      :type: str

   .. attribute:: create_unit

      Class method to create a `_UnitType` object.

      :type: _UnitType

   .. attribute:: is_unit_type

      Internal method to validate that an object is an instance of `_UnitType`

      :type: bool

   .. attribute:: - **Usage example**



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

   .. attribute:: To create a conversion standard with another unit, read the documentation



   .. attribute:: on _ConversionTableType or read the full documentation at <https



      :type: //github.com/techkaduna/mudu>_.


   .. py:attribute:: _dimension
      :type:  str


   .. py:attribute:: _unit_name
      :type:  str


   .. py:attribute:: _unit_symbol
      :type:  str | sympy.Symbol


   .. py:attribute:: _quantity
      :type:  str
      :value: 'generic_quantity'



   .. py:attribute:: _order
      :type:  _OrderType
      :value: None



   .. py:attribute:: _base
      :type:  Self
      :value: None



   .. py:method:: create_unit(**kwargs)
      :classmethod:


      Internal alternate `_UnitType` constructor.

      :param `create_unit` takes same parameters as the `_UnitType` `__init__`.:



   .. py:method:: __post_init__()


   .. py:method:: __repr__()


   .. py:method:: __mul__(x: Self)


   .. py:method:: __rmul__(x: Self)


   .. py:method:: __truediv__(x)


   .. py:method:: __rtruediv__(x)


   .. py:method:: __pow__(x)


.. py:data:: OrderUnit

.. py:data:: INCH

.. py:data:: METER

.. py:data:: KILOMETER

.. py:data:: FEET

.. py:data:: YARD

.. py:data:: MILE

.. py:data:: NAUTICAL_MILE

.. py:data:: GRAM

.. py:data:: KILOGRAM

.. py:data:: POUND

.. py:data:: SLUG

.. py:data:: SHORT_TON

.. py:data:: LONG_TON

.. py:data:: METRIC_TON

.. py:data:: SECOND

.. py:data:: MINUTE

.. py:data:: HOUR

.. py:data:: KELVIN

.. py:data:: RANKINE

.. py:data:: CELSIUS

.. py:data:: FARENHEIT

.. py:data:: DEGREE

.. py:data:: RADIAN

.. py:data:: STERADIAN

.. py:data:: AMPERE

.. py:data:: MOLE

.. py:data:: CANDELA

.. py:data:: NEWTON

.. py:data:: POUND_FORCE

.. py:data:: POUNDAL

.. py:data:: DYNE

.. py:data:: PASCAL

.. py:data:: PSI

.. py:data:: mmHg

.. py:data:: inHg

.. py:data:: BAR

.. py:data:: ATM

.. py:data:: POUND_PER_SQUARE_FOOT

.. py:data:: JOULE

.. py:data:: BRITISH_THERMAL_UNIT

.. py:data:: CALORIE

.. py:data:: WATT_HOUR

.. py:data:: ELECTRON_VOLT

.. py:data:: KILOGRAM_PER_CUBIC_METER

.. py:data:: GRAM_PER_CUBIC_CENTIMETER

.. py:data:: GRAM_PER_CUBIC_MILLILITER

.. py:data:: POUND_PER_CUBIC_FOOT

.. py:data:: POUND_PER_CUBIC_INCH

.. py:data:: SLUG_PER_CUBIC_FOOT

.. py:data:: WATT

.. py:data:: HORSEPOWER

.. py:data:: BTU_PER_HOUR

.. py:data:: VOLT

.. py:data:: FARAD

.. py:data:: HENRY

.. py:data:: WEBER

.. py:data:: OHMS

.. py:data:: TESLA

.. py:data:: SIEMENS

.. py:data:: LUX

.. py:data:: BECQUEREL

.. py:data:: CURIE

.. py:data:: GRAY

.. py:data:: RAD

.. py:data:: SIEVERT

.. py:data:: REM

.. py:data:: METER_PER_SECOND

.. py:data:: MILE_PER_HOUR

.. py:data:: KM_PER_HOUR

.. py:data:: FOOT_PER_SECOND

.. py:data:: KNOT

.. py:class:: _DimensionUnitBase

   Base class for all dimensions model.

   .. attribute:: _conversion_standards

      Conversion table definition of conversion standards for converting
      from one unit to another provided that the units are of the same dimension.

      :type: _ConversionTableType

   .. attribute:: _dimension

      The dimension represented by the dimension model e.g. `METER`, `LENGTH`, `TIME`

      :type: str

   .. attribute:: _check_and_convert

      Performs an arithemetic or boolean operation on a `_DimensionUnitBase` child object.
      Makes sure of unit homogeniety by implicitly converting units where required before
      performing the operation.

      :type: _DimensionUnitBase | int | float | bool

   .. attribute:: convert_to

      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :type: _DimensionUnitBase | bool


   .. py:attribute:: _conversion_standards
      :type:  mudu.base._ConversionTableType
      :value: None



   .. py:attribute:: _dimension
      :type:  str
      :value: None



   .. py:method:: __repr__()


   .. py:method:: __str__()


   .. py:method:: __int__()


   .. py:method:: __float__()


   .. py:method:: __add__(x)


   .. py:method:: __radd__(x)


   .. py:method:: __sub__(x)


   .. py:method:: __rsub__(x)


   .. py:method:: __mul__(x)


   .. py:method:: __rmul__(x)


   .. py:method:: __truediv__(x)


   .. py:method:: __rtruediv__(x)


   .. py:method:: __floordiv__(x)


   .. py:method:: __rfloordiv__(x)


   .. py:method:: __pow__(x)


   .. py:method:: __round__(y=0)


   .. py:method:: __lt__(x)


   .. py:method:: __gt__(x)


   .. py:method:: __le__(x)


   .. py:method:: __ge__(x)


   .. py:method:: __eq__(x)


   .. py:method:: _check_and_convert(x: Any, _operator: Callable) -> Self | bool | int | float

      Performs an arithemetic or boolean operation on a `_DimensionUnitBase` child object.
      Makes sure of unit homogeniety by implicitly converting units where required before
      performing the operation.

      :param x: Object to perform operation on.
      :type x: Any
      :param _operator: Operator representing operation to be performed
      :type _operator: Callable
      :param return:
      :type return: _DimensionUnitBase | bool | int | float



   .. py:method:: convert_to(_to: mudu.base._UnitType)

      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :param unit_type: The _UnitType instance to be converted to.
      :type unit_type: _UnitType
      :param return:
      :type return: _DimensionUnitBase object with the `unit_type` as the unit.



.. py:class:: _DimensionType(unit: mudu.base._UnitType, value: int | float | collections.abc.Sequence)

   Bases: :py:obj:`_DimensionUnitBase`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards
      :type:  mudu.base._ConversionTableType
      :value: None



   .. py:attribute:: _dimension
      :value: None



   .. py:attribute:: _base_unit_standard
      :value: None



   .. py:attribute:: dimension


   .. py:attribute:: unit_type


   .. py:attribute:: unit


   .. py:attribute:: symbol


   .. py:attribute:: value


   .. py:method:: create_unit(**kwargs)
      :classmethod:



   .. py:property:: __value_not_seq

      value is not a sequence


   .. py:method:: __repr__()


   .. py:method:: __str__()


   .. py:method:: __len__()


   .. py:method:: __iter__()


   .. py:method:: __round__(y=0)


   .. py:method:: __mul__(x)


   .. py:method:: __truediv__(x)


   .. py:method:: __rtruediv__(x)


   .. py:method:: __pow__(x)


   .. py:method:: _check_and_convert(x, _operator: Callable) -> Self | bool

      Performs an arithemetic or boolean operation on a _DimensionType object.
      Makes sure of unit homogeniety by implicitly converting units where required before
      performing the operation.

      :param x: Object to perform operation on.
      :type x: Any
      :param _operator: Operator representing operation to be performed
      :type _operator: Callable
      :param return:
      :type return: _DimensionType | bool | int | float



   .. py:method:: convert_to(_to) -> Self | None

      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :param unit_type: The _UnitType instance to be converted to.
      :type unit_type: _UnitType
      :param return:
      :type return: _DimensionType object with the `unit_type` as the unit.



.. py:class:: DerivedQuantity(value: int | float, unit_definition: mudu.base._UnitType, quantity: str = GENERIC_QUANTITY)

   Bases: :py:obj:`_DimensionUnitBase`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards
      :type:  mudu.base._ConversionTableType
      :value: None



   .. py:attribute:: value


   .. py:attribute:: unit_type


   .. py:attribute:: symbol


   .. py:attribute:: quantity
      :type:  str


   .. py:method:: create_unit(**kwargs)
      :classmethod:


      Internal class method to create a new DerivedQuantity object,
      the same argument signature as init.



   .. py:attribute:: dimension


   .. py:property:: __value_not_seq

      value is not a sequence


   .. py:method:: __repr__()


   .. py:method:: __str__()


   .. py:method:: __len__()


   .. py:method:: __iter__()


   .. py:method:: __round__(y=0)


   .. py:method:: __mul__(x)


   .. py:method:: __truediv__(x)


   .. py:method:: __rtruediv__(x)


   .. py:method:: __pow__(x)


   .. py:method:: _check_and_convert(x, _operator: Callable) -> Self

      Performs an arithemetic or boolean operation on a DerivedQuantity child object.
      Makes sure of unit homogeniety by implicitly converting units where required before
      performing the operation.

      :param x: Object to perform operation on.
      :type x: Any
      :param _operator: Operator representing operation to be performed
      :type _operator: Callable
      :param return:
      :type return: DerivedQuantity | bool | int | float



   .. py:method:: convert_to(_to) -> Self | None

      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :param unit_type: The _UnitType instance to be converted to.
      :type unit_type: _UnitType
      :param return:
      :type return: _DimensionType object with the `unit_type` as the unit.



.. py:class:: GenericUnit(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _dimension


.. py:class:: GenericUnit2(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


.. py:class:: custom_unit(value: int | float, *, num: collections.abc.Sequence[mudu.base._UnitType], per: (collections.abc.Sequence[int] | collections.abc.Sequence[mudu.base._UnitType]) = (1, ), quantity=GENERIC_QUANTITY)

   Bases: :py:obj:`DerivedQuantity`


   Custom units


   .. py:attribute:: __numerator_unit
      :value: 1



   .. py:attribute:: __denominator_unit
      :value: 1



   .. py:attribute:: __numerator
      :value: []



   .. py:attribute:: __denominator
      :value: []



   .. py:attribute:: __unit_definition
      :value: 1.0



   .. py:method:: __check_condition(_from, allow_int=False)


   .. py:method:: __list2unit(_from: int | collections.abc.Sequence[mudu.base._UnitType], allow_int=False)


   .. py:method:: __repr_only_one_quantity(_from: collections.abc.Sequence, is_denum=False)

      Ensure that each unit represent exclusively only one quanitity



   .. py:method:: convert_to(num: collections.abc.Sequence, per: collections.abc.Sequence)
      :abstractmethod:


      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :param unit_type: The _UnitType instance to be converted to.
      :type unit_type: _UnitType
      :param return:
      :type return: _DimensionType object with the `unit_type` as the unit.



.. py:class:: Length(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


   .. py:attribute:: _dimension


   .. py:attribute:: _base_unit_standard


.. py:class:: Mass(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


   .. py:attribute:: _dimension


   .. py:attribute:: _base_unit_standard


.. py:class:: Time(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


   .. py:attribute:: _dimension


   .. py:attribute:: _base_unit_standard


.. py:class:: Temperature(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


   .. py:attribute:: _dimension


   .. py:attribute:: _base_unit_standard


.. py:class:: Angle(value, unit)

   Bases: :py:obj:`_DimensionType`


   Base class for all fundamental quantities.  As an example,
   `Length` class, `Mass` class and `Time`class are child classes of `_DimensionType`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: _DimensiionType

   .. attribute:: _check_and_convert

      same as the base class  (_DimensionUnitBase)

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


   .. py:attribute:: _dimension


.. py:data:: SolidAngle

.. py:data:: ElectricCurrent

.. py:data:: AmountOfSubstance

.. py:data:: LuminousIntensity

.. py:class:: Force(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: Pressure(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: Energy(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: Density(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: Power(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:data:: Voltage

.. py:data:: Capacitance

.. py:data:: Inductance

.. py:data:: MagneticFlux

.. py:data:: Resistance

.. py:data:: Conductance

.. py:data:: MageneticFieldStrength

.. py:data:: Illuminance

.. py:class:: Radioactivity(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: AbsorbedDose(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: DoseEquivalent(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:class:: Speed(value, unit_definition)

   Bases: :py:obj:`DerivedQuantity`


   Base class for all derived quantities.  As an example,
   `Force` class is a child class of `DerivedQuantity`. Check
   the documenation at by running `mudu --doc` on the cli
   on how to extend this class.

   .. attribute:: _conversion_standards

      Same as in `_DimensionUnitBase`

      :type: _ConversionTableType

   .. attribute:: _dimension

      Same as in  `DimensionUnitBase`

      :type: str

   .. attribute:: value

      Scalar value of the quantity

      :type: _SetOnce[int | float]

   .. attribute:: unit_type

      unit definition of the quantity

      :type: _UnitType

   .. attribute:: symbol

      Symbolic representation of the quantity unit

      :type: sympy.Symbol

   .. attribute:: create_unit

      Internal class method for creating a new DerivedQuantity object instance
      with the same argument signature as init.

      :type: DerivedQuantity

   .. attribute:: _check_and_convert

      same as the base class  ((_DimensionUnitBase))

      :type: x: Any, operator: Callable

   .. attribute:: convert_to

      same as the base class (_DimensionUnitBase)

      :type: _to


   .. py:attribute:: _conversion_standards


.. py:exception:: DimensionError

   Bases: :py:obj:`ArithmeticError`


   Base class for dimension errors.


.. py:exception:: ConversionError

   Bases: :py:obj:`ArithmeticError`


   Base class for conversion errors.


.. py:exception:: NotIterableError

   Bases: :py:obj:`Exception`


   Base class for iteration errors


.. py:exception:: SequenceOperationErrorr

   Bases: :py:obj:`Exception`


   Base class for sequence operation errors


.. py:exception:: OperationNotAvailable

   Bases: :py:obj:`Exception`


   Operation is not available in this version


