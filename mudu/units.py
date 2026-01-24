"""
====================
mudu.units
=====================

mudu module, defines all dimensionunit units and their
conversion table.

For more information, read the documenation using

.. code-block:: shell
    mudu --doc
    
in your cli

"""


import functools
import math

from .base import (
    SOLID_ANGLE,
    _UnitType,
    LENGTH,
    MASS,
    TIME,
    THERMODYNAMIC_TEMPERATURE,
    PLANE_ANGLE,
    FORCE,
    SPEED,
    PRESSURE,
    ENERGY,
    DENSITY,
    POWER,
    ILLUMINANCE,
    VOLTAGE,
    CAPACITANCE,
    INDUCTANCE,
    RESISTANCE,
    MAGNETIC_FLUX,
    MAGNETIC_FIELD_STRENGTH,
    CONDUCTANCE,
    RADIOACTIVITY,
    DOSE_EQUIVALENT,
    ABSORBED_DOSE,
    AMOUNT_OF_SUBSTANCE,
    LUMINOUS_INTENSITY,
    ELECTRIC_CURRENT,
    OrderUnit,
    KILO,
    _ConversionTableType,
)


# ================================ UNIT TYPE DEFINITIONS ===========================================

# =============
# Length Units
# =============
LENGTH_QUANTITY = "length"
INCH = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="inch",
    _unit_symbol="in",
)

METER = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="meter",
    _unit_symbol="m",
)

FEET = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="feet",
    _unit_symbol="ft",
)

YARD = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="yard",
    _unit_symbol="y",
)

MILE = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="mile",
    _unit_symbol="mi",
)

NAUTICAL_MILE = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="nautical mile",
    _unit_symbol="NM",
)

# ===========
# Mass Units
# ===========
MASS_QUANTITY = "mass"
GRAM = _UnitType(
    _quantity=MASS_QUANTITY,
    _dimension=MASS,
    _unit_name="gram",
    _unit_symbol="g",
)

OUNCE = _UnitType(_quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="ounce", _unit_symbol="oz")

POUND = _UnitType(_quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="pound", _unit_symbol="lb")

SLUG = _UnitType(
    _quantity=MASS_QUANTITY,
    _dimension=MASS,
    _unit_name="slug",
    _unit_symbol="slug",
)

SHORT_TON = _UnitType(_quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="short_ton", _unit_symbol="t")

LONG_TON = _UnitType(_quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="long_ton", _unit_symbol="t")

METRIC_TON = _UnitType(_quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="metric_ton", _unit_symbol="t")

# ===========
# Time Units
# ===========
TIME_QUANTITY = "time"
SECOND = _UnitType(
    _quantity=TIME_QUANTITY,
    _dimension=TIME,
    _unit_name="second",
    _unit_symbol="s",
)

MINUTE = _UnitType(
    _quantity=TIME_QUANTITY,
    _dimension=TIME,
    _unit_name="minute",
    _unit_symbol="min",
)

HOUR = _UnitType(
    _quantity=TIME_QUANTITY,
    _dimension=TIME,
    _unit_name="hour",
    _unit_symbol="hr",
)

# ==================
# Temperature Units
# ==================
TEMP_QUANTITY = "temperature"
KELVIN = _UnitType(
    _quantity=TEMP_QUANTITY, _dimension=THERMODYNAMIC_TEMPERATURE, _unit_name="kelvin", _unit_symbol="K"
)

RANKINE = _UnitType(
    _quantity=TEMP_QUANTITY, _dimension=THERMODYNAMIC_TEMPERATURE, _unit_name="rankine", _unit_symbol="R"
)

CELSIUS = _UnitType(
    _quantity=TEMP_QUANTITY,_dimension=THERMODYNAMIC_TEMPERATURE, _unit_name="celsius", _unit_symbol="C"
)

FARENHEIT = _UnitType(
    _quantity=TEMP_QUANTITY,_dimension=THERMODYNAMIC_TEMPERATURE, _unit_name="farenheit", _unit_symbol="F"
)

# ============
# Angle Units
# ============
ANGLE_QUANTITY = "angle"
RADIAN = _UnitType(_quantity=ANGLE_QUANTITY,_dimension=PLANE_ANGLE, _unit_name="radian", _unit_symbol="rad")

DEGREE = _UnitType(_quantity=ANGLE_QUANTITY,_dimension=PLANE_ANGLE, _unit_name="degree", _unit_symbol="deg")

# SOLID ANGLE
STERADIAN = _UnitType(_quantity=ANGLE_QUANTITY,_dimension=SOLID_ANGLE, _unit_name="steradian", _unit_symbol="sr")

# ==============
# AMPERE UNIT
# ==============
AMPERE = _UnitType(_quantity=ELECTRIC_CURRENT,_dimension=ELECTRIC_CURRENT, _unit_name="current", _unit_symbol="A")

# ===================================
# Units for the amount of substances
# ===================================
MOLE = _UnitType(
    _quantity=AMOUNT_OF_SUBSTANCE,
    _dimension=AMOUNT_OF_SUBSTANCE,
    _unit_name="mole",
    _unit_symbol="mol",
    _order=None,
)

# =========================
# Luminous Intensity Unit
# =========================
CANDELA = _UnitType(_quantity=LUMINOUS_INTENSITY,_dimension=LUMINOUS_INTENSITY, _unit_name="candela", _unit_symbol="cd")

# ==================================================================================


# =================== Derived Units ================================================
KILOGRAM = OrderUnit(KILO, GRAM)
KILOMETER = OrderUnit(KILO, METER)

# ============
# Force Units
# ============
__force_dimension = (KILOGRAM * (METER / SECOND**2))._dimension
NEWTON = _UnitType(
    _quantity=FORCE,
    _dimension=__force_dimension,
    _unit_name="newton",
    _unit_symbol="N",
    _order=None,
)

POUND_FORCE = _UnitType(
    _quantity=FORCE,
    _dimension=__force_dimension,
    _unit_name="pound",
    _unit_symbol="lbf",
    _order=None,
)

POUNDAL = _UnitType(
    _quantity=FORCE,
    _dimension=__force_dimension,
    _unit_name="poundal",
    _unit_symbol="pdl",
    _order=None,
)

DYNE = _UnitType(
    _quantity=FORCE,
    _dimension=__force_dimension,
    _unit_name="dyne",
    _unit_symbol="dyn",
    _order=None,
)

# ==============
# Speed Units
# ==============
__speed_dimension = (METER / SECOND)._dimension
METER_PER_SECOND = _UnitType(
    _quantity=SPEED,
    _dimension=__speed_dimension,
    _unit_name="meter_per_second",
    _unit_symbol="m/s",
    _order=None,
)

KM_PER_HOUR = _UnitType(
    _quantity=SPEED,
    _dimension=__speed_dimension,
    _unit_name="km_per_hour",
    _unit_symbol="km/h",
    _order=None,
)

FOOT_PER_SECOND = _UnitType(
    _quantity=SPEED,
    _dimension=__speed_dimension,
    _unit_name="foot_per_second",
    _unit_symbol="ft/s",
    _order=None,
)

MILE_PER_HOUR = _UnitType(
    _quantity=SPEED,
    _dimension=__speed_dimension,
    _unit_name="mile_per_hour",
    _unit_symbol="mph",
    _order=None,
)

KNOT = _UnitType(
    _quantity=SPEED,
    _dimension=__speed_dimension,
    _unit_name="knot",
    _unit_symbol="kn",
    _order=None,
)

# ===============
# Pressure Units
# ===============
__pressure_dimension = (NEWTON / (METER * METER))._dimension
PASCAL = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="pascal",
    _unit_symbol="Pa",
    _order=None,
)

PSI = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="pascal",
    _unit_symbol="psi",
    _order=None,
)

ATM = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="atm",
    _unit_symbol="atm",
    _order=None,
)

BAR = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="bar",
    _unit_symbol="bar",
    _order=None,
)

mmHg = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="mmHg",
    _unit_symbol="mmHg",
    _order=None,
)

inHg = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="inHg",
    _unit_symbol="inHg",
    _order=None,
)

POUND_PER_SQUARE_FOOT = _UnitType(
    _quantity=PRESSURE,
    _dimension=__pressure_dimension,
    _unit_name="pound_per_square_foot",
    _unit_symbol="lb/ft2",
    _order=None,
)

# =============
# Energy Units
# =============
__energy_dimension = (NEWTON * METER)._dimension
JOULE = _UnitType(
    _quantity=ENERGY,
    _dimension=__energy_dimension,
    _unit_name="joule",
    _unit_symbol="J",
    _order=None,
)

CALORIE = _UnitType(
    _quantity=ENERGY,
    _dimension=__energy_dimension,
    _unit_name="calorie",
    _unit_symbol="cal",
    _order=None,
)

WATT_HOUR = _UnitType(
    _quantity=ENERGY,
    _dimension=__energy_dimension,
    _unit_name="watt_hour",
    _unit_symbol="Wh",
    _order=None,
)

ELECTRON_VOLT = _UnitType(
    _quantity=ENERGY,
    _dimension=__energy_dimension,
    _unit_name="electron_volt",
    _unit_symbol="eV",
    _order=None,
)

BRITISH_THERMAL_UNIT = _UnitType(
    _quantity=ENERGY,
    _dimension=__energy_dimension,
    _unit_name="british_thermal_unit",
    _unit_symbol="BTU",
    _order=None,
)

# ==============
# Density Units
# ==============
__density_dimension = (KILOGRAM / (METER * METER * METER))._dimension
KILOGRAM_PER_CUBIC_METER = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="kilogram_per_cubic_meter",
    _unit_symbol="kg/m3",
    _order=None,
)

GRAM_PER_CUBIC_CENTIMETER = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="gram_per_cubic_centimeter",
    _unit_symbol="g/cm3",
    _order=None,
)

GRAM_PER_CUBIC_MILLILITER = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="gram_per_cubic_centimeter",
    _unit_symbol="g/cm3",
    _order=None,
)

POUND_PER_CUBIC_FOOT = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="pound_per_cubic_foot",
    _unit_symbol="lb/ft3",
    _order=None,
)

POUND_PER_CUBIC_INCH = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="pound_per_cubic_inch",
    _unit_symbol="lb/in3",
    _order=None,
)

SLUG_PER_CUBIC_FOOT = _UnitType(
    _quantity=DENSITY,
    _dimension=__density_dimension,
    _unit_name="slug_per_cubic_foot",
    _unit_symbol="slug/ft3",
    _order=None,
)

# ============
# Power Units
# ============
__power_dimension = (JOULE / SECOND)._dimension
WATT = _UnitType(
    _quantity=POWER,
    _dimension=__power_dimension,
    _unit_name="watt",
    _unit_symbol="W",
    _order=None,
)

HORSEPOWER = _UnitType(
    _quantity=POWER,
    _dimension=__power_dimension,
    _unit_name="horsepower",
    _unit_symbol="hp",
    _order=None,
)

BTU_PER_HOUR = _UnitType(
    _quantity=POWER,
    _dimension=__power_dimension,
    _unit_name="btu_per_hour",
    _unit_symbol="BTU/h",
    _order=None,
)

# =================
# Electrical Units
# =================
VOLT = _UnitType(
    _quantity=VOLTAGE,
    _dimension=(KILOGRAM * (METER**2) / (SECOND**3) * AMPERE)._dimension,
    _unit_name="volt",
    _unit_symbol="V",
    _order=None,
)

FARAD = _UnitType(
    _quantity=CAPACITANCE,
    _dimension=((SECOND**4) * AMPERE**2 / (METER**2) * KILOGRAM)._dimension,
    _unit_name="farad",
    _unit_symbol="F",
    _order=None,
)

HENRY = _UnitType(
    _quantity=INDUCTANCE,
    _dimension=(KILOGRAM * (METER**2) / (SECOND**2) * AMPERE**2)._dimension,
    _unit_name="henry",
    _unit_symbol="H",
    _order=None,
)

WEBER = _UnitType(
    _quantity=MAGNETIC_FLUX,
    _dimension=(KILOGRAM * (METER**2) / (SECOND**2) * AMPERE)._dimension,
    _unit_name="weber",
    _unit_symbol="Wb",
    _order=None,
)

OHMS = _UnitType(
    _quantity=RESISTANCE,
    _dimension=(KILOGRAM * (METER**2) / (SECOND**2) * AMPERE)._dimension,
    _unit_name="ohms",
    _unit_symbol="Ω",
    _order=None,
)

SIEMENS = _UnitType(
    _quantity=CONDUCTANCE,
    _dimension=((SECOND**3) * AMPERE**2 / (METER**2) / KILOGRAM)._dimension,
    _unit_name="siemens",
    _unit_symbol="S",
    _order=None,
)

TESLA = _UnitType(
    _quantity=MAGNETIC_FIELD_STRENGTH,
    _dimension=(KILOGRAM / (SECOND**2) * AMPERE)._dimension,
    _unit_name="tesla",
    _unit_symbol="T",
    _order=None,
)

# ============
# Illuminance
# ============
LUX = _UnitType(
    _quantity=ILLUMINANCE,
    _dimension=(CANDELA * STERADIAN / METER**2)._dimension,
    _unit_name="lux",
    _unit_symbol="lx",
    _order=None,
)

# ==============
# Radioactivity
# ==============
BECQUEREL = _UnitType(
    _quantity=RADIOACTIVITY,
    _dimension=(CANDELA * STERADIAN / METER**2)._dimension,
    _unit_name="becquerel",
    _unit_symbol="Bq",
    _order=None,
)

CURIE = _UnitType(
    _quantity=RADIOACTIVITY,
    _dimension=(1/SECOND)._dimension,
    _unit_name="curie",
    _unit_symbol="Ci",
    _order=None,
)

# ==============
# Absorbed Dose
# ==============
__radioactive_dose_dimension = (JOULE / KILOGRAM)._dimension
GRAY = _UnitType(
    _quantity=ABSORBED_DOSE,
    _dimension=__radioactive_dose_dimension,
    _unit_name="gray",
    _unit_symbol="Gy",
    _order=None,
)

RAD = _UnitType(
    _quantity=ABSORBED_DOSE,
    _dimension=__radioactive_dose_dimension,
    _unit_name="rad",
    _unit_symbol="rad",
    _order=None,
)

# ================
# Dose Equivalent
# ================
SIEVERT = _UnitType(
    _quantity=DOSE_EQUIVALENT,
    _dimension=__radioactive_dose_dimension,
    _unit_name="sievert",
    _unit_symbol="Sv",
    _order=None,
)

REM = _UnitType(
    _quantity=DOSE_EQUIVALENT,
    _dimension=__radioactive_dose_dimension,
    _unit_name="rem",
    _unit_symbol="rem",
    _order=None,
)

# =================
# ============================
# utility conversion function
# ============================
_basic_unit_converter = lambda x, y, invert=False: x * y if invert is False else x / y

# ============================ CONVERSION TABLES =====================================
_LENGTH_CONVERSION_TABLE = _ConversionTableType(
    dimension=LENGTH,
    conversion_table=[
        ((INCH, METER), functools.partial(_basic_unit_converter, y=0.0254)),
        ((FEET, METER), functools.partial(_basic_unit_converter, y=0.3048)),
        ((YARD, METER), functools.partial(_basic_unit_converter, y=0.9144)),
        ((MILE, METER), functools.partial(_basic_unit_converter, y=1609.344)),
        ((NAUTICAL_MILE, METER), functools.partial(_basic_unit_converter, y=1852)),
        ((INCH, FEET), functools.partial(_basic_unit_converter, y=12)),
    ],
)

_MASS_CONVERSION_TABLE = _ConversionTableType(
    dimension=MASS,
    conversion_table=[
        ((POUND, GRAM), functools.partial(_basic_unit_converter, y=453.59237)),
        ((OUNCE, GRAM), functools.partial(_basic_unit_converter, y=28.3495)),
        ((POUND, OUNCE), functools.partial(_basic_unit_converter, y=16)),
        ((SLUG, GRAM), functools.partial(_basic_unit_converter, y=14.593903)),
        ((SHORT_TON, GRAM), functools.partial(_basic_unit_converter, y=907000)),
        ((LONG_TON, GRAM), functools.partial(_basic_unit_converter, y=1016000)),
        ((METRIC_TON, GRAM), functools.partial(_basic_unit_converter, y=1000000)),
        
    ],
)

_TIME_CONVERSION_TABLE = _ConversionTableType(
    dimension=TIME,
    conversion_table=(
        ((MINUTE, SECOND), functools.partial(_basic_unit_converter, y=60)),
        ((HOUR, SECOND), functools.partial(_basic_unit_converter, y=3600)),
        ((HOUR, MINUTE), functools.partial(_basic_unit_converter, y=60)),
    ),
)

_TEMPERATURE_CONVERSION_TABLE = _ConversionTableType(
    dimension=THERMODYNAMIC_TEMPERATURE,
    conversion_table=(
        (
            (KELVIN, RANKINE),
            lambda x, invert=False: x * 1.8 if invert is False else x / 1.8,
        ),
        (
            (KELVIN, CELSIUS),
            lambda x, invert=False: x - 273.15 if invert is False else x + 273.15,
        ),
        (
            (KELVIN, FARENHEIT),
            lambda x, invert=False: (
                (1.8 * x) - 459.67 if invert is False else (x + 459.67) / 1.8
            ),
        ),
    ),
)

_ANGLE_CONVERSION_TABLE = _ConversionTableType(
    dimension=PLANE_ANGLE,
    conversion_table=(
        (
            (DEGREE, RADIAN),
            lambda x, invert=False: (
                math.radians(x) if invert is False else math.degrees(x)
            ),
        ),
    ),
)

_FORCE_CONVERSION_TABLE = _ConversionTableType(
    dimension=FORCE,
    conversion_table=(
        (
            (DYNE, NEWTON),
            functools.partial(_basic_unit_converter, y=0.00001)
        ),
        (
            (POUND_FORCE, NEWTON),
                functools.partial(_basic_unit_converter, y=4.44822)
        ),
        (
            (POUNDAL, NEWTON),
                functools.partial(_basic_unit_converter, y=0.138255)
        ),
    )
)

_SPEED_CONVERSION_TABLE = _ConversionTableType(
    dimension=SPEED,
    conversion_table=(
        (
            (KM_PER_HOUR, METER_PER_SECOND),
            functools.partial(_basic_unit_converter, y=1000/3600)
        ),
        (
            (MILE_PER_HOUR, METER_PER_SECOND),
                functools.partial(_basic_unit_converter, y=0.44704)
        ),
        (
            (KNOT, METER_PER_SECOND),
                functools.partial(_basic_unit_converter, y=1852/3600)
        ),
        (
            (FOOT_PER_SECOND, METER_PER_SECOND),
                functools.partial(_basic_unit_converter, y=0.3048)
        ),
    )
)

_PRESSURE_CONVERSION_TABLE = _ConversionTableType(
    dimension=PRESSURE,
    conversion_table=(
        (
            (PSI, PASCAL),
                functools.partial(_basic_unit_converter, y=6894.76)
        ),
        (
            (ATM, PASCAL),
                functools.partial(_basic_unit_converter, y=101325)
        ),
        (
            (BAR, PASCAL),
                functools.partial(_basic_unit_converter, y=100000)
        ),
        (
            (mmHg, PASCAL),
                functools.partial(_basic_unit_converter, y=133.322)
        ),
        (
            (inHg, PASCAL),
                functools.partial(_basic_unit_converter, y=3386.389)
        ),
        (
            (POUND_PER_SQUARE_FOOT, PASCAL),
                functools.partial(_basic_unit_converter, y=47.8803)
        ),
)
)

_ENERGY_CONVERSION_TABLE = _ConversionTableType(
    dimension=ENERGY,
    conversion_table=(
        (
            (CALORIE, JOULE),
                functools.partial(_basic_unit_converter, y=4.184)
        ),
        (
            (WATT_HOUR, JOULE),
                functools.partial(_basic_unit_converter, y=3600)
        ),
        (
            (ELECTRON_VOLT, JOULE),
                functools.partial(_basic_unit_converter, y=1.60217662e-19)
        ),
        (
            (BRITISH_THERMAL_UNIT, JOULE),
                functools.partial(_basic_unit_converter, y=1055)
        ),
    )
)

_DENSITY_CONVERSION_TABLE = _ConversionTableType(
    dimension=DENSITY,
    conversion_table=(
        (
            (GRAM_PER_CUBIC_CENTIMETER, KILOGRAM_PER_CUBIC_METER),
                functools.partial(_basic_unit_converter, y=1000)
        ),
        (
            (GRAM_PER_CUBIC_MILLILITER, KILOGRAM_PER_CUBIC_METER),
                functools.partial(_basic_unit_converter, y=1000)
        ),
        (
            (POUND_PER_CUBIC_FOOT, KILOGRAM_PER_CUBIC_METER),
                functools.partial(_basic_unit_converter, y=16.0185)
        ),
        (
            (POUND_PER_CUBIC_INCH, KILOGRAM_PER_CUBIC_METER),
                functools.partial(_basic_unit_converter, y=27679.9)
        ),
        (
            (SLUG_PER_CUBIC_FOOT, KILOGRAM_PER_CUBIC_METER),
                functools.partial(_basic_unit_converter, y=515.3788)
        ),
    )
)

_POWER_CONVERSION_TABLE = _ConversionTableType(
    dimension=POWER,
    conversion_table=(
        (
            (HORSEPOWER, WATT),
                functools.partial(_basic_unit_converter, y=745.7)
        ),
        (
            (BTU_PER_HOUR, WATT),
                functools.partial(_basic_unit_converter, y=0.293071)
        ),
    )
)

_RADIOACTIVITY_CONVERSION_TABLE = _ConversionTableType(
    dimension=RADIOACTIVITY,
    conversion_table=(
        (
            (CURIE, BECQUEREL),
                functools.partial(_basic_unit_converter, y=3.7e10)
        ),
    )
)

_ABSORBED_DOSE_CONVERSION_TABLE = _ConversionTableType(
    dimension=ABSORBED_DOSE,
    conversion_table=(
        (
            (GRAY, RAD),
                functools.partial(_basic_unit_converter, y=100)
        ),
    )
)

_DOSE_EQUIVALENT_TABLE = _ConversionTableType(
    dimension=DOSE_EQUIVALENT,
    conversion_table=(
        (
            (SIEVERT, REM),
                functools.partial(_basic_unit_converter, y=100)
        ),
    )
)

# =========================================================================================
