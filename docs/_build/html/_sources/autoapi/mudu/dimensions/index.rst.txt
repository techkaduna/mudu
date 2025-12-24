mudu.dimensions
===============

.. py:module:: mudu.dimensions

.. autoapi-nested-parse::

   =========================
   mudu.dimensions
   =========================

   mudu module, defines dimensions (quantities).

   For more information, read the documenation using

   .. code-block:: shell
       mudu --doc

   in your cli



Attributes
----------

.. autoapisummary::

   mudu.dimensions.SolidAngle
   mudu.dimensions.ElectricCurrent
   mudu.dimensions.AmountOfSubstance
   mudu.dimensions.LuminousIntensity
   mudu.dimensions.Voltage
   mudu.dimensions.Capacitance
   mudu.dimensions.Inductance
   mudu.dimensions.MagneticFlux
   mudu.dimensions.Resistance
   mudu.dimensions.Conductance
   mudu.dimensions.MageneticFieldStrength
   mudu.dimensions.Illuminance


Classes
-------

.. autoapisummary::

   mudu.dimensions._DimensionUnitBase
   mudu.dimensions.DerivedQuantity
   mudu.dimensions._DimensionType
   mudu.dimensions.Length
   mudu.dimensions.Mass
   mudu.dimensions.Time
   mudu.dimensions.Temperature
   mudu.dimensions.Angle
   mudu.dimensions.GenericUnit
   mudu.dimensions.Force
   mudu.dimensions.Pressure
   mudu.dimensions.Energy
   mudu.dimensions.Density
   mudu.dimensions.Power
   mudu.dimensions.Radioactivity
   mudu.dimensions.AbsorbedDose
   mudu.dimensions.DoseEquivalent
   mudu.dimensions.GenericUnit2
   mudu.dimensions.custom_unit


Functions
---------

.. autoapisummary::

   mudu.dimensions._unit_conversion


Module Contents
---------------

.. py:function:: _unit_conversion(self, _to)

   Converts from one unit to another, provided that there is a conversion standard
   defined for the units involved.

   :param unit_type: The _UnitType instance to be converted to.
   :type unit_type: _UnitType
   :param return:
   :type return: _DimensionType object with the `unit_type` as the unit.


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


.. py:data:: Voltage

.. py:data:: Capacitance

.. py:data:: Inductance

.. py:data:: MagneticFlux

.. py:data:: Resistance

.. py:data:: Conductance

.. py:data:: MageneticFieldStrength

.. py:data:: Illuminance

.. py:class:: custom_unit(value: int | float, *, num: collections.abc.Sequence[mudu.base._UnitType] | mudu.base._UnitType, per: int | collections.abc.Sequence[mudu.base._UnitType] | mudu.base._UnitType = 1, quantity=GENERIC_QUANTITY)

   Bases: :py:obj:`DerivedQuantity`


   Custom units


   .. py:attribute:: __numerator_unit
      :value: 1



   .. py:attribute:: __denuminator_unit
      :value: 1



   .. py:attribute:: __numerator
      :value: []



   .. py:attribute:: __denuminator
      :value: []



   .. py:method:: __list2unit(_from: int | mudu.base._UnitType | collections.abc.Sequence[mudu.base._UnitType], check_length=False)


   .. py:method:: convert_to(num: mudu.base._UnitType | collections.abc.Sequence)

      Converts from one unit to another, provided that there is a conversion standard
      defined for the units involved.

      :param unit_type: The _UnitType instance to be converted to.
      :type unit_type: _UnitType
      :param return:
      :type return: _DimensionType object with the `unit_type` as the unit.



