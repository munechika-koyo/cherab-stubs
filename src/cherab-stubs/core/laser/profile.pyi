from collections.abc import Callable

from raysect.core.math import Vector3D
from raysect.core.math.function.float import Function3D
from raysect.core.math.function.vector3d import Function3D as VectorFunction3D
from raysect.primitive import Cylinder

from ..utility.notify import Notifier as Notifier

class LaserProfile:
    """
    LaserProfile base class.

    This is an abstract class and cannot be used for observing.

    Provides information about spatial properties of the laser beam:
    direction of the laser propagation (direction
    of the Poynting vector), polarisation of the light as the direction
    of the electric component vector and volumetric energy density of
    the laser light.

    All the laser properties are evaluated in the frame of reference of
    the laser.

    .. warning::
        When combining a LaserProfile with a LaserSpectrum for a laser,
        a special care has to be given to obtain the correct power
        of the scattered spectrum. Scattering models can multiply
        both the spectral power density given by the LaserProfile and
        the volumetric energy density given by the LaserProfile.
        Combination of incompatible cases may yield incorrect
        values of scattered power.

    :ivar Laser laser: The Laser scenegraph node the LaserProfile
      is connected to.
    """

    notifier: Notifier
    def __init__(self) -> None: ...
    def set_polarization_function(self, function: VectorFunction3D | Callable[[float, float, float], Vector3D]) -> None:
        """
        Assigns the 3D vector function describing the polarisation vector.

        The polarisation is given as the direction of the electric
        component of the electromagnetic wave.

        The function is specified in the laser space.

        :param VectorFunction3D function: A 3D vector function describing
          the polarisation vector.
        """
    def set_pointing_function(self, function: VectorFunction3D | Callable[[float, float, float], Vector3D]) -> None:
        """
        Assigns the 3D vector function describing the direction of the laser propagation.

        The direction of the laser light propagation is the direction
        of the Poynting vector.

        :param VectorFunction3D function: A 3D vector function describing
          the laser light propagation direction
        """
    def set_energy_density_function(self, function: Function3D | Callable[[float, float, float], float]) -> None:
        """
        Assigns the 3D scalar function describing the laser energy distribution.

        The laser power distribution is the value of the volumetric
        energy density of the laser light.
        """
    def get_pointing(self, x: float, y: float, z: float) -> Vector3D:
        """
        Returns the laser light propagation direction.

        At the point (x, y, z) in the laser space.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: Intensity in m^-3.
        """
    def get_polarization(self, x: float, y: float, z: float) -> Vector3D:
        """
        Returns a vector denoting the laser polarisation.

        The polarisation direction is the direction of the electric
        component of the electromagnetic wave for the point (x, y, z)
        in the laser space.

        :param x: x coordinate in meters.
        :param y: y coordinate in meters.
        :param z: z coordinate in meters.
        :return: power density in Wm^-3.
        """
    def get_energy_density(self, x: float, y: float, z: float) -> float:
        """
        Returns the volumetric energy density of the laser light in W*m^-3.

        At the point (x, y, z) in the laser space.

        :param x: x coordinate in meters in the laser frame.
        :param y: y coordinate in meters in the laser frame.
        :param z: z coordinate in meters in the laser frame.
        :return: power density in W*m^-3.
        """
    def generate_geometry(self) -> list[Cylinder]:
        """
        returns list of raysect primitives composing the laser geometry

        This method is called from the Laser instance to which the instance
        of Profile is attached to. The Laser instance will be assigned as
        the parent to the returned primitives in the Laser._configure method.
        The Laser._configure method does not change any transforms. This is
        why the returned primitives have to have their transforms already
        initialised in the frame of the laser, when returned.
        """
    def _change(self) -> None:
        """
        Called if the laser properties change.

        If the model caches calculation data that would be invalidated if its
        source data changes then this method may be overridden to clear the
        cache.
        """
