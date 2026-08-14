from collections.abc import Iterator, Mapping
from enum import Enum
from typing import ClassVar

import numpy as np
from numpy.typing import NDArray
from raysect.core import Node
from raysect.core.math import AffineMatrix3D, Point3D, Vector3D
from raysect.core.scenegraph import Primitive
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical.observer import Pipeline0D, Pipeline2D, SightLine, TargetedCCDArray, TargetedPixel

from ..inversions.voxels import VoxelCollection as VoxelCollection

R_2_PI: float

class _Units(Enum):
    POWER = "power"
    RADIANCE = "radiance"

class BolometerCamera(Node):
    """
    A group of bolometer sight-lines under a single scenegraph node.

    A scenegraph object that manages a collection of :class:`BolometerFoil`
    objects. Allows combined observation and display control simultaneously.

    :param Primitive camera_geometry: A Raysect primitive to supply as the
      box/aperture geometry.
    :param Node parent: The parent node of this camera in the scenegraph, often
      an optical World object.
    :param AffineMatrix3D transform: The relative coordinate transform of this
      bolometer camera relative to the parent.
    :param str name: The name for this bolometer camera.

    :ivar list foil_detectors: A list of the foil detector objects that belong
      to this camera.
    :ivar list slits: A list of the bolometer slit objects that belong to
      this camera.

    .. code-block:: pycon

       >>> from raysect.optical import World
       >>> from cherab.tools.observers import BolometerCamera
       >>>
       >>> world = World()
       >>> camera = BolometerCamera(name="MyBolometer", parent=world)
    """

    _foil_detectors: list[BolometerFoil]
    _slits: list[BolometerSlit]
    _camera_geometry: Primitive

    def __init__(
        self,
        camera_geometry: Primitive | None = None,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str = "",
    ) -> None: ...
    def __len__(self) -> int:
        """Yields the number of detectors in this bolometer camera."""
    def __iter__(self) -> Iterator[BolometerFoil]:
        """
        Iterates over the foil detectors in this camera.

        .. code-block:: pycon

           >>> detector_a, detector_b, detector_c = bolometer_camera
        """
    def __getitem__(self, item: int | str) -> BolometerFoil:
        """
        Returns the detectors by integer index or the detector name.

        .. code-block:: pycon

           >>> detector_2 = bolometer_camera[1]
           >>> detector_a = bolometer_camera["detector_a"]
        """
    @property
    def slits(self) -> list[BolometerSlit]: ...
    @property
    def foil_detectors(self) -> list[BolometerFoil]: ...
    @foil_detectors.setter
    def foil_detectors(self, value: list[BolometerFoil]) -> None: ...
    def add_foil_detector(self, foil_detector: BolometerFoil) -> None:
        """
        Add the given detector to this camera.

        :param (BolometerFoil, BolometerIRVB) foil_detector: An instanced bolometer foil detector.

        .. code-block:: pycon

           >>> bolometer_camera.add_foil_detector(foil_detector)
        """
    def observe(self) -> list[float]:
        """
        Take an observation with this camera.

        Calls observe() on each foil detector and returns their power measurements.
        """

class BolometerSlit(Node):
    """
    A rectangular bolometer slit.

    A single slit can be shared by multiple detectors in the parent camera. The slit
    geometry is specified in terms of its centre_point, basis vectors in the plane of
    the slit and their respective lengths. When instantiating a
    :class:`BolometerSlit` object these values are defined in the local coordinate
    system of the slit\'s parent, usually a :class:`BolometerCamera` object. Accessing
    these properties on an existing :class:`BolometerSlit` object returns them in the
    world\'s coordinate system.

    If an external mesh model has been loaded for ray occlusion evaluation then this
    object is only used for targeting rays on the slit. If no mesh has been supplied,
    this object can construct an effective slit primitive from CSG operations.

    .. warning::
       Be very careful when using a CSG aperture. The aperture geometry is slightly
       larger than the slit dx and dy, which can cause partial occlusion of
       nearby primitives. It also relies on no rays being launched with directions
       outside the solid angle of the aperture\'s bounding sphere: depending on the
       foil-slit distance and slit size, and also the foil\'s targeted_path_prob,
       this may not be guaranteed. Supplying a proper mesh geometry for the camera
       is recommended instead of using a CSG aperture.

    :param str slit_id: The name for this slit.
    :param Point3D centre_point: The centre point of the slit.
    :param Vector3D basis_x: The x basis vector for the slit.
    :param float dx: The width of the slit along the x basis vector.
    :param Vector3D basis_y: The y basis vector for the slit.
    :param float dy: The height of the slit along the y basis vector.
    :param float dz: The thickness of the slit along the z basis vector.
    :param Node parent: The parent scenegraph node to which this slit belongs.
      Typically a :class:`BolometerCamera` or an optical :class:`World` object.
    :param bool csg_aperture: Toggles whether an occluding surface should be
      constructed for this slit using CSG operations.
    :param float curvature_radius: Slits in real bolometer cameras may
      have curved corners due to machining limitations. This parameter species
      the corner radius.

    :ivar Vector3D normal_vector: The normal vector of the slit constructed from
      the cross product of the x and y basis vectors.

    .. code-block:: pycon

       >>> from raysect.core import Point3D, Vector3D
       >>> from raysect.optical import World
       >>> from cherab.tools.observers import BolometerSlit
       >>>
       >>> world = World()
       >>>
       >>> # construct basis vectors
       >>> basis_x = Vector3D(1, 0, 0)
       >>> basis_y = Vector3D(0, 1, 0)
       >>> basis_z = Vector3D(0, 0, 1)
       >>>
       >>> # specify the slit
       >>> dx = 0.0025
       >>> dy = 0.005
       >>> centre_point = Point3D(0, 0, 0)
       >>> slit = BolometerSlit("slit", centre_point, basis_x, dx, basis_y, dy, parent=camera)
    """

    _centre_point: Point3D
    _basis_x: Vector3D
    dx: float
    _basis_y: Vector3D
    dy: float
    dz: float
    _curvature_radius: float
    target: BolometerFoil
    _csg_aperture: bool
    def __init__(
        self,
        slit_id: str,
        centre_point: Point3D,
        basis_x: Vector3D,
        dx: float,
        basis_y: Vector3D,
        dy: float,
        dz: float = 0.001,
        parent: _NodeBase | None = None,
        csg_aperture: bool = False,
        curvature_radius: float = 0,
    ) -> None: ...
    @property
    def centre_point(self) -> Point3D: ...
    @property
    def normal_vector(self) -> Vector3D: ...
    @property
    def basis_x(self) -> Vector3D: ...
    @property
    def basis_y(self) -> Vector3D: ...
    @property
    def csg_aperture(self) -> bool: ...
    @csg_aperture.setter
    def csg_aperture(self, value: bool) -> None: ...
    @property
    def curvature_radius(self) -> float: ...

class BolometerFoil(TargetedPixel):
    """
    A rectangular foil bolometer detector.

    When instantiating a detector, the position and orientation
    (i.e. centre_point, basis_x and basis_y) are given in the local coordinate
    system of the foil\'s parent, usually a :class:`BolometerCamera` instance.
    When these properties are accessed after instantiation, they are given in
    the coordinate system of the world.

    :param str detector_id: The name for this detector.
    :param Point3D centre_point: The centre point of the detector.
    :param Vector3D basis_x: The x basis vector for the detector.
    :param float dx: The width of the detector along the x basis vector.
    :param Vector3D basis_y: The y basis vector for the detector.
    :param float dy: The height of the detector along the y basis vector.
    :param Node parent: The parent scenegraph node to which this detector belongs.
      Typically a :class:`BolometerCamera` or an optical :class:`World` object.
    :param str units: The units in which to perform observations, can
      be [\'Power\', \'Radiance\'].
    :param bool accumulate: Whether this observer should accumulate samples
      with multiple calls to observe.
    :param float curvature_radius: Detectors in real bolometer cameras typically
      have curved corners due to machining limitations. This parameter specifies
      the corner radius.

    :ivar Vector3D normal_vector: The normal vector of the detector constructed from
      the cross product of the x and y basis vectors.
    :ivar Vector3D sightline_vector: The vector that points from the centre of the foil
      detector to the centre of the slit. Defines the effective sightline vector of the
      detector.

    .. code-block:: pycon

       >>> from raysect.core import Point3D, Vector3D
       >>> from raysect.optical import World
       >>> from cherab.tools.observers import BolometerFoil
       >>>
       >>> world = World()
       >>>
       >>> # construct basis vectors
       >>> basis_x = Vector3D(1, 0, 0)
       >>> basis_y = Vector3D(0, 1, 0)
       >>> basis_z = Vector3D(0, 0, 1)
       >>>
       >>> # specify a detector, you need already created slit and camera objects
       >>> dx = 0.0025
       >>> dy = 0.005
       >>> centre_point = Point3D(0, 0, -0.08)
       >>> detector = BolometerFoil("ch#1", centre_point, basis_x, dx, basis_y, dy, slit, parent=camera)
    """

    _slit: BolometerSlit
    _curvature_radius: float
    _accumulate: bool
    def __init__(
        self,
        detector_id: str,
        centre_point: Point3D,
        basis_x: Vector3D,
        dx: float,
        basis_y: Vector3D,
        dy: float,
        slit: BolometerSlit,
        parent: _NodeBase | None = None,
        units: str = "Power",
        accumulate: bool = False,
        curvature_radius: float = 0,
    ) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of this BolometerFoil object."""
    @property
    def centre_point(self) -> Point3D: ...
    @property
    def normal_vector(self) -> Vector3D: ...
    @property
    def basis_x(self) -> Vector3D: ...
    @property
    def basis_y(self) -> Vector3D: ...
    @property
    def sightline_vector(self) -> Vector3D: ...
    @property
    def slit(self) -> BolometerSlit: ...
    @property
    def curvature_radius(self) -> float: ...
    _units: _Units
    pipelines: list[Pipeline0D]
    @property
    def units(self) -> str: ...
    @units.setter
    def units(self, units: str) -> None: ...
    @property
    def accumulate(self) -> bool: ...
    @accumulate.setter
    def accumulate(self, value: bool) -> None: ...
    def as_sightline(self) -> SightLine:
        """
        Constructs a SightLine observer for this bolometer.

        :rtype: SightLine
        """
    def trace_sightline(self) -> tuple[Point3D, Point3D, Primitive]:
        """
        Traces the central sightline through the detector to see where the sightline terminates.

        Raises a RuntimeError exception if no intersection was found.

        :return: A tuple containing the origin point, hit point and terminating surface
          primitive.
        """
    min_wavelength: float
    max_wavelength: float
    spectral_bins: int
    pixel_samples: int
    def calculate_sensitivity(self, voxel_collection: VoxelCollection, ray_count: int = 10000) -> NDArray[np.float64]:
        """
        Calculates a sensitivity vector for this detector on the specified voxel collection.

        This function is used for calculating sensitivity matrices which can be
        combined for multiple detectors into a sensitivity matrix
        :math:`\\mathbf{W}`. If the :class:`BolometerFoil` has units of "Power", the
        returned sensitivity matrix has units of [m³ sr]. If the
        :class:`BolometerFoil` has units of "Radiance", the returned sensitivity
        matrix has units of [m sr].

        :param VoxelCollection voxel_collection: The voxel collection on which to calculate
          the sensitivities.
        :param int ray_count: The number of rays to use in the calculation. This should be
          at least >= 10000 for decent statistics.
        :return: A 1D array of sensitivities with length equal to the number of voxels
          in the collection.
        """
    def calculate_etendue(self, ray_count: int = 10000, batches: int = 10, max_distance: float = np.inf) -> tuple[float, float]:
        """
        Calculates the etendue of this detector.

        This function calculates the detectors etendue by evaluating the fraction of rays that
        pass un-impeded through the detector's aperture.

        :param int ray_count: The number of rays used per batch.
        :param int batches: The number of batches used to estimate the error on the etendue calculation.
        :param float max_distance: The maximum distance from the detector to consider intersections.
            If a ray makes it further than this, it is assumed to have passed through the aperture,
            regardless of what it hits. Use this if there are other primitives present in the scene
            which do not form the aperture.
        :return: A tuple (etendue, etendue_error).
        """

class BolometerIRVB(TargetedCCDArray):
    """
    A rectangular infra red video bolometer (IRVB).

    Can be configured to sample a single ray per pixel, or fan of rays
    oriented along the observer\'s z axis.

    :param str name: The name for this detector.
    :param float width: The width of the detector along the x basis vector.
    :param tuple pixels: The number of pixels to divide the foil into.
      Pixels are square, so the height of the foil is determined by the
      width of the foil and the number of rows and columns of pixels.
    :param BolometerSlit slit: The slit the IRVB views through.
    :param AffineMatrix3D transform: The foil\'s transform relative to its parent.
    :param Node parent: The parent scenegraph node to which this detector belongs.
      Typically a BolometerCamera() or an optical World() object.
    :param bool units: The units in which to perform observations, can
      be [\'power\', \'radiance\'], defaults to \'power\'.
    :param bool accumulate: Whether this observer should accumulate samples
      with multiple calls to observe. Defaults to False.
    :param float curvature_radius: Detectors in real bolometer cameras may
      have curved corners due to machining limitations. This parameter species
      the corner radius.

    :ivar Vector3D normal_vector: The normal vector of the detector constructed from
      the cross product of the x and y basis vectors.
    :ivar float width: The extent of the bolometer foil in the basis_x direction.
    :ivar float height: The extent of the bolometer foil in the basis_y direction.
    :ivar array pixels_as_foils: A 2D array of pixels as individual BolometerFoil objects,
      useful for calling BolometerFoil methods on each pixel (e.g. sightline tracing).
      The array is indexed by (column, row).
    :ivar Vector3D sightline_vectors: A 2D array of vectors that point from the centre
      of each pixel on the foil detector to the centre of the slit. Defines the
      effective sightline vectors of the pixels of the detector. The array is indexed by
      (column, row).

    .. code-block:: pycon

       >>> from raysect.core import Point3D, Vector3D, translate, rotate_basis
       >>> from raysect.optical import World
       >>> from cherab.tools.observers import BolometerIRVB
       >>>
       >>> world = World()
       >>>
       >>> # construct transform, relative to parent\'s transform
       >>> centre_point = Point3D(0, 0, -0.08)
       >>> basis_x = Vector3D(1, 0, 0)
       >>> basis_y = Vector3D(0, 1, 0)
       >>> normal = basis_x.cross(basis_y)
       >>> transform = translate(*centre_point) * rotate_basis(normal, basis_y)
       >>>
       >>> # specify a detector, you need already created slit and camera objects
       >>> width = 0.0025
       >>> pixels = (10, 20)
       >>> detector = BolometerIRVB("irvb", width, pixels, slit, transform, parent=camera)
    """

    _PIPELINES: ClassVar[Mapping[_Units, type[Pipeline2D]]]
    _SPECTRAL_PIPELINES: ClassVar[Mapping[_Units, type[Pipeline2D]]]
    _slit: BolometerSlit
    _curvature_radius: float
    _accumulate: bool
    pixel_samples: int
    spectral_bins: int
    quiet: bool
    def __init__(
        self,
        name: str,
        width: float,
        pixels: tuple[int, int],
        slit: BolometerSlit,
        transform: AffineMatrix3D | None,
        parent: _NodeBase | None = None,
        units: str = "power",
        accumulate: bool = False,
        curvature_radius: float = 0,
    ) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of this BolometerIRVB object."""
    @property
    def pixels_as_foils(self) -> NDArray[np.object_]: ...
    @property
    def height(self) -> float: ...
    @property
    def centre_point(self) -> Point3D: ...
    @property
    def normal_vector(self) -> Vector3D: ...
    @property
    def basis_x(self) -> Vector3D: ...
    @property
    def basis_y(self) -> Vector3D: ...
    @property
    def sightline_vectors(self) -> NDArray[np.object_]: ...
    @property
    def slit(self) -> BolometerSlit: ...
    @property
    def curvature_radius(self) -> float: ...
    _units: _Units
    pipelines: list[Pipeline2D]
    @property
    def units(self) -> str: ...
    @units.setter
    def units(self, units: str) -> None: ...
    @property
    def accumulate(self) -> bool: ...
    @accumulate.setter
    def accumulate(self, value: bool) -> None: ...
    def as_sightlines(self) -> NDArray[np.object_]:
        """
        Constructs a SightLine observer for each pixel in this bolometer.

        :return: A 2D array of Sightline objects.
        """
    def trace_sightlines(self) -> NDArray[np.object_]:
        """
        Trace the central sightlines through each pixel in the detector
        to see where the sightline terminates.

        Raises a RuntimeError exception if no intersections were found.

        :return: A 2D array of tuples containing the origin point, hit
          point and terminating surface primitive for each pixel.
        """
    min_wavelength: float
    max_wavelength: float
    def calculate_sensitivity(self, voxel_collection: VoxelCollection, ray_count: int | None = None) -> NDArray[np.float64]:
        """
        Calculates a sensitivity vector for this detector on the specified voxel collection.

        This function is used for calculating sensitivity matrices which can be combined for
        multiple detectors into a sensitivity matrix :math:`\\mathbf{W}`.

        :param VoxelCollection voxel_collection: The voxel collection on which to calculate
          the sensitivities.
        :param int ray_count: The number of rays to use in the calculation. This should be
          at least >= 10000 for decent statistics. Default is 10000.
        :return: A 3D array of sensitivities (ncol, nrow, nvoxels)
        """
    def calculate_etendue(
        self,
        ray_count: int | None = None,
        batches: int | None = None,
        max_distance: float | None = None,
    ) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
        """
        Calculates the etendue of each pixel in this detector.

        This function calculates the detector etendue by evaluating the ratio of rays that
        pass un-impeded through the detector's aperture. For this method to work, the detector
        and its aperture structures should be the only primitives present in the scene. If any
        other primitives are present, the results may be misleading.

        :param int ray_count: The number of rays used per batch (default 10000).
        :param int batches: The number of batches used to estimate the error on the etendue
          calculation. Default is 10.
        :param float max_distance: The maximum distance from the detector to consider intersections.
            If a ray makes it further than this, it is assumed to have passed through the aperture,
            regardless of what it hits. Use this if there are other primitives present in the scene
            which do not form the aperture. Default is infinity (no max distance).
        :return: a tuple (etendue, etendue_error), each of which is a 2D
          array of size (ncol, nrow)
        """

def mask_corners(element: BolometerSlit | BolometerFoil | BolometerIRVB) -> None:
    """
    Support detectors with rounded corners, by producing a mask to cover
    the corners.

    The mask is produced by cutting a rounded rectangle, formed of the
    union of two smaller perpendicular rectangles and four cylinders,
    from a rectangle the same size as the detector.

    The curvature radius should be given in units of metres.
    """
