from collections.abc import Callable

from raysect.core.math import Vector3D
from raysect.core.math.function.float import Function3D
from raysect.core.math.function.vector3d import Function3D as VectorFunction3D

class CylindricalTransform(Function3D):
    """
    Convert Cartesian coordinates to cylindrical coordinates and calls a 3D function
    defined in cylindrical coordinates, f(r, :math:`\\phi`, z).

    The angular coordinate is given in radians.

    Positive angular coordinate is measured counterclockwise from the xz plane.

    :param Function3D function3d: The function to be mapped. Must be defined
                                  in the interval (:math:`-\\pi`, :math:`\\pi`]
                                  on the angular axis.

    .. code-block:: pycon

       >>> from math import sqrt, cos
       >>> from cherab.core.math import CylindricalTransform
       >>>
       >>> def my_func(r, phi, z):
       >>>     return r * cos(phi)
       >>>
       >>> f = CylindricalTransform(my_func)
       >>>
       >>> f(1, 0, 0)
       1.0
       >>> f(0.5 * sqrt(3), 0.5, 0)
       0.8660254037844385
    """

    function3d: Function3D

    def __init__(
        self,
        function3d: Function3D | Callable[[float, float, float], float],
    ) -> None: ...

class VectorCylindricalTransform(VectorFunction3D):
    """
    Convert Cartesian coordinates to cylindrical coordinates, calls
    a 3D vector function defined in cylindrical coordinates, f(r, :math:`\\phi`, z),
    then converts the returned 3D vector to Cartesian coordinates.

    The angular coordinate is given in radians.

    Positive angular coordinate is measured counterclockwise from the xz plane.

    :param VectorFunction3D function3d: The function to be mapped. Must be defined
                                        in the interval (:math:`-\\pi`, :math:`\\pi`]
                                        on the angular axis.

    .. code-block:: pycon

       >>> from math import sqrt, cos
       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import VectorCylindricalTransform
       >>>
       >>> def my_vec_func(r, phi, z):
       >>>     v = Vector3D(0, 1, 0)
       >>>     v.length = r * abs(cos(phi))
       >>>     return v
       >>>
       >>> f = VectorCylindricalTransform(my_vec_func)
       >>>
       >>> f(1, 0, 0)
       Vector3D(0.0, 1.0, 0.0)
       >>> f(1/sqrt(2), 1/sqrt(2), 0)
       Vector3D(-0.5, 0.5, 0.0)
    """

    function3d: VectorFunction3D

    def __init__(
        self,
        function3d: VectorFunction3D | Callable[[float, float, float], Vector3D],
    ) -> None: ...
