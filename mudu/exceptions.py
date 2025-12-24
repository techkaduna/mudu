"""
=========================
mudu.exceptions
=========================

mudu module, defines all dimensionunit exceptions.

For more information, read the documenation using

.. code-block:: shell
    mudu --doc
    
in your cli

"""

class DimensionError(ArithmeticError):
    """Base class for dimension errors."""
    pass


class ConversionError(ArithmeticError):
    """Base class for conversion errors."""
    pass


class NotIterableError(Exception):
    """Base class for iteration errors"""
    pass


class SequenceOperationErrorr(Exception):
    """Base class for sequence operation errors"""
    pass


class OperationNotAvailable(Exception):
    """Operation is not available in this version"""
    pass
