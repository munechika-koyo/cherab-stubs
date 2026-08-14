from .elements import Element
from .gaunt import FreeFreeGauntFactor
from .line import Line
from .rates import (
    BeamCXPEC,
    BeamEmissionPEC,
    BeamPopulationRate,
    BeamStoppingRate,
    ContinuumPower,
    CXRadiationPower,
    FractionalAbundance,
    ImpactExcitationPEC,
    IonisationRate,
    LineRadiationPower,
    RecombinationPEC,
    RecombinationRate,
    ThermalCXPEC,
    ThermalCXRate,
    TotalRadiatedPower,
)
from .zeeman import ZeemanStructure

class AtomicData:
    """Atomic data source abstraction layer.

    This base class specifies a standardised set of methods for obtaining
    atomic data.
    """

    def wavelength(self, ion: Element, charge: int, transition: tuple[int, int]) -> float:
        """The natural wavelength of the specified transition in nm."""

    def ionisation_rate(self, ion: Element, charge: int) -> IonisationRate:
        """Electron impact ionisation rate for a given species in m^3/s."""

    def recombination_rate(self, ion: Element, charge: int) -> RecombinationRate:
        """Recombination rate for a given species in m^3/s."""

    def thermal_cx_rate(self, donor_ion: Element, donor_charge: int, receiver_ion: Element, receiver_charge: int) -> ThermalCXRate:
        """Thermal charge exchange effective rate coefficient for a given donor and receiver species in m^3/s."""

    def beam_cx_pec(self, donor_ion: Element, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int]) -> list[BeamCXPEC]:
        """A list of Effective charge exchange photon emission coefficient for a given donor (beam) in W.m^3."""

    def beam_stopping_rate(self, beam_ion: Element, plasma_ion: Element, charge: int) -> BeamStoppingRate:
        """Beam stopping coefficient for a given beam and target species in m^3/s."""

    def beam_population_rate(self, beam_ion: Element, metastable: int, plasma_ion: Element, charge: int) -> BeamPopulationRate:
        """Dimensionless Beam population coefficient for a given beam and target species."""

    def beam_emission_pec(self, beam_ion: Element, plasma_ion: Element, charge: int, transition: tuple[int, int]) -> BeamEmissionPEC:
        """The beam photon emission coefficient for a given beam and target species and a given transition in W.m^3."""

    def impact_excitation_pec(self, ion: Element, charge: int, transition: tuple[int, int]) -> ImpactExcitationPEC:
        """Electron impact excitation photon emission coefficient for a given species in W.m^3."""

    def recombination_pec(self, ion: Element, charge: int, transition: tuple[int, int]) -> RecombinationPEC:
        """Recombination photon emission coefficient for a given species in W.m^3."""

    def thermal_cx_pec(
        self,
        donor_ion: Element,
        donor_charge: int,
        receiver_ion: Element,
        receiver_charge: int,
        transition: tuple[int, int],
    ) -> ThermalCXPEC:
        """Thermal charge exchange photon emission coefficient for given donor and receiver species in W.m^3."""

    def total_radiated_power(self, element: Element) -> TotalRadiatedPower:
        """The total (summed over all charge states) radiated power in equilibrium conditions for a given species in W.m^3."""

    def line_radiated_power_rate(self, element: Element, charge: int) -> LineRadiationPower:
        """Line radiated power coefficient for a given species in W.m^3."""

    def continuum_radiated_power_rate(self, element: Element, charge: int) -> ContinuumPower:
        """Continuum radiated power coefficient for a given species in W.m^3."""

    def cx_radiated_power_rate(self, element: Element, charge: int) -> CXRadiationPower:
        """Charge exchange radiated power coefficient for a given species in W.m^3."""

    def fractional_abundance(self, ion: Element, charge: int) -> FractionalAbundance:
        """Fractional abundance of a given species in thermodynamic equilibrium."""

    def zeeman_structure(self, line: Line, b_field: object = None) -> ZeemanStructure:
        r"""Wavelengths and ratios of :math:`\pi`-/:math:`\sigma`-polarised Zeeman components for any given value of magnetic field strength."""

    def zeeman_triplet_parameters(self, line: Line) -> tuple[float, float, float]:
        """Return Zeeman truplet parameters.

        See Table 1 in A. Blom and C. Jupén.
        "Parametrisation of the Zeeman effect for hydrogen-like spectra in
        high-temperature plasmas", Plasma Phys. Control. Fusion 44 (2002) `1229-1241
        <https://doi.org/10.1088/0741-3335/44/7/312>`_.
        """

    def stark_model_coefficients(self, line: Line) -> tuple[float, float, float]:
        """Return Stark model coefficients.

        See Table 1 in B. Lomanowski, et al.
        "Inferring divertor plasma properties from hydrogen Balmer
        and Paschen series spectroscopy in JET-ILW." Nuclear Fusion 55.12 (2015)
        `123028 <https://doi.org/10.1088/0029-5515/55/12/123028>`_.
        """

    def free_free_gaunt_factor(self) -> FreeFreeGauntFactor:
        """Return the Maxwellian-averaged free-free Gaunt factor.

        Interpolated over the data from Table A.1 in M.A. de Avillez and D. Breitschwerdt, 2015,
        Astron. & Astrophys. 580, `A124 <https://www.aanda.org/articles/aa/full_html/2015/08/aa26104-15/aa26104-15.html>`_.

        The Born approximation is used outside the interpolation range.
        """
