import numpy as np
from numpy.typing import NDArray
from raysect.core import AffineMatrix3D, Primitive
from raysect.core.scenegraph._nodebase import _NodeBase

from .emitters import CartesianRayTransferEmitter, CylindricalRayTransferEmitter, RayTransferEmitter

class RayTransferObject:
    """
    Basic class for ray transfer objects.

    :ivar np.ndarray voxel_map: An array containing the indices of the light sources.
    :ivar np.ndarray ~.mask: A boolean mask array showing active (True) and inactive (False) gird cells.
    :ivar Node parent: Scene-graph parent node.
    :ivar AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system
        relative to the scene-graph parent.
    :ivar float step: Integration step of volume integrator.
    :ivar int bins: Number of light sources (the size of spectral array must be equal to this value).
    """

    _primitive: Primitive
    def __init__(self, primitive: Primitive) -> None: ...
    @property
    def parent(self) -> _NodeBase | None: ...
    @parent.setter
    def parent(self, value: _NodeBase | None) -> None: ...
    @property
    def transform(self) -> AffineMatrix3D: ...
    @transform.setter
    def transform(self, value: AffineMatrix3D) -> None: ...
    @property
    def step(self) -> float: ...
    @step.setter
    def step(self, value: float) -> None: ...
    @property
    def voxel_map(self) -> NDArray[np.int_]: ...
    @voxel_map.setter
    def voxel_map(self, value: NDArray[np.int_]) -> None: ...
    @property
    def mask(self) -> NDArray[np.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray[np.bool_]) -> None: ...
    @property
    def bins(self) -> int: ...
    @property
    def material(self) -> RayTransferEmitter: ...
    def invert_voxel_map(self) -> list[NDArray[np.int_]]:
        """
        Returns a list of arrays of cell indices belonging to each light source.
        This list is an inversion of `voxel_map` array.
        """

class RayTransferCylinder(RayTransferObject):
    r"""
    Ray transfer object for cylindrical emitter defined on a regular 3D :math:`(R, \phi, Z)` grid.
    This emitter is periodic in :math:`\phi` direction.
    The base of the cylinder is located at `Z = 0` plane. Use `transform`
    parameter to move it.

    :param float radius_outer: Radius of the outer cylinder and the upper bound of grid in
        `R` direction (in meters).
    :param float height: Height of the cylinder and the length of grid in `Z` direction
        (in meters).
    :param int n_radius: Number of grid points in `R` direction.
    :param int n_height: Number of grid points in `Z` direction.
    :param float radius_inner: Radius of the inner cylinder and the lower bound of grid in
        `R` direction (in meters), defaults to `radius_inner=0`.
    :param int n_polar: Number of grid points in :math:`\phi` direction, defaults to
        `n_polar=1` (axisymmetric case).
    :param float period: A period in :math:`\phi` direction (in degree), defaults to `period=360`.
    :param float step: The step of integration along the ray (in meters),
        defaults to `step = 0.1 * min((radius_outer - radius_inner)/n_radius, height/n_height)`.
    :param np.ndarray voxel_map: An array with shape `(n_radius, n_polar, n_height)`
        containing the indices of the light sources.
        This array maps the cells in :math:`(R, \phi, Z)` space to the respective voxels
        (light sources). The cells with identical indices in `voxel_map` array form a single voxel
        (light source). If `voxel_map[ir, iphi, is] == -1`, the cell with index `(ir, iphi, is)`
        will not be mapped to any light source. This parameters allows to apply a custom geometry
        (pixelated though) to the light sources. Default value: `voxel_map=None`.
        Convert 2D (axisymmetric) `voxel_map` to 3D with `voxel_map = voxel_map[:, None, :]`.
    :param np.ndarray mask: A boolean mask array with shape `(n_radius, n_polar, n_height)`.
        Allows to include (`mask[ir, iphi, is] == True`) or exclude (`mask[ir, iphi, is] == False`)
        the cells from the calculation. The ray transfer matrix will be calculated only for those
        cells for which mask is True. This parameter is ignored if `voxel_map` is provided,
        defaults to `mask=None` (all cells are included).
        Convert 2D (axisymmetric) `mask` to 3D with `mask = mask[:, None, :]`.
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system
        relative to the scene-graph parent (default = identity matrix).

    .. code-block:: pycon

        >>> from raysect.optical import World, translate
        >>> from cherab.tools.raytransfer import RayTransferCylinder
        >>> world = World()
        >>> rtc = RayTransferCylinder(radius_outer=8., height=10., n_radius=400, n_height=1000,
                                      radius_inner=4.)
        >>> rtc.parent = world
        >>> rtc.transform = translate(0, 0, -5.)
        ...
        >>> camera.spectral_bins = rtc.bins
        >>> # ray transfer matrix will be calculated for 600.5 nm
        >>> camera.min_wavelength = 600.
        >>> camera.max_wavelength = 601.
    """
    def __init__(
        self,
        radius_outer: float,
        height: float,
        n_radius: int,
        n_height: int,
        radius_inner: float = 0,
        n_polar: int = 1,
        period: float = 360.0,
        step: float | None = None,
        voxel_map: NDArray[np.int_] | None = None,
        mask: NDArray[np.bool_] | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
    ) -> None: ...
    @property
    def material(self) -> CylindricalRayTransferEmitter: ...

class RayTransferBox(RayTransferObject):
    """
    Ray transfer object for rectangular emitter defined on a regular 3D :math:`(X, Y, Z)` grid.
    The grid starts at (0, 0, 0). Use `transform` parameter to move it.

    :param float xmax: Upper bound of grid in `X` direction (in meters).
    :param float ymax: Upper bound of grid in `Y` direction (in meters).
    :param float zmax: Upper bound of grid in `Z` direction (in meters).
    :param int nx: Number of grid points in `X` direction.
    :param int ny: Number of grid points in `Y` direction.
    :param int nz: Number of grid points in `Z` direction.
    :param float step: The step of integration along the ray (in meters), defaults to
        `step = 0.1 * min(xmax / nx, ymax / ny, zmax / nz)`.
    :param np.ndarray voxel_map: An array with shape `(nx, ny, nz)`
        containing the indices of the light sources. This array maps the cells in
        :math:`(X, Y, Z)` space to the respective voxels (light sources). The cells with
        identical indices in `voxel_map` array form a single voxel (light source).
        If `voxel_map[ix, it, is] == -1`, the cell with index `(ix, it, is)` will not be mapped
        to any light source. This parameters allows to apply a custom geometry (pixelated though)
        to the light sources. Default value: `voxel_map=None`.
    :param np.ndarray mask: A boolean mask array with shape `(nx, ny, nz)`.
        Allows to include (`mask[ix, it, is] == True`) or exclude (`mask[ix, it, is] == False`)
        the cells from the calculation. The ray transfer matrix will be calculated only for those
        cells for which mask is True. This parameter is ignored if `voxel_map` is provided,
        defaults to `mask=None` (all cells are included).
    :param Node parent: Scene-graph parent node or None (default = None).
    :param AffineMatrix3D transform: An AffineMatrix3D defining the local co-ordinate system
        relative to the scene-graph parent (default = identity matrix).

    .. code-block:: pycon

        >>> from raysect.optical import World, translate
        >>> from cherab.tools.raytransfer import RayTransferBox
        >>> world = World()
        >>> rtb = RayTransferBox(xmax=1., ymax=1., zmax=1., nx=100, ny=100, nz=100)
        >>> rtb.parent = world
        >>> rtb.transform = translate(-0.5, -0.5, -0.5)
        >>> ### cutting out a sphere of radius 0.5 ###
        >>> x = np.linspace(-0.495, 0.495, 100)
        >>> xsqr = x * x
        >>> ### mask is a boolean array of shape (100, 100, 100) ###
        >>> mask = xsqr[:, None, None] + xsqr[None, :, None] + xsqr[None, None, :] < 0.25
        >>> rtb.mask = mask  # all cells outside this sphere are excluded
        ...
        >>> camera.spectral_bins = rtb.bins
        >>> # ray transfer matrix will be calculated for 600.5 nm
        >>> camera.min_wavelength = 600.
        >>> camera.max_wavelength = 601.
    """
    def __init__(
        self,
        xmax: float,
        ymax: float,
        zmax: float,
        nx: int,
        ny: int,
        nz: int,
        step: float | None = None,
        voxel_map: NDArray[np.int_] | None = None,
        mask: NDArray[np.bool_] | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
    ) -> None: ...
    @property
    def material(self) -> CartesianRayTransferEmitter: ...
