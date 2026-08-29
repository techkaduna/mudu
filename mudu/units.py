"""
====================
mudu.units
=====================

mudu module, defines all dimension/unit units and their
conversion tables.

For more information, read the documentation using

.. code-block:: shell
    mudu --doc

in your cli
"""

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
    Linear,
    Affine,
    _ConversionTableType,
)

# ================================ UNIT TYPE DEFINITIONS ===========================================

# =============
# Length Units
# =============
LENGTH_QUANTITY = "length"
INCH = _UnitType(
    _quantity=LENGTH_QUANTITY, _dimension=LENGTH, _unit_name="inch", _unit_symbol="in"
)
METER = _UnitType(
    _quantity=LENGTH_QUANTITY, _dimension=LENGTH, _unit_name="meter", _unit_symbol="m"
)
FEET = _UnitType(
    _quantity=LENGTH_QUANTITY, _dimension=LENGTH, _unit_name="feet", _unit_symbol="ft"
)
YARD = _UnitType(
    _quantity=LENGTH_QUANTITY, _dimension=LENGTH, _unit_name="yard", _unit_symbol="y"
)
MILE = _UnitType(
    _quantity=LENGTH_QUANTITY, _dimension=LENGTH, _unit_name="mile", _unit_symbol="mi"
)
NAUTICAL_MILE = _UnitType(
    _quantity=LENGTH_QUANTITY,
    _dimension=LENGTH,
    _unit_name="nautical_mile",
    _unit_symbol="NM",
)

# ===========
# Mass Units
# ===========
MASS_QUANTITY = "mass"
GRAM = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="gram", _unit_symbol="g"
)
OUNCE = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="ounce", _unit_symbol="oz"
)
POUND = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="pound", _unit_symbol="lb"
)
SLUG = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="slug", _unit_symbol="slug"
)
SHORT_TON = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="short_ton", _unit_symbol="t"
)
LONG_TON = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="long_ton", _unit_symbol="t"
)
METRIC_TON = _UnitType(
    _quantity=MASS_QUANTITY, _dimension=MASS, _unit_name="metric_ton", _unit_symbol="t"
)

# ===========
# Time Units
# ===========
TIME_QUANTITY = "time"
SECOND = _UnitType(
    _quantity=TIME_QUANTITY, _dimension=TIME, _unit_name="second", _unit_symbol="s"
)
MINUTE = _UnitType(
    _quantity=TIME_QUANTITY, _dimension=TIME, _unit_name="minute", _unit_symbol="min"
)
HOUR = _UnitType(
    _quantity=TIME_QUANTITY, _dimension=TIME, _unit_name="hour", _unit_symbol="hr"
)

# ==================
# Temperature Units
# ==================
TEMP_QUANTITY = "temperature"
KELVIN = _UnitType(
    _quantity=TEMP_QUANTITY,
    _dimension=THERMODYNAMIC_TEMPERATURE,
    _unit_name="kelvin",
    _unit_symbol="K",
)
RANKINE = _UnitType(
    _quantity=TEMP_QUANTITY,
    _dimension=THERMODYNAMIC_TEMPERATURE,
    _unit_name="rankine",
    _unit_symbol="R",
)
CELSIUS = _UnitType(
    _quantity=TEMP_QUANTITY,
    _dimension=THERMODYNAMIC_TEMPERATURE,
    _unit_name="celsius",
    _unit_symbol="C",
)
FARENHEIT = _UnitType(
    _quantity=TEMP_QUANTITY,
    _dimension=THERMODYNAMIC_TEMPERATURE,
    _unit_name="farenheit",
    _unit_symbol="F",
)

# ============
# Angle Units
# ============
ANGLE_QUANTITY = "angle"
RADIAN = _UnitType(
    _quantity=ANGLE_QUANTITY,
    _dimension=PLANE_ANGLE,
    _unit_name="radian",
    _unit_symbol="rad",
)
DEGREE = _UnitType(
    _quantity=ANGLE_QUANTITY,
    _dimension=PLANE_ANGLE,
    _unit_name="degree",
    _unit_symbol="deg",
)

# SOLID ANGLE
STERADIAN = _UnitType(
    _quantity=ANGLE_QUANTITY,
    _dimension=SOLID_ANGLE,
    _unit_name="steradian",
    _unit_symbol="sr",
)

# ==============
# AMPERE UNIT
# ==============
AMPERE = _UnitType(
    _quantity=ELECTRIC_CURRENT,
    _dimension=ELECTRIC_CURRENT,
    _unit_name="ampere",
    _unit_symbol="A",
)

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
CANDELA = _UnitType(
    _quantity=LUMINOUS_INTENSITY,
    _dimension=LUMINOUS_INTENSITY,
    _unit_name="candela",
    _unit_symbol="cd",
)

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
    _unit_name="pound_force",
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
    _unit_name="psi",
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
    _unit_name="gram_per_cubic_milliliter",
    _unit_symbol="g/mL",
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
    _unit_symbol="Ω",
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
__radioactivity_dimension = (1 / SECOND)._dimension
BECQUEREL = _UnitType(
    _quantity=RADIOACTIVITY,
    _dimension=__radioactivity_dimension,
    _unit_name="becquerel",
    _unit_symbol="Bq",
    _order=None,
)
CURIE = _UnitType(
    _quantity=RADIOACTIVITY,
    _dimension=__radioactivity_dimension,
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

# ============================================================================
# CONVERSION TABLES -- star topology.
#
# Every table below has exactly ONE base unit per dimension, and every
# other unit registers exactly one Conversion relative to that base unit.
# Converting between any two non-base units is always a two-hop
# from_unit -> base_unit -> to_unit operation handled generically in
# dimensions.py; no pairwise entries are needed or supported.
# r
# Uses NIST SP 811 or common engineering reference values.
# ============================================================================

_LENGTH_CONVERSION_TABLE = _ConversionTableType(dimension=LENGTH, base_unit=METER)
_LENGTH_CONVERSION_TABLE.register(INCH, Linear(0.0254))
_LENGTH_CONVERSION_TABLE.register(FEET, Linear(0.3048))
_LENGTH_CONVERSION_TABLE.register(YARD, Linear(0.9144))
_LENGTH_CONVERSION_TABLE.register(MILE, Linear(1609.344))
_LENGTH_CONVERSION_TABLE.register(NAUTICAL_MILE, Linear(1852))

_MASS_CONVERSION_TABLE = _ConversionTableType(dimension=MASS, base_unit=GRAM)
_MASS_CONVERSION_TABLE.register(POUND, Linear(453.59237))
_MASS_CONVERSION_TABLE.register(OUNCE, Linear(28.349523125))
_MASS_CONVERSION_TABLE.register(SLUG, Linear(14593.903))
_MASS_CONVERSION_TABLE.register(SHORT_TON, Linear(907184.74))
_MASS_CONVERSION_TABLE.register(LONG_TON, Linear(1016046.9088))
_MASS_CONVERSION_TABLE.register(METRIC_TON, Linear(1_000_000))

_TIME_CONVERSION_TABLE = _ConversionTableType(dimension=TIME, base_unit=SECOND)
_TIME_CONVERSION_TABLE.register(MINUTE, Linear(60))
_TIME_CONVERSION_TABLE.register(HOUR, Linear(3600))

_TEMPERATURE_CONVERSION_TABLE = _ConversionTableType(
    dimension=THERMODYNAMIC_TEMPERATURE, base_unit=KELVIN
)
_TEMPERATURE_CONVERSION_TABLE.register(RANKINE, Linear(5 / 9))
_TEMPERATURE_CONVERSION_TABLE.register(CELSIUS, Affine(scale=1.0, offset=273.15))
_TEMPERATURE_CONVERSION_TABLE.register(
    FARENHEIT, Affine(scale=5 / 9, offset=273.15 - 32 * (5 / 9))
)

_ANGLE_CONVERSION_TABLE = _ConversionTableType(dimension=PLANE_ANGLE, base_unit=RADIAN)
_ANGLE_CONVERSION_TABLE.register(DEGREE, Linear(3.14159265358979323846 / 180))

_FORCE_CONVERSION_TABLE = _ConversionTableType(
    dimension=__force_dimension, base_unit=NEWTON
)
_FORCE_CONVERSION_TABLE.register(DYNE, Linear(0.00001))
_FORCE_CONVERSION_TABLE.register(POUND_FORCE, Linear(4.4482216153))
_FORCE_CONVERSION_TABLE.register(POUNDAL, Linear(0.138254954376))

_SPEED_CONVERSION_TABLE = _ConversionTableType(
    dimension=__speed_dimension, base_unit=METER_PER_SECOND
)
_SPEED_CONVERSION_TABLE.register(KM_PER_HOUR, Linear(1000 / 3600))
_SPEED_CONVERSION_TABLE.register(MILE_PER_HOUR, Linear(0.44704))
_SPEED_CONVERSION_TABLE.register(KNOT, Linear(1852 / 3600))
_SPEED_CONVERSION_TABLE.register(FOOT_PER_SECOND, Linear(0.3048))

_PRESSURE_CONVERSION_TABLE = _ConversionTableType(
    dimension=__pressure_dimension, base_unit=PASCAL
)
_PRESSURE_CONVERSION_TABLE.register(PSI, Linear(6894.757293168))
_PRESSURE_CONVERSION_TABLE.register(ATM, Linear(101325))
_PRESSURE_CONVERSION_TABLE.register(BAR, Linear(100000))
_PRESSURE_CONVERSION_TABLE.register(mmHg, Linear(133.322387415))
_PRESSURE_CONVERSION_TABLE.register(inHg, Linear(3386.389))
_PRESSURE_CONVERSION_TABLE.register(POUND_PER_SQUARE_FOOT, Linear(47.880259))

_ENERGY_CONVERSION_TABLE = _ConversionTableType(
    dimension=__energy_dimension, base_unit=JOULE
)
_ENERGY_CONVERSION_TABLE.register(CALORIE, Linear(4.184))
_ENERGY_CONVERSION_TABLE.register(WATT_HOUR, Linear(3600))
_ENERGY_CONVERSION_TABLE.register(ELECTRON_VOLT, Linear(1.602176634e-19))
_ENERGY_CONVERSION_TABLE.register(BRITISH_THERMAL_UNIT, Linear(1055.05585262))

_DENSITY_CONVERSION_TABLE = _ConversionTableType(
    dimension=__density_dimension, base_unit=KILOGRAM_PER_CUBIC_METER
)
_DENSITY_CONVERSION_TABLE.register(GRAM_PER_CUBIC_CENTIMETER, Linear(1000))
_DENSITY_CONVERSION_TABLE.register(GRAM_PER_CUBIC_MILLILITER, Linear(1000))
_DENSITY_CONVERSION_TABLE.register(POUND_PER_CUBIC_FOOT, Linear(16.01846337))
_DENSITY_CONVERSION_TABLE.register(POUND_PER_CUBIC_INCH, Linear(27679.90471))
_DENSITY_CONVERSION_TABLE.register(SLUG_PER_CUBIC_FOOT, Linear(515.3788184))

_POWER_CONVERSION_TABLE = _ConversionTableType(
    dimension=__power_dimension, base_unit=WATT
)
_POWER_CONVERSION_TABLE.register(HORSEPOWER, Linear(745.69987158227))
_POWER_CONVERSION_TABLE.register(BTU_PER_HOUR, Linear(0.29307107))

_RADIOACTIVITY_CONVERSION_TABLE = _ConversionTableType(
    dimension=__radioactivity_dimension, base_unit=BECQUEREL
)
_RADIOACTIVITY_CONVERSION_TABLE.register(CURIE, Linear(3.7e10))

_ABSORBED_DOSE_CONVERSION_TABLE = _ConversionTableType(
    dimension=__radioactive_dose_dimension, base_unit=GRAY
)
_ABSORBED_DOSE_CONVERSION_TABLE.register(RAD, Linear(0.01))

_DOSE_EQUIVALENT_TABLE = _ConversionTableType(
    dimension=__radioactive_dose_dimension, base_unit=SIEVERT
)
_DOSE_EQUIVALENT_TABLE.register(REM, Linear(0.01))

# =========================================================================================

__all__ = [
    # length
    "INCH",
    "METER",
    "KILOMETER",
    "FEET",
    "YARD",
    "MILE",
    "NAUTICAL_MILE",
    # mass
    "GRAM",
    "OUNCE",
    "KILOGRAM",
    "POUND",
    "SLUG",
    "SHORT_TON",
    "LONG_TON",
    "METRIC_TON",
    # time
    "SECOND",
    "MINUTE",
    "HOUR",
    # temperature
    "KELVIN",
    "RANKINE",
    "CELSIUS",
    "FARENHEIT",
    # angle
    "DEGREE",
    "RADIAN",
    "STERADIAN",
    # base SI
    "AMPERE",
    "MOLE",
    "CANDELA",
    # force
    "NEWTON",
    "POUND_FORCE",
    "POUNDAL",
    "DYNE",
    # pressure
    "PASCAL",
    "PSI",
    "mmHg",
    "inHg",
    "BAR",
    "ATM",
    "POUND_PER_SQUARE_FOOT",
    # energy
    "JOULE",
    "BRITISH_THERMAL_UNIT",
    "CALORIE",
    "WATT_HOUR",
    "ELECTRON_VOLT",
    # density
    "KILOGRAM_PER_CUBIC_METER",
    "GRAM_PER_CUBIC_CENTIMETER",
    "GRAM_PER_CUBIC_MILLILITER",
    "POUND_PER_CUBIC_FOOT",
    "POUND_PER_CUBIC_INCH",
    "SLUG_PER_CUBIC_FOOT",
    # power
    "WATT",
    "HORSEPOWER",
    "BTU_PER_HOUR",
    # electrical
    "VOLT",
    "FARAD",
    "HENRY",
    "WEBER",
    "OHMS",
    "TESLA",
    "SIEMENS",
    "LUX",
    # radioactivity / dose
    "BECQUEREL",
    "CURIE",
    "GRAY",
    "RAD",
    "SIEVERT",
    "REM",
    # speed
    "METER_PER_SECOND",
    "MILE_PER_HOUR",
    "KM_PER_HOUR",
    "FOOT_PER_SECOND",
    "KNOT",
    # conversion tables used in dimensions.py
    "_LENGTH_CONVERSION_TABLE",
    "_MASS_CONVERSION_TABLE",
    "_TIME_CONVERSION_TABLE",
    "_ANGLE_CONVERSION_TABLE",
    "_TEMPERATURE_CONVERSION_TABLE",
    "_FORCE_CONVERSION_TABLE",
    "_PRESSURE_CONVERSION_TABLE",
    "_ENERGY_CONVERSION_TABLE",
    "_DENSITY_CONVERSION_TABLE",
    "_POWER_CONVERSION_TABLE",
    "_RADIOACTIVITY_CONVERSION_TABLE",
    "_ABSORBED_DOSE_CONVERSION_TABLE",
    "_DOSE_EQUIVALENT_TABLE",
    "_SPEED_CONVERSION_TABLE",
]
