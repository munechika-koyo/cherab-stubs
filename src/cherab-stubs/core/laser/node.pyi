from collections.abc import Iterable, Iterator

from raysect.core.math import AffineMatrix3D
from raysect.core.scenegraph import Node, Primitive
from raysect.core.scenegraph._nodebase import _NodeBase
from raysect.optical.material.emitter import VolumeIntegrator

from ..plasma import Plasma
from ..utility.notify import Notifier as Notifier
from .laserspectrum import LaserSpectrum
from .model import LaserModel
from .profile import LaserProfile

class ModelManager:
    notifier: Notifier
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[LaserModel]: ...
    def set(self, models: Iterable[LaserModel]) -> None: ...
    def add(self, model: LaserModel) -> None: ...
    def clear(self) -> None: ...

class Laser(Node):
    """
    A scene-graph object representing a laser of laser light.

    The Cherab laser object holds basic information about the laser and connects
    the components which are needed for the laser description. With specified
    emission models it can contribute to observed radiation.

    The Laser object is a Raysect scene-graph node and lives in it's own
    coordinate space. This coordinate space is defined relative to it's parent
    scene-graph object by an AffineTransform. The beam parameters are defined
    in the Laser object coordinate space. Models using the beam object must
    convert any spatial coordinates into beam space before requesting values
    from the Laser object.

    The main physical properties of the laser are defined by the three
    attributes laser_spectrum, laser_profile and models. The laser_spectrum
    has to be an instance of LaserSpectrum and defines the spectral properties
    of the laser light. The laser_profile has to be an instance of LaserProfile
    and it holds all the space related definitions as volumetric distribution
    of laser light energy polarisation direction. In the models a list of LaserModels
    can be stored, which calculate the contribution of the laser light to the observed
    radiation. The models can cover various applications as for example
    Thomson scattering. Please see the documentation of individual classes
    for more detail.

    The shape of the laser (e.g. cylinder) and its parameters (e.g. radius)
    is controlled by the LaserProfile.

    The plasma reference has to be specified to attach the any models.

    :param Node parent: The parent node in the Raysect scene-graph.
      See the Raysect documentation for more guidance.
    :param AffineMatrix3D transform: The transform defining the spatial position
      and orientation of this laser. See the Raysect documentation if you need
      guidance on how to use AffineMatrix3D transforms.
    :param str name: The name for this laser object.
    :ivar Plasma plasma: The plasma instance with which this laser interacts.
    :ivar float importance: The importance sampling factor.
    :ivar LaserSpectrum laser_spectrum: The LaserSpectrum instance with which this laser interacts.
    :ivar LaserProfile laser_profile: The LaserProfile instance with which this laser interacts.
    :ivar ModelManager models: The manager class that sets and provides access to the
      emission models for this laser.
    :ivar VolumeIntegrator integrator: The configurable method for doing
      volumetric integration through the laser along a Ray's path. Defaults to
      a numerical integrator with 1mm step size, NumericalIntegrator(step=0.001).
    """

    notifier: Notifier
    def __init__(self, parent: _NodeBase | None = None, transform: AffineMatrix3D | None = None, name: str | None = None) -> None: ...
    def _set_init_values(self) -> None:
        """
        Sets initial values of the laser shape to avoid errors.
        """
    @property
    def plasma(self) -> Plasma | None: ...
    @plasma.setter
    def plasma(self, value: Plasma | None) -> None: ...
    @property
    def importance(self) -> float: ...
    @importance.setter
    def importance(self, value: float) -> None: ...
    @property
    def laser_spectrum(self) -> LaserSpectrum | None: ...
    @laser_spectrum.setter
    def laser_spectrum(self, value: LaserSpectrum | None) -> None: ...
    @property
    def laser_profile(self) -> LaserProfile | None: ...
    @laser_profile.setter
    def laser_profile(self, value: LaserProfile | None) -> None: ...
    @property
    def models(self) -> ModelManager: ...
    @models.setter
    def models(self, value: Iterable[LaserModel]) -> None: ...
    @property
    def integrator(self) -> VolumeIntegrator: ...
    @integrator.setter
    def integrator(self, value: VolumeIntegrator) -> None: ...
    def configure_geometry(self) -> None:
        """
        Reconfigure the laser primitives and materials.
        """
    def _build_geometry(self) -> None:
        """
        Delete and build new laser segments
        """
    def _configure_materials(self) -> None:
        """
        Configure laser segment materials
        """
    def get_geometry(self) -> list[Primitive]: ...
    def _plasma_changed(self) -> None:
        """React to change of plasma and propagate the information."""
    def _modified(self) -> None: ...
