from ...core.atomic.rates import ImpactExcitationPEC as CoreImpactExcitationPEC
from ...core.atomic.rates import RecombinationPEC as CoreRecombinationPEC
from ...core.atomic.rates import ThermalCXPEC as CoreThermalCXPEC
from ...core.utility.conversion import PhotonToJ as PhotonToJ

class ImpactExcitationPEC(CoreImpactExcitationPEC):
    """
    Electron impact excitation photon emission coefficient.

    The data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param double wavelength: Resting wavelength of corresponding emission line in nm.
    :param dict data: Excitation PEC dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with excitation PEC in photon.m^3.s^-1.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    wavelength: float
    def __init__(self, wavelength: float, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class NullImpactExcitationPEC(CoreImpactExcitationPEC):
    """
    A electron impact excitation PEC rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class RecombinationPEC(CoreRecombinationPEC):
    """
    Recombination photon emission coefficient.

    The data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param double wavelength: Resting wavelength of corresponding emission line in nm.
    :param dict data: Rcombination PEC dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with recombination PEC in photon.m^3.s^-1.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    wavelength: float
    def __init__(self, wavelength: float, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class NullRecombinationPEC(CoreRecombinationPEC):
    """
    A recombination PEC rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class ThermalCXPEC(CoreThermalCXPEC):
    density_range: tuple[float, float]
    donor_temperature_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    wavelength: float
    def __init__(self, wavelength: float, data: dict[str, object], extrapolate: bool = False) -> None:
        """
        :param wavelength: Resting wavelength of corresponding emission line in nm.
        :param data: Dictionary containing rate data.
        :param extrapolate: Enable nearest-neighbour extrapolation (default=False).
        """
    def evaluate(self, electron_density: float, electron_temperature: float, donor_temperature: float) -> float: ...

class NullThermalCXPEC(CoreThermalCXPEC):
    """
    A PEC rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, electron_density: float, electron_temperature: float, donor_temperature: float) -> float: ...
