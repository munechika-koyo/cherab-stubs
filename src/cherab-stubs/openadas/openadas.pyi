import sys

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

from ..core.atomic import AtomicData
from ..core.atomic.elements import Element
from ..core.atomic.rates import BeamCXPEC as CoreBeamCXPEC
from .rates import (
    BeamEmissionPEC,
    BeamPopulationRate,
    BeamStoppingRate,
    ContinuumPower,
    CXRadiationPower,
    ImpactExcitationPEC,
    IonisationRate,
    LineRadiationPower,
    NullBeamEmissionPEC,
    NullBeamPopulationRate,
    NullBeamStoppingRate,
    NullContinuumPower,
    NullCXRadiationPower,
    NullImpactExcitationPEC,
    NullIonisationRate,
    NullLineRadiationPower,
    NullRecombinationPEC,
    NullRecombinationRate,
    NullThermalCXPEC,
    NullThermalCXRate,
    RecombinationPEC,
    RecombinationRate,
    ThermalCXPEC,
    ThermalCXRate,
)

class OpenADAS(AtomicData):
    """
    OpenADAS atomic data source.

    :param str data_path: OpenADAS local repository path.
    :param bool permit_extrapolation: If true, informs interpolation objects to allow extrapolation
                                      beyond the limits of the tabulated data. Default is False.
    :param bool missing_rates_return_null: If true, allows Null rate objects to be returned when
                                           the requested atomic data is missing. Default is False.
    :param bool wavelength_element_fallback: If true, allows to use the element's wavelength when
                                             the isotope's wavelength is not available.
                                             Default is False.
    """

    _data_path: str
    _permit_extrapolation: bool
    _missing_rates_return_null: bool
    _wavelength_element_fallback: bool

    def __init__(
        self,
        data_path: str | None = None,
        permit_extrapolation: bool = False,
        missing_rates_return_null: bool = False,
        wavelength_element_fallback: bool = False,
    ) -> None: ...
    @property
    def data_path(self) -> str: ...
    @override
    def wavelength(self, ion: Element, charge: int, transition: tuple[int, int]) -> float:
        """
        Spectral line wavelength for a given transition.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :param transition: Tuple containing (initial level, final level)
        :return: Wavelength in nanometers.
        """
    @override
    def ionisation_rate(self, ion: Element, charge: int) -> IonisationRate | NullIonisationRate:
        """
        Electron impact ionisation rate for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :return: Ionisation rate in m^3/s as a function of electron density and temperature.
        """
    @override
    def recombination_rate(self, ion: Element, charge: int) -> RecombinationRate | NullRecombinationRate:
        """
        Recombination rate for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :return: Recombination rate in m^3/s as a function of electron density and temperature.
        """
    @override
    def thermal_cx_rate(  # pyrefly: ignore [bad-override-param-name]
        self, donor_element: Element, donor_charge: int, receiver_element: Element, receiver_charge: int
    ) -> ThermalCXRate | NullThermalCXRate:
        """
        Thermal charge exchange effective rate coefficient for a given donor and receiver species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Linear extrapolation is used when permit_extrapolation is True.

        :param donor_element: Element object defining the donor ion type.
        :param donor_charge: Charge state of the donor ion.
        :param receiver_element: Element object defining the receiver ion type.
        :param receiver_charge: Charge state of the receiver ion.
        :return: Thermal charge exchange rate in m^3/s as a function of electron density and
                 temperature.
        """
    def beam_cx_pec(self, donor_ion: Element, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int]) -> list[CoreBeamCXPEC]:
        """
        Effective charge exchange photon emission coefficient for a given donor (beam)
        and receiver (plasma) species and a given transition.

        The data for "qeb" is interpolated with a cubic spline in log-log space.
        The data for "qti", "qni", "qz" and "qb" are interpolated with a cubic spline
        in linear space.
        Quadratic extrapolation is used for "qeb" and nearest neighbour extrapolation is used for
        "qti", "qni", "qz" and "qb" when permit_extrapolation is True.


        :param donor_ion: Element object defining the donor ion type.
        :param receiver_ion: Element object defining the receiver ion type.
        :param receiver_charge: Charge state of the receiver ion.
        :param transition: Tuple containing (initial level, final level) of the receiver species.
        :return: Charge exchange photon emission coefficient in W.m^3 as a function of
                 interaction energy, receiver ion temperature, receiver ion density,
                 plasma Z-effective, magnetic field magnitude.
        """
    @override
    def beam_stopping_rate(self, beam_ion: Element, plasma_ion: Element, charge: int) -> BeamStoppingRate | NullBeamStoppingRate:
        """
        Beam stopping coefficient for a given beam and target species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Linear and quadratic extrapolations are used for "sen" and "st" respectively
        when permit_extrapolation is True.

        :param beam_ion: Element object defining the beam ion type.
        :param plasma_ion: Element object defining the target ion type.
        :param charge: Charge state of the target ion.
        :return: The beam stopping coefficient in m^3.s^-1 as a function of interaction energy,
                 target equivalent electron density, target temperature.
        """
    def beam_population_rate(self, beam_ion: Element, metastable: int, plasma_ion: Element, charge: int) -> BeamPopulationRate | NullBeamPopulationRate:
        """
        Beam population coefficient for a given beam and target species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Linear and quadratic extrapolations are used for "sen" and "st" respectively
        when permit_extrapolation is True.

        :param beam_ion: Element object defining the beam ion type.
        :param metastable: The beam ion metastable number.
        :param plasma_ion: Element object defining the target ion type.
        :param charge: Charge state of the target ion.
        :return: The beam population coefficient in dimensionless units as a function of
                 interaction energy, target equivalent electron density, target temperature.
        """
    def beam_emission_pec(self, beam_ion: Element, plasma_ion: Element, charge: int, transition: tuple[int, int]) -> BeamEmissionPEC | NullBeamEmissionPEC:
        """
        The beam photon emission coefficient for a given beam and target species
        and a given transition.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Linear and quadratic extrapolations are used for "sen" and "st" respectively
        when permit_extrapolation is True.

        :param beam_ion: Element object defining the beam ion type.
        :param plasma_ion: Element object defining the target ion type.
        :param charge: Charge state of the target ion.
        :param transition: Tuple containing (initial level, final level) of the beam ion.
        :return: The beam photon emission coefficient in W.m^3 as a function of
                 interaction energy, target equivalent electron density, target temperature.
        """
    def impact_excitation_pec(self, ion: Element, charge: int, transition: tuple[int, int]) -> ImpactExcitationPEC | NullImpactExcitationPEC:
        """
        Electron impact excitation photon emission coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :param transition: Tuple containing (initial level, final level).
        :return: Impact excitation photon emission coefficient in W.m^3 as a
                 function of electron density and temperature.
        """
    def recombination_pec(self, ion: Element, charge: int, transition: tuple[int, int]) -> RecombinationPEC | NullRecombinationPEC:
        """
        Recombination photon emission coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion after recombination.
        :param transition: Tuple containing (initial level, final level).
        :return: Recombination photon emission coefficient in W.m^3 as a function of electron
                 density and temperature.
        """
    def thermal_cx_pec(  # pyrefly: ignore [bad-override-param-name]
        self, donor_element: Element, donor_charge: int, receiver_element: Element, receiver_charge: int, transition: tuple[int, int]
    ) -> ThermalCXPEC | NullThermalCXPEC:
        """
        Thermal CX photon emission coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param donor_element: Element object defining the donor ion type.
        :param donor_charge: Charge state of the donor ion.
        :param receiver_element: Element object defining the receiver ion type.
        :param receiver_charge: Charge state of the receiver ion.
        :param transition: Tuple containing (initial level, final level) of the receiver
                           in charge state receiver_charge - 1.
        :return: Thermal charge exchange photon emission coefficient in W.m^3
                 as a function of electron density, electron temperature and donor temperature.
        """
    def line_radiated_power_rate(  # pyrefly: ignore [bad-override-param-name]
        self, ion: Element, charge: int
    ) -> LineRadiationPower | NullLineRadiationPower:
        """
        Line radiated power coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :return: Line radiated power coefficient in W.m^3 as a function of electron
                 density and temperature.
        """
    def continuum_radiated_power_rate(  # pyrefly: ignore [bad-override-param-name]
        self, ion: Element, charge: int
    ) -> ContinuumPower | NullContinuumPower:
        """
        Recombination continuum radiated power coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Nearest neighbour extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :return: Continuum radiated power coefficient in W.m^3 as a function
                 of electron density and temperature.
        """
    def cx_radiated_power_rate(  # pyrefly: ignore [bad-override-param-name]
        self, ion: Element, charge: int
    ) -> CXRadiationPower | NullCXRadiationPower:
        """
        Charge exchange radiated power coefficient for a given species.

        Open-ADAS data is interpolated with cubic spline in log-log space.
        Linear extrapolation is used when permit_extrapolation is True.

        :param ion: Element object defining the ion type.
        :param charge: Charge state of the ion.
        :return: Charge exchange radiated power coefficient in W.m^3 as a function
                 of electron density and temperature.
        """
