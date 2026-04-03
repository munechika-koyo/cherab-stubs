from collections.abc import Callable

from raysect.core.math import Vector3D
from raysect.core.math.function.float import Function1D, Function2D, Function3D
from raysect.core.math.function.vector3d import Function1D as VectorFunction1D
from raysect.core.math.function.vector3d import Function2D as VectorFunction2D
from raysect.core.math.function.vector3d import Function3D as VectorFunction3D

class PeriodicTransform1D(Function1D):
    """
    Extend a periodic 1D function to an infinite 1D space.

    :param Function1D function1d: The periodic 1D function defined
                                  in the [0, period) interval.
    :param double period: The period of the function.

    .. code-block:: pycon

       >>> from cherab.core.math import PeriodicTransform1D
       >>>
       >>> def f1(x):
       >>>     return x
       >>>
       >>> f2 = PeriodicTransform1D(f1, 1.)
       >>>
       >>> f2(1.5)
       0.5
       >>> f2(-0.3)
       0.7
    """

    function1d: Function1D
    period: float

    def __init__(
        self,
        function1d: Function1D | Callable[[float], float],
        period: float,
    ) -> None: ...

class PeriodicTransform2D(Function2D):
    """
    Extend a periodic 2D function to an infinite 2D space.

    Set period_x/period_y to 0 if the function is not periodic along x/y axis.

    :param Function2D function2d: The periodic 2D function defined
                                  in the ([0, period_x), [0, period_y)) intervals.
    :param double period_x: The period of the function along x-axis.
                            0 if not periodic.
    :param double period_y: The period of the function along y-axis.
                            0 if not periodic.

    .. code-block:: pycon

       >>> from cherab.core.math import PeriodicTransform2D
       >>>
       >>> def f1(x, y):
       >>>     return x * y
       >>>
       >>> f2 = PeriodicTransform2D(f1, 1., 1.)
       >>>
       >>> f2(1.5, 1.5)
       0.25
       >>> f2(-0.3, -1.3)
       0.49
       >>>
       >>> f3 = PeriodicTransform2D(f1, 1., 0)
       >>>
       >>> f3(1.5, 1.5)
       0.75
       >>> f3(-0.3, -1.3)
       -0.91
    """

    function2d: Function2D
    period_x: float
    period_y: float

    def __init__(
        self,
        function2d: Function2D | Callable[[float, float], float],
        period_x: float,
        period_y: float,
    ) -> None: ...

class PeriodicTransform3D(Function3D):
    """
    Extend a periodic 3D function to an infinite 3D space.

    Set period_x/period_y/period_z to 0 if the function is not periodic along x/y/z axis.

    :param Function3D function3d: The periodic 3D function defined in the
                                  ([0, period_x), [0, period_y), [0, period_z)) intervals.
    :param double period_x: The period of the function along x-axis.
                            0 if not periodic.
    :param double period_y: The period of the function along y-axis.
                            0 if not periodic.
    :param double period_z: The period of the function along z-axis.
                            0 if not periodic.

    .. code-block:: pycon

       >>> from cherab.core.math import PeriodicTransform3D
       >>>
       >>> def f1(x, y, z):
       >>>     return x * y * z
       >>>
       >>> f2 = PeriodicTransform3D(f1, 1., 1., 1.)
       >>>
       >>> f2(1.5, 1.5, 1.5)
       0.125
       >>> f2(-0.3, -1.3, -2.3)
       0.343
       >>>
       >>> f3 = PeriodicTransform3D(f1, 0, 1., 0)
       >>>
       >>> f3(1.5, 1.5, 1.5)
       1.125
       >>> f3(-0.3, -1.3, -0.3)
       0.063
    """

    function3d: Function3D
    period_x: float
    period_y: float
    period_z: float

    def __init__(
        self,
        function3d: Function3D | Callable[[float, float, float], float],
        period_x: float,
        period_y: float,
        period_z: float,
    ) -> None: ...

class VectorPeriodicTransform1D(VectorFunction1D):
    """
    Extends a periodic 1D vector function to an infinite 1D space.

    :param VectorFunction1D function1d: The periodic 1D vector function
                                        defined in the [0, period) interval.
    :param double period: The period of the function.

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import VectorPeriodicTransform1D
       >>>
       >>> def f1(x):
       >>>     return Vector3D(x, 0, 0)
       >>>
       >>> f2 = VectorPeriodicTransform1D(f1, 1.)
       >>>
       >>> f2(1.5)
       Vector3D(0.5, 0, 0)
       >>> f2(-0.3)
       Vector3D(0.7, 0, 0)
    """

    function1d: VectorFunction1D
    period: float

    def __init__(
        self,
        function1d: VectorFunction1D | Callable[[float], Vector3D],
        period: float,
    ) -> None: ...

class VectorPeriodicTransform2D(VectorFunction2D):
    """
    Extend a periodic 2D vector function to an infinite 2D space.

    Set period_x/period_y to 0 if the function is not periodic along x/y axis.

    :param VectorFunction2D function2d: The periodic 2D vector function defined in
                                        the ([0, period_x), [0, period_y)) intervals.
    :param double period_x: The period of the function along x-axis.
                            0 if not periodic.
    :param double period_y: The period of the function along y-axis.
                            0 if not periodic.

    .. code-block:: pycon

       >>> from cherab.core.math import VectorPeriodicTransform2D
       >>>
       >>> def f1(x, y):
       >>>     return Vector3D(x, y, 0)
       >>>
       >>> f2 = VectorPeriodicTransform2D(f1, 1., 1.)
       >>>
       >>> f2(1.5, 1.5)
       Vector3D(0.5, 0.5, 0)
       >>> f2(-0.3, -1.3)
       Vector3D(0.7, 0.7, 0)
       >>>
       >>> f3 = VectorPeriodicTransform2D(f1, 1., 0)
       >>>
       >>> f3(1.5, 1.5)
       Vector3D(0.5, 1.5, 0)
       >>> f3(-0.3, -1.3)
       Vector3D(0.7, -1.3, 0)
    """

    function2d: VectorFunction2D
    period_x: float
    period_y: float

    def __init__(
        self,
        function2d: VectorFunction2D | Callable[[float, float], Vector3D],
        period_x: float,
        period_y: float,
    ) -> None: ...

class VectorPeriodicTransform3D(VectorFunction3D):
    """
    Extend a periodic 3D vector function to an infinite 3D space.

    Set period_x/period_y/period_z to 0 if the function is not periodic along x/y/z axis.

    :param VectorFunction3D function3d: The periodic 3D vector function defined in the
                                        ([0, period_x), [0, period_y), [0, period_z)) intervals.
    :param double period_x: The period of the function along x-axis.
                            0 if not periodic.
    :param double period_y: The period of the function along y-axis.
                            0 if not periodic.
    :param double period_z: The period of the function along z-axis.
                            0 if not periodic.

    .. code-block:: pycon

       >>> from cherab.core.math import VectorPeriodicTransform3D
       >>>
       >>> def f1(x, y, z):
       >>>     return Vector3D(x, y, z)
       >>>
       >>> f2 = VectorPeriodicTransform3D(f1, 1., 1., 1.)
       >>>
       >>> f2(1.5, 1.5, 1.5)
       Vector3D(0.5, 0.5, 0.5)
       >>> f2(-0.3, -1.3, -2.3)
       Vector3D(0.7, 0.7, 0.7)
       >>>
       >>> f3 = VectorPeriodicTransform3D(f1, 0, 1., 0)
       >>>
       >>> f3(1.5, 0.5, 1.5)
       Vector3D(1.5, 0.5, 1.5)
    """

    function3d: VectorFunction3D
    period_x: float
    period_y: float
    period_z: float

    def __init__(
        self,
        function3d: VectorFunction3D | Callable[[float, float, float], Vector3D],
        period_x: float,
        period_y: float,
        period_z: float,
    ) -> None: ...
