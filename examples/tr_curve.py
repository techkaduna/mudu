"""
Simple program that plots the Tr-curve for an aircraft at a particular altitude for a range of velocities.

The problem sample is an excerpt from the textbook Aircraft Performance by J.D Anderson.
"""

import os
import sys

import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mudu import Force, POUND_FORCE, Length, FEET, Mass, Time, SECOND, SLUG

"""
Problem statement:
For an aircraft in steady level flight at an altitude of 30,000 ft,
plot is Tr-curve of the aircraft between a velocity range of 300 ft/s to 1500 ft/s.

The following are the required aircraft parameters:
    weight, W = 73, 000 lb
    flight altitude, h =  30, 000 ft
    wing span, S = 950 sqr ft
    ISA density @ 30,000 ftpo = 0.00089068 slug/cube(ft)
    drag polar co.eff, K = 0.08
    zero-lift drag, Cd,o = 0.015

"""

# NOTE: previously this example redefined its own local `SLUG` unit via a
# raw `_UnitType(...)` (with no `_quantity` tag and no conversion table
# entry), likely as a workaround for a bug in mudu's own built-in `SLUG`
# conversion factor at the time. That bug is fixed (see CHANGELOG), and
# mudu's built-in, properly-tagged, correctly-convertible `SLUG` unit is
# used directly below -- no local redefinition needed. `MASS` is no
# longer imported here since it's unused now that the built-in unit
# supplies its own dimension.

WEIGHT = Force(73_000, POUND_FORCE)
ALTITUDE = Length(30_000, FEET)
WING_SPAN = 950 * (Length(1, FEET)) ** 2  # wing_span is in sqr ft
DRAG_POLAR, ZERO_LIFT_DRAG = 0.08, 0.015

# a work around
arb_mass = Mass(1, SLUG)
arb_length = Length(1, FEET)
arb_volume = arb_length**3
arb_density = arb_mass / arb_volume
DENSITY = 0.00089068 * arb_density


def lift_co_eff(velocity):
    """Calculate the coefficient of lift for the given velocity."""
    numerator = 2 * WEIGHT
    denuminator = DENSITY * (velocity**2) * WING_SPAN
    # Coercing to pound-force here is dimensionally exact, not an
    # approximation: in the US customary "engineering" unit system, SLUG
    # is *defined* such that 1 slug * 1 ft/s^2 == 1 lbf, with a scale
    # factor of exactly 1 -- so as long as every input above is
    # consistently in slug/ft/s, the raw numeric value already IS the
    # value in pound-force, and this is just relabeling the unit, not
    # converting a value.
    denuminator = Force(denuminator.value, POUND_FORCE)

    return numerator / denuminator


drag_co_eff = lambda c_l: ZERO_LIFT_DRAG + (DRAG_POLAR * (c_l**2))
thrust_required = lambda vel, c_d: (0.5) * DENSITY * (vel**2) * WING_SPAN * c_d

velocity = [
    (i * Length(1, FEET) / Time(1, SECOND)) for i in range(300, 1600, 100)
]  # v in ft/s
c_l = [round(lift_co_eff(x), 4) for x in velocity]
c_d = [round(drag_co_eff(c), 4) for c in c_l]
t_r = [
    Force(thrust_required(velocity[i], c_d[i]).value, POUND_FORCE)
    for i in range(len(velocity))
]
t_r = [round(x) for x in t_r]

df = pd.DataFrame(
    {"velocity [ft/s]": velocity, "c_l": c_l, "c_d": c_d, "Tr [lb_f]": t_r}
)

# print(df)

vel_values = [x.value for x in velocity]
t_r_values = [y.value for y in t_r]

plt.plot(
    vel_values,
    t_r_values,
)
plt.title("Thrust required curve for the aircraft at 30, 000 ft")
plt.xlabel("Velocity (ft/s)")
plt.ylabel("Thrust required (lbf)")
plt.grid(True)
plt.show()
