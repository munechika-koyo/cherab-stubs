from collections.abc import Iterable, Iterator

from raysect.core.math import AffineMatrix3D, Vector3D
from raysect.core.scenegraph import Node, Primitive
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical.material.emitter import VolumeIntegrator

from ..atomic import AtomicData, Element
from ..plasma import Plasma
from ..utility.notify import Notifier as Notifier
from .model import BeamAttenuator, BeamModel

class ModelManager:
    notifier: Notifier
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[BeamModel]: ...
    def set(self, models: Iterable[BeamModel]) -> None: ...
    def add(self, model: BeamModel) -> None: ...
    def clear(self) -> None: ...

class Beam(Node):
    """
    A scene-graph object representing a Gaussian mono-energetic beam.

    The Cherab beam object holds all the properties and state of a mono-energetic
    particle beam to which beam attenuation and emission models may be attached.
    The Beam object is defined in terms of its power, energy, geometric properties
    and the plasma it interacts with.

    The Beam object is a Raysect scene-graph node and lives in it's own
    coordinate space. This coordinate space is defined relative to it's parent
    scene-graph object by an AffineTransform. The beam parameters are defined
    in the Beam object coordinate space. Models using the beam object must
    convert any spatial coordinates into beam space before requesting values
    from the Beam object. The Beam axis is defined to lie along the positive
    z-axis with its origin at the origin of the local coordinate system.

    While a Beam object can be used to simply hold and sample beam properties,
    it can also be used as an emitter in Raysect scenes by attaching
    emission models. The Beam's bounding geometry is automatically defined from
    the Beam's initial width and divergence. The length of the Beam geometry
    needs to be set by the user.

    Beam emission models may be attached to the beam
    object by either setting the full list of models or adding to the list of
    models. See the Beam's ModelManager for more information. The beam emission models
    must be derived from the BeamModel base class.

    Any change to the beam object properties and models
    will result in a automatic notification being sent to objects that register
    with the Beam objects' Notifier. All Cherab models and associated scene-graph
    objects automatically handle the notifications internally to clear
    cached data. If you need to keep track of beam changes in your own classes,
    a callback can be registered with the beam Notifier which will be called in
    the event of a change to the Beam object. See the Notifier documentation.

    .. warning::
       In the current implementation of the Beam class, the Beam can only be associated
       with a single plasma instance. If your scene has overlapping plasmas the
       beam attenuation will only be calculated for the plasma instance to which
       this beam is attached.

    :param Node parent: The parent node in the Raysect scene-graph.
      See the Raysect documentation for more guidance.
    :param AffineMatrix3D transform: The transform defining the spatial position
      and orientation of this beam. See the Raysect documentation if you need
      guidance on how to use AffineMatrix3D transforms.
    :param str name: The name for this beam object.

    :ivar AtomicData atomic_data: The atomic data provider class for this beam.
      All beam emission and attenuation rates will be calculated from the same provider.
    :ivar BeamAttenuator attenuator: The method used for calculating the attenuation
      of this beam into the plasma. Defaults to a SingleRayAttenuator().
    :ivar float divergence_x: The beam profile divergence in the x dimension in beam
      coordinates (degrees).
    :ivar float divergence_y: The beam profile divergence in the y dimension in beam
      coordinates (degrees).
    :ivar Element element: The element of which this beam is composed.
    :ivar float energy: The beam energy in eV/amu.
    :ivar VolumeIntegrator integrator: The configurable method for doing
      volumetric integration through the beam along a Ray's path. Defaults to
      a numerical integrator with 1mm step size, NumericalIntegrator(step=0.001).
    :ivar float length: The approximate length of this beam from source to extinction
      in the plasma. This is used for setting the bounding geometry over which calculations
      will occur. Units of m.
    :ivar ModelManager models: The manager class that sets and provides access to the
      emission models for this beam.
    :ivar Plasma plasma: The plasma instance with which this beam interacts.
    :ivar float power: The total beam power in W.
    :ivar float sigma: The Gaussian beam width at the origin in m.
    :ivar float temperature: The broadening of the beam (eV).


    .. code-block:: pycon

       >>> # This example shows how to initialise and populate a basic beam
       >>>
       >>> from raysect.core.math import Vector3D, translate, rotate
       >>> from raysect.optical import World
       >>>
       >>> from cherab.core.atomic import carbon, deuterium, Line
       >>> from cherab.core.model import BeamCXLine
       >>> from cherab.openadas import OpenADAS
       >>>
       >>>
       >>> world = World()
       >>>
       >>> beam = Beam(parent=world, transform=translate(1.0, 0.0, 0) * rotate(90, 0, 0))
       >>> beam.plasma = plasma  # put your plasma object here
       >>> beam.atomic_data = OpenADAS()
       >>> beam.energy = 60000
       >>> beam.power = 1e4
       >>> beam.element = deuterium
       >>> beam.sigma = 0.025
       >>> beam.divergence_x = 0.5
       >>> beam.divergence_y = 0.5
       >>> beam.length = 3.0
       >>> beam.models = [BeamCXLine(Line(carbon, 5, (8, 7)))]
       >>> beam.integrator.step = 0.001
       >>> beam.integrator.min_samples = 5
    """
    def __init__(self, parent: _NodeBase | None = None, transform: AffineMatrix3D | None = None, name: str | None = None) -> None: ...
    def density(self, x: float, y: float, z: float) -> float:
        """
        Returns the bean density at the specified position in beam coordinates.

        Note: this function is only defined over the domain 0 < z < beam_length.
        Outside of this range the density is clamped to zero.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Beam density in m^-3
        """
    def direction(self, x: float, y: float, z: float) -> Vector3D:
        r"""
        Calculates the beam direction vector at a point in beam coordinate space.

        The beam direction (non-normalised) is calculated as follows (z > 0):

        .. math::
            e_x = x\frac{(ztg(\alpha_x))^2}{\sigma^2 + (ztg(\alpha_x))^2},

            e_y = y\frac{(ztg(\alpha_y))^2}{\sigma^2 + (ztg(\alpha_y))^2},

            e_z = z,

        where :math:`\sigma` is the Gaussian beam deviation at origin,
        :math:`\alpha_x` and :math:`\alpha_y` are the beam divergence angles
        in the x and y dimensions respectively.

        For z <= 0 the beam direction is (0, 0, 1).

        The function returns normalised beam direction.

        Note the values of the beam outside of the beam envelope should be
        treated with caution.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Direction vector.
        """
    @property
    def energy(self) -> float: ...
    @energy.setter
    def energy(self, value: float) -> None: ...
    @property
    def power(self) -> float: ...
    @power.setter
    def power(self, value: float) -> None: ...
    @property
    def temperature(self) -> float: ...
    @temperature.setter
    def temperature(self, value: float) -> None: ...
    @property
    def element(self) -> Element | None: ...
    @element.setter
    def element(self, value: Element | None) -> None: ...
    @property
    def divergence_x(self) -> float: ...
    @divergence_x.setter
    def divergence_x(self, value: float) -> None: ...
    @property
    def divergence_y(self) -> float: ...
    @divergence_y.setter
    def divergence_y(self, value: float) -> None: ...
    @property
    def length(self) -> float: ...
    @length.setter
    def length(self, value: float) -> None: ...
    @property
    def sigma(self) -> float: ...
    @sigma.setter
    def sigma(self, value: float) -> None: ...
    @property
    def atomic_data(self) -> AtomicData | None: ...
    @atomic_data.setter
    def atomic_data(self, value: AtomicData | None) -> None: ...
    @property
    def plasma(self) -> Plasma | None: ...
    @plasma.setter
    def plasma(self, value: Plasma | None) -> None: ...
    @property
    def attenuator(self) -> BeamAttenuator | None: ...
    @attenuator.setter
    def attenuator(self, value: BeamAttenuator | None) -> None: ...
    @property
    def models(self) -> ModelManager: ...
    @models.setter
    def models(self, value: Iterable[BeamModel]) -> None: ...
    @property
    def integrator(self) -> VolumeIntegrator: ...
    @integrator.setter
    def integrator(self, value: VolumeIntegrator) -> None: ...
    def _configure_geometry(self) -> None: ...
    def _generate_geometry(self) -> Primitive:
        """
        Generate the bounding geometry for the beam model.

        Where possible the beam is bound by a cone as this offers the tightest
        fitting bounding volume. To avoid numerical issues caused by creating
        extremely long cones in low divergence cases, the geometry is switched
        to a cylinder where the difference in volume between the cone and a
        cylinder is less than 10%.

        :return: Beam geometry Primitive.
        """
    def _configure_attenuator(self) -> None: ...
