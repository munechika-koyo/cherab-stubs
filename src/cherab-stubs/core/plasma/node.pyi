from collections.abc import Iterator

from raysect.core.math.function.vector3d import Function3D as VectorFunction3D
from raysect.core.scenegraph import Node, Primitive
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical import AffineMatrix3D, Vector3D
from raysect.optical.material.emitter import VolumeIntegrator
from raysect.optical.material.emitter.inhomogeneous import NumericalIntegrator

from ..atomic import AtomicData
from ..atomic.elements import Element
from ..distribution import DistributionFunction
from ..species import Species
from ..utility import Notifier
from .model import PlasmaModel

DEFAULT_INTEGRATOR = NumericalIntegrator(step=0.001)

class Composition:
    """
    The plasma composition manager.

    Used to control the adding and removing of Species objects from the Plasma object.
    This is because there can only ever be one Species object instance for each plasma
    species of a given element and charge state. Users never instantiate this class
    directly. Its always used indirectly through an instantiated Plasma object.
    """

    _species: dict[tuple[Element, int], Species]
    notifier: Notifier

    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Species]:
        """
        Iterate over all the Species objects in the parent plasma.

        .. code-block:: pycon

           >>> [species for species in plasma.composition]
           [<Species: element=deuterium, charge=0>,
            <Species: element=deuterium, charge=1>]
        """

    def __getitem__(self, item: tuple[Element, int]) -> Species:
        """
        Species objects can be indexed with a tuple specifying their element and charge state.

        .. code-block:: pycon

           >>> plasma.composition[(deuterium, 0)]
           <Species: element=deuterium, charge=0>
        """

    def set(self, species: list[Species]) -> None:
        """
        Replace the species in the composition with a new list of species.

        If there are multiple species with the same element and charge state in
        the list, only the last species with that specification will be added
        to the composition.

        :param Species species: A list containing the new species.

        .. code-block:: pycon

           >>> d0_species = Species(deuterium, 0, d0_distribution)
           >>> d1_species = Species(deuterium, 1, d1_distribution)
           >>> plasma.composition.set([d0_species, d1_species])
           >>> [species for species in plasma.composition]
           [<Species: element=deuterium, charge=0>,
            <Species: element=deuterium, charge=1>]
        """

    def add(self, species: Species) -> None:
        """
        Add a species to the plasma composition.

        Replaces any existing species with the same element and charge
        state already in the composition.

        :param Species species: A Species object.

        .. code-block:: pycon

           >>> d1_species = Species(deuterium, 1, d1_distribution)
           >>> plasma.composition.add(d1_species)
        """

    def get(self, element: Element, charge: int) -> Species:
        """
        Get a specified plasma species.

        Raises a ValueError if the specified species is not found in the composition.

        :param Element element: The element object of the requested species.
        :param int charge: The charge state of the requested species.
        :return: The requested Species object.

        .. code-block:: pycon

           >>> plasma.composition.get(deuterium, 1)
           <Species: element=deuterium, charge=1>
        """

    def clear(self) -> None:
        """Remove all Species object instances from the parent plasma."""

class ModelManager:
    _models: list[PlasmaModel]
    notifier: Notifier

    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[PlasmaModel]: ...
    def set(self, models: list[PlasmaModel]) -> None: ...
    def add(self, model: PlasmaModel) -> None: ...
    def clear(self) -> None: ...

class Plasma(Node):
    """
    A scene-graph object representing a plasma.

    The Cherab Plasma object holds all the properties and state of a plasma
    and can optionally have emission models attached to it.

    To define a Plasma object you need to define the plasma composition,
    magnetic field and electron distribution. The Plasma composition consists
    of a collection of Species objects that define the individual distribution
    functions of specific neutral atoms or ions in the plasma. Each individual
    species can only appear once in the composition. For more information see
    the related objects, Species, Composition, and DistributionFunction. To
    define the magnetic field you must provide a function that returns a
    magnetic field vector at the requested coordinate in the local plasma
    coordinate system.

    The Plasma object is a Raysect scene-graph Node and lives in it's own
    coordinate space. This coordinate space is defined relative to it's parent
    scene-graph object by an AffineTransform. The plasma parameters are defined
    in the Plasma object coordinate space. Models using the plasma object must
    convert any spatial coordinates into plasma space before requesting values
    from the Plasma object.

    While a Plasma object can be used to simply hold and sample plasma properties,
    it can also be used as an emitter in Raysect scenes by attaching geometry
    and emission models. To add emission models you first need to define a
    bounding geometry for the plasma. The geometry is described by a Raysect
    Primitive. The Primitive may be positioned relative to the plasma coordinate
    system by setting the geometry_transform attribute. If no geometry transform
    is set, the Primitive will share the same coordinate system as the
    plasma.

    Once geometry is defined, plasma emission models may be attached to the plasma
    object by either setting the full list of models or adding to the list of
    models. See the ModelManager for more information. The plasma emission models
    must be derived from the PlasmaModel base class.

    Any change to the plasma object including adding/removing of species or models
    will result in a automatic notification being sent to objects that register
    with the Plasma objects' Notifier. All Cherab models and associated scene-graph
    objects such as Beams automatically handle the notifications internally to clear
    cached data. If you need to keep track of plasma changes in your own classes,
    a callback can be registered with the plasma Notifier which will be called in
    the event of a change to the plasma object. See the Notifier documentation.

    :param Node parent: The parent node in the Raysect scene-graph.
      See the Raysect documentation for more guidance.
    :param AffineMatrix3D transform: The transform defining the spatial position
      and orientation of this plasma. See the Raysect documentation if you need
      guidance on how to use AffineMatrix3D transforms.
    :param str name: The name for this plasma.
    :param VolumeIntegrator integrator: The configurable method for doing
      volumetric integration through the plasma along a Ray's path. Defaults to
      a numerical integrator with 1mm step size, NumericalIntegrator(step=0.001).

    :ivar AtomicData atomic_data: The atomic data provider class for this plasma.
      All plasma emission from this plasma will be calculated with the same provider.
    :ivar VectorFunction3D b_field: A vector function in 3D space that returns the
      magnetic field vector at any requested point.
    :ivar Composition composition: The composition object manages all the atomic plasma
      species and provides access to their distribution functions.
    :ivar DistributionFunction electron_distribution: A distribution function object
      describing the electron species properties.
    :ivar Primitive geometry: The Raysect primitive that defines the geometric extent
      of this plasma.
    :ivar AffineMatrix3D geometry_transform: The relative difference between the plasmas'
      local coordinate system and the bounding geometries' local coordinate system. Defaults
      to a Null transform.
    :ivar ModelManager models: The manager class that sets and provides access to the
      emission models for this plasma.


    .. code-block:: pycon

       >>> # This example shows how to initialise and populate a basic plasma
       >>>
       >>> from scipy.constants import atomic_mass, electron_mass
       >>> from raysect.core.math import Vector3D
       >>> from raysect.primitive import Sphere
       >>> from raysect.optical import World
       >>>
       >>> from cherab.core import Plasma, Species, Maxwellian
       >>> from cherab.core.atomic import deuterium
       >>> from cherab.openadas import OpenADAS
       >>>
       >>>
       >>> world = World()
       >>>
       >>> # create atomic data source
       >>> adas = OpenADAS(permit_extrapolation=True)
       >>>
       >>>
       >>> # Setup basic distribution functions for the species
       >>> d0_density = 1e17
       >>> d0_temperature = 1
       >>> bulk_velocity = Vector3D(0, 0, 0)
       >>> d0_distribution = Maxwellian(
       ...     d0_density, d0_temperature, bulk_velocity, deuterium.atomic_weight * atomic_mass
       ... )
       >>> d0_species = Species(deuterium, 0, d0_distribution)
       >>>
       >>> d1_density = 1e18
       >>> d1_temperature = 10
       >>> d1_distribution = Maxwellian(
       ...     d1_density, d1_temperature, bulk_velocity, deuterium.atomic_weight * atomic_mass
       ... )
       >>> d1_species = Species(deuterium, 1, d1_distribution)
       >>>
       >>> e_distribution = Maxwellian(1e18, 9.0, bulk_velocity, electron_mass)
       >>>
       >>> # Initialise Plasma object and populate with species specifications
       >>> plasma = Plasma(parent=world)
       >>> plasma.atomic_data = adas
       >>> plasma.geometry = Sphere(2.0)
       >>> plasma.b_field = Vector3D(1.0, 1.0, 1.0)
       >>> plasma.composition = [d0_species, d1_species]
       >>> plasma.electron_distribution = e_distribution
    """

    notifier: Notifier
    _b_field: VectorFunction3D
    _electrin_distribution: DistributionFunction
    _composition: Composition
    _atomic_data: AtomicData
    _geometry: Primitive
    _geometry_transform: AffineMatrix3D
    _integrator: VolumeIntegrator
    _models: ModelManager

    def __init__(
        self,
        parent: _NodeBase | None = None,
        transform: AffineMatrix3D | None = None,
        name: str | None = None,
        integrator: VolumeIntegrator | None = DEFAULT_INTEGRATOR,
    ) -> None: ...
    @property
    def b_field(self) -> VectorFunction3D: ...
    @b_field.setter
    def b_field(self, value: VectorFunction3D | Vector3D) -> None: ...
    @property
    def electron_distribution(self) -> DistributionFunction: ...
    @electron_distribution.setter
    def electron_distribution(self, value: DistributionFunction | None) -> None: ...
    @property
    def composition(self) -> Composition: ...
    @composition.setter
    def composition(self, values: list[Species]) -> None: ...
    def z_effective(self, x: float, y: float, z: float) -> float:
        r"""
        Calculate the effective Z of the plasma.

        .. math::
            Z_{eff} = \sum_{j=1}^N n_{i(j)} Z_j^2 / \sum_{k=1}^N n_{i(k)} Z_k

        where n is the species density and Z is the ionisation of the species.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Calculated Z effective.
        :raises ValueError: If plasma does not contain any ionised species.

        .. code-block:: pycon

            >>> # With an already initialised plasma object...
            >>> plasma.z_effective(1, 1, 1)
            1.0
        """

    def ion_density(self, x: float, y: float, z: float) -> float:
        r"""
        Calculate the total ion density of the plasma.

        .. math::
            n_I = \sum_{k=1}^N n_i(k)

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Total ion density in m^-3.

        .. code-block:: pycon

           >>> # With an already initialised plasma object...
           >>> plasma.ion_density(1, 1, 1)
           1.1e+18
        """

    @property
    def geometry(self) -> Primitive: ...
    @geometry.setter
    def geometry(self, value: Primitive) -> None: ...
    @property
    def geometry_transform(self) -> AffineMatrix3D: ...
    @geometry_transform.setter
    def geometry_transform(self, value: AffineMatrix3D) -> None: ...
    @property
    def integrator(self) -> VolumeIntegrator: ...
    @integrator.setter
    def integrator(self, value: VolumeIntegrator) -> None: ...
    @property
    def models(self) -> ModelManager: ...
    @models.setter
    def models(self, values: ModelManager) -> None: ...
    @property
    def atomic_data(self) -> AtomicData: ...
    @atomic_data.setter
    def atomic_data(self, value: AtomicData) -> None: ...
    def _configure_geometry(self) -> None: ...
    def _modified(self) -> None:
        """
        Called when a scene-graph change occurs that modifies this Node's root
        transforms. This will occur if the Node's transform is modified, a
        parent node transform is modified or if the Node's section of scene-
        graph is re-parented.
        """
