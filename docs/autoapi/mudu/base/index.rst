mudu.base
=========

.. py:module:: mudu.base

.. autoapi-nested-parse::

   ===================
   mudu.base
   ===================

   base module for mudu.

   For more information, read the documenation using

   .. code-block:: shell
       mudu --doc

   in your cli



Attributes
----------

.. autoapisummary::

   mudu.base.LENGTH
   mudu.base.MASS
   mudu.base.TIME
   mudu.base.PLANE_ANGLE
   mudu.base.SOLID_ANGLE
   mudu.base.THERMODYNAMIC_TEMPERATURE
   mudu.base.ELECTRIC_CURRENT
   mudu.base.AMOUNT_OF_SUBSTANCE
   mudu.base.LUMINOUS_INTENSITY
   mudu.base.FORCE
   mudu.base.PRESSURE
   mudu.base.ENERGY
   mudu.base.DENSITY
   mudu.base.POWER
   mudu.base.ILLUMINANCE
   mudu.base.VOLTAGE
   mudu.base.CAPACITANCE
   mudu.base.RESISTANCE
   mudu.base.CONDUCTANCE
   mudu.base.MAGNETIC_FLUX
   mudu.base.MAGNETIC_FIELD_STRENGTH
   mudu.base.INDUCTANCE
   mudu.base.RADIOACTIVITY
   mudu.base.ABSORBED_DOSE
   mudu.base.DOSE_EQUIVALENT
   mudu.base.GENERIC_UNIT
   mudu.base.GENERIC_DIMENSION
   mudu.base.GENERIC_QUANTITY
   mudu.base.DIMENSIONLESS
   mudu.base.DIMENSIONLESS_UNIT
   mudu.base.GIGA
   mudu.base.MEGA
   mudu.base.KILO
   mudu.base.CENTI
   mudu.base.MILLI
   mudu.base.MICRO
   mudu.base.NANO
   mudu.base.PICO
   mudu.base.FEMTO
   mudu.base.ATTO
   mudu.base.OrderUnit


Classes
-------

.. autoapisummary::

   mudu.base._OrderType
   mudu.base._ConversionTableType
   mudu.base._UnitType
   mudu.base._OrderUnitType
   mudu.base._SetOnce


Module Contents
---------------

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


.. py:data:: PRESSURE
   :value: 'pressure'


.. py:data:: ENERGY
   :value: 'energy'


.. py:data:: DENSITY
   :value: 'density'


.. py:data:: POWER
   :value: 'power'


.. py:data:: ILLUMINANCE
   :value: 'illuminance'


.. py:data:: VOLTAGE
   :value: 'voltage'


.. py:data:: CAPACITANCE
   :value: 'capacitance'


.. py:data:: RESISTANCE
   :value: 'resistance'


.. py:data:: CONDUCTANCE
   :value: 'conductance'


.. py:data:: MAGNETIC_FLUX
   :value: 'magnetic_flux'


.. py:data:: MAGNETIC_FIELD_STRENGTH
   :value: 'magnetic_field_strength'


.. py:data:: INDUCTANCE
   :value: 'inductance'


.. py:data:: RADIOACTIVITY
   :value: 'radioactivity'


.. py:data:: ABSORBED_DOSE
   :value: 'absorbed_dose'


.. py:data:: DOSE_EQUIVALENT
   :value: 'dose_equivalent'


.. py:data:: GENERIC_UNIT
   :value: 'generic_unit'


.. py:data:: GENERIC_DIMENSION
   :value: 'generic_dimension'


.. py:data:: GENERIC_QUANTITY
   :value: 'generic_quantity'


.. py:data:: DIMENSIONLESS
   :value: 'dimensionless'


.. py:data:: DIMENSIONLESS_UNIT
   :value: 'dimensionless_unit'


.. py:class:: _OrderType

   Internal base class for defining multiple prefix (order).

   .. attribute:: name

      name of the multiple prefix e.g. `kilo`

      :type: str

   .. attribute:: symbol

      symbol of the multiple prefix e.g. `k`

      :type: str

   .. attribute:: value

      multiple value the _OrderType represents `kilo represents 1000 `

      :type: float


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: symbol
      :type:  str


   .. py:attribute:: value
      :type:  float


.. py:class:: _ConversionTableType

   Internal base class definition for conversion table for dimension objects.

   .. attribute:: dimension

      Conversion table contains units of dimension. Dimension could be `LENGTH TIME MASS` e.t.c.

      :type: str

   .. attribute:: conversion_table

      `tuple` containing the conversion units and a lambda calculating the conversion. e.g.
      `((INCH, METER), functools.partial(_basic_unit_converter, y=0.0254))`

      :type: Sequence

   .. attribute:: extend

      Extend an existing conversion table with more conversion standards.

      :type: None


   .. py:attribute:: dimension
      :type:  str


   .. py:attribute:: conversion_table
      :type:  Sequence


   .. py:method:: extend(seq: Sequence) -> None

      Convieniece method to extend the built-in conversion standard to
      accomodate other user defined units.

      :param seq:
                  tuple that contains:
                      a tuple of the units
                      and a callable that defines the conversion operation.
      :type seq: Sequence
      :param - **Usage example**:
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

.. py:class:: _OrderUnitType

   Intenal class for creating a multiple prefix unit.

   - **Usage example**

       .. code-block:: python

           from mudu import Length, METER, OrderUnit, KILO

           # define an OrderUnit
           KILOMETER = OrderUnit(KILO, METER)

           some_length = Length(12, KILOMETER)

   **NOTE** `_OrderUnit` was not used to create the multiple prefix unit,
   `OrderUnit`, which is an instance of `_OrderUnit`, was used instead.


   .. py:method:: __call__(_order: _OrderType, unit: _UnitType)


.. py:data:: OrderUnit

.. py:class:: _SetOnce(name: str, expected_types)

   Internal base class descriptor for setting attributes only once.

   .. attribute:: name

      Attribute identifier

      :type: str

   .. attribute:: expected_types

      Attribute expected type(s)

      :type: obj | Sequence


   .. py:attribute:: name


   .. py:attribute:: expected_types


   .. py:method:: __get__(instance, cls)


   .. py:method:: __set__(instance, value)


