from typing import Literal

import numpy as np
from numpy.typing import ArrayLike
from raysect.core.math.function.float import Function2D

_EXTRAPOLATION_TYPES: dict[str, Literal[0, 1, 2]]

class _Interpolate2DBase(Function2D):
    """
    Base class for 2D interpolators. Coordinates and data arrays are here
    sorted and transformed into numpy arrays.

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object f: A 2D array-like object of sample values corresponding to the
    `x` and `y` array points.
    :param bint extrapolate: optional
    If True, the extrapolation of data is enabled outside the range of the
    data set. The default is False. A ValueError is raised if extrapolation
    is disabled and a point is requested outside the data set.
    :param object extrapolation_type: optional
    Sets the method of extrapolation. The options are: 'nearest' (default)
    and other options given by the subclass.
    :param double extrapolation_range: optional
    The attribute can be set to limit the range beyond the data set bounds
    that extrapolation is permitted. The default range is set to infinity.
    Requesting data beyond the extrapolation range will result in a
    ValueError being raised.
    :param tolerate_single_value: optional
    If True, single-value arrays will be tolerated as inputs. If a single
    value is supplied, that value will be extrapolated over the entire
    real range. If False (default), supplying a single value will result
    in a ValueError being raised.
    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...
    def derivative(
        self,
        px: float,
        py: float,
        order_x: int,
        order_y: int,
    ) -> float:
        """
        Evaluate the interpolating function.

        :param double px, double py: coordinates at which to evaluate the derivative.
        :param int order_x, int order_y: the order of the derivative in x and y
        :return: the interpolated value
        """

class Interpolate2DLinear(_Interpolate2DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator2DArray` instead.

    Interpolates 2D data using linear interpolation.

    Inherits from Function2D, implements `__call__(x, y)`.

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object f: A 2D array-like object of sample values corresponding to the
      `x` and `y` array points.
    :param bint extrapolate: If True, the extrapolation of data is enabled outside
      the range of the data set. The default is False. A ValueError is raised if
      extrapolation is disabled and a point is requested outside the data set.
    :param object extrapolation_type: Sets the method of extrapolation. The options
      are: 'nearest' (default), 'linear'
    :param double extrapolation_range: The attribute can be set to limit the range
      beyond the data set bounds that extrapolation is permitted. The default range
      is set to infinity. Requesting data beyond the extrapolation range will result
      in a ValueError being raised.
    :param tolerate_single_value: If True, single-value arrays will be tolerated as
      inputs. If a single value is supplied, that value will be extrapolated over
      the entire real range. If False (default), supplying a single value will
      result in a ValueError being raised.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import Interpolate2DLinear
       >>>
       >>> # implements x**2 + y
       >>> drange = np.linspace(-2.5, 2.5, 100)
       >>> values = np.zeros((100, 100))
       >>> for i in range(100):
       >>>     for j in range(100):
       >>>         values[i, j] = drange[i]**2 + drange[j]
       >>>
       >>> f2d = Interpolate2DLinear(drange, drange, values)
       >>>
       >>> f2d(0, 0)
       0.00063769
       >>> f2d(-2, 1)
       5.00022956
       >>> f2d(-2, 3)
       ValueError: The specified value (x=-2.0, y=3.0) is outside the range of the supplied
       data and/or extrapolation range: x bounds=(-2.5, 2.5), y bounds=(-2.5, 2.5)
    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...

class Interpolate2DCubic(_Interpolate2DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator2DArray` instead.

    Interpolates 2D data using cubic interpolation.

    Inherits from Function2D, implements `__call__(x, y)`.

    Data and coordinates are first normalised to the range [0, 1] so as to
    prevent inaccuracy from float numbers. A local calculation based on finite
    differences is used. The splines coefficients are not calculated before
    evaluation but on demand only and are cached as they are calculated. Plus,
    only one polynomial is calculated at each evaluation. The first derivatives
    and the cross derivative are imposed by the finite differences. The resulting
    function is C1.

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object f: A 2D array-like object of sample values corresponding to the
      `x` and `y` array points.
    :param bint extrapolate: If True, the extrapolation of data is enabled outside
      the range of the data set. The default is False. A ValueError is raised if
      extrapolation is disabled and a point is requested outside the data set.
    :param object extrapolation_type: Sets the method of extrapolation. The options
      are: 'nearest' (default), 'linear', 'quadratic'.
    :param double extrapolation_range: The attribute can be set to limit the range
      beyond the data set bounds that extrapolation is permitted. The default range
      is set to infinity. Requesting data beyond the extrapolation range will result
      in a ValueError being raised.
    :param tolerate_single_value: If True, single-value arrays will be tolerated as
      inputs. If a single value is supplied, that value will be extrapolated over
      the entire real range. If False (default), supplying a single value will
      result in a ValueError being raised.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import Interpolate2DCubic
       >>>
       >>> # implements x**2 + y
       >>> drange = np.linspace(-2.5, 2.5, 100)
       >>> values = np.zeros((100, 100))
       >>> for i in range(100):
       >>>     for j in range(100):
       >>>         values[i, j] = drange[i]**2 + drange[j]
       >>>
       >>> f2d = Interpolate2DCubic(drange, drange, values)
       >>>
       >>> f2d(0, 0)
       0.00063769
       >>> f2d(-2, 1)
       5.00022956
       >>> f2d(-2, 3)
       ValueError: The specified value (x=-2.0, y=3.0) is outside the range of the supplied
       data and/or extrapolation range: x bounds=(-2.5, 2.5), y bounds=(-2.5, 2.5)
    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...
