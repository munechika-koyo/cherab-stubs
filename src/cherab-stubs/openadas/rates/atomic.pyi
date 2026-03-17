from raysect.core.math.function.float.function2d import Interpolator2DArray

from ...core.atomic.rates import IonisationRate as CoreIonisationRate
from ...core.atomic.rates import RecombinationRate as CoreRecombinationRate
from ...core.atomic.rates import ThermalCXRate as CoreThermalCXRate

class IonisationRate(CoreIonisationRate):
    """
    Ionisation rate.

    Data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param dict data: Ionisation rate dictionary containing the following entries:

    |   'ne': 1D array of size (N) with electron density in m^-3,
    |   'te': 1D array of size (M) with electron temperature in eV,
    |   'rate': 2D array of size (N, M) with ionisation rate in m^3.s^-1.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    raw_data: dict
    density_range: tuple[float, float]
    temperature_range: tuple[float, float]
    _rate: Interpolator2DArray

    def __init__(self, data: dict, extrapolate: bool = False) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class NullIonisationRate(CoreIonisationRate):
    """
    An ionisation rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def evaluate(self, density: float, temperature: float) -> float: ...

class RecombinationRate(CoreRecombinationRate):
    """
    Recombination rate.

    Data is interpolated with cubic spline in log-log space.
    Nearest neighbour extrapolation is used if extrapolate is True.

    :param dict data: Recombination rate dictionary containing the following entries:

    |       'ne': 1D array of size (N) with electron density in m^-3,
    |       'te': 1D array of size (M) with electron temperature in eV,
    |       'rate': 2D array of size (N, M) with recombination rate in m^3.s^-1.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    raw_data: dict
    density_range: tuple[float, float]
    temperature_range: tuple[float, float]
    _rate: Interpolator2DArray

    def __init__(self, data: dict, extrapolate: bool = False) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class NullRecombinationRate(CoreRecombinationRate):
    """
    A recombination rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def evaluate(self, density: float, temperature: float) -> float: ...

class ThermalCXRate(CoreThermalCXRate):
    """
    Thermal charge exchange rate.

    Data is interpolated with cubic spline in log-log space.
    Linear extrapolation is used if extrapolate is True.

    :param dict data: CX rate dictionary containing the following entries:

    |       'ne': 1D array of size (N) with electron density in m^-3,
    |       'te': 1D array of size (M) with electron temperature in eV,
    |       'rate': 2D array of size (N, M) with thermal CX rate in m^3.s^-1.

    :param bint extrapolate: Enable extrapolation (default=False).

    :ivar tuple density_range: Electron density interpolation range.
    :ivar tuple temperature_range: Electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    raw_data: dict
    density_range: tuple[float, float]
    temperature_range: tuple[float, float]
    _rate: Interpolator2DArray

    def __init__(self, data: dict, extrapolate: bool = False) -> None: ...
    def evaluate(self, density: float, temperature: float) -> float: ...

class NullThermalCXRate(CoreThermalCXRate):
    """
    A thermal CX rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def evaluate(self, density: float, temperature: float) -> float: ...
