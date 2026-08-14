from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ..plasma import Plasma
from .laserspectrum import LaserSpectrum
from .profile import LaserProfile

class LaserModel:
    """
    Laser spectrum base class.

    This is an abstract class and cannot be used for observing.

    Calculates the contribution to a spectrum caused by a laser.

    :param laser_profile: LaserProfile object
    :param plasma: Plasma object
    :param laser_spectrum: LaserSpectrum object

    :ivar laser_profile: LaserProfile object
    :ivar plasma: Plasma object
    :ivar laser_spectrum: LaserSpectrum object
    """
    def __init__(self) -> None: ...
    def emission(
        self,
        point_plasma: Point3D,
        observation_plasma: Vector3D,
        point_laser: Point3D,
        observation_laser: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
    @property
    def laser_profile(self) -> LaserProfile | None: ...
    @laser_profile.setter
    def laser_profile(self, value: LaserProfile | None) -> None: ...
    @property
    def plasma(self) -> Plasma | None: ...
    @plasma.setter
    def plasma(self, value: Plasma | None) -> None: ...
    @property
    def laser_spectrum(self) -> LaserSpectrum | None: ...
    @laser_spectrum.setter
    def laser_spectrum(self, value: LaserSpectrum | None) -> None: ...
