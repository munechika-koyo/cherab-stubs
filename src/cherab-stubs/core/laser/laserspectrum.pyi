import numpy as np
from numpy.typing import NDArray
from raysect.core.math.function.float.function1d.base import Function1D

from ..utility.notify import Notifier as Notifier

class LaserSpectrum(Function1D):
    """
    Laser spectrum base class.

    This is an abstract class and cannot be used for observing.

    A 1D function holding information about the spectral properties
    of a laser.  The scattered spectrum is calculated as an iteration
    over the laser spectrum.


    .. warning::
        When adding a LaserSpectrum, a special care should be given
        to the integral power of the laser spectrum. During the
        scattering calculation, the spectral power can be multiplied
        by the power spatial distribution [W * m ** -3] of the laser
        power from the LaserProfile. If the integral power
        of the LaserSpectrum is not 1, unexpected values
        might be obtained.

    .. note::
        It is expected that majority of the fusion applications can
        neglect the influence of the spectral shape of the
        laser and can use laser spectrum with a single
        bin, which approximates an infinitely narrow laser spectrum.

    :param float min_wavelength: The minimum wavelength of the laser
      spectrum in nm.
    :param float max_wavelength: The maximum wavelength of the laser
      spectrum in nm.
    :param int bins: The number of spectral bins of the laser spectrum.
    :ivar float min_wavelength: The minimum wavelength of the laser
      spectrum in nm.
    :ivar float max_wavelength: The maximum wavelength of the laser
      spectrum in nm.
    :ivar int bins: The number of specral bins of the laser spectrum
    :ivar ndarray wavelengths: The wavelengt coordinate vector in nm.
    :ivar ndarray power_spectral_density: The values of the power
      spectral density in W / nm.
    :ivar float delta_wavelength: Spectral width of the bins in nm.
    """
    def __init__(self, min_wavelength: float, max_wavelength: float, bins: int) -> None: ...
    @property
    def min_wavelength(self) -> float: ...
    @min_wavelength.setter
    def min_wavelength(self, value: float) -> None: ...
    @property
    def max_wavelength(self) -> float: ...
    @max_wavelength.setter
    def max_wavelength(self, value: float) -> None: ...
    @property
    def bins(self) -> int: ...
    @bins.setter
    def bins(self, value: int) -> None: ...
    @property
    def wavelengths(self) -> NDArray[np.float64]: ...
    @property
    def power_spectral_density(self) -> NDArray[np.float64]: ...
    @property
    def delta_wavelength(self) -> float: ...
    def _check_wavelength_validity(self) -> None: ...
    def get_min_wavelenth(self) -> float: ...
    def get_max_wavelenth(self) -> float: ...
    def get_spectral_bins(self) -> int: ...
    def get_delta_wavelength(self) -> float: ...
    def _update_cache(self) -> None: ...
    def evaluate_integral(self, lower_limit: float, upper_limit: float) -> float: ...
    def _get_bin_power_spectral_density(self, bin_index: int) -> float:
        """
        Returns the power spectral density in a bin.

        This method can be overridden if a better precision is needed.
        For example for distributions with known cumulative distribution function.
        """
