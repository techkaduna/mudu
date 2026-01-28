import sys
import os
import math
import pytest
from hypothesis import given, strategies as st
import numpy as np

# Ensure package import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mudu import Length, METER, INCH, Time, SECOND, Force, NEWTON, DYNE, custom_unit

# ---------------------------
# Helper functions
# ---------------------------


def get_values(obj):
    """Safely extract numeric values from Length, Force, Time, or custom_unit objects."""
    val = getattr(obj, "value", obj)
    if isinstance(val, (list, tuple)):
        return val
    try:
        # handle numpy scalars
        return val.tolist() if hasattr(val, "tolist") else [val]
    except Exception:
        return [val]


def get_dimension_str(obj):
    """Safely convert dimension to string for comparison."""
    dim = getattr(obj, "dimension", None)
    return str(dim) if dim is not None else None


def get_unit_str(obj):
    """Safely convert unit type to string for comparison."""
    unit = getattr(obj, "unit_type", None)
    return str(unit) if unit is not None else None


# ---------------------------
# Scalar Tests
# ---------------------------


@given(v1=st.floats(-1e6, 1e6), v2=st.floats(-1e6, 1e6))
def test_scalar_addition_commutativity(v1, v2):
    l1 = Length(v1, METER)
    l2 = Length(v2, METER)
    r1 = l1 + l2
    r2 = l2 + l1
    assert math.isclose(get_values(r1)[0], get_values(r2)[0], rel_tol=1e-12)
    assert get_unit_str(r1) == get_unit_str(r2)


@given(value=st.floats(-1e6, 1e6))
def test_scalar_addition_identity(value):
    l = Length(value, METER)
    result = l + Length(0, METER)
    assert math.isclose(get_values(result)[0], value, rel_tol=1e-12)
    assert get_unit_str(result) == get_unit_str(l)


def test_zero_length_operations():
    l = Length(0, METER)
    result = l + l
    assert math.isclose(get_values(result)[0], 0, rel_tol=1e-12)


def test_negative_and_large_values():
    l = Length(-1e6, METER)
    result = l + Length(1e6, METER)
    assert math.isclose(get_values(result)[0], 0, rel_tol=1e-12)


# ---------------------------
# Vectorized Tests
# ---------------------------


@pytest.mark.experimental
@given(values=st.lists(st.floats(-1000, 1000), min_size=1, max_size=20))
def test_vectorized_addition(values):
    l = Length(values, METER)
    zeros = Length([0] * len(values), METER)
    result = l + zeros
    result_vals = get_values(result)
    for a, b in zip(result_vals, values):
        assert math.isclose(a, b, rel_tol=1e-12)


@pytest.mark.experimental
@given(values=st.lists(st.floats(0.1, 1000), min_size=1, max_size=20))
def test_vectorized_division(values):
    l = Length(values, METER)
    t = Time([1] * len(values), SECOND)
    v = l / t
    v_vals = get_values(v)
    l_vals = get_values(l)
    for vi, li in zip(v_vals, l_vals):
        assert math.isclose(vi, li, rel_tol=1e-12)


# ---------------------------
# Force Tests
# ---------------------------


def test_force_conversion():
    f = Force([12, 24, 45], NEWTON)
    f_dyne = f.convert_to(DYNE)
    f_vals = get_values(f_dyne)
    expected = [1200000.0, 2400000.0, 4500000.0]
    for a, b in zip(f_vals, expected):
        assert math.isclose(a, b, rel_tol=1e-12)


# ---------------------------
# Custom Unit Tests
# ---------------------------


@pytest.mark.experimental
def test_custom_unit_creation_and_operations():
    c = custom_unit(20, num=(METER,), per=(SECOND,))
    assert get_values(c)[0] == 20
    assert get_dimension_str(c) == "L/T"


@pytest.mark.experimental
def test_custom_unit_convert_not_implemented():
    c = custom_unit(10, num=(METER,), per=(SECOND,))
    with pytest.raises(NotImplementedError):
        c.convert_to()


# ---------------------------
# Velocity Tests
# ---------------------------


def test_velocity_creation():
    l = Length(100, METER)
    t = Time(20, SECOND)
    v = l / t
    assert get_dimension_str(v) == "L/T"


# ---------------------------
# Unit Registration (Optional)
# ---------------------------


# Ensure pytest recognizes custom marks
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "experimental: marks tests as experimental features"
    )
