from abc import abstractmethod

from raysect.core.math import Vector3D
from raysect.core.math.function.float import Function3D
from raysect.core.math.function.vector3d import Function3D as VectorFunction3D

class DistributionFunction:
    """
    The distribution function base class.

    All plasma Species objects are defined through distribution functions. This base
    class defines the core interface which is used by the rest of the framework.
    This base class cannot be used on its own, it raises a NotImplementedError() on all
    method calls. Users should either use a simpler distribution instance
    (such as the Maxwellian distribution) or implement their own.
    """

    def __init__(self) -> None: ...
    def __call__(self, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> float:
        """
        Evaluate the phase space density at the specified point in 6D phase space.

        Wraps the cython evaluate() function for fast evaluation.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :param float vx: velocity in meters per second
        :param float vy: velocity in meters per second
        :param float vz: velocity in meters per second
        :return: phase space density in s^3/m^6
        """

    @abstractmethod
    def bulk_velocity(self, x: float, y: float, z: float) -> Vector3D:
        """
        Evaluate the species' bulk velocity at the specified 3D coordinate.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: velocity vector in m/s
        :rtype: Vector3D
        """

    @abstractmethod
    def effective_temperature(self, x: float, y: float, z: float) -> float:
        """
        Evaluate the species' effective temperature at the specified 3D coordinate.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: temperature in eV
        :rtype: float
        """

    @abstractmethod
    def density(self, x: float, y: float, z: float) -> float:
        """
        Evaluate the species' density at the specified 3D coordinate.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: density in m^-3
        :rtype: float
        """

class ZeroDistribution(DistributionFunction):
    """
    A zero distribution function.

    All distribution properties are zero.
    """

    def __init__(self) -> None: ...
    def __call__(self, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> float:
        """
        Evaluate the phase space density at the specified point in 6D phase space.

        Wraps the cython evaluate() function for fast evaluation.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :param float vx: velocity in meters per second
        :param float vy: velocity in meters per second
        :param float vz: velocity in meters per second
        :return: phase space density 0 s^3/m^6
        """

    def bulk_velocity(self, x: float, y: float, z: float) -> Vector3D:
        """
        Evaluate the species' bulk velocity at the specified 3D coordinate.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: velocity vector (0, 0, 0) in m/s
        :rtype: Vector3D
        """

    def effective_temperature(self, x: float, y: float, z: float) -> float:
        """
        Return 0 species' effective temperature at the specified 3D coordinate.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: temperature 0 eV
        :rtype: float
        """

    def density(self, x: float, y: float, z: float) -> float:
        """
        Return 0 species' density.

        :param float x: position in meters
        :param float y: position in meters
        :param float z: position in meters
        :return: density 0 m^-3
        :rtype: float
        """

class Maxwellian(DistributionFunction):
    """
    A Maxwellian distribution function.

    This class implements a Maxwell-Boltzmann distribution, the statistical distribution
    describing a system of particles that have reached thermodynamic equilibrium. The
    user supplies 3D functions that provide the mean density, temperature and velocity
    respectively.

    :param Function3D density: 3D function defining the density in cubic meters.
    :param Function3D temperature: 3D function defining the temperature in eV.
    :param VectorFunction3D velocity: 3D vector function defining the bulk velocity in meters per second.
    :param double atomic_mass: Atomic mass of the species in kg.

    .. code-block:: pycon

       >>> from scipy.constants import atomic_mass
       >>> from raysect.core.math import Vector3D
       >>> from cherab.core import Maxwellian
       >>> from cherab.core.atomic import deuterium
       >>>
       >>> # Setup distribution for a slab of plasma in thermodynamic equilibrium
       >>> d0_density = 1e17
       >>> d0_temperature = 1
       >>> bulk_velocity = Vector3D(0, 0, 0)
       >>> d0_distribution = Maxwellian(
       ...     d0_density, d0_temperature, bulk_velocity, deuterium.atomic_weight * atomic_mass
       ... )
    """

    _density: Function3D
    _temperature: Function3D
    _velocity: VectorFunction3D
    _atomic_mass: float

    def __init__(self, density: object, temperature: object, velocity: object, atomic_mass: float) -> None: ...
    def bulk_velocity(self, x: float, y: float, z: float) -> Vector3D:
        """
        Evaluate the species' bulk velocity at the specified 3D coordinate.

        :param x: position in meters
        :param y: position in meters
        :param z: position in meters
        :return: velocity vector in m/s

        .. code-block:: pycon

           >>> d0_distribution.bulk_velocity(1, 0, 0)
           Vector3D(0.0, 0.0, 0.0)
        """

    def effective_temperature(self, x: float, y: float, z: float) -> float:
        """
        Evaluate the species' effective temperature at the specified 3D coordinate.

        :param x: position in meters
        :param y: position in meters
        :param z: position in meters
        :return: temperature in eV

        .. code-block:: pycon

           >>> d0_distribution.effective_temperature(1, 0, 0)
           1.0
        """

    def density(self, x: float, y: float, z: float) -> float:
        """
        Evaluate the species' density at the specified 3D coordinate.

        :param x: position in meters
        :param y: position in meters
        :param z: position in meters
        :return: density in m^-3

        .. code-block:: pycon

           >>> d0_distribution.density(1, 0, 0)
           1e+17
        """
