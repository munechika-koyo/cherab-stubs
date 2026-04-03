from collections.abc import Callable

import numpy as np
from numpy.typing import NDArray
from raysect.core.math.function.float import Function3D

EPSILON: float

class Caching3D(Function3D):
    """
    Precalculate and cache a 3D function on a finite space area.

    The function is sampled and a cubic interpolation is then used to calculate
    a cubic spline approximation of the function. As the spline has a constant
    cost of evaluation, this decreases the evaluation time of functions which
    are very often used.

    The sampling and interpolation are done locally and on demand, so that the
    caching is done progressively when the function is evaluated. Coordinates
    are normalised to the range [0, 1] to avoid float accuracy troubles. The
    values of the function are normalised if their boundaries are given.

    :param object function3d: 3D function to be cached.
    :param tuple space_area: space area where the function has to be cached:
      (minx, maxx, miny, maxy, minz, maxz).
    :param tuple resolution: resolution of the sampling:
      (resolutionx, resolutiony, resolutionz).
    :param no_boundary_error: Behaviour when evaluated outside the caching area.
      When False a ValueError is raised. When True the function is directly
      evaluated (without caching). Default is False.
    :param function_boundaries: Boundaries of the function values for
      normalisation: (min, max). If None, function values are not normalised.
      Default is None.

    .. code-block:: pycon

       >>> from numpy import sqrt
       >>> from time import sleep
       >>> from cherab.core.math import Caching3D
       >>>
       >>> def expensive_radius(x, y, z):
       >>>     sleep(5)
       >>>     return sqrt(x**2 + y**2 + z**2)
       >>>
       >>> f1 = Caching3D(expensive_radius, (-5, 5, -5, 5, -5, 5), (0.1, 0.1, 0.1))
       >>>
       >>> # if you try this, first two executions will be slow, third will be fast
       >>> # Note: the first execution might be particularly slow, this is because it
       >>> # sets up the caching structures on first execution.
       >>> f1(1.5, 1.5, 1.5)
       2.598076
       >>> f1(1.6, 1.5, 1.5)
       2.657066
       >>> f1(1.55, 1.5, 1.5)
       2.627260
    """

    function: Function3D
    no_boundary_error: bool
    x_np: NDArray[np.float64]
    y_np: NDArray[np.float64]
    z_np: NDArray[np.float64]
    x_domain_view: NDArray[np.float64]
    y_domain_view: NDArray[np.float64]
    z_domain_view: NDArray[np.float64]
    top_index_x: int
    top_index_y: int
    top_index_z: int
    x_min: NDArray[np.float64]
    x_delta_inv: NDArray[np.float64]
    y_min: NDArray[np.float64]
    y_delta_inv: NDArray[np.float64]
    z_min: NDArray[np.float64]
    z_delta_inv: NDArray[np.float64]
    data_min: NDArray[np.float64]
    data_max: NDArray[np.float64]
    data_delta: NDArray[np.float64]
    data_delta_inv: NDArray[np.float64]
    x_view: NDArray[np.float64]
    x2_view: NDArray[np.float64]
    x3_view: NDArray[np.float64]
    y_view: NDArray[np.float64]
    y2_view: NDArray[np.float64]
    y3_view: NDArray[np.float64]
    z_view: NDArray[np.float64]
    z2_view: NDArray[np.float64]
    z3_view: NDArray[np.float64]
    data_view: NDArray[np.float64]
    coeffs_view: NDArray[np.float64]
    calculated_view: NDArray[np.float64]

    def __init__(
        self,
        function3d: float | Function3D | Callable[[float, float, float], float],
        space_area: tuple[float, float, float, float, float, float],
        resolution: tuple[float, float, float],
        no_boundary_error: bool = False,
        function_boundaries: tuple[float, float] | None = None,
    ) -> None: ...
