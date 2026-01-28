"""
Simple program that plots the Tr-curve for an aircraft at a particular altitude for a range of velocities.

The problem sample is an excerpt from the textbook Aircraft Performance by J.D Anderson.
"""

import os
import sys

import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mudu import Force, POUND_FORCE, Length, FEET, MASS, Mass, Time, SECOND
from mudu.base import _UnitType

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

SLUG = _UnitType(
    _dimension=MASS,
    _unit_name="slug",
    _unit_symbol="slug",
)

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
    denuminator = Force(denuminator.value, POUND_FORCE)  # coercing to pound force

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

print(df)

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
