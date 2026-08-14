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
    """
    A Voxel base class.

    Each Voxel is a Node in the scenegraph. Each Voxel type that
    inherits from this class defines its own geometry.

    :ivar float volume: The geometric volume of this voxel.
    """

    @property
    def volume(self) -> float: ...
    def emissivity_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> float: ...

class AxisymmetricVoxel(Voxel):
    """
    An axis-symmetric Voxel.

    This Voxel is symmetric about the vertical z-axis. The cross section
    of the voxel can be arbitrarily defined by a polygon in the r-z plane.
    The type of geometric primitive used to define the geometric extent of
    this Voxel can be selected by the user and either of type Mesh or CSG.
    The two representations should approximately the same geometry but have
    different performance goals. The CSG representation uses lower memory and
    is a better choice when large numbers of Voxels will be present in a single
    scene. The Mesh representation is split into smaller components and better
    for cases where multiple importance sampling is important, such as weight
    matrices including reflection effects.


    :param vertices: An Nx2 array specifying the voxel's polygon outline in the
      r-z plane.
    :param Node parent: The scenegraph to which this Voxel is attached.
    :param Material material: The emission material of this Voxel, defaults
      to a UnityVolumeEmitter() for weight matrix calculations.
    :param str primitive_type: Specifies the primitive type, can be either
      'mesh' or 'csg'. Defaults to the CSG representation.

    :ivar float volume: The geometric volume of this voxel.
    :ivar float cross_sectional_area: The cross sectional area of the voxel in
      the r-z plane.
    :ivar Point2D cross_section_centroid: The centroid of the voxel in
      the r-z plane.
    """
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
    def emissivity_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> float:
        """
        Calculate the average emissivity in the voxel.

        :param callable emission_function: a function defining the emissivity
            in (r, ϕ, z) space
        :param int grid_samples: the number of samples of the emissivitiy to use
            to calculate the average

        :return float emissivity: the average emissivity in the voxel cross section

        Note that while the emissivity function is a 3D function, for
        Axisymmetric voxels the return value should be independent of
        toroidal angle ϕ.
        """

class VoxelCollection(Node):
    """
    The base class for collections of voxels.

    Used for managing a collection of voxels when calculating a weight
    matrix for example.

    .. warning:
       No checks are performed by the base class to ensure that the voxel
       volumes don't overlap. This is the responsibility of the user.

    :ivar float count: The number of voxels in this collection.
    :ivar float total_volume: The total volume of all voxels.
    """
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
    def set_active(self, item: int | Literal["all"]) -> None:
        """
        Set the ith voxel as an active emitter.

        :param item: If item is an int, the ith voxel will be configured as an active emitter,
          all the others will be turned off. If item is the string 'all', all voxels will be
          active emitters.
        """
    def parent_all_voxels(self) -> None:
        """Add all voxels in this collection to the scenegraph."""
    def unparent_all_voxels(self) -> None:
        """Remove all voxels in this collection from the scenegraph."""
    def emissivities_from_function(self, emission_function: _ScalarFunction3D, grid_samples: int = 10) -> NDArray[np.float64]:
        """
        Returns an array of sampled emissivities at each voxel location.

        Note that the results will be nonsense if you mix an emission function
        and VoxelCollection with incompatible symmetries.

        :param Function3D emission_function: Emission function to sample over.
        :param int grid_samples: Number of emission samples to average over.
        :rtype: np.ndarray
        """

class ToroidalVoxelGrid(VoxelCollection):
    """
    A collection of axis-symmetric toroidal voxels.

    This object manages a collection of voxels, where each voxel in the collection
    is an AxisymmetricVoxel object.

    :param voxel_coordinates: An array/list of voxels, where each voxel element
      is defined by a list of 2D points.
    :param str name: The name of this voxel collection.
    :param Node parent: The parent scenegraph to which these voxels belong.
    :param AffineMatrix3D transform: The coordinate transformation of this local
      coordinate system relative to the scenegraph parent, defaults to the identity
      transform.
    :param active: Selects which voxels are active emitters in the initialised state.
      If active is an int, the ith voxel will be configured as an active emitter, all
      the others will be turned off. If active is the string 'all', all voxels will be
      active emitters.
    :param str primitive_type: The geometry type to use for the AxisymmetricVoxel
      instances, can be ['mesh', 'csg']. See their documentation for more information.
      Defaults to `primitive_type='csg'`.
    """
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
    ) -> object:
        """
        Plots a voxel grid.

        If no voxel data values are provided, the plot is an outline of the grid in the r-z plane. If
        voxel values are provided, this method plots the voxel grid coloured by the voxel intensities.

        :param str title: The title of the plot.
        :param np.ndarray voxel_values: A 1D numpy array with length equal to the number of voxels
          in the collection.
        :param ax: The matplotlib Axes object on which the plot will be made. If None, this function
          generates a new plot.
        :param float vmin: The minimum value for the colour map.
        :param float vmax: The maximum value for the colour map.
        :param cmap: The matplotlib colour map to use for colouring the voxel intensities.
        """

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
