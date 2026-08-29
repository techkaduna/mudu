# An Example
---
## The Tr-curve

The Tr-curve (Tr stands for thrust required) is a graphical representation of the thrust required by an aircraft to maintain steady and level flight for a range of operating velocities. For an aircraft in steady and level flight (cruise), the thrust required to maintain flight at a particular altitude and velocity is theoretically equal to the drag force experienced by the aircraft. The Tr-curve gives insight into the aircraft's behaviour (stable and unstable flight regions) as it relates to the aircraft's velocity. Speaking more about the Tr-curve is beyond the scope of this section, so let's get down to dealing with some aircraft performance problem.

## Problem statement

For an aircraft in steady level flight at an altitude of 30,000 ft, plot the Tr-curve for the aircraft between a velocity range of 300 ft/s to 1500 ft/s.

The following are the required aircraft parameters:

- weight, *W* = 73,000 lb
- flight altitude, *h* = 30,000 ft
- wing span, *S* = 950 sqr ft
- ISA density @ 30,000 ft, *ρ₀* = 0.00089068 slug/cube(ft)
- drag polar co.eff, *K* = 0.08
- zero-lift drag, *Cd,o* = 0.015

## Solution

The following are the data required to plot the Tr-curve.

- velocity
- coefficient of lift, *Cl*
- coefficient of drag, *Cd*
- thrust required, *Tr*

So the first step is to import what's necessary and define the constants.

```python
import matplotlib.pyplot as plt

from mudu import Force, POUND_FORCE, Length, FEET, Mass, Time, SECOND, SLUG

WEIGHT = Force(73_000, POUND_FORCE)
ALTITUDE = Length(30_000, FEET)
WING_SPAN = 950 * (Length(1, FEET))**2  # wing_span is in sqr ft
DRAG_POLAR, ZERO_LIFT_DRAG = 0.08, 0.015

# a work around
arb_mass = Mass(1, SLUG)
arb_length = Length(1, FEET)
arb_volume = arb_length**3
arb_density = arb_mass / arb_volume
DENSITY = 0.00089068 * arb_density
```

!!! note
    This example previously (in an earlier version of mudu) defined its own local, untagged `SLUG` unit as a workaround for a now-fixed bug in mudu's built-in `SLUG` conversion factor. That bug is fixed, so mudu's own exported `SLUG` (`from mudu import SLUG`) is used directly here, with no local redefinition needed.

The code block above has a couple of interesting (*I hope*) manipulations, but let's dig in. When defining the `WING_SPAN` parameter, which is in square feet, we squared the length object, which results in a `DerivedQuantity`, and multiplied it with a scalar, which also results in a `DerivedQuantity` object, in square feet. This method is used throughout this example. A similar method is used to define the `DENSITY` parameter, a bit more elaborate, but the same idea.

Next, we continue by defining a function to calculate the coefficient of lift, and some `lambda`s to evaluate the coefficient of drag and thrust required, `drag_co_eff` and `thrust_required` respectively.

```python
def lift_co_eff(velocity):

    numerator = 2 * WEIGHT
    denuminator = DENSITY * (velocity**2) * WING_SPAN
    # Coercing to pound-force here is dimensionally exact, not an
    # approximation -- see the note below.
    denuminator = Force(denuminator.value, POUND_FORCE)

    return numerator / denuminator

drag_co_eff = lambda c_l: ZERO_LIFT_DRAG + (DRAG_POLAR * (c_l**2))
thrust_required = lambda vel, c_d: (0.5) * DENSITY * (vel**2) * WING_SPAN * c_d
```

!!! note "On the “coercion” above"
    In the US customary "engineering" system of units, `SLUG` is *defined* such that `1 slug * 1 ft/s^2 == 1 lbf` exactly (scale factor of 1). So as long as every input above is consistently in slug/ft/s, the raw numeric value of `DENSITY * velocity**2 * WING_SPAN` already *is* the value in pound-force. The following line is relabeling the unit, not converting a value, and introduces no approximation.

Then we define a range of velocities for which we're going to calculate the thrust required to maintain flight at an altitude of 30,000 ft. We also define lists of the corresponding coefficients of lift, `c_l`, coefficients of drag, `c_d`, and thrust required, `t_r`.

```python
velocity = [(i * Length(1, FEET)/Time(1, SECOND)) for i in range(300, 1600, 100)]   # v in ft/s
c_l = [round(lift_co_eff(x), 4) for x in velocity]  # dimensionless
c_d = [round(drag_co_eff(c), 4) for c in c_l]   # dimensionless
t_r = [Force(thrust_required(velocity[i], c_d[i]).value, POUND_FORCE) for i in range(len(velocity))]    # in pounds
t_r = [round(x) for x in t_r]
```

Plotting the graph using matplotlib:

```python
vel_values = [x.value for x in velocity]
t_r_values = [y.value for y in t_r]

plt.plot(vel_values, t_r_values, )
plt.title("Thrust required curve for the aircraft")
plt.xlabel("Velocity (ft/s)")
plt.ylabel("Thrust required (lbf)")
plt.grid(True)
plt.show()
```

The resulting plot looks like this:

<p align="center">
  <img src="/assets/tr_curve.png" alt="Tr-curve" width="800" height="400">
</p>

In this example, we tried to use as many object methods as possible to solve the problem at hand, with minimal concern for speed or coding style. This is to emphasize that there are other, mostly better, ways of solving this problem and exploring those method is left to the reader.

For more examples, visit the [GitHub repo](https://github.com/techkaduna/mudu).