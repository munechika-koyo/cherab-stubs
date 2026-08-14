from collections.abc import Callable, Collection

import numpy as np
from numpy.typing import ArrayLike, NDArray
from raysect.core.math.function.float import Blend2D as ScalarBlend2D
from raysect.core.math.function.float import Interpolator1DArray
from raysect.core.math.function.float.function2d import Interpolator2DArray
from raysect.core.math.function.vector3d import Blend2D as VectorBlend2D
from raysect.core.math.function.vector3d import Function2D as VectorFunction2D
from raysect.optical import Point2D, Vector3D

from ...core.math import AxisymmetricMapper, Function1D, Function2D, PolygonMask2D, VectorAxisymmetricMapper

class EFITEquilibrium:
    r"""
    An object representing an EFIT equilibrium time-slice.

    EFIT is a code commonly used throughout the Fusion research community
    for calculating the plasma magnetic equilibrium from a range of magnetics
    measurements (L. Lao et. al. Nucl. Fusion **25** 1985). This equilibrium object
    allows the calculation of the tokamak magnetic field from a number of EFIT
    code outputs. To use this class properly users should be familiar with
    the output data of EFIT.

    The EFIT data is interpolated to produced continuous functions of the
    equilibrium attributes, such as the magnetic flux (psi) and magnetic
    field.

    Note: psin_to_r mapping only exists if the psi axis is monotonic.

    For examples of how to instantiate this class, see the examples in the
    machine specific packages.

    :param r: EFIT grid radius axis values (array).
    :param z: EFIT grid height axis values (array).
    :param psi_grid: EFIT psi grid values (array).
    :param float psi_axis: The psi value at the magnetic axis.
    :param float psi_lcfs: The psi value at the LCFS.
    :param Point2D magnetic_axis: The coordinates of the magnetic axis.
    :param x_points: A list or tuple of x-points.
    :param strike_points: A list or tuple of strike-points.
    :param f_profile: The current flux profile on psin (2xN array).
    :param q_profile: The safety factor (q) profile on psin (2xN array).
    :param float b_vacuum_radius: Vacuum B-field reference radius (in meters).
    :param float b_vacuum_magnitude: Vacuum B-Field magnitude at the reference radius.
    :param lcfs_polygon: A 2xN array of [[x0, ...], [y0, ...]] vertices specifying the LCFS boundary.
    :param limiter_polygon: A 2xN array of [[x0, ...], [y0, ...]] vertices specifying the limiter.
    :param float time: The time stamp of the time-slice (in seconds).

    :ivar Function2D psi: The poloidal flux in the r-z plane, :math:`\psi(r,z)`.
    :ivar Function2D psi_normalised: The normalised poloidal flux in the r-z plane, :math:`\psi_n(r,z)`.
    :ivar Function1D f_profile: The current flux at the specified normalised poloidal flux, :math:`F(\psi_n)`.
    :ivar Function1D q: The safety factor :math:`q` at the specified normalised poloidal flux, :math:`q(\psi_n)`.
    :ivar VectorFunction2D b_field: A 2D function that returns the magnetic field vector at the specified
      point in the r-z plane, :math:`B(r, z)`.
    :ivar VectorFunction2D toroidal_vector: The toroidal flux coordinate basis vector, :math:`\hat{\phi}(r, z)`.
    :ivar VectorFunction2D poloidal_vector: The poloidal flux coordinate basis vector, :math:`\hat{ \theta }(r, z)`.
    :ivar VectorFunction2D surface_normal: The surface normal flux coordinate basis vector, :math:`\hat{\psi}(r, z)`.
    :ivar Function2D inside_lcfs: A 2D function that identifies if a given (r, z) coordinate lies inside or outside
      the plasma Last Closed Flux Surface (LCFS). This mask function returns a value of 1 if the requested point
      lies inside the LCFS. A value of 0.0 is returned outside the LCFS.
    :ivar Function2D inside_limiter: A 2D function that identifies if a given (r, z) coordinate lies inside or
      outside the first wall limiter polygon. This mask function returns a value of 1 if the requested point
      lies inside the limit polygon. A value of 0.0 is returned outside the polygon.
    """

    time: float
    r_data: NDArray[np.float64]
    z_data: NDArray[np.float64]
    psi_data: NDArray[np.float64]

    psi: Function2D
    psi_axis: float
    psi_lcfs: float
    psi_normalised: Function2D
    r_range: tuple[float, float]
    z_range: tuple[float, float]
    f_profile: Function1D
    q: Function1D

    b_field: VectorFunction2D
    toroidal_vector: VectorFunction2D
    poloidal_vector: VectorFunction2D
    surface_normal: VectorFunction2D

    magnetic_axis: Point2D
    x_points: tuple[Point2D, ...]
    strike_points: tuple[Point2D, ...]

    lcfs_polygon: NDArray[np.float64]
    inside_lcfs: EFITLCFSMask
    limiter_polygon: NDArray[np.float64] | None
    inside_limiter: PolygonMask2D | None

    psin_to_r: Interpolator1DArray | None

    def __init__(
        self,
        r: ArrayLike,
        z: ArrayLike,
        psi_grid: ArrayLike,
        psi_axis: float,
        psi_lcfs: float,
        magnetic_axis: Point2D,
        x_points: Collection[Point2D],
        strike_points: Collection[Point2D],
        f_profile: ArrayLike,
        q_profile: ArrayLike,
        b_vacuum_radius: float,
        b_vacuum_magnitude: float,
        lcfs_polygon: ArrayLike,
        limiter_polygon: ArrayLike | None,
        time: float,
    ) -> None: ...
    def _process_points(
        self,
        magnetic_axis: Point2D,
        x_points: Collection[Point2D],
        strike_points: Collection[Point2D],
    ) -> None: ...
    def _process_polygons(
        self,
        lcfs_polygon: ArrayLike,
        limiter_polygon: ArrayLike | None,
        psi_normalised: Function2D,
    ) -> None: ...
    def _calculate_differentials(self, r: ArrayLike, z: ArrayLike, psi_grid: ArrayLike) -> tuple[Interpolator2DArray, Interpolator2DArray]: ...
    def _generate_psin_to_r_mapping(self) -> None: ...
    def map2d(
        self,
        profile: Function1D | Callable[[float], float] | ArrayLike,
        value_outside_lcfs: float = 0.0,
    ) -> ScalarBlend2D:
        """
        Map a 1D profile onto the equilibrium to give a 2D profile.

        Useful for mapping flux surface quantities in the r-z plane.

        :param profile: A 1D function or 2xN array.
        :param value_outside_lcfs: Value returned if point requested outside the LCFS (default=0.0).
        :return: Function2D object.

        .. code-block:: pycon

           >>> # Hypothesise a 1D electron temperature profile as a function of psi_n.
           >>> te_data = np.zeros((2, 6))
           >>> te_data[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> te_data[1, :] = [0, 100, 400, 500, 550, 600]
           >>> te = equilibrium.map2d(te_data)
           >>>
           >>> # evaluate temperature mapped on flux surfaces in (r, z)
           >>> te(3.1, 0.2)
           487.924780234
        """

    def map3d(
        self,
        profile: Function1D | Callable[[float], float] | ArrayLike,
        value_outside_lcfs: float = 0.0,
    ) -> AxisymmetricMapper:
        """
        Map a 1D profile onto the equilibrium to give a 3D profile.

        Useful for mapping flux surface quantities in 3D space.

        :param profile: A 1D function or Nx2 array.
        :param value_outside_lcfs: Value returned if point requested outside the LCFS (default=0.0).
        :return: Function3D object.

        .. code-block:: pycon

           >>> # Hypothesise a 1D electron temperature profile as a function of psi_n.
           >>> te_data = np.zeros((2, 6))
           >>> te_data[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> te_data[1, :] = [0, 100, 400, 500, 550, 600]
           >>> te = equilibrium.map3d(te_data)
           >>>
           >>> # evaluate temperature mapped on flux surfaces in (r, z)
           >>> te(3.1, -2.9, 0.2)
           357.8793240
        """

    def map_vector2d(
        self,
        toroidal: Function1D | Callable[[float], float] | ArrayLike,
        poloidal: Function1D | Callable[[float], float] | ArrayLike,
        normal: Function1D | Callable[[float], float] | ArrayLike | float,
        value_outside_lcfs: Vector3D | None = None,
    ) -> VectorBlend2D:
        r"""
        Map velocity components in flux coordinates onto flux surfaces in the r-z plane.

        It is often convenient to express the plasma velocity components in flux coordinates,
        assuming the velocities are flux functions. This function allows the user to
        specify velocity components as 1D functions of :math:`\psi_n`. The three velocity
        components are combined to yield a velocity vector at the requested r-z coordinate.

        :param toroidal: Toroidal velocity :math:`v_{\phi} (\psi_n)`, specified as a 1D function
          or Nx2 array.
        :param poloidal: Poloidal vector :math:`v_{\theta} (\psi_n)`, specified as a 1D function
          or Nx2 array.
        :param normal: Velocity along the flux surface normal :math:`v_{\psi} (\psi_n)`, specified
          as a 1D function or Nx2 array.
        :return: VectorFunction2D object that returns the velocity vector at a given r,z coordinate,
          :math:`v(r,z)`.
        :param value_outside_lcfs: Value returned if point requested outside the LCFS (default=
          Vector3D(0, 0, 0)).
        :return: VectorFunction2D object that returns the velocity vector at a given r,z coordinate, :math:`v(r,z)`.
        :rtype: VectorFunction2D

        .. code-block:: pycon

           >>> # Hypothesise 1D profiles for the toroidal and poloidal velocities on psi_n.
           >>> v_toroidal = np.zeros((2, 6))
           >>> v_toroidal[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> v_toroidal[1, :] = [0, 1e4, 3e4, 5e4, 5.5e4, 6e4]
           >>> v_poloidal = np.zeros((2, 6))
           >>> v_poloidal[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> v_poloidal[1, :] = [4e4, 1e4, 3e3, 1e3, 0, 0]
           >>> # Assume zero velocity normal to flux surface
           >>> v_normal = 0.0
           >>>
           >>> # generate VectorFunction2D and sample
           >>> v = equilibrium.map_vector2d(v_toroidal, v_poloidal, v_normal)
           >>> v(3.1, 0.2)
           Vector3D(134.523, 543.6347, 25342.16)
        """

    def map_vector3d(
        self,
        toroidal: Function1D | Callable[[float], float] | ArrayLike,
        poloidal: Function1D | Callable[[float], float] | ArrayLike,
        normal: Function1D | Callable[[float], float] | ArrayLike | float,
        value_outside_lcfs: Vector3D | None = None,
    ) -> VectorAxisymmetricMapper:
        r"""
        Map velocity components in flux coordinates onto flux surfaces in 3D space.

        It is often convenient to express the plasma velocity components in flux coordinates,
        assuming the velocities are flux functions. This function allows the user to
        specify velocity components as 1D functions of :math:`\psi_n`. The three velocity
        components are combined to yield a velocity vector at the requested 3D coordinate.

        :param toroidal: Toroidal velocity :math:`v_{\phi} (\psi_n)`, specified as a 1D function
          or Nx2 array.
        :param poloidal: Poloidal vector :math:`v_{\theta} (\psi_n)`, specified as a 1D function
          or Nx2 array.
        :param normal: Velocity along the flux surface normal :math:`v_{\psi} (\psi_n)`, specified
          as a 1D function or Nx2 array.
        :return: VectorFunction2D object that returns the velocity vector at a given r,z coordinate,
          :math:`v(r,z)`.
        :param value_outside_lcfs: Value returned if point requested outside the LCFS (default=
          Vector3D(0, 0, 0)).

        .. code-block:: pycon

           >>> # Hypothesise 1D profiles for the toroidal and poloidal velocities on psi_n.
           >>> v_toroidal = np.zeros((2, 6))
           >>> v_toroidal[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> v_toroidal[1, :] = [0, 1e4, 3e4, 5e4, 5.5e4, 6e4]
           >>> v_poloidal = np.zeros((2, 6))
           >>> v_poloidal[0, :] = [0, 0.1, 0.2, 0.4, 0.7, 1.0]
           >>> v_poloidal[1, :] = [4e4, 1e4, 3e3, 1e3, 0, 0]
           >>> # Assume zero velocity normal to flux surface
           >>> v_normal = 0.0
           >>>
           >>> # generate VectorFunction2D and sample
           >>> v = equilibrium.map_vector3d(v_toroidal, v_poloidal, v_normal)
           >>> v(3.1, -0.1, 0.2)
           Vector3D(134.523, 543.6347, 25342.16)
        """

class EFITLCFSMask(Function2D):
    """
    A 2D function that identifies if a point lies inside or outside the plasma LCFS.

    This mask function returns a value of 1 if the requested point lies inside
    the Last Closed Flux Surface (LCFS). A value of 0.0 is returns outside the LCFS.

    :param lcfs_polygon: An Nx2 array of (x, y) vertices specifying the LCFS boundary.
    :param psi_normalised: A 2D function of normalised poloidal flux.
    """

    def __init__(self, lcfs_polygon: object, psi_normalised: Callable[[float, float], float]) -> None: ...

class MagneticField(VectorFunction2D):
    """
    A 2D magnetic field vector function derived from EFIT data.

    :param psi_normalised: A 2D function of normalised poloidal flux.
    :param dpsi_dr: A 2D function of the radius differential of poloidal flux.
    :param dpsi_dz: A 2D function of the height differential of poloidal flux.
    :param f_profile: A 1D function containing a current flux profile.
    :param b_vacuum_radius: Vacuum B-field reference radius (in meters).
    :param b_vacuum_magnitude: Vacuum B-Field magnitude at the reference radius.
    :param inside_lcfs: A 2D mask function returning 1 if inside the LCFS and 0 otherwise.
    """

    _psi_normalised: Function2D
    _dpsi_dr: Function2D
    _dpsi_dz: Function2D
    _f_profile: Function1D
    _b_vacuum_radius: float
    _b_vacuum_magnitude: float
    _inside_lcfs: Function2D

    def __init__(
        self,
        psi_normalised: ArrayLike,
        dpsi_dr: ArrayLike,
        dpsi_dz: ArrayLike,
        f_profile: ArrayLike,
        b_vacuum_radius: float,
        b_vacuum_magnitude: float,
        inside_lcfs: ArrayLike,
    ) -> None: ...

class PoloidalFieldVector(VectorFunction2D):
    def __init__(self, field: object) -> None: ...

class FluxSurfaceNormal(VectorFunction2D):
    def __init__(self, field: object) -> None: ...

class FluxCoordToCartesian(VectorFunction2D):
    _field: VectorFunction2D
    _psin: Function2D
    _toroidal: Function1D
    _poloidal: Function1D
    _normal: Function1D
    _value_outside_lcfs: Vector3D

    def __init__(
        self,
        field: ArrayLike,
        psi_normalised: ArrayLike,
        toroidal: ArrayLike,
        poloidal: ArrayLike,
        normal: ArrayLike,
        value_outside_lcfs: Vector3D = Vector3D(0, 0, 0),  # noqa: B008
    ) -> None: ...
