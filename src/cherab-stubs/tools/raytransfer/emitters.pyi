import numpy as np
from numpy.typing import NDArray
from raysect.core import AffineMatrix3D, Point3D, Primitive, Vector3D
from raysect.optical import Ray, Spectrum, World
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter, VolumeIntegrator

_GridShape = tuple[int, int, int]
_GridSteps = tuple[float, float, float]

class RayTransferIntegrator(VolumeIntegrator):
    """
    Basic class for ray transfer integrators that calculate distances traveled by the ray
    through the voxels defined on a regular grid.

    :param float step: Integration step (in meters), defaults to `step=0.001`.
    :param int min_samples: The minimum number of samples to use over integration range,
        defaults to `min_samples=2`.

    :ivar float step: Integration step.
    :ivar int min_samples: The minimum number of samples to use over integration range.
    """
    def __init__(self, step: float = 0.001, min_samples: int = 2) -> None: ...
    @property
    def step(self) -> float: ...
    @step.setter
    def step(self, value: float) -> None: ...
    @property
    def min_samples(self) -> int: ...
    @min_samples.setter
    def min_samples(self, value: int) -> None: ...

class CylindricalRayTransferIntegrator(RayTransferIntegrator):
    r"""
    Calculates the distances traveled by the ray through the voxels defined on a regular grid
    in cylindrical coordinate system: :math:`(R, \phi, Z)`. This integrator is used
    with the `CylindricalRayTransferEmitter` material class to calculate ray transfer matrices
    (geometry matrices). The value for each voxel is stored in respective bin of the spectral
    array. It is assumed that the emitter is periodic in :math:`\phi` direction with a period
    equal to `material.period`. The distances traveled by the ray through the voxel is calculated
    approximately and the accuracy depends on the integration step.
    """
    def integrate(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        material: InhomogeneousVolumeEmitter,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...

class CartesianRayTransferIntegrator(RayTransferIntegrator):
    """
    Calculates the distances traveled by the ray through the voxels defined on a regular grid
    in Cartesian coordinate system: :math:`(X, Y, Z)`. This integrator is used with
    the `CartesianRayTransferEmitter` material to calculate ray transfer matrices (geometry
    matrices). The value for each voxel is stored in respective bin of the spectral array.
    The distances traveled by the ray through the voxel is calculated approximately and
    the accuracy depends on the integration step.
    """
    def integrate(
        self,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        material: InhomogeneousVolumeEmitter,
        start_point: Point3D,
        end_point: Point3D,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...

class RayTransferEmitter(InhomogeneousVolumeEmitter):
    """
    Basic class for ray transfer emitters defined on a regular 3D grid. Ray transfer emitters
    are used to calculate ray transfer matrices (geometry matrices) for a single value
    of wavelength.

    :param tuple grid_shape: The shape of regular grid (the number of grid cells
        along each direction).
    :param tuple grid_steps: The sizes of grid cells along each direction.
    :param np.ndarray voxel_map: An array with shape `grid_shape` containing the indices of
        the light sources. This array maps the cells of regular grid to the respective voxels
        (light sources). The cells with identical indices in `voxel_map` array form a single
        voxel (light source). If `voxel_map[i1, i2, i3] == -1`, the cell with indices
        `(i1, i2, i3)` will not be mapped to any light source. This parameters allows to
        apply a custom geometry (pixelated though) to the light sources.
        Default value: `voxel_map=None`.
    :param np.ndarray mask: A boolean mask array with shape `grid_shape`.
        Allows to include (`mask[i1, i2, i3] == True`) or exclude (`mask[i1, i2, i3] == False`)
        the cells from the calculation. The ray transfer matrix will be calculated only for those
        cells for which mask is True. This parameter is ignored if `voxel_map` is provided,
        defaults to `mask=None` (all cells are included).
    :param raysect.optical.material.VolumeIntegrator integrator: Volume integrator,
        defaults to `integrator=NumericalVolumeIntegrator()`

    :ivar tuple grid_shape: The shape of regular 3D grid.
    :ivar tuple grid_steps: The sizes of grid cells along each direction.
    :ivar np.ndarray voxel_map: An array containing the indices of the light sources.
    :ivar np.ndarray ~.mask: A boolean mask array showing active (True) and inactive
        (False) gird cells.
    :ivar int bins: Number of light sources (the size of spectral array must be equal to this value).
    """

    voxel_map_mv: NDArray[np.int32]
    def __init__(
        self,
        grid_shape: _GridShape,
        grid_steps: _GridSteps,
        voxel_map: NDArray[np.generic] | None = None,
        mask: NDArray[np.bool_] | None = None,
        integrator: VolumeIntegrator | None = None,
    ) -> None: ...
    @property
    def grid_shape(self) -> _GridShape: ...
    @property
    def grid_steps(self) -> _GridSteps: ...
    @property
    def bins(self) -> int: ...
    @property
    def voxel_map(self) -> NDArray[np.int32]: ...
    @voxel_map.setter
    def voxel_map(self, value: NDArray[np.generic]) -> None: ...
    @property
    def mask(self) -> NDArray[np.bool_]: ...
    @mask.setter
    def mask(self, value: NDArray[np.bool_]) -> None: ...

class CylindricalRayTransferEmitter(RayTransferEmitter):
    r"""
    A unit emitter defined on a regular 3D :math:`(R, \phi, Z)` grid, which
    can be used to calculate ray transfer matrices (geometry matrices) for a single value
    of wavelength.
    This emitter is periodic in :math:`\phi` direction.
    Note that for performance reason there are no boundary checks in `emission_function()`,
    or in `CylindricalRayTransferIntegrator`, so this emitter must be placed between a couple
    of coaxial cylinders that act like a bounding box.

    :param tuple grid_shape: The shape of regular :math:`(R, \phi, Z)` 3D grid.
        If `grid_shape[1] = 1`, the emitter is axisymmetric.
    :param tuple grid_steps: The sizes of grid cells in `R`, :math:`\phi` and `Z`
        directions. The size in :math:`\phi` must be provided in degrees (sizes in `R` and `Z`
        are provided in meters). The period in :math:`\phi` direction is defined as
        `grid_shape[1] * grid_steps[1]`. Note that the period must be a multiple of 360.
    :param np.ndarray voxel_map: An array with shape `grid_shape` containing the indices of
        the light sources. This array maps the cells in :math:`(R, \phi, Z)` space to
        the respective voxels (light sources). The cells with identical indices in `voxel_map`
        array form a single voxel (light source). If `voxel_map[ir, iphi, is] == -1`, the
        cell with indices `(ir, iphi, is)` will not be mapped to any light source.
        This parameters allows to apply a custom geometry (pixelated though) to the light
        sources. Default value: `voxel_map=None`.
    :param np.ndarray mask: A boolean mask array with shape `grid_shape`.
        Allows to include (mask[ir, iphi, is] == True) or exclude (mask[ir, iphi, is] == False)
        the cells from the calculation. The ray transfer matrix will be calculated only for
        those cells for which mask is True. This parameter is ignored if `voxel_map` is provided,
        defaults to `mask=None` (all cells are included).
    :param raysect.optical.material.VolumeIntegrator integrator: Volume integrator, defaults to
        `integrator=CylindricalRayTransferIntegrator(step=0.1*min(grid_shape[0], grid_shape[-1]))`.
    :param float rmin: Lower bound of grid in `R` direction (in meters), defaults to `rmin=0`.

    :ivar float period: The period in :math:`\phi` direction (equals to
        `grid_shape[1] * grid_steps[1]`).
    :ivar float rmin: Lower bound of grid in `R` direction.
    :ivar float dr: The size of grid cell in `R` direction (equals to `grid_shape[0]`).
    :ivar float dphi: The size of grid cell in :math:`\phi` direction (equals to `grid_shape[1]`).
    :ivar float dz: The size of grid cell in `Z` direction (equals to `grid_shape[2]`).

    .. code-block:: pycon

        >>> from raysect.optical import World, translate
        >>> from raysect.primitive import Cylinder, Subtract
        >>> from cherab.tools.raytransfer import CylindricalRayTransferEmitter
        >>> world = World()
        >>> grid_shape = (10, 1, 10)  # axisymmetric case
        >>> grid_steps = (0.5, 360, 0.5)
        >>> rmin = 2.5
        >>> material = CylindricalRayTransferEmitter(grid_shape, grid_steps, rmin=rmin)
        >>> eps = 1.e-6  # ray must never leave the grid when passing through the volume
        >>> radius_outer = grid_shape[0] * grid_steps[0] - eps
        >>> height = grid_shape[2] * grid_steps[2] - eps
        >>> radius_inner = rmin + eps
        >>> bounding_box = Subtract(Cylinder(radius_outer, height), Cylinder(radius_inner, height),
                                    material=material, parent=world)  # bounding primitive
        >>> bounding_box.transform = translate(0, 0, -2.5)
        ...
        >>> camera.spectral_bins = material.bins
        >>> # ray transfer matrix will be calculated for 600.5 nm
        >>> camera.min_wavelength = 600.
        >>> camera.max_wavelength = 601.
    """
    def __init__(
        self,
        grid_shape: _GridShape,
        grid_steps: _GridSteps,
        voxel_map: NDArray[np.generic] | None = None,
        mask: NDArray[np.bool_] | None = None,
        integrator: VolumeIntegrator | None = None,
        rmin: float = 0,
    ) -> None: ...
    @property
    def rmin(self) -> float: ...
    @rmin.setter
    def rmin(self, value: float) -> None: ...
    @property
    def period(self) -> float: ...
    @property
    def dr(self) -> float: ...
    @property
    def dphi(self) -> float: ...
    @property
    def dz(self) -> float: ...
    def emission_function(
        self,
        point: Point3D,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...

class CartesianRayTransferEmitter(RayTransferEmitter):
    """
    A unit emitter defined on a regular 3D :math:`(X, Y, Z)` grid, which can be used
    to calculate ray transfer matrices (geometry matrices).
    Note that for performance reason there are no boundary checks in `emission_function()`,
    or in `CartesianRayTransferIntegrator`, so this emitter must be placed inside a bounding box.

    :param tuple grid_shape: The shape of regular :math:`(X, Y, Z)` grid.
        The number of points in `X`, `Y` and `Z` directions.
    :param tuple grid_steps: The sizes of grid cells in `X`, `Y` and `Z`
        directions (in meters).
    :param np.ndarray voxel_map: An array with shape `grid_shape` containing the indices
        of the light sources. This array maps the cells in :math:`(X, Y, Z)` space to the
        respective voxels (light sources). The cells with identical indices in `voxel_map`
        array form a single voxel (light source). If `voxel_map[ix, it, is] == -1`,
        the cell with indices `(ix, it, is)` will not be mapped to any light source.
        This parameters allows to apply a custom geometry (pixelated though) to the
        light sources. Default value: `voxel_map=None`.
    :param np.ndarray mask: A boolean mask array with shape `grid_shape`.
        Allows to include (`mask[ix, it, is] == True`) or exclude (`mask[ix, it, is] == False`)
        the cells from the calculation. The ray transfer matrix will be calculated only for
        those cells for which mask is True. This parameter is ignored if `voxel_map` is
        provided, defaults to `mask=None` (all cells are included).
    :param raysect.optical.material.VolumeIntegrator integrator: Volume integrator,
        defaults to `integrator=CartesianRayTransferIntegrator(step=0.1 * min(grid_steps))`

    :ivar float dx: The size of grid cell in `X` direction (equals to `grid_shape[0]`).
    :ivar float dy: The size of grid cell in `Y` direction (equals to `grid_shape[1]`).
    :ivar float dz: The size of grid cell in `Z` direction (equals to `grid_shape[2]`).

     .. code-block:: pycon

        >>> from raysect.optical import World, translate, Point3D
        >>> from raysect.primitive import Box
        >>> from cherab.tools.raytransfer import CartesianRayTransferEmitter
        >>> world = World()
        >>> grid_shape = (10, 10, 10)
        >>> grid_steps = (0.5, 0.5, 0.5)
        >>> material = CartesianRayTransferEmitter(grid_shape, grid_steps)
        >>> eps = 1.e-6  # ray must never leave the grid when passing through the volume
        >>> upper = Point3D(grid_shape[0] * grid_steps[0] - eps,
                            grid_shape[1] * grid_steps[1] - eps,
                            grid_shape[2] * grid_steps[2] - eps)
        >>> bounding_box = Box(lower=Point3D(0, 0, 0), upper=upper, material=material,
                               parent=world)
        >>> bounding_box.transform = translate(-2.5, -2.5, -2.5)
        ...
        >>> camera.spectral_bins = material.bins
        >>> # ray transfer matrix will be calculated for 600.5 nm
        >>> camera.min_wavelength = 600.
        >>> camera.max_wavelength = 601.
    """
    def __init__(
        self,
        grid_shape: _GridShape,
        grid_steps: _GridSteps,
        voxel_map: NDArray[np.generic] | None = None,
        mask: NDArray[np.bool_] | None = None,
        integrator: VolumeIntegrator | None = None,
    ) -> None: ...
    @property
    def dx(self) -> float: ...
    @property
    def dy(self) -> float: ...
    @property
    def dz(self) -> float: ...
    def emission_function(
        self,
        point: Point3D,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...
