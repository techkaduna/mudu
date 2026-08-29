# Welcome to **mudu** documentation
---

**Mudu** is a package for units and dimension handling, unit conversion and unit arithmetic, with support for custom units definition.

---

!!! note "The name Mudu"
    Mudu is the measurement standard used to sell grains and similar food materials in most of northern Nigeria.

As it is standard in engineering to specify the units of data so as to ensure dimensional homogeneity and reproducibility, Mudu is designed as a means of specifying the units of data, the quantity they represent, converting between units and doing arithmetic operations effortlessly with emphasis on flexibility, readability and speed.

Mudu provides a set of classes and methods, while retaining Python's expressiveness, to add unit signatures to numeric data, convert between units and perform valid arithmetic operations on dimension (or quantities) and unit objects. At its core, Mudu creates dimensions using the `_DimensionUnitBase` base class while units are all instances or child classes of the `_UnitType` class, both of these classes are composed of other classes.

---

!!! note "D-Check release"
    This release (dubbed the "D-Check release") includes a set of correctness fixes and a new supported extension API. If you used mudu before this release, see [What's Changed](whats_changed.md) before relying on custom units or conversion factors you may have worked around previously.

## Why use **Mudu**

- It provides a simple and expressive way of specifying units
- It provides the capability to perform conversion from one unit to another while ensuring dimensional homogeneity as it applies in mathematics
- Supports valid arithmetic operations on `_DimensionUnitBase` child objects and `_UnitType` objects
- It provides a public interface to define custom units and register conversions against existing dimensions, and to define wholly new custom quantities

This documentation contains information about the general structure of mudu, a quick tutorial that captures all the important functionalities of mudu, and some selected examples as an easy start on the usage of the package.

---

## Contents

- [Installation](installation.md)
- [Usage Guide](usage.md)
- [What's Changed](whats_changed.md)
- [Examples](examples.md)
- [Contributing](contributing.md)

---

## Finding Things

Use the search bar above to look up any term, class, or function across this documentation. For a full listing of every class, method, and unit mudu exposes, see the [API Reference](api.md).