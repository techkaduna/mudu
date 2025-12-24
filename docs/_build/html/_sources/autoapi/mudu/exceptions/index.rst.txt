mudu.exceptions
===============

.. py:module:: mudu.exceptions

.. autoapi-nested-parse::

   =========================
   mudu.exceptions
   =========================

   mudu module, defines all dimensionunit exceptions.

   For more information, read the documenation using

   .. code-block:: shell
       mudu --doc

   in your cli



Exceptions
----------

.. autoapisummary::

   mudu.exceptions.DimensionError
   mudu.exceptions.ConversionError
   mudu.exceptions.NotIterableError
   mudu.exceptions.SequenceOperationErrorr
   mudu.exceptions.OperationNotAvailable


Module Contents
---------------

.. py:exception:: DimensionError

   Bases: :py:obj:`ArithmeticError`


   Base class for dimension errors.


.. py:exception:: ConversionError

   Bases: :py:obj:`ArithmeticError`


   Base class for conversion errors.


.. py:exception:: NotIterableError

   Bases: :py:obj:`Exception`


   Base class for iteration errors


.. py:exception:: SequenceOperationErrorr

   Bases: :py:obj:`Exception`


   Base class for sequence operation errors


.. py:exception:: OperationNotAvailable

   Bases: :py:obj:`Exception`


   Operation is not available in this version


