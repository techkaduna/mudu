=========================
WELCOME TO mudu
=========================

**mudu** is a package for units and dimension handling, unit conversion and unit arithemtic,
with support for custom units definition.

**mudu** was created as part of a larger project (my final year project), `flightperformance`, which is a Python package
for analyzing aircraft (fixed wing) performance.
As it is standard in engineering to specify the units of data so as to ensure dimensional homogeniety and reproducability, the `flightperformance` package required a means of specifying the units of  data, the quantity they represents, convert between units and do arithemtic operations efforlessly with emphasis on flexibiliy and readability, this is what mudu does.

**mudu** provides a set of classes and methods, while retaining Python's expressiveness, to add unit signatures to numeric data, convert between units and perform valid arithemtic operations on dimension (or quantities) and unit objects. At its core, mudu creates dimensions using the `DimensionUnitBase` base class while units are all instances or child classes of the `_UnitType` class, both these classes are composed of other classes.

.. raw:: html
   <hr style='border-top: 3px dashed #2e7d32; margin: 30px 0'>

Why use **mudu**
--------------------------
   - It provides an simple and expressive way of specifying units
   - Capability to perform conversion from one unit to another while ensuring dimensional homogeniety as it applies in mathematics
   - Supports valid arithemtic operations on `_DimensionUnitBase` child objects and `_UnitType` objects
   - It provides interfaces to define custom units, dimensions ( or quantities) and define relationships between custom units and existing units

This documentation, contains information about the general structure of mudu, a quick tutorial that captures almost all the important functionalities of mudu and some selected examples to give to an easy start on the usage of the package.


Installation
------------

To install using pip, run:

   .. code-block:: shell

      $ pip install mudu

You can view a better documentation of this project on `<https://mudu.readthedocs.io>`_ or if you already have the package installed, use:

   .. code-block:: shell

      $ mudu --doc

local webpage version of the documentation.

.. raw:: html
   <hr style='border-top: 3px dashed #2e7d32; margin: 30px 0'>
