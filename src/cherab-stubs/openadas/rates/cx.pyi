from ...core.atomic.rates import BeamCXPEC as CoreBeamCXPEC
from ...core.utility.conversion import Cm3ToM3 as Cm3ToM3
from ...core.utility.conversion import PerCm3ToPerM3 as PerCm3ToPerM3
from ...core.utility.conversion import PhotonToJ as PhotonToJ

class BeamCXPEC(CoreBeamCXPEC):
    """
    Effective charge exchange photon emission coefficient.

    The data for "qeb" is interpolated with a cubic spline in log-log space.
    The data for "qti", "qni", "qz" and "qb" are interpolated with a cubic spline
    in linear space.

    Quadratic extrapolation is used for "qeb" and nearest neighbour extrapolation is used for
    "qti", "qni", "qz" and "qb" if extrapolate is True.

    :param int donor_metastable: The metastable state of the donor species for which the rate data applies.
    :param double wavelength: The natural wavelength of the emission line associated with the rate data in nm.
    :param data: Beam CX PEC dictionary containing the following entries:

    |      \'eb\': 1D array of size (N) with beam energy in eV/amu,
    |      \'ti\': 1D array of size (M) with receiver ion temperature in eV,
    |      \'ni\': 1D array of size (K) with receiver ion density in m^-3,
    |      \'z\': 1D array of size (L) with receiver Z-effective,
    |      \'b\': 1D array of size (J) with magnetic field strength in Tesla,
    |      \'qeb\': 1D array of size (N) with CX PEC energy component in photon.m^3.s-1,
    |      \'qti\': 1D array of size (M) with CX PEC temperature component in photon.m^3.s-1,
    |      \'qni\': 1D array of size (K) with CX PEC density component in photon.m^3.s-1,
    |      \'qz\': 1D array of size (L) with CX PEC Zeff component in photon.m^3.s-1,
    |      \'qb\': 1D array of size (J) with CX PEC B-field component in photon.m^3.s-1,
    |      \'qref\': reference CX PEC in photon.m^3.s-1.
    |  The total beam CX PEC: q = qeb * qti * qni * qz * qb / qref^4.

    :param bint extrapolate: Set to True to enable extrapolation, False to disable (default).

    :ivar tuple beam_energy_range: Interaction energy interpolation range.
    :ivar tuple density_range: Receiver ion density interpolation range.
    :ivar tuple temperature_range: Receiver ion temperature interpolation range.
    :ivar tuple zeff_range: Z-effective interpolation range.
    :ivar tuple b_field_range: Magnetic field strength interpolation range.
    :ivar int donor_metastable: The metastable state of the donor species.
    :ivar double wavelength: The natural wavelength of the emission line in nm.
    :ivar dict raw_data: Dictionary containing the raw data.
    """

    _b: object
    _eb: object
    _ni: object
    _ti: object
    _zeff: object
    b_field_range: tuple[float, float]
    beam_energy_range: tuple[float, float]
    density_range: tuple[float, float]
    raw_data: dict[str, object]
    temperature_range: tuple[float, float]
    wavelength: float
    zeff_range: tuple[float, float]
    def __init__(self, donor_metastable: int, wavelength: float, data: dict[str, object], extrapolate: bool = False) -> None: ...
    def evaluate(
        self,
        energy: float,
        temperature: float,
        density: float,
        z_effective: float,
        b_field: float,
    ) -> float:
        """
        Interpolates and returns the effective cx rate for the given plasma parameters.

        If the requested data is out-of-range then the call with throw a ValueError exception.

        :param energy: Interaction energy in eV/amu.
        :param temperature: Receiver ion temperature in eV.
        :param density: Plasma total ion density in m^-3
        :param z_effective: Plasma Z-effective.
        :param b_field: Magnetic field magnitude in Tesla.
        :return: The effective cx rate in W.m^3
        """

class NullBeamCXPEC(CoreBeamCXPEC):
    """
    A beam CX rate that always returns zero.
    Needed for use cases where the required atomic data is missing.
    """

    def __init__(self) -> None: ...
    def evaluate(
        self,
        energy: float,
        temperature: float,
        density: float,
        z_effective: float,
        b_field: float,
    ) -> float: ...
