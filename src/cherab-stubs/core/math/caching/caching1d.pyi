from collections.abc import Callable

import numpy as np
from numpy.typing import NDArray
from raysect.core.math.function.float import Function1D

EPSILON: float

class Caching1D(Function1D):
    """
    Precalculate and cache a 1D function on a finite space area.

    The function is sampled and a cubic interpolation is then used to calculate
    a cubic spline approximation of the function. As the spline has a constant
    cost of evaluation, this decreases the evaluation time of functions which
    are very often used.

    The sampling and interpolation are done locally and on demand, so that the
    caching is done progressively when the function is evaluated. Coordinates
    are normalised to the range [0, 1] to avoid float accuracy troubles. The
    values of the function are normalised if their boundaries are given.

    :param object function1d: 1D function to be cached.
    :param tuple space_area: space area where the function has to be cached:
      (minx, maxx).
    :param double resolution: resolution of the sampling
    :param no_boundary_error: Behaviour when evaluated outside the caching area.
      When False a ValueError is raised. When True the function is directly
      evaluated (without caching). Default is False.
    :param function_boundaries: Boundaries of the function values for
      normalisation: (min, max). If None, function values are not normalised.
      Default is None.

    .. code-block:: pycon

       >>> from numpy import sqrt
       >>> from time import sleep
       >>> from cherab.core.math import Caching1D
       >>>
       >>> def expensive_sqrt(x):
       >>>     sleep(5)
       >>>     return sqrt(x)
       >>>
       >>> f1 = Caching1D(expensive_sqrt, (-5, 5), 0.1)
       >>>
       >>> # if you try this, first two executions will be slow, third will be fast
       >>> f1(2.5)
       1.5811388
       >>> f1(2.6)
       1.6124515
       >>> f1(2.55)
       1.5968720
    """

    function: Function1D
    no_boundary_error: int
    x_np: NDArray[np.float64]
    x_domain_view: NDArray[np.float64]
    top_index_x: int
    x_min: float
    x_delta_inv: float
    data_min: float
    data_max: float
    data_delta: float
    data_delta_inv: float
    x_view: NDArray[np.float64]
    x2_view: NDArray[np.float64]
    x3_view: NDArray[np.float64]
    data_view: NDArray[np.float64]
    coeffs_view: NDArray[np.float64]
    calculated_view: NDArray[np.int8]

    def __init__(
        self,
        function1d: float | Function1D | Callable[[float], float],
        space_area: tuple[float, float],
        resolution: float,
        no_boundary_error: bool = False,
        function_boundaries: tuple[float, float] | None = None,
    ) -> None: ...
