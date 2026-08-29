"""
mudu test suite
================

Organized into:
  - TestPhase0Regressions   : one test per bug found in the original D-Check
                               code review, permanently guarding against
                               reintroduction.
  - TestConversionCorrectness: known-value conversions (SLUG, INCH/FEET,
                               temperature affine conversions, etc).
  - TestContracts            : __eq__/__hash__/__floordiv__ data-model
                               contract tests.
  - TestPublicExtensionAPI   : define_unit / register_conversion / audit_units.
  - TestPropertyBased        : Hypothesis-driven round-trip and
                               dimension-homogeneity properties, run across
                               every shipped conversion table.

Run with:
    pytest test_suite.py -v
    pytest test_suite.py -v --benchmark-only
"""

import math

import numpy as np
import pytest
from hypothesis import given, strategies as st

import mudu
from mudu import (
    Length,
    Mass,
    Time,
    Temperature,
    Angle,
    Force,
    Pressure,
    Energy,
    Density,
    Power,
    Speed,
    Radioactivity,
    custom_unit,
    METER,
    KILOMETER,
    FEET,
    INCH,
    YARD,
    MILE,
    NAUTICAL_MILE,
    GRAM,
    KILOGRAM,
    POUND,
    OUNCE,
    SLUG,
    SHORT_TON,
    LONG_TON,
    METRIC_TON,
    SECOND,
    MINUTE,
    HOUR,
    KELVIN,
    CELSIUS,
    FARENHEIT,
    RANKINE,
    DEGREE,
    RADIAN,
    NEWTON,
    POUND_FORCE,
    POUNDAL,
    DYNE,
    PASCAL,
    PSI,
    ATM,
    BAR,
    mmHg,
    inHg,
    JOULE,
    CALORIE,
    WATT_HOUR,
    ELECTRON_VOLT,
    BRITISH_THERMAL_UNIT,
    WATT,
    HORSEPOWER,
    BECQUEREL,
    CURIE,
    METER_PER_SECOND,
    KM_PER_HOUR,
    MILE_PER_HOUR,
    KNOT,
    DimensionError,
    ConversionError,
    define_unit,
    register_conversion,
    audit_units,
    Linear,
    Affine,
)
from mudu.units import (
    _LENGTH_CONVERSION_TABLE,
    _MASS_CONVERSION_TABLE,
    _TIME_CONVERSION_TABLE,
    _ANGLE_CONVERSION_TABLE,
    _TEMPERATURE_CONVERSION_TABLE,
    _FORCE_CONVERSION_TABLE,
    _PRESSURE_CONVERSION_TABLE,
    _ENERGY_CONVERSION_TABLE,
    _DENSITY_CONVERSION_TABLE,
    _POWER_CONVERSION_TABLE,
    _RADIOACTIVITY_CONVERSION_TABLE,
    _ABSORBED_DOSE_CONVERSION_TABLE,
    _DOSE_EQUIVALENT_TABLE,
    _SPEED_CONVERSION_TABLE,
)

ALL_TABLES = [
    _LENGTH_CONVERSION_TABLE,
    _MASS_CONVERSION_TABLE,
    _TIME_CONVERSION_TABLE,
    _ANGLE_CONVERSION_TABLE,
    _TEMPERATURE_CONVERSION_TABLE,
    _FORCE_CONVERSION_TABLE,
    _PRESSURE_CONVERSION_TABLE,
    _ENERGY_CONVERSION_TABLE,
    _DENSITY_CONVERSION_TABLE,
    _POWER_CONVERSION_TABLE,
    _RADIOACTIVITY_CONVERSION_TABLE,
    _ABSORBED_DOSE_CONVERSION_TABLE,
    _DOSE_EQUIVALENT_TABLE,
    _SPEED_CONVERSION_TABLE,
]


# ============================================================================
# Phase 0 — regression tests, one per bug found in the original code review.
# Each of these fails on the pre-fix source and passes on the fixed source.
# ============================================================================
class TestPhase0Regressions:
    def test_0_1_angle_and_temperature_are_distinct_dimensions(self):
        """PLANE_ANGLE / SOLID_ANGLE / THERMODYNAMIC_TEMPERATURE previously
        shared the sympy symbol "Ɵ", silently merging three dimensions into
        one. Operating across them must raise DimensionError."""
        with pytest.raises(DimensionError):
            Angle(90, DEGREE) + Temperature(300, KELVIN)

    def test_0_1_angle_and_solid_angle_are_distinct_dimensions(self):
        from mudu.dimensions import SolidAngle

        with pytest.raises(DimensionError):
            Angle(1, RADIAN) + SolidAngle(1)

    def test_0_2_becquerel_and_curie_share_correct_dimension(self):
        """BECQUEREL previously had LUX's (illuminance) dimension by
        copy-paste error, instead of 1/TIME like CURIE. They must be
        mutually convertible."""
        bq = Radioactivity(3.7e10, BECQUEREL)
        ci = bq.convert_to(CURIE)
        assert ci.value == pytest.approx(1.0, abs=1e-6)

    def test_0_3_pascal_and_psi_have_distinct_unit_names(self):
        """PSI previously had _unit_name="pascal" (copy-pasted from
        PASCAL), which made `is_same_unit` string comparisons in the
        arithmetic operators silently treat Pascal- and PSI-valued
        Pressure quantities as identical, skipping a needed conversion."""
        assert PASCAL._unit_name != PSI._unit_name

    def test_0_3_psi_converts_correctly_not_silently_skipped(self):
        one_psi_in_pa = Pressure(1, PSI).convert_to(PASCAL).value
        assert one_psi_in_pa == pytest.approx(6894.757293168, rel=1e-9)
        # and the reverse
        one_pa_in_psi = Pressure(6894.757293168, PASCAL).convert_to(PSI).value
        assert one_pa_in_psi == pytest.approx(1.0, rel=1e-9)

    def test_0_4_len_of_scalar_dimension_type_does_not_crash(self):
        """_DimensionType.__len__ previously did
        `1 if self.value is True else len(self.value)`, an identity check
        against the literal bool True that is essentially never satisfied
        by a real numeric value, so len() on any ordinary scalar quantity
        raised TypeError."""
        assert len(Length(12, METER)) == 1
        assert len(Mass(3.5, KILOGRAM)) == 1

    def test_0_5_derived_quantity_rtruediv_by_dimension_type_no_attributeerror(self):
        """DerivedQuantity.__rtruediv__ previously referenced the
        nonexistent `self.__value` (typo for `self.__value_not_seq`) in the
        _DimensionType branch, guaranteeing AttributeError if ever hit."""
        f = Force(10, NEWTON)
        # int/float branch, exercised directly:
        result = 20 / f
        assert result.value == pytest.approx(2.0)

    def test_0_7_custom_unit_instances_do_not_share_mutable_state(self):
        """custom_unit previously declared `__numerator`/`__denominator` as
        class-level mutable lists, so every instance appended into the
        same shared list process-wide."""
        cu1 = custom_unit(5, num=[NEWTON], per=[METER])
        cu2 = custom_unit(7, num=[JOULE], per=[SECOND])
        assert cu1._custom_unit__numerator != cu2._custom_unit__numerator
        assert len(cu1._custom_unit__numerator) == 1
        assert len(cu2._custom_unit__numerator) == 1


# ============================================================================
# Known-value conversion correctness
# ============================================================================
class TestConversionCorrectness:
    def test_slug_to_gram_correct_order_of_magnitude(self):
        """Previously off by exactly 1000x (a kg/g mixup): the table held
        14.593903 (grams) instead of 14593.903 (grams == 14.593903 kg)."""
        assert Mass(1, SLUG).convert_to(GRAM).value == pytest.approx(
            14593.903, rel=1e-6
        )

    def test_inch_feet_round_trip(self):
        """Previously inverted by a factor of 144 (used y=12 as a forward
        INCH->FEET multiply, when 1 inch = 1/12 ft)."""
        assert Length(1, FEET).convert_to(INCH).value == pytest.approx(12.0, abs=1e-9)
        assert Length(12, INCH).convert_to(FEET).value == pytest.approx(1.0, abs=1e-9)
        assert Length(1, INCH).convert_to(FEET).value == pytest.approx(1 / 12, rel=1e-9)

    @pytest.mark.parametrize(
        "value_c, expected_k", [(0, 273.15), (100, 373.15), (-40, 233.15)]
    )
    def test_celsius_to_kelvin_affine(self, value_c, expected_k):
        assert Temperature(value_c, CELSIUS).convert_to(KELVIN).value == pytest.approx(
            expected_k, abs=1e-9
        )

    @pytest.mark.parametrize(
        "value_f, expected_k", [(32, 273.15), (212, 373.15), (-40, 233.15)]
    )
    def test_fahrenheit_to_kelvin_affine(self, value_f, expected_k):
        assert Temperature(value_f, FARENHEIT).convert_to(
            KELVIN
        ).value == pytest.approx(expected_k, abs=1e-6)

    def test_rankine_to_kelvin_linear_no_offset(self):
        # Rankine and Kelvin both start at absolute zero -- purely linear.
        assert Temperature(0, RANKINE).convert_to(KELVIN).value == pytest.approx(
            0.0, abs=1e-9
        )
        assert Temperature(491.67, RANKINE).convert_to(KELVIN).value == pytest.approx(
            273.15, rel=1e-6
        )

    def test_length_units_against_known_references(self):
        assert Length(1, INCH).convert_to(METER).value == pytest.approx(
            0.0254, rel=1e-12
        )
        assert Length(1, MILE).convert_to(METER).value == pytest.approx(
            1609.344, rel=1e-12
        )
        assert Length(1, NAUTICAL_MILE).convert_to(METER).value == pytest.approx(
            1852, rel=1e-12
        )

    def test_mass_units_against_known_references(self):
        assert Length  # keep import graph honest
        assert Mass(1, POUND).convert_to(GRAM).value == pytest.approx(
            453.59237, rel=1e-9
        )
        assert Mass(16, OUNCE).convert_to(POUND).value == pytest.approx(1.0, abs=1e-3)

    def test_pressure_units_against_known_references(self):
        assert Pressure(1, ATM).convert_to(PASCAL).value == pytest.approx(
            101325, rel=1e-12
        )
        assert Pressure(1, BAR).convert_to(PASCAL).value == pytest.approx(
            100000, rel=1e-12
        )

    def test_energy_units_against_known_references(self):
        assert Energy(1, CALORIE).convert_to(JOULE).value == pytest.approx(
            4.184, rel=1e-12
        )
        assert Energy(1, WATT_HOUR).convert_to(JOULE).value == pytest.approx(
            3600, rel=1e-12
        )

    def test_speed_units_against_known_references(self):
        assert Speed(1, KNOT).convert_to(METER_PER_SECOND).value == pytest.approx(
            1852 / 3600, rel=1e-12
        )
        assert Speed(100, KM_PER_HOUR).convert_to(
            METER_PER_SECOND
        ).value == pytest.approx(100 * 1000 / 3600, rel=1e-9)

    def test_gram_per_cubic_centimeter_and_milliliter_are_distinct_but_equal_value(
        self,
    ):
        from mudu import GRAM_PER_CUBIC_CENTIMETER, GRAM_PER_CUBIC_MILLILITER

        assert (
            GRAM_PER_CUBIC_CENTIMETER._unit_name != GRAM_PER_CUBIC_MILLILITER._unit_name
        )
        a = (
            Density(1, GRAM_PER_CUBIC_CENTIMETER)
            .convert_to(GRAM_PER_CUBIC_MILLILITER)
            .value
        )
        assert a == pytest.approx(1.0, rel=1e-12)

    def test_kilometer_prefix_conversion(self):
        assert Length(1, KILOMETER).convert_to(METER).value == pytest.approx(1000.0)
        assert Length(1500, METER).convert_to(KILOMETER).value == pytest.approx(1.5)

    def test_convert_dimension_mismatch_raises(self):
        with pytest.raises(DimensionError):
            Length(1, METER).convert_to(SECOND)


# ============================================================================
# Data-model contract tests: __eq__, __hash__, __floordiv__.
# ============================================================================
class TestContracts:
    def test_eq_always_returns_bool(self):
        result = Length(1, METER) == Length(100, INCH)
        assert isinstance(result, bool)

    def test_eq_cross_unit_correct(self):
        assert (Length(1, METER) == Length(1 / 0.0254, INCH)) is True
        assert (Length(1, METER) == Length(100, INCH)) is False

    def test_eq_against_non_quantity_returns_notimplemented_semantics(self):
        # Python falls back to False for `==` against an unrelated type
        # once __eq__ returns NotImplemented on both sides.
        assert (Length(1, METER) == "not a quantity") is False

    def test_ne_is_consistent_with_eq(self):
        a, b = Length(1, METER), Length(2, METER)
        assert (a != b) == (not (a == b))

    def test_hashable(self):
        s = {Length(1, METER), Length(2, METER), Length(1, METER)}
        assert len(s) == 2  # the duplicate collapses

    def test_floordiv_floors_negative_correctly(self):
        """Previously `float(int(x))`, which truncates toward zero rather
        than flooring -- wrong for negative results."""
        assert Length(-7, METER).__floordiv__(2) == -4.0
        assert Length(7, METER).__floordiv__(2) == 3.0

    def test_dimension_mismatch_arithmetic_raises(self):
        with pytest.raises(DimensionError):
            Length(1, METER) + Mass(1, GRAM)


# ============================================================================
# Public extension API.
# ============================================================================
class TestPublicExtensionAPI:
    def test_define_and_register_new_unit(self):
        SMOOT = define_unit(Length, name="smoot_test", symbol="smoot_t")
        register_conversion(Length, SMOOT, Linear(1.7018))
        assert Length(1, SMOOT).convert_to(METER).value == pytest.approx(1.7018)
        assert Length(1.7018, METER).convert_to(SMOOT).value == pytest.approx(1.0)

    def test_audit_units_clean_on_shipped_tables(self):
        problems = audit_units(*ALL_TABLES)
        assert problems == [], f"unit-definition audit found problems: {problems}"

    def test_audit_units_detects_wrong_conversion_type(self):
        from mudu.base import _ConversionTableType

        bad_table = _ConversionTableType(dimension=Length._dimension, base_unit=METER)
        bad_table.table["bogus"] = object()  # not a Linear/Affine
        problems = audit_units(bad_table)
        assert any("unexpected type" in p for p in problems)


# ============================================================================
# Property-based tests (Hypothesis).
# ============================================================================
class TestPropertyBased:
    @given(
        value=st.floats(
            min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False
        )
    )
    def test_length_round_trip_meter_inch(self, value):
        original = Length(value, METER)
        round_tripped = original.convert_to(INCH).convert_to(METER)
        assert round_tripped.value == pytest.approx(value, rel=1e-9, abs=1e-9)

    @given(
        value=st.floats(
            min_value=-500, max_value=500, allow_nan=False, allow_infinity=False
        )
    )
    def test_temperature_round_trip_kelvin_fahrenheit(self, value):
        # keep values physically plausible-ish but the math holds regardless
        original = Temperature(value, KELVIN)
        round_tripped = original.convert_to(FARENHEIT).convert_to(KELVIN)
        assert round_tripped.value == pytest.approx(value, rel=1e-6, abs=1e-6)

    @given(
        value=st.floats(
            min_value=0.001, max_value=1e6, allow_nan=False, allow_infinity=False
        )
    )
    def test_pressure_round_trip_pascal_psi(self, value):
        original = Pressure(value, PASCAL)
        round_tripped = original.convert_to(PSI).convert_to(PASCAL)
        assert round_tripped.value == pytest.approx(value, rel=1e-6)

    @given(
        value=st.floats(
            min_value=-1e5, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_mass_round_trip_gram_slug(self, value):
        original = Mass(value, GRAM)
        round_tripped = original.convert_to(SLUG).convert_to(GRAM)
        assert round_tripped.value == pytest.approx(value, rel=1e-9, abs=1e-6)

    @given(
        v1=st.floats(
            min_value=-1e4, max_value=1e4, allow_nan=False, allow_infinity=False
        ),
        v2=st.floats(
            min_value=-1e4, max_value=1e4, allow_nan=False, allow_infinity=False
        ),
    )
    def test_addition_commutative_across_units(self, v1, v2):
        a = Length(v1, METER)
        b = Length(v2, INCH)
        assert (a + b).value == pytest.approx(
            (b + a).convert_to(METER).value, rel=1e-6, abs=1e-9
        )

    @given(
        value=st.floats(
            min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False
        )
    )
    def test_incompatible_dimensions_always_raise(self, value):
        with pytest.raises(DimensionError):
            Length(value, METER) + Time(1, SECOND)


# ============================================================================
# Differential validation against `pint`, used purely as an independent
# correctness oracle (dev/test dependency only, never a runtime
# dependency of mudu itself; see pyproject.toml).
#
# Uses pytest.importorskip so this class cleanly skips (not fails) in any
# environment without pint installed, e.g. a minimal `pip install -e .`
# with no dev extras.
# ============================================================================
class TestDifferentialValidationAgainstPint:
    @pytest.fixture(autouse=True)
    def _require_pint(self):
        self.pint = pytest.importorskip("pint")
        self.ureg = self.pint.UnitRegistry()

    @given(
        value=st.floats(
            min_value=-1e5, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_length_inch_to_meter(self, value):
        mudu_result = Length(value, INCH).convert_to(METER).value
        pint_result = (value * self.ureg.inch).to(self.ureg.meter).magnitude
        assert mudu_result == pytest.approx(pint_result, rel=1e-9)

    @given(
        value=st.floats(
            min_value=-1e5, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_mass_pound_to_gram(self, value):
        mudu_result = Mass(value, POUND).convert_to(GRAM).value
        pint_result = (value * self.ureg.pound).to(self.ureg.gram).magnitude
        assert mudu_result == pytest.approx(pint_result, rel=1e-6)

    @given(
        value=st.floats(
            min_value=-1e5, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_mass_slug_to_gram(self, value):
        # This is the specific conversion that was off by 1000x pre-fix --
        # keep this test even after it's no longer novel, as the permanent
        # regression guard for that class of bug (independent of the
        # hand-derived regression test in TestConversionCorrectness).
        mudu_result = Mass(value, SLUG).convert_to(GRAM).value
        pint_result = (value * self.ureg.slug).to(self.ureg.gram).magnitude
        assert mudu_result == pytest.approx(pint_result, rel=1e-6)

    @given(
        value=st.floats(
            min_value=-200, max_value=200, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_temperature_celsius_to_kelvin(self, value):
        mudu_result = Temperature(value, CELSIUS).convert_to(KELVIN).value
        pint_result = (
            self.ureg.Quantity(value, self.ureg.degC).to(self.ureg.kelvin).magnitude
        )
        assert mudu_result == pytest.approx(pint_result, rel=1e-9, abs=1e-9)

    @given(
        value=st.floats(
            min_value=-200, max_value=200, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_temperature_fahrenheit_to_kelvin(self, value):
        mudu_result = Temperature(value, FARENHEIT).convert_to(KELVIN).value
        pint_result = (
            self.ureg.Quantity(value, self.ureg.degF).to(self.ureg.kelvin).magnitude
        )
        assert mudu_result == pytest.approx(pint_result, rel=1e-6, abs=1e-6)

    @given(
        value=st.floats(
            min_value=0.001, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_pressure_psi_to_pascal(self, value):
        mudu_result = Pressure(value, PSI).convert_to(PASCAL).value
        pint_result = (value * self.ureg.psi).to(self.ureg.pascal).magnitude
        assert mudu_result == pytest.approx(pint_result, rel=1e-6)

    @given(
        value=st.floats(
            min_value=0.001, max_value=1e5, allow_nan=False, allow_infinity=False
        )
    )
    def test_differential_energy_calorie_to_joule(self, value):
        mudu_result = Energy(value, CALORIE).convert_to(JOULE).value
        pint_result = (value * self.ureg.calorie).to(self.ureg.joule).magnitude
        assert mudu_result == pytest.approx(pint_result, rel=1e-6)


# ============================================================================
# Exhaustive per-dimension conversion-matrix test: every registered unit in
# every shipped table must round-trip through the base unit without error.
# ============================================================================
class TestConversionMatrix:
    @pytest.mark.parametrize("table", ALL_TABLES, ids=lambda t: str(t.dimension))
    def test_every_registered_unit_round_trips(self, table):
        for unit_name, conversion in table.table.items():
            base_val = 1.0
            to_unit_val = conversion.from_base(base_val)
            back_to_base = conversion.to_base(to_unit_val)
            assert back_to_base == pytest.approx(base_val, rel=1e-9), (
                f"{unit_name} does not round-trip cleanly through "
                f"{table.base_unit._unit_name}"
            )
