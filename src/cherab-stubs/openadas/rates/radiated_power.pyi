from ...core.atomic import Element
from ...core.atomic.rates import ContinuumPower as CoreContinuumPower
from ...core.atomic.rates import CXRadiationPower as CoreCXRadiationPower
from ...core.atomic.rates import LineRadiationPower as CoreLineRadiationPower

class LineRadiationPower(CoreLineRadiationPower):
    """
    Line radiated power coefficient.

    The data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param Element species: Element object defining the ion type.
    :param int ionisation: Charge state of the ion.
    :param dict data: Line radiated power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with radiated power rate in W.m^3.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    def __init__(self, species: Element, ionisation: int, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...

class NullLineRadiationPower(CoreLineRadiationPower):
    """
    A line radiation power rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...

class ContinuumPower(CoreContinuumPower):
    """
    Recombination continuum radiated power coefficient.

    The data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param Element species: Element object defining the ion type.
    :param int ionisation: Charge state of the ion.
    :param dict data: Recombination continuum radiated power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with radiated power rate in W.m^3.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    raw_data: dict[str, object]
    density_range: tuple[float, float]
    temperature_range: tuple[float, float]
    def __init__(self, species: Element, ionisation: int, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...

class NullContinuumPower(CoreContinuumPower):
    """
    A continuum radiation power rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...

class CXRadiationPower(CoreCXRadiationPower):
    """
    Charge exchange radiated power coefficient.

    The data is interpolated with cubic spline in log-log space.
    Linear extrapolation is used if extrapolate is True.

    :param Element species: Element object defining the ion type.
    :param int ionisation: Charge state of the ion.
    :param dict data: CX radiated power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with radiated power rate in W.m^3.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    raw_data: dict[str, object]
    density_range: tuple[float, float]
    temperature_range: tuple[float, float]
    def __init__(self, species: Element, ionisation: int, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...

class NullCXRadiationPower(CoreCXRadiationPower):
    """
    A CX radiation power rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """
    def evaluate(self, electron_density: float, electron_temperature: float) -> float: ...
