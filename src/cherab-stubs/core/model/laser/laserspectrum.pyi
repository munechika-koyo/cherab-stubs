from ...laser.laserspectrum import LaserSpectrum

class ConstantSpectrum(LaserSpectrum):
    """
    A laser spectrum with constant power.

    Has a constant, non-zero distribution of power spectral density
    between the min_wavelength and max_wavelength. The integral value
    of the power is 1 W.

    .. note::
        The ConstantSpectrum class is suitable for approximation
        of an infinitely thin laser spectrum, e.g.:
        ConstantSpectrum(1063.9, 1064.1, 1)
    """

    def __init__(self, min_wavelength: float, max_wavelength: float, bins: int) -> None: ...

class GaussianSpectrum(LaserSpectrum):
    """
    A laser spectrum with a normally distributed power spectral density.

    Has a Gaussian-like spectral shape. The inegral value of power is 1 W.

    :param float mean: The mean value of the Gaussian distribution
      of the laser spectrum in nm, can be thought of as the central
      wavelength of the laser.
    :param float stddev: Standard deviation of the Gaussian
      distribution of the laser spectrum.

    :ivar float stddev: Standard deviation of the Gaussian
      distribution of the laser spectrum.
    :ivar float mean: The mean value of the Gaussian distribution
      of the laser spectrum in nm, can be thought of as the central
      wavelength of the laser.
    """
    def __init__(self, min_wavelength: float, max_wavelength: float, bins: int, mean: float, stddev: float) -> None: ...
    @property
    def stddev(self) -> float: ...
    @stddev.setter
    def stddev(self, value: float) -> None: ...
    @property
    def mean(self) -> float: ...
    @mean.setter
    def mean(self, value: float) -> None: ...
    def _get_bin_power_spectral_density(self, bin_index: int) -> float:
        """
        Returns the power spectral density in a bin.

        Overrides the parent method to deliver better precision.
        """
