from ...core.atomic.rates import BeamEmissionPEC as CoreBeamEmissionPEC
from ...core.atomic.rates import BeamPopulationRate as CoreBeamPopulationRate
from ...core.atomic.rates import BeamStoppingRate as CoreBeamStoppingRate
from ...core.utility.conversion import PhotonToJ as PhotonToJ

class BeamStoppingRate(CoreBeamStoppingRate):
    """
    The beam stopping coefficient interpolation class.

    Data is interpolated with cubic spline in log-log space.
    Linear and quadratic extrapolations are used for "sen" and "st" respectively
    if extrapolate is True.

    :param dict data: A beam stopping rate dictionary containing the following entries:

    |      \'e\': 1D array of size (N) with interaction energy in eV/amu,
    |      \'n\': 1D array of size (M) with target electron density in m^-3,
    |      \'t\': 1D array of size (K) with target electron temperature in eV,
    |      \'sen\': 2D array of size (N, M) with beam stopping rate energy component in m^3.s^-1.
    |      \'st\': 1D array of size (K) with beam stopping rate temperature component in m^3.s^-1.
    |      \'sref\': reference beam stopping rate in m^3.s^-1.
    |  The total beam stopping rate: s = sen * st / sref.

    :param bint extrapolate: Set to True to enable extrapolation, False to disable (default).

    :ivar tuple beam_energy_range: Interaction energy interpolation range.
    :ivar tuple density_range: Target electron density interpolation range.
    :ivar tuple temperature_range: Target electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    _npl_eb: object
    _tp: object
    beam_energy_range: tuple[float, float]
    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    def __init__(self, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float:
        """
        Interpolates and returns the beam coefficient for the supplied parameters.

        If the requested data is out-of-range then the call with throw a ValueError exception.

        :param energy: Interaction energy in eV/amu.
        :param density: Target electron density in m^-3
        :param temperature: Target temperature in eV.
        :return: The beam stopping coefficient in m^3.s^-1
        """

class NullBeamStoppingRate(CoreBeamStoppingRate):
    """
    A beam stopping rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float: ...

class BeamPopulationRate(CoreBeamPopulationRate):
    """
    The beam population coefficient interpolation class.

    Data is interpolated with cubic spline in log-log space.
    Linear and quadratic extrapolations are used for "sen" and "st" respectively
    if extrapolate is True.

    :param dict data: Beam population rate dictionary containing the following entries:

    |      \'e\': 1D array of size (N) with interaction energy in eV/amu,
    |      \'n\': 1D array of size (M) with target electron density in m^-3,
    |      \'t\': 1D array of size (K) with target electron temperature in eV,
    |      \'sen\': 2D array of size (N, M) with dimensionless beam population rate energy component.
    |      \'st\': 1D array of size (K) with dimensionless beam population rate temperature component.
    |      \'sref\': reference dimensionless beam population rate.
    |  The total beam population rate: s = sen * st / sref.

    :param bint extrapolate: Set to True to enable extrapolation, False to disable (default).

    :ivar tuple beam_energy_range: Interaction energy interpolation range.
    :ivar tuple density_range: Target electron density interpolation range.
    :ivar tuple temperature_range: Target electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    _npl_eb: object
    _tp: object
    beam_energy_range: tuple[float, float]
    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    def __init__(self, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float:
        """
        Interpolates and returns the beam coefficient for the supplied parameters.

        If the requested data is out-of-range then the call with throw a ValueError exception.

        :param energy: Interaction energy in eV/amu.
        :param density: Target electron density in m^-3
        :param temperature: Target temperature in eV.
        :return: The beam population coefficient in dimensionless units.
        """

class NullBeamPopulationRate(CoreBeamPopulationRate):
    """
    A beam population rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float: ...

class BeamEmissionPEC(CoreBeamEmissionPEC):
    """
    The beam emission coefficient interpolation class.

    Data is interpolated with cubic spline in log-log space.
    Linear and quadratic extrapolations are used for "sen" and "st" respectively
    if extrapolate is True.

    :param dict data: Beam emission rate dictionary containing the following entries:

    |      \'e\': 1D array of size (N) with interaction energy in eV/amu,
    |      \'n\' 1D array of size (M) with target electron density in m^-3,
    |      \'t\' 1D array of size (K) with target electron temperature in eV,
    |      \'sen\' 2D array of size (N, M) with beam emission rate energy component in photon.m^3.s^-1.
    |      \'st\' 1D array of size (K) with beam emission rate temperature component in photon.m^3.s^-1.
    |      \'sref\': reference beam emission rate in photon.m^3.s^-1.

    :param double wavelength: The natural wavelength of the emission line associated with the rate data in nm.
    :param bint extrapolate: Set to True to enable extrapolation, False to disable (default).

    :ivar tuple beam_energy_range: Interaction energy interpolation range.
    :ivar tuple density_range: Target electron density interpolation range.
    :ivar tuple temperature_range: Target electron temperature interpolation range.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    _npl_eb: object
    _tp: object
    beam_energy_range: tuple[float, float]
    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    wavelength: float
    def __init__(self, data: dict[str, object], wavelength: float, extrapolate: bool = False) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float:
        """
        Interpolates and returns the beam coefficient for the supplied parameters.

        If the requested data is out-of-range then the call with throw a ValueError exception.

        :param energy: Interaction energy in eV/amu.
        :param density: Target electron density in m^-3
        :param temperature: Target temperature in eV.
        :return: The beam emission coefficient in m^3.s^-1
        """

class NullBeamEmissionPEC(CoreBeamEmissionPEC):
    """
    A beam emission PEC that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(self, energy: float, density: float, temperature: float) -> float: ...
