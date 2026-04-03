from numpy.typing import ArrayLike
from raysect.core.math.function.float import Function2D

class PolygonMask2D(Function2D):
    """
    A 2D mask defined by a simple n-sided closed polygon.

    Inherits from Function2D, implements `__call__(x, y)`.

    This 2D function returns 1.0 if the (x, y) point lies inside the polygon
    and 0.0 outside.

    The mesh is specified as a set of 2D vertices supplied as an Nx2 numpy
    array or a suitably sized sequence that can be converted to a numpy array.

    The vertex list must define a closed polygon without self intersections -
    a mathematically "simple" polygon.

    .. code-block:: pycon

       >>> from cherab.core.math import PolygonMask2D
       >>>
       >>> fp = PolygonMask2D([[0, 0], [1, 0], [1, 1], [0, 1]])
       >>>
       >>> fp(0.5, 0.5)
       1.0
       >>> fp(-0.5, 0.5)
       0.0
    """
    def __init__(self, vertices: ArrayLike) -> None: ...
