from collections.abc import Callable

import numpy as np
from raysect.core.math.function.float import Function1D, Function2D, Function3D

class ClampOutput1D(Function1D):
    """
    Clamp the output of a Function1D to the range [min, max].

    :param object f: A Function1D instance or a callable python object that takes one argument.
    :param float min: the lower bound, default=-INFINITY.
    :param float max: the upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampOutput1D
       >>>
       >>> clamped_func = ClampOutput1D(np.exp, min=0.5, max=3)
       >>> clamped_func(-3)
       0.5
       >>> clamped_func(0)
       1.0
       >>> clamped_func(3)
       3.0
    """

    def __init__(
        self,
        f: float | Function1D | Callable[[float], float],
        min: float = -np.inf,
        max: float = np.inf,
    ) -> None: ...

class ClampOutput2D(Function2D):
    """
    Clamp the output of a Function2D to the range [min, max].

    :param object f: A Function2D instance or a callable python object that takes two arguments.
    :param float min: the lower bound, default=-INFINITY.
    :param float max: the upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampOutput2D
       >>>
       >>> clamped_func = ClampOutput2D(np.arctan2, min=-1, max=1)
       >>> clamped_func(-1, -1)
       -1.0
       >>> clamped_func(1, -1)
       1.0
    """

    def __init__(
        self,
        f: float | Function2D | Callable[[float, float], float],
        min: float = -np.inf,
        max: float = np.inf,
    ) -> None: ...

class ClampOutput3D(Function3D):
    """
    Clamp the output of a Function3D to the range [min, max].

    :param object f: A Function3D instance or a callable python object that takes three arguments.
    :param float min: the lower bound, default=-INFINITY.
    :param float max: the upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampOutput3D
       >>>
       >>> def my_func(x, y, z):
       >>>     return x**2 + y**2 + z**2
       >>>
       >>> clamped_func = ClampOutput3D(my_func, max=10)
       >>>
       >>> my_func(1, 2, 3)
       14
       >>> clamped_func(1, 2, 3)
       10
    """

    def __init__(
        self,
        f: float | Function3D | Callable[[float, float, float], float],
        min: float = -np.inf,
        max: float = np.inf,
    ) -> None: ...

class ClampInput1D(Function1D):
    """
    Clamp the x input of a Function1D to the range [xmin, xmax].

    :param object f: A Function1D instance or a callable python object that takes one argument.
    :param float xmin: the lower bound, default=-INFINITY.
    :param float xmax: the upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampInput1D
       >>>
       >>> clamped_func = ClampInput1D(np.exp, xmin=0)
       >>> clamped_func(1)
       2.718281828459045
       >>> clamped_func(-1)
       1.0
    """

    def __init__(
        self,
        f: float | Function1D | Callable[[float], float],
        xmin: float = -np.inf,
        xmax: float = np.inf,
    ) -> None: ...

class ClampInput2D(Function2D):
    """
    Clamp the [x, y] inputs of a Function2D to the ranges [xmin, xmax], [ymin, ymax].

    :param object f: A Function2D instance or a callable python object that takes two arguments.
    :param float xmin: the x lower bound, default=-INFINITY.
    :param float xmax: the x upper bound, default=+INFINITY.
    :param float ymin: the y lower bound, default=-INFINITY.
    :param float ymax: the y upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampInput2D
       >>>
       >>> def my_func(x, y):
       >>>     return x**2 + y**2
       >>>
       >>> my_func(1, 1)
       2
       >>> clamped_func = ClampInput2D(my_func, xmax=0, ymax=0)
       >>> clamped_func(1, 1)
       0.0
    """

    def __init__(
        self,
        f: float | Function2D | Callable[[float, float], float],
        xmin: float = -np.inf,
        xmax: float = np.inf,
        ymin: float = -np.inf,
        ymax: float = np.inf,
    ) -> None: ...

class ClampInput3D(Function3D):
    """
    Clamp the [x, y, z] inputs of a Function3D to the ranges [xmin, xmax], [ymin, ymax], [zmin, zmax].

    :param object f: A Function3D instance or a callable python object that takes three arguments.
    :param float xmin: the x lower bound, default=-INFINITY.
    :param float xmax: the x upper bound, default=+INFINITY.
    :param float ymin: the y lower bound, default=-INFINITY.
    :param float ymax: the y upper bound, default=+INFINITY.
    :param float zmin: the z lower bound, default=-INFINITY.
    :param float zmax: the z upper bound, default=+INFINITY.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import ClampInput3D
       >>>
       >>> def my_func(x, y, z):
       >>>     return x**2 + y**2 + z**2
       >>>
       >>> my_func(-1, -1, -1)
       3
       >>> clamped_func = ClampInput3D(my_func, xmin=0, ymin=0, zmin=0)
       >>> clamped_func(-1, -1, -1)
       0.0
    """

    def __init__(
        self,
        f: float | Function3D | Callable[[float, float, float], float],
        xmin: float = -np.inf,
        xmax: float = np.inf,
        ymin: float = -np.inf,
        ymax: float = np.inf,
        zmin: float = -np.inf,
        zmax: float = np.inf,
    ) -> None: ...
