from collections.abc import Callable, Iterator, Sequence
from typing import Literal, overload

import numpy as np
from numpy.typing import ArrayLike, NDArray
from raysect.core import AffineMatrix3D, Node, Point2D, Primitive, Vector3D, World
from raysect.core.math.function.float import Function3D
from raysect.optical import Ray, Spectrum
from raysect.optical.material import Material
from raysect.optical.material.emitter import HomogeneousVolumeEmitter

_ScalarFunction3D = Callable[[float, float, float], float] | Function3D

class Voxel(Node):
    @property
    def volume(self) -> float: ...
    def emissivity_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> float: ...

class AxisymmetricVoxel(Voxel):
    def __init__(
        self,
        vertices: ArrayLike | Sequence[Point2D],
        parent: Node | None = None,
        material: Material | None = None,
        primitive_type: Literal["mesh", "csg"] = "csg",
    ) -> None: ...
    @property
    def material(self) -> Material: ...
    @material.setter
    def material(self, value: Material) -> None: ...
    @property
    def vertices(self) -> list[Point2D]: ...
    @property
    def cross_sectional_area(self) -> float: ...
    @property
    def cross_section_centroid(self) -> Point2D: ...
    @property
    def volume(self) -> float: ...
    def emissivity_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> float: ...

class VoxelCollection(Node):
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, item: int) -> Voxel: ...
    @overload
    def __getitem__(self, item: slice) -> list[Voxel]: ...
    def __iter__(self) -> Iterator[Voxel]: ...
    @property
    def count(self) -> int: ...
    @property
    def total_volume(self) -> float: ...
    def set_active(self, item: int | Literal["all"]) -> None: ...
    def parent_all_voxels(self) -> None: ...
    def unparent_all_voxels(self) -> None: ...
    def emissivities_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> NDArray[np.float64]: ...

class ToroidalVoxelGrid(VoxelCollection):
    def __init__(
        self,
        voxel_coordinates: Sequence[ArrayLike | Sequence[Point2D]],
        name: str = "",
        parent: Node | None = None,
        transform: AffineMatrix3D | None = None,
        active: int | Literal["all"] = "all",
        primitive_type: Literal["mesh", "csg"] = "csg",
    ) -> None: ...
    @property
    def min_radius(self) -> float: ...
    @property
    def max_radius(self) -> float: ...
    @property
    def min_height(self) -> float: ...
    @property
    def max_height(self) -> float: ...
    def set_active(self, item: int | Literal["all"]) -> None: ...
    def plot(
        self,
        title: str | None = None,
        voxel_values: ArrayLike | None = None,
        ax: object | None = None,
        vmin: float | None = None,
        vmax: float | None = None,
        cmap: object | None = None,
    ) -> object: ...

class UnityVoxelEmitter(HomogeneousVolumeEmitter):
    voxel_id: int
    def __init__(self, voxel_id: int) -> None: ...
    def emission_function(
        self,
        direction: Vector3D,
        spectrum: Spectrum,
        world: World,
        ray: Ray,
        primitive: Primitive,
        world_to_primitive: AffineMatrix3D,
        primitive_to_world: AffineMatrix3D,
    ) -> Spectrum: ...
