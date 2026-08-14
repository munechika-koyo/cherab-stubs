import numpy as np
from numpy.typing import NDArray
from raysect.core import AffineMatrix3D, Point3D, Primitive, Vector3D
from raysect.optical import Ray, Spectrum, World
from raysect.optical.material.emitter import InhomogeneousVolumeEmitter, VolumeIntegrator

_GridShape = tuple[int, int, int]
_GridSteps = tuple[float, float, float]

class RayTransferIntegrator(VolumeIntegrator):
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
