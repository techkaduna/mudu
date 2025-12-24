mudu.unit_registry
==================

.. py:module:: mudu.unit_registry


Attributes
----------

.. autoapisummary::

   mudu.unit_registry.METER_PER_SECOND
   mudu.unit_registry.FEET_PER_SECOND
   mudu.unit_registry.KNOT
   mudu.unit_registry.KELVIN_PER_METER
   mudu.unit_registry.FARENHEIT_PER_FEET
   mudu.unit_registry.CELSIUS_PER_FEET
   mudu.unit_registry.KILOGRAM_PER_METER_SECOND
   mudu.unit_registry.SLUG_PER_FEET_SECOND
   mudu.unit_registry.POUND_PER_FEET_SECOND
   mudu.unit_registry.METER_SQR_PER_SECOND
   mudu.unit_registry.FEET_PER_SQR_SECOND
   mudu.unit_registry.JOULE_PER_KILOGRAM_KELVIN
   mudu.unit_registry.JOULE_PER_MOL_KELVIN
   mudu.unit_registry.KILOGRAM_PER_MOL
   mudu.unit_registry._make_unit
   mudu.unit_registry.si_units
   mudu.unit_registry.uscs_units
   mudu.unit_registry.imperial_units
   mudu.unit_registry.si
   mudu.unit_registry.uscs
   mudu.unit_registry.imperial
   mudu.unit_registry._set_SI_standard


Classes
-------

.. autoapisummary::

   mudu.unit_registry.QuantityTable
   mudu.unit_registry.UnitRegistry
   mudu.unit_registry._UnitParam


Functions
---------

.. autoapisummary::

   mudu.unit_registry.to_si
   mudu.unit_registry.to_user_unit


Module Contents
---------------

.. py:class:: QuantityTable

   Table (dataclass) containing most of the quantities used in this module.


   .. py:attribute:: UNIT_NAME
      :type:  str


   .. py:attribute:: TEMPERATURE
      :type:  Callable


   .. py:attribute:: DENSITY
      :type:  Callable


   .. py:attribute:: PRESSURE
      :type:  Callable


   .. py:attribute:: DISTANCE
      :type:  Callable


   .. py:attribute:: DYNAMIC_VISCOSITY
      :type:  Callable


   .. py:attribute:: KINEMATIC_VISCOSITY
      :type:  Callable


   .. py:attribute:: SPEED
      :type:  Callable


   .. py:attribute:: LAPSE_RATE
      :type:  Callable


   .. py:attribute:: UNIV_GAS_CONSTANT
      :type:  Callable


   .. py:attribute:: EARTH_MOLAR_MASS
      :type:  Callable


   .. py:attribute:: SPEC_HEAT_CONSTANT
      :type:  Callable


.. py:data:: METER_PER_SECOND

.. py:data:: FEET_PER_SECOND

.. py:data:: KNOT

.. py:data:: KELVIN_PER_METER

.. py:data:: FARENHEIT_PER_FEET

.. py:data:: CELSIUS_PER_FEET

.. py:data:: KILOGRAM_PER_METER_SECOND

.. py:data:: SLUG_PER_FEET_SECOND

.. py:data:: POUND_PER_FEET_SECOND

.. py:data:: METER_SQR_PER_SECOND

.. py:data:: FEET_PER_SQR_SECOND

.. py:data:: JOULE_PER_KILOGRAM_KELVIN

.. py:data:: JOULE_PER_MOL_KELVIN

.. py:data:: KILOGRAM_PER_MOL

.. py:data:: _make_unit

.. py:data:: si_units

.. py:data:: uscs_units

.. py:data:: imperial_units

.. py:data:: si

.. py:data:: uscs

.. py:data:: imperial

.. py:class:: UnitRegistry

   Central blah


   .. py:attribute:: STANDARDS
      :value: ('SI', 'USCS', 'IMPERIAL')



   .. py:attribute:: _unit_standard
      :type:  str
      :value: 'SI'



   .. py:attribute:: _locked
      :type:  bool
      :value: False



   .. py:attribute:: SI


   .. py:attribute:: USCS


   .. py:attribute:: IMPERIAL


   .. py:attribute:: SI_UNITS


   .. py:attribute:: USCS_UNITS


   .. py:attribute:: IMPERIAL_UNITS


   .. py:attribute:: _unit_mapping


   .. py:attribute:: _unit_std_mapping


   .. py:method:: set_unit_standard(standard: str)
      :classmethod:


      Set the global unit standard.
      This can be done only one.



   .. py:property:: get_units
      :type: object

      :classmethod:


      Docs stay here


   .. py:property:: get_unit_standard
      :type: Dict

      :classmethod:


      Docs stay here


.. py:data:: _set_SI_standard

.. py:class:: _UnitParam(name: str, quantity: str)

   Internal base class descriptor for setting unit attributes only once.

   .. attribute:: name



      :type: str


   .. py:attribute:: name


   .. py:attribute:: quantity


   .. py:method:: __get__(instance, cls)


   .. py:method:: __set__(instance, value)


.. py:function:: to_si(x: float, quantity: str)

.. py:function:: to_user_unit(x, quantity: str)

   x is assumed to be in SI since all calculations are done in SI


