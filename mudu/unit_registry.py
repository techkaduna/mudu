import os
import sys
import functools
from typing import Callable, Dict
from dataclasses import dataclass, field

from .dimensions import (
    Length, 
    Time, 
    Mass, 
    Temperature, 
    Force, 
    Density,
    Pressure,
    GenericUnit2, 
)

from .units import (
    FEET,
    METER,
    INCH,
    KILOMETER,
    SECOND,
    HOUR,
    GRAM,
    SLUG,
    POUND,
    KILOGRAM,
    FARENHEIT,
    CELSIUS,
    KELVIN,
    NEWTON,
    POUND_FORCE,
    KILOGRAM_PER_CUBIC_METER,
    SLUG_PER_CUBIC_FOOT,
    POUND_PER_CUBIC_FOOT,
    PASCAL,
    inHg,
    POUND_PER_SQUARE_FOOT,
    JOULE,
    MOLE,
    KILO,
    OrderUnit,
    _UnitType
)



# ========================UNITS WORK============================================
@dataclass
class QuantityTable:
    """Table (dataclass) containing most of the quantities used in this module."""

    UNIT_NAME: str
    TEMPERATURE: Callable
    DENSITY: Callable
    PRESSURE: Callable
    DISTANCE: Callable
    DYNAMIC_VISCOSITY: Callable
    KINEMATIC_VISCOSITY: Callable
    SPEED: Callable
    LAPSE_RATE: Callable
    UNIV_GAS_CONSTANT: Callable
    EARTH_MOLAR_MASS: Callable
    SPEC_HEAT_CONSTANT: Callable


# ============
# SPEED UNITS
# =============
METER_PER_SECOND = METER / SECOND
FEET_PER_SECOND = FEET / SECOND
KNOT = _UnitType(
    _dimension="speed",
    _unit_name="knot",
    _unit_symbol="kn",
    _order=None,
)
# define conversion standard

# =================
# LAPSE RATE UNITS
# ==================
KELVIN_PER_METER = KELVIN / METER  # SI UNIT
FARENHEIT_PER_FEET = FARENHEIT / FEET  # USCS UNIT
CELSIUS_PER_FEET = CELSIUS / FEET  # IMPERIAL UNIT

# ==================
# DYNAMIC VISCOSITY
# ===================
KILOGRAM_PER_METER_SECOND = KILOGRAM / (METER * SECOND)  # SI UNIT
SLUG_PER_FEET_SECOND = SLUG / (FEET * SECOND)  # USCS UNIT
POUND_PER_FEET_SECOND = POUND / (FEET * SECOND)  # IMPERIAL

# ====================
# KINEMATIC VISCOSITY
# =====================
METER_SQR_PER_SECOND = (METER**2) / SECOND  # SI UNIT
FEET_PER_SQR_SECOND = (FEET**2) / SECOND  # USCS & IMPERIAL UNIT

# =====================
# SPECT HEAT CONSTANT
# =====================
JOULE_PER_KILOGRAM_KELVIN = JOULE / (KILOGRAM * KELVIN)  # SI UNIT

# =======================
# UNIVERSAL GAS CONSTANT
# ========================
JOULE_PER_MOL_KELVIN = JOULE / (MOLE * KELVIN)  # SI UNIT

# ====================
# EARTH MASS PER MOLE
# ====================
KILOGRAM_PER_MOL = KILOGRAM / MOLE  # SI UNIT

_make_unit = lambda unit: functools.partial(GenericUnit2, unit_definition=unit)


# ======================= UNIT STANDARDS DEFINITIONS =============================================
si_units = {
    "UNIT_NAME": "SI",
    "TEMPERATURE": KELVIN,
    "DENSITY": KILOGRAM_PER_CUBIC_METER,
    "PRESSURE": PASCAL,
    "DISTANCE": KILOMETER,
    "DYNAMIC_VISCOSITY": KILOGRAM_PER_METER_SECOND,
    "KINEMATIC_VISCOSITY": METER_SQR_PER_SECOND,
    "SPEED": METER_PER_SECOND,
    "LAPSE_RATE": KELVIN_PER_METER,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}

uscs_units = {
    "UNIT_NAME": "USCS",
    "TEMPERATURE": FARENHEIT,
    "DENSITY": SLUG_PER_CUBIC_FOOT,
    "PRESSURE": inHg,
    "DISTANCE": FEET,
    "DYNAMIC_VISCOSITY": SLUG_PER_FEET_SECOND,
    "KINEMATIC_VISCOSITY": FEET_PER_SQR_SECOND,
    "SPEED": FEET_PER_SECOND,
    "LAPSE_RATE": FARENHEIT_PER_FEET,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}

imperial_units = {
    "UNIT_NAME": "IMPERIAL",
    "TEMPERATURE": CELSIUS,
    "DENSITY": POUND_PER_CUBIC_FOOT,
    "PRESSURE": POUND_PER_SQUARE_FOOT,
    "DISTANCE": FEET,
    "DYNAMIC_VISCOSITY": POUND_PER_FEET_SECOND,
    "KINEMATIC_VISCOSITY": FEET_PER_SQR_SECOND,
    "SPEED": KNOT,
    "LAPSE_RATE": CELSIUS_PER_FEET,
    "UNIV_GAS_CONSTANT": JOULE_PER_MOL_KELVIN,
    "EARTH_MOLAR_MASS": KILOGRAM_PER_MOL,
    "SPEC_HEAT_CONSTANT": JOULE_PER_KILOGRAM_KELVIN,
}
# ====================================================================================================


# ====================== SI STANDARDS DEFINITIONS =====================================================
si = {
    "UNIT_NAME": "SI",
    "TEMPERATURE": functools.partial(Temperature, unit=si_units.get("TEMPERATURE")),
    "DENSITY": functools.partial(Density, unit_definition=si_units.get("DENSITY")),
    "PRESSURE": functools.partial(Pressure, unit_definition=si_units.get("PRESSURE")),
    "DISTANCE": functools.partial(Length, unit=si_units.get("DISTANCE")),
    "DYNAMIC_VISCOSITY": _make_unit(unit=si_units.get("DYNAMIC_VISCOSITY")),
    "KINEMATIC_VISCOSITY": _make_unit(unit=si_units.get("KINEMATIC_VISCOSITY")),
    "SPEED": _make_unit(unit=si_units.get("SPEED")),
    "LAPSE_RATE": _make_unit(unit=si_units.get("LAPSE_RATE")),
    "UNIV_GAS_CONSTANT": _make_unit(unit=si_units.get("UNIV_GAS_CONSTANT")),
    "EARTH_MOLAR_MASS": _make_unit(unit=si_units.get("EARTH_MOLAR_MASS")),
    "SPEC_HEAT_CONSTANT": _make_unit(unit=si_units.get("SPEC_HEAT_CONSTANT")),
}

uscs = {
    "UNIT_NAME": "USCS",
    "TEMPERATURE": functools.partial(Temperature, unit=uscs_units.get("TEMPERATURE")),
    "DENSITY": functools.partial(Density, unit_definition=uscs_units.get("DENSITY")),
    "PRESSURE": functools.partial(Pressure, unit_definition=uscs_units.get("PRESSURE")),
    "DISTANCE": functools.partial(Length, unit=uscs_units.get("DISTANCE")),
    "DYNAMIC_VISCOSITY": _make_unit(unit=uscs_units.get("DYNAMIC_VISCOSITY")),
    "KINEMATIC_VISCOSITY": _make_unit(unit=uscs_units.get("KINEMATIC_VISCOSITY")),
    "SPEED": _make_unit(unit=uscs_units.get("SPEED")),
    "LAPSE_RATE": _make_unit(unit=uscs_units.get("LAPSE_RATE")),
    "UNIV_GAS_CONSTANT": _make_unit(unit=uscs_units.get("UNIV_GAS_CONSTANT")),
    "EARTH_MOLAR_MASS": _make_unit(unit=uscs_units.get("EARTH_MOLAR_MASS")),
    "SPEC_HEAT_CONSTANT": _make_unit(unit=uscs_units.get("SPEC_HEAT_CONSTANT")),
}

imperial = {
    "UNIT_NAME": "IMPERIAL",
    "TEMPERATURE": functools.partial(
        Temperature, unit=imperial_units.get("TEMPERATURE")
    ),
    "DENSITY": functools.partial(
        Density, unit_definition=imperial_units.get("DENSITY")
    ),
    "PRESSURE": functools.partial(
        Pressure, unit_definition=imperial_units.get("PRESSURE")
    ),
    "DISTANCE": functools.partial(Length, unit=imperial_units.get("DISTANCE")),
    "DYNAMIC_VISCOSITY": _make_unit(unit=imperial_units.get("DYNAMIC_VISCOSITY")),
    "KINEMATIC_VISCOSITY": _make_unit(unit=imperial_units.get("KINEMATIC_VISCOSITY")),
    "SPEED": _make_unit(unit=imperial_units.get("SPEED")),
    "LAPSE_RATE": _make_unit(unit=imperial_units.get("LAPSE_RATE")),
    "UNIV_GAS_CONSTANT": _make_unit(unit=imperial_units.get("UNIV_GAS_CONSTANT")),
    "EARTH_MOLAR_MASS": _make_unit(unit=imperial_units.get("EARTH_MOLAR_MASS")),
    "SPEC_HEAT_CONSTANT": _make_unit(unit=imperial_units.get("SPEC_HEAT_CONSTANT")),
}
# =======================================================================================================


@dataclass
class UnitRegistry:
    """Central blah"""

    STANDARDS = ("SI", "USCS", "IMPERIAL")
    _unit_standard: str = field(default="SI", init=False, repr=False)
    _locked: bool = field(default=False, init=False, repr=False)

    SI = QuantityTable(**si)
    USCS = QuantityTable(**uscs)
    IMPERIAL = QuantityTable(**imperial)

    SI_UNITS = si_units
    USCS_UNITS = uscs_units
    IMPERIAL_UNITS = imperial_units

    _unit_mapping = dict(zip(STANDARDS, [SI, USCS, IMPERIAL]))
    _unit_std_mapping = dict(zip(STANDARDS, [SI_UNITS, USCS_UNITS, IMPERIAL_UNITS]))

    @classmethod
    def set_unit_standard(cls, standard: str):
        """Set the global unit standard.
        This can be done only one.
        """
        standard = standard.upper()

        if cls._locked is True:
            raise RuntimeError(
                f"Unit standard has already been set to {cls._unit_standard}"
            )

        if standard not in cls.STANDARDS:
            return ValueError(f"{standard} is not an available unit standard")

        cls._unit_standard = standard
        cls._locked = True

    @classmethod
    @property
    def get_units(cls) -> object:
        """Docs stay here"""
        res = cls._unit_mapping.get(cls._unit_standard)
        return res

    @classmethod
    @property
    def get_unit_standard(cls) -> Dict:
        """Docs stay here"""
        res = cls._unit_std_mapping.get(cls._unit_standard)
        return res


_set_SI_standard = lambda quantity, value: si.get(quantity)(value)


class _UnitParam:
    """Internal base class descriptor for setting unit attributes only once.

    Attributes
    ----------

    name: str

    """

    def __init__(self, name: str, quantity: str) -> None:
        self.name = name
        self.quantity = quantity

    def __get__(self, instance, cls):

        if instance is None:
            return self

        if self.name not in instance.__dict__:
            raise AttributeError(f"{self.name} has not been set.")

        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        if self.name in instance.__dict__:
            raise RuntimeError(f"{self.name} is a constant and cannot be changed.")

        # attribute does not exist; now set attribute but check type first
        if isinstance(value, (int, float)) is False:
            raise TypeError(f"{self.name} must be of type {(int, float)}")
        # sets the unit to SI units
        instance.__dict__[self.name] = si.get(self.quantity)(value)


def to_si(x: float, quantity: str):

    unit_standard = UnitRegistry.get_unit_standard
    val = getattr(UnitRegistry.get_units, quantity.upper())(x)
    if unit_standard.get("UNIT_NAME") != "SI":
        return val.convert_to(si_units.get(quantity.upper()))
    else:
        return val


def to_user_unit(x, quantity: str):
    """x is assumed to be in SI since all calculations are done in SI"""

    value = _set_SI_standard(quantity.upper(), x)
    user_std = UnitRegistry.get_unit_standard.get("UNIT_NAME")
    
    if user_std == "SI":
        return value
    else:
        std = uscs_units if user_std == "USCS" else imperial_units
        return value.convert_to(std.get(quantity.upper()))
