from collections.abc import Callable
from typing import Literal

from raysect.core.math.function.float import Function1D, Function2D, Function3D

class Slice2D(Function1D):
    """
    Expose a slice of a Function2D as a Function1D.

    :param Function2D function: the function to be sliced.
    :param axis: the axis to be sliced. Must be ['x', 'y'] or [0, 1].
    :param float value: the axis value at which to return a slice

    .. code-block:: pycon

       >>> from cherab.core.math import Slice2D
       >>>
       >>> def f1(x, y):
       >>>     return x**2 + y
       >>>
       >>> f2 = Slice2D(f1, 'x', 1.5)
       >>>
       >>> f2(0)
       2.25
       >>> f2(1)
       3.25
    """

    axis: Literal[0, 1]
    value: float
    def __init__(
        self,
        function: float | Function2D | Callable[[float, float], float],
        axis: Literal[0, 1, "x", "y"],
        value: float,
    ) -> None: ...

class Slice3D(Function2D):
    """
    Expose a slice of a Function3D as a Function2D.

    :param Function3D function: the function to be sliced.
    :param axis: the axis to be sliced. Must be ['x', 'y', 'z'] or [0, 1, 2].
    :param float value: the axis value at which to return a slice

    .. code-block:: pycon

       >>> from cherab.core.math import Slice3D
       >>>
       >>> def f1(x, y, z):
       >>>     return x**3 + y**2 + z
       >>>
       >>> f2 = Slice3D(f1, 'x', 1.5)
       >>>
       >>> f2(0, 0)
       3.375
       >>> f2(1, 0)
       4.375
    """

    axis: Literal[0, 1, 2]
    value: float
    def __init__(
        self,
        function: float | Function3D | Callable[[float, float, float], float],
        axis: Literal[0, 1, 2, "x", "y", "z"],
        value: float,
    ) -> None: ...
