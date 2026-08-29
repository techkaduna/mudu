"""
=========================
mudu.exceptions
=========================

mudu module, defines all dimension/unit exceptions.

For more information, read the documentation using

.. code-block:: shell
    mudu --doc

in your cli
"""

import warnings

__all__ = [
    "ConversionError",
    "DimensionError",
    "NotIterableError",
    "OperationNotAvailable",
    "SequenceOperationError",
]


class DimensionError(ArithmeticError):
    """Raised when an operation is attempted between incompatible dimensions."""

    pass


class ConversionError(ArithmeticError):
    """Raised when a unit conversion cannot be carried out."""

    pass


class NotIterableError(Exception):
    """Raised when iteration is attempted on a non-sequence quantity."""

    pass


class SequenceOperationError(Exception):
    """Raised for invalid operations on sequence-valued quantities."""

    pass


def SequenceOperationErrorr(*args, **kwargs):
    """Deprecated: use `SequenceOperationError` (this name had an extra
    trailing "r" and is kept only for backward compatibility). Will be
    removed in a future major version.
    """

    warnings.warn(
        "SequenceOperationErrorr is a deprecated misspelling; use "
        "SequenceOperationError instead. This alias will be removed in a "
        "future release.",
        DeprecationWarning,
        stacklevel=2,
    )
    return SequenceOperationError(*args, **kwargs)


class OperationNotAvailable(Exception):
    """Raised when the requested operation is not available in this version."""

    pass
