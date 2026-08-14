import numpy as np
from numpy.typing import NDArray
from raysect.core import AffineMatrix3D, Primitive
from raysect.core.scenegraph._nodebase import _NodeBase

from .emitters import CartesianRayTransferEmitter, CylindricalRayTransferEmitter, RayTransferEmitter

class RayTransferObject:
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
    def invert_voxel_map(self) -> list[NDArray[np.int_]]: ...

class RayTransferCylinder(RayTransferObject):
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
