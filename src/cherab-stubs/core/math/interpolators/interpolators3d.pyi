from typing import Literal

import numpy as np
from numpy.typing import ArrayLike
from raysect.core.math.function.float import Function3D

_EXTRAPOLATION_TYPES: dict[str, Literal["nearest", "linear", "quadratic"]]

class _Interpolate3DBase(Function3D):
    """
    Base class for 3D interpolators. Coordinates and data arrays are here
    sorted and transformed into numpy arrays.

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object z: An array-like object containing real values.
    :param object f: A 3D array-like object of sample values corresponding to the
    `x`, `y` and `z` array points.
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
        z: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...

class Interpolate3DLinear(_Interpolate3DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator3DArray` instead.

    Interpolates 3D data using linear interpolation.

    Inherits from Function3D, implements `__call__(x, y, z)`.

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object z: An array-like object containing real values.
    :param object f: A 3D array-like object of sample values corresponding to the
      `x`, `y` and `z` array points.
    :param bint extrapolate: If True, the extrapolation of data is enabled outside
      the range of the data set. The default is False. A ValueError is raised if
      extrapolation is disabled and a point is requested outside the data set.
    :param object extrapolation_type: Sets the method of extrapolation.
      The options are: 'nearest' (default), 'linear'.
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
       >>> from cherab.core.math import Interpolate3DLinear
       >>>
       >>> # implements x**3 + y**2 + z
       >>> drange = np.linspace(-2.5, 2.5, 100)
       >>> values = np.zeros((100, 100, 100))
       >>> for i in range(100):
       >>>     for j in range(100):
       >>>         for k in range(100):
       >>>             values[i, j, k] = drange[i]**3 + drange[j]**2 + drange[k]
       >>>
       >>> f3d = Interpolate3DLinear(drange, drange, drange, values)
       >>>
       >>> f3d(0, 0, 0)
       0.00063769
       >>> f3d(-2, 1, 1.5)
       -5.50085102
       >>> f3d(-3, 1, 0)
       ValueError: The specified value (x=-3.0, y=1.0, z=0.0) is outside the range
       of the supplied data and/or extrapolation range: x bounds=(-2.5, 2.5),
       y bounds=(-2.5, 2.5), z bounds=(-2.5, 2.5)
    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...

class Interpolate3DCubic(_Interpolate3DBase):
    """
    .. deprecated:: 1.3.0
       Use `raysect.core.math.function.float.Interpolator3DArray` instead.

    Interpolates 3D data using cubic interpolation.

    Inherits from Function3D, implements `__call__(x, y, z)`.

    Data and coordinates are first normalised to the range [0, 1] so as to
    prevent inaccuracy from float numbers. A local calculation based on
    finite differences is used. The splines coefficients are calculated
    on demand and are cached as they are calculated. Plus, no more than
    one polynomial is calculated at each evaluation. The first derivatives
    and the cross derivatives (xy, xz, yz and xyz) are imposed by the
    finite differences approximation, and the resulting function is C1
    (first derivatives are continuous).

    :param object x: An array-like object containing real values.
    :param object y: An array-like object containing real values.
    :param object z: An array-like object containing real values.
    :param object f: A 3D array-like object of sample values corresponding to the
      `x`, `y` and `z` array points.
    :param bint extrapolate: If True, the extrapolation of data is enabled
      outside the range of the data set. The default is False. A ValueError
      is raised if extrapolation is disabled and a point is requested
      outside the data set.
    :param object extrapolation_type: Sets the method of extrapolation.
      The options are: 'nearest' (default), 'linear', 'quadratic'.
    :param double extrapolation_range: The attribute can be set to limit
      the range beyond the data set bounds that extrapolation is permitted.
      The default range is set to infinity. Requesting data beyond the
      extrapolation range will result in a ValueError being raised.
    :param tolerate_single_value: If True, single-value arrays will be
      tolerated as inputs. If a single value is supplied, that value will
      be extrapolated over the entire real range. If False (default),
      supplying a single value will result in a ValueError being raised.

    .. code-block:: pycon

       >>> import numpy as np
       >>> from cherab.core.math import Interpolate3DCubic
       >>>
       >>> # implements x**3 + y**2 + z
       >>> drange = np.linspace(-2.5, 2.5, 100)
       >>> values = np.zeros((100, 100, 100))
       >>> for i in range(100):
       >>>     for j in range(100):
       >>>         for k in range(100):
       >>>             values[i, j, k] = drange[i]**3 + drange[j]**2 + drange[k]
       >>>
       >>> f3d = Interpolate3DCubic(drange, drange, drange, values)
       >>>
       >>> f3d(0, 0, 0)
       -1.7763e-14
       >>> f3d(-2, 1, 1.5)
       -5.50000927
       >>> f3d(-3, 1, 0)
       ValueError: The specified value (x=-3.0, y=1.0, z=0.0) is outside the range
       of the supplied data and/or extrapolation range: x bounds=(-2.5, 2.5),
       y bounds=(-2.5, 2.5), z bounds=(-2.5, 2.5)
    """

    def __init__(
        self,
        x: ArrayLike,
        y: ArrayLike,
        z: ArrayLike,
        f: ArrayLike,
        extrapolate: bool = False,
        extrapolation_type: Literal["nearest", "linear", "quadratic"] = "nearest",
        extrapolation_range: float = np.inf,
        tolerate_single_value: bool = False,
    ) -> None: ...
