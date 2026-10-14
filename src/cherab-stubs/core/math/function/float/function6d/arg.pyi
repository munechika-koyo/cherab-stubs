from typing import Literal

from .base import Function6D

class Arg6D(Function6D):
    """
    Returns one of the arguments the function is passed, unmodified

    This is used to pass coordinates through to other functions in the
    function framework which expect a Function6D object.

    Valid options for argument are "x", "y", "z", "u", "v", or "w".

    >>> argx = Arg6D("x")
    >>> argx(2, 3, 5, 7, 11, 13)
    2.0
    >>> argy = Arg6D("y")
    >>> argy(2, 3, 5, 7, 11, 13)
    3.0
    >>> argz = Arg6D("z")
    >>> argz(2, 3, 5, 7, 11, 13)
    5.0
    >>> argu = Arg6D("u")
    >>> argu(2, 3, 5, 7, 11, 13)
    7.0
    >>> argv = Arg6D("v")
    >>> argv(2, 3, 5, 7, 11, 13)
    11.0
    >>> argw = Arg6D("w")
    >>> argw(2, 3, 5, 7, 11, 13)
    13.0

    :param str argument: either "x", "y", "z", "u", "v", or "w", the argument to return
    """
    def __init__(self, argument: Literal["x", "y", "z", "u", "v", "w"]) -> None: ...
