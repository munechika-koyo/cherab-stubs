from typing import Literal

import numpy as np
from numpy.typing import ArrayLike
from raysect.core.math.function.float.function1d import Function1D

_EXTRAPOLATION_TYPES: dict[str, Literal[0, 1, 2]]

class _Interpolate1DBase(Function1D):
    """
    Base class for 1D interpolators. Coordinate and data arrays are here
    sorted and transformed into numpy arrays.

    :param object x: A 1D array-like object of real values.
    :param object f: A 1D array-like object of real values. The length
     of `f` must be equal to the length of `x`.
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
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...
    def derivative(
        self,
        px: float,
        order: int = 1,
    ) -> float:
        """
        Return the derivative of the interpolating function to the specified order.

        :param px: The x coordinate.
        :param order: The order of the derivative.
        :return: The interpolated derivative.
        """

class Interpolate1DLinear(_Interpolate1DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator1DArray` instead.

    Interpolates 1D data using linear interpolation.

    Inherits from Function1D, implements `__call__(x)`.

    :param object x: A 1D array-like object of real values.
    :param object f: A 1D array-like object of real values. The length
      of `f_data` must be equal to the length of `x_data`.
    :param bint extrapolate: If True, the extrapolation of data is enabled
      outside the range of the data set. The default is False. A ValueError
      is raised if extrapolation is disabled and a point is requested outside
      the data set.
    :param object extrapolation_type: Sets the method of extrapolation. The
      options are: 'nearest' (default), 'linear'.
    :param double extrapolation_range: The attribute can be set to limit the
      range beyond the data set bounds that extrapolation is permitted. The
      default range is set to infinity. Requesting data beyond the extrapolation
      range will result in a ValueError being raised.
    :param tolerate_single_value: If True, single-value arrays will be tolerated
      as inputs. If a single value is supplied, that value will be extrapolated
      over the entire real range. If False (default), supplying a single value
      will result in a ValueError being raised.

    .. code-block:: pycon

       >>> from cherab.core.math import Interpolate1DLinear
       >>>
       >>> f1d = Interpolate1DLinear([0, 0.5, 0.9, 1.0], [2500, 2000, 1000, 0])
       >>>
       >>> f1d(0.2)
       2300.0
       >>> f1d(0.875)
       1062.5
       >>> f1d(1.2)
       ValueError: The specified value (x=1.2) is outside the range of the supplied
       data and/or extrapolation range: x bounds=(0.0, 1.0)
    """

    def __init__(
        self,
        x: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...

class Interpolate1DCubic(_Interpolate1DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator1DArray` instead.

    Interpolates 1D data using cubic interpolation.

    Inherits from Function1D, implements `__call__(x)`.

    Data and coordinates are first normalised to the range [0, 1] so as to
    prevent inaccuracy from float numbers. Spline coefficients are cached
    so they have to be calculated at initialisation only.

    :param object x: A 1D array-like object of real values.
    :param object f: A 1D array-like object of real values. The length
      of `f_data` must be equal to the length of `x_data`.
    :param int continuity_order: Sets the continuity of the cubic spline.
      When set to 1 the cubic spline second derivatives are estimated from
      the data samples and is not continuous. Here, the first derivative is
      free and forced to be continuous, but the second derivative is imposed
      from finite differences estimation. When set to 2 the cubic spline
      second derivatives are free but are forced to be continuous. Defaults
      to `continuity_order = 2`.
    :param bint extrapolate: If True, the extrapolation of data is enabled
      outside the range of the data set. The default is False. A ValueError
      is raised if extrapolation is disabled and a point is requested
      outside the data set.
    :param object extrapolation_type: Sets the method of extrapolation.
      The options are: 'nearest' (default), 'linear', 'quadratic'
    :param double extrapolation_range: The attribute can be set to limit
      the range beyond the data set bounds that extrapolation is permitted.
      The default range is set to infinity. Requesting data beyond the
      extrapolation range will result in a ValueError being raised.
    :param tolerate_single_value: If True, single-value arrays will be
      tolerated as inputs. If a single value is supplied, that value
      will be extrapolated over the entire real range. If False (default),
      supplying a single value will result in a ValueError being raised.

    .. code-block:: pycon

       >>> from cherab.core.math import Interpolate1DCubic
       >>>
       >>> f1d = Interpolate1DCubic([0, 0.5, 0.9, 1.0], [2500, 2000, 1000, 0])
       >>>
       >>> f1d(0.2)
       2197.4683
       >>> f1d(0.875)
       1184.4343
       >>> f1d(1.2)
       ValueError: The specified value (x=1.2) is outside the range of the supplied
       data and/or extrapolation range: x bounds=(0.0, 1.0)
    """

    def __init__(
        self,
        x: ArrayLike,
        f: ArrayLike,
        continuity_order: Literal[1, 2] = 2,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...
