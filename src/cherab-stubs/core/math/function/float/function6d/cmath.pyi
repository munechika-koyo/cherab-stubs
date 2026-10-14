from typing import TypeAlias

from .base import Function6D, _Function6DCallable

_Function6DInput: TypeAlias = Function6D | float | _Function6DCallable

class Exp6D(Function6D):
    """
    A Function6D class that implements the exponential of the result of a Function6D object: exp(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Sin6D(Function6D):
    """
    A Function6D class that implements the sine of the result of a Function6D object: sin(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Cos6D(Function6D):
    """
    A Function6D class that implements the cosine of the result of a Function6D object: cos(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Tan6D(Function6D):
    """
    A Function6D class that implements the tangent of the result of a Function6D object: tan(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Asin6D(Function6D):
    """
    A Function6D class that implements the arcsine of the result of a Function6D object: asin(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Acos6D(Function6D):
    """
    A Function6D class that implements the arccosine of the result of a Function6D object: acos(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Atan6D(Function6D):
    """
    A Function6D class that implements the arctangent of the result of a Function6D object: atan(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Atan4Q6D(Function6D):
    """
    A Function6D class that implements the arctangent of the result of 2 Function6D objects: atan2(f1(), f2())

    This differs from Atan6D in that it takes separate functions for the
    numerator and denominator, in order to get the quadrant correct.

    :param Function6D numerator: A Function6D object representing the numerator
    :param Function6D denominator: A Function6D object representing the denominator
    """
    def __init__(self, numerator: _Function6DInput, denominator: _Function6DInput) -> None: ...

class Sqrt6D(Function6D):
    """
    A Function6D class that implements the square root of the result of a Function6D object: sqrt(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...

class Erf6D(Function6D):
    """
    A Function6D class that implements the error function of the result of a Function6D object: erf(f())

    :param Function6D function: A Function6D object.
    """
    def __init__(self, function: _Function6DInput) -> None: ...
