from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray
from raysect.core.math import Vector3D

def sample1d(
    function1d: Callable[[float], float],
    x_range: tuple[float, float, int],
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """
    Sample a 1D function over the specified range.

    :param function1d: a Python function or Function1D object
    :param x_range: a tuple defining the sample range: (min, max, samples)
    :return: a tuple containing the sampled values: (x_points, function_samples)

    .. code-block:: pycon

       >>> from cherab.core.math import sample1d
       >>>
       >>> def f1(x):
       >>>     return x**2
       >>>
       >>> x_pts, f_vals = sample1d(f1, (0, 3, 5))
       >>> x_pts
       array([0.  , 0.75, 1.5 , 2.25, 3.  ])
       >>> f_vals
       array([0.    , 0.5625, 2.25  , 5.0625, 9.    ])
    """

def sample1d_points(
    function1d: Callable[[float], float],
    x_points: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 1D function at the specified points.

    :param function1d: a Python function or Function1D object
    :param x_points: a 1D array of points to sample the function at
    :return: a 1D array containing the sampled values at the specified points
    """

def sample2d(
    function2d: Callable[[float, float], float],
    x_range: tuple[float, float, int],
    y_range: tuple[float, float, int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Sample a 2D function over the specified ranges.

    :param function2d: a Python function or Function2D object
    :param x_range: a tuple defining the x sample range: (min, max, samples)
    :param y_range: a tuple defining the y sample range: (min, max, samples)
    :return: a tuple containing the sampled values: (x_points, y_points, function_samples)

    .. code-block:: pycon

       >>> from cherab.core.math import sample2d
       >>>
       >>> def f2(x, y):
       >>>     return x**2 + y**2
       >>>
       >>> x_pts, y_pts, f_vals = sample2d(f2, (0, 3, 4), (0, 3, 4))
       >>> x_pts
       array([0., 1., 2., 3.])
       >>> y_pts
       array([0., 1., 2., 3.])
       >>> f_vals
       array([[0., 1., 4., 9.],
              [1., 2., 5.,10.],
              [4., 5., 8.,13.],
              [9.,10.,13.,18.]])
    """

def sample2d_grid(
    function2d: Callable[[float, float], float],
    x: ArrayLike,
    y: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 2D function on a rectilinear grid

    Note that v[i, j] = f(x[i], y[j])

    :param function2d: a Python function or Function2D object
    :param x: the x coordinates of each column in the grid
    :param y: the y coordinates of each row in the grid
    :return v: a 2D array containing the sampled values at each grid point

    .. code-block:: pycon

       >>> from cherab.core.math import sample2d_grid
       >>>
       >>> def f1(x, y):
       >>>     return x**2 + y
       >>>
       >>> f_vals = sample2d_grid(f1, [1, 2], [1, 2, 3])
       >>> f_vals
       array([[2., 3., 4.],
              [5., 6., 7.]])
    """

def sample2d_points(
    function2d: Callable[[float, float], float],
    points: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 2D function at the specified points.

    This function is for sampling at an unstructured sequence of points.
    For sampling over a regular grid, consider sample2d or sample2d_grid
    instead.

    :param function2d: a Python function or Function2D object
    :param points: an Nx2 array of points at which to sample the function
    :return: a 1D array containing the sampled values at each point

    .. code-block:: pycon

       >>> from cherab.core.math import sample2d_points
       >>>
       >>> def f1(x, y):
       >>>     return x**2 + y
       >>>
       >>> f_vals = sample2d_points(f1, [[1, 1], [2, 2], [3, 3]])
       >>> f_vals
       array([ 2.,  6., 12.])
    """

def sample3d(
    function3d: Callable[[float, float, float], float],
    x_range: tuple[float, float, int],
    y_range: tuple[float, float, int],
    z_range: tuple[float, float, int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Sample a 3D function over the specified range.

    :param function3d: a Python function or Function3D object
    :param x_range: a tuple defining the x sample range: (x_min, x_max, x_samples)
    :param y_range: a tuple defining the y sample range: (y_min, y_max, y_samples)
    :param z_range: a tuple defining the z sample range: (z_min, z_max, z_samples)
    :return: a tuple containing the sampled values: (x_points, y_points, z_points, function_samples)

    .. code-block:: pycon

       >>> from cherab.core.math import sample3d
       >>>
       >>> def f1(x, y, z):
       >>>     return x**3 + y**2 + z
       >>>
       >>> x_pts, y_pts, z_pts, f_vals = sample3d(f1, (1, 3, 3), (1, 3, 3), (1, 3, 3))
       >>> x_pts
       array([1., 2., 3.])
       >>> f_vals
       array([[[ 3.,  4.,  5.],
               [ 6.,  7.,  8.],
               [11., 12., 13.]],
              [[10., 11., 12.],
               [13., 14., 15.],
               [18., 19., 20.]],
              [[29., 30., 31.],
               [32., 33., 34.],
               [37., 38., 39.]]])
    """

def sample3d_points(
    function3d: Callable[[float, float, float], float],
    points: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 3D function at the specified points.

    This function is for sampling at an unstructured sequence of points.
    For sampling over a regular grid, consider sample3d or sample3d_grid
    instead.

    :param function3d: a Python function or Function3D object
    :param points: an Nx3 array of points at which to sample the function
    :return: a 1D array containing the sampled values at each point

    .. code-block:: pycon

       >>> from cherab.core.math import sample3d_points
       >>>
       >>> def f1(x, y, z):
       >>>     return x**3 + y**2 + z
       >>>
       >>> f_vals = sample3d_points(f1, [[1,1,1], [2,2,2], [3,3,3]])
       >>> f_vals
       array([ 3., 14., 39.])
    """

def sample3d_grid(
    function3d: Callable[[float, float, float], float],
    x: ArrayLike,
    y: ArrayLike,
    z: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 3D function on a rectilinear grid.

    Note that v[i, j, k] = f(x[i], y[j], z[k])

    :param function3d: a Python function or Function3D object
    :param x: the x coordinates of each column in the grid
    :param y: the y coordinates of each row in the grid
    :param z: the z coordinates of each plane in the grid
    :return v: a 3D array containing the sampled values at each grid point

    .. code-block:: pycon

       >>> from cherab.core.math import sample3d_grid
       >>>
       >>> def f1(x, y, z):
       >>>     return x**3 + y**2 + z
       >>>
       >>> f_vals = sample3d_grid(f1, (1, 3, 3), (1, 3, 3), (1, 3, 3))
       >>> f_vals
       array([[[ 3.,  5.,  5.],
               [11., 13., 13.],
               [11., 13., 13.]],
              [[29., 31., 31.],
               [37., 39., 39.],
               [37., 39., 39.]],
              [[29., 31., 31.],
               [37., 39., 39.],
               [37., 39., 39.]]])
    """

def samplevector2d(
    function2d: Callable[[float, float], Vector3D],
    x_range: tuple[float, float, int],
    y_range: tuple[float, float, int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Sample a 2D vector function over the specified range.

    The function samples returns are an NxMx3 array where the last axis are the
    x, y, and z components of the vector respectively.

    :param function2d: a Python function or Function2D object
    :param x_range: a tuple defining the x sample range: (x_min, x_max, x_samples)
    :param y_range: a tuple defining the y sample range: (y_min, y_max, y_samples)
    :return: a tuple containing the sampled values: (x_points, y_points, function_samples)

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector2d
       >>>
       >>> def my_func(x, y):
       >>>     return Vector3D(x, y, 0)
       >>>
       >>> x_pts, y_pts, f_vals = samplevector2d(my_func, (1, 3, 3), (1, 3, 3))
       >>> x_pts
       array([1., 2., 3.])
       >>> y_pts
       array([1., 2., 3.])
       >>> f_vals
       array([[[1., 1., 0.],
               [1., 2., 0.],
               [1., 3., 0.]],
              [[2., 1., 0.],
               [2., 2., 0.],
               [2., 3., 0.]],
              [[3., 1., 0.],
               [3., 2., 0.],
               [3., 3., 0.]]])
    """

def samplevector2d_points(
    function2d: Callable[[float, float], Vector3D],
    points: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 2D vector function at the specified points.

    This function is for sampling at an unstructured sequence of points.
    For sampling over a regular grid, consider samplevector2d or
    samplevector2d_grid instead.

    :param function2d: a Python function or Function2D object
    :param points: an Nx2 array of points at which to sample the function
    :return: a Nx3 array containing the sampled values at each point

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector2d_points
       >>>
       >>> def my_func(x, y):
       >>>     return Vector3D(x, y, 0)
       >>>
       >>> f_vals = samplevector2d_points(my_func, [[1, 1], [2, 2], [3, 3]])
       >>> f_vals
       array([[1., 1., 0.],
              [2., 2., 0.],
              [3., 3., 0.]])
    """

def samplevector2d_grid(
    function2d: Callable[[float, float], Vector3D],
    x: ArrayLike,
    y: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 2D vector function on a rectilinear grid

    :param function2d: a Python function or Function2D object
    :param x: the x coordinates of each column in the grid
    :param y: the y coordinates of each row in the grid
    :return v: a 3D array containing the sampled values at each grid point

    Note that v[i, j] = f(x[i], y[j])

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector2d_grid
       >>>
       >>> def my_func(x, y):
       >>>     return Vector3D(x, y, 0)
       >>>
       >>> f_vals = samplevector2d_grid(my_func, [1, 2], [1, 2, 3])
       >>> f_vals
       array([[[1., 1., 0.],
               [1., 2., 0.],
               [1., 3., 0.]],
              [[2., 1., 0.],
               [2., 2., 0.],
               [2., 3., 0.]]])
    """

def samplevector3d(
    function3d: Callable[[float, float, float], Vector3D],
    x_range: tuple[float, float, int],
    y_range: tuple[float, float, int],
    z_range: tuple[float, float, int],
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]:
    """
    Sample a 3D vector function over the specified range.

    The function samples returns are an NxMxKx3 array where the last axis are the
    x, y, and z components of the vector respectively.

    :param function3d: a Python function or Function3D object
    :param x_range: a tuple defining the x sample range: (x_min, x_max, x_samples)
    :param y_range: a tuple defining the y sample range: (y_min, y_max, y_samples)
    :param z_range: a tuple defining the z sample range: (z_min, z_max, z_samples)
    :return: a tuple containing the sampled values: (x_points, y_points, z_points, function_samples)

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector3d
       >>>
       >>> def my_func(x, y, z):
       >>>     return Vector3D(x, y, z)
       >>>
       >>> x_pts, y_pts, z_pts, f_vals = samplevector3d(my_func, (1, 2, 2), (1, 3, 3), (1, 3, 3))
       >>> x_pts
       array([1., 2.])
       >>> f_vals
       array([[[[1., 1., 1.],
                [1., 1., 2.],
                [1., 1., 3.]],
               [[1., 2., 1.],
                [1., 2., 2.],
                [1., 2., 3.]],
               [[1., 3., 1.],
                [1., 3., 2.],
                [1., 3., 3.]]],

              [[[2., 1., 1.],
                [2., 1., 2.],
                [2., 1., 3.]],
               [[2., 2., 1.],
                [2., 2., 2.],
                [2., 2., 3.]],
               [[2., 3., 1.],
                [2., 3., 2.],
                [2., 3., 3.]]]])
    """

def samplevector3d_points(
    function3d: Callable[[float, float, float], Vector3D],
    points: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 3D vector function at the specified points.

    This function is for sampling at an unstructured sequence of points.
    For sampling over a regular grid, consider samplevector3d or
    samplevector3d_grid instead.

    :param function3d: a Python function or Function3D object
    :param points: an Nx3 array of points at which to sample the function
    :return: an Nx3 array containing the sampled values at each point

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector3d_points
       >>>
       >>> def my_func(x, y, z):
       >>>     return Vector3D(x, y, z)
       >>>
       >>> f_vals = samplevector3d_points(my_func, [[1,1,1], [2,2,2], [3,3,3]])
       >>> f_vals
       array([[1., 1., 1.],
              [2., 2., 2.],
              [3., 3., 3.]])
    """

def samplevector3d_grid(
    function3d: Callable[[float, float, float], Vector3D],
    x: ArrayLike,
    y: ArrayLike,
    z: ArrayLike,
) -> NDArray[np.float64]:
    """
    Sample a 3D vector function on a rectilinear grid

    Note that v[i, j, k] = f(x[i], y[j], z[k])

    :param function3d: a Python function or Function3D object
    :param x: the x coordinates of each column in the grid
    :param y: the y coordinates of each row in the grid
    :param z: the z coordinates of each plane in the grid
    :return v: an NxMxKx3 array containing the sampled values at each grid point

    .. code-block:: pycon

       >>> from raysect.core.math import Vector3D
       >>> from cherab.core.math import samplevector3d_grid
       >>>
       >>> def my_func(x, y, z):
       >>>     return Vector3D(x, y, z)
       >>>
       >>> f_vals = samplevector3d_grid(my_func, [1,2], [1,2,3], [1,2,3])
       >>> f_vals
       array([[[[1., 1., 1.],
                [1., 1., 2.],
                [1., 1., 3.]],
               [[1., 2., 1.],
                [1., 2., 2.],
                [1., 2., 3.]],
               [[1., 3., 1.],
                [1., 3., 2.],
                [1., 3., 3.]]],

              [[[2., 1., 1.],
                [2., 1., 2.],
                [2., 1., 3.]],
               [[2., 2., 1.],
                [2., 2., 2.],
                [2., 2., 3.]],
               [[2., 3., 1.],
                [2., 3., 2.],
                [2., 3., 3.]]]])
    """
