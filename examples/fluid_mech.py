"""
Problem statement:
A 400 mm diameter shaft is rotating at 200 r.p.m in a bearing of length 120 mm. If the thickness of oil film is 1.5 mm and the dynamic viscosity of the oil is 0.7 N.s/m^2, determine:
    i. the torque required to overcome friction in bearing.
    ii. the power utilized in overcoming viscous resitance.
    Assumption: The flow has a linear velocity profile.

    Given:
        shaft diameter=400mm
        shaft rotation=200 r.p.m
        bearing length=120mm
        oil film thickness=1.5mm
        oil dynamic viscosity=0.7N.s/m^2
"""

import os
import sys
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mudu import (
    Length,
    Time,
    Force,
    METER,
    MILLI,
    OrderUnit,
    NEWTON,
    SECOND,
    MINUTE,
)
from mudu.base import _UnitType
from mudu.dimensions import DerivedQuantity

MILLIMETER = OrderUnit(MILLI, METER)

shaft_diameter = Length(400, MILLIMETER).convert_to(METER)  # conversion to meter
shaft_rotation = 200 / Time(1, MINUTE).convert_to(SECOND)  # rpm converted to rps
film_thickness = Length(1.5, MILLIMETER).convert_to(METER)
length_of_bearing = Length(120, MILLIMETER).convert_to(METER)

# a work around for creating the unit of viscosity
arb_force = Force(1, NEWTON)
arb_time = Time(1, SECOND)
arb_length = Length(1, METER)

arb_viscosity = arb_force * arb_time / (arb_length**2)
viscosity = 0.7 * arb_viscosity

# calculating the tangential velocity the shaft
shaft_tangent_vel = math.pi * (shaft_diameter * shaft_rotation)

# 1. Torque required to overcome friction, T
# t = U(du/dy)
# t = shear stress (tau)
# U = co.eff of viscosity
# du/dy = velocity profile
# in this case:
#   du = shaft angential velocity
#   dy = oil film thickness

shear_stress = viscosity * (shaft_tangent_vel / film_thickness)
area = math.pi * shaft_diameter * length_of_bearing
shear_force = shear_stress * area
print("Shear force: ", shear_force)

viscous_torque = shear_force * (shaft_diameter / 2)

print("Viscous torque: ", viscous_torque)

# 2. Power Utlized

power = viscous_torque * 2 * math.pi * shaft_rotation

print("Power utilized: ", power)

##########################################################################################
# An alternative method of computing power would be to create a 'custom' unit and quantity
# The unit is created by creating a new '_UnitType' dataclass instance, while the quantity
# is created by inheriting from the 'DerivedQuantity' class.


class Power(DerivedQuantity):
    _conversion_standards = None

    def __init__(self, value, unit_definition):
        super().__init__(value, unit_definition, quantity="power")


JOULES = _UnitType(
    _dimension=((NEWTON * METER) / SECOND)._dimension,
    _unit_name="joules",
    _unit_symbol="J",
    _quantity="power",
    _order=None,
)

power_in_joules = Power(power.value, JOULES)

print("Power (J): ", power_in_joules)
