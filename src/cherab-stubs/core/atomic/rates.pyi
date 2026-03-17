from abc import abstractmethod

from .elements import Element

class IonisationRate:
    """Effective ionisation rate for a given ion."""

    def __call__(self, density: float, temperature: float) -> float:
        """Return an effective ionisation rate coefficient at the specified plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, density: float, temperature: float) -> float:
        """Return an effective ionisation rate coefficient at the specified plasma conditions.

        :param density: Electron density in m^-3.
        :param temperature: Electron temperature in eV.
        :return: The effective ionisation rate in m^3.s^-1.
        """

class RecombinationRate:
    """Effective recombination rate for a given ion."""

    def __call__(self, density: float, temperature: float) -> float:
        """Return an effective recombination rate coefficient at the specified plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, density: float, temperature: float) -> float:
        """Return an effective recombination rate coefficient at the specified plasma conditions.

        :param density: Electron density in m^-3.
        :param temperature: Electron temperature in eV.
        :return: The effective recombination rate in m^3.s^-1.
        """

class ThermalCXRate:
    """Effective charge exchange rate between two ions."""

    def __call__(self, density: float, temperature: float) -> float:
        """Return an effective charge exchange rate coefficient at the specified plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, density: float, temperature: float) -> float:
        """Return an effective charge exchange rate coefficient at the specified plasma conditions.

        :param density: Electron density in m^-3.
        :param temperature: Electron temperature in eV.
        :return: The effective charge exchange rate in m^3.s^-1.
        """

class _PECRate:
    """Photon emissivity coefficient base class."""

    def __call__(self, density: float, temperature: float) -> float:
        """Return a photon emissivity coefficient at the specified plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, density: float, temperature: float) -> float:
        """Return a photon emissivity coefficient at given conditions.

        :param density: Electron density in m^-3.
        :param temperature: Electron temperature in eV.
        :return: The effective PEC rate in W.m^3.
        """

    def plot_temperature(
        self,
        temp_low: float = 1,
        temp_high: float = 1000,
        num_points: int = 100,
        dens: float = 1e19,
    ) -> None: ...

class ImpactExcitationPEC(_PECRate):
    """Impact excitation rate coefficient."""

class RecombinationPEC(_PECRate):
    """Recombination rate coefficient."""

class ThermalCXPEC:
    """Thermal charge exchange rate coefficient."""

    def __call__(
        self, electron_density: float, electron_temperature: float, donor_temperature: float
    ) -> float:
        """Return a CX photon emissivity coefficient at the specified plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(
        self, electron_density: float, electron_temperature: float, donor_temperature: float
    ) -> float:
        """Return a CX photon emissivity coefficient at given conditions.

        :param electron_density: Electron density in m^-3.
        :param electron_temperature: Electron temperature in eV.
        :param donor_temperature: Donor temperature in eV.
        :return: The effective CX PEC rate in W/m^3.
        """

class BeamCXPEC:
    r""":math:`q^{eff}_{n\rightarrow n'}` [:math:`W.m^{3}`].

    Effective emission coefficient (or rate) for a charge-exchange line corresponding to a
    transition :math:`n\rightarrow n'` of ion :math:`Z^{(\alpha+1)+}` with electron donor
    :math:`H^0` in metastable state :math:`m_{i}`. Equivalent to
    :math:`q^{eff}_{n\rightarrow n'}` in `adf12 <http://open.adas.ac.uk/adf12>_`.

    :param donor_metastable: The metastable state of the donor species for which the rate data applies.
    """

    donor_metastable: int

    def __init__(self, donor_metastable: int) -> None: ...
    def __call__(
        self, energy: float, temperature: float, density: float, z_effective: float, b_field: float
    ) -> float:
        """Evaluate the Beam CX rate at the given plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(
        self, energy: float, temperature: float, density: float, z_effective: float, b_field: float
    ) -> float:
        """Evaluate the Beam CX rate at the given plasma conditions.

        :param float energy: Interaction energy in eV/amu.
        :param float temperature: Receiver ion temperature in eV.
        :param float density: Plasma total ion density in m^-3
        :param float z_effective: Plasma Z-effective.
        :param float b_field: Magnetic field magnitude in Tesla.
        :return: The effective rate
        """

class _BeamRate:
    """Beam coefficient base class."""

    @abstractmethod
    def evaluate(self, energy: float, density: float, temperature: float) -> float:
        """
        Return the beam coefficient for the supplied parameters.

        :param energy: Interaction energy in eV/amu.
        :param density: Target electron density in m^-3
        :param temperature: Target temperature in eV.
        :return: The beam coefficient
        """

    def __call__(self, energy: float, density: float, temperature: float) -> float: ...

class BeamStoppingRate(_BeamRate):
    """:math:`S^{e, i}_{CR}` [:math:`m^3.s^{-1}`].

    The effective collisional radiative stopping coefficient :math:`S^{e, i}_{CR}`
    [:math:`m^3.s^{-1}`] for neutral atom :math:`X^0` in a mono-energetic beam by
    fully stripped ions :math:`Y^i` and their electrons.

    Equivalent to :math:`S^{e, i}_{CR}` as defined in ADAS `adf21 <http://open.adas.ac.uk/adf21>`_.
    """

class BeamPopulationRate(_BeamRate):
    """:math:`bmp(X^0(m_i))` [dimensionless].

    Relative beam population of excited state :math:`m_i` over ground state for atom :math:`X^0`, :math:`bmp(X^0(m_i))`.

    The rate :math:`bmp(X^0(m_i))` is equivalent to the :math:`BMP` rate as defined in
    `adf22 <http://open.adas.ac.uk/adf22>`_ and is dimensionless.
    """

class BeamEmissionPEC(_BeamRate):
    """:math:`bme(X^0(m_i))` [:math:`W.m^3`].

    The effective beam emission coefficient, :math:`bme(X^0(m_i))`.

    The rate :math:`bme(X^0(m_i))` is equivalent to the :math:`BME` rate as defined in
    `adf22 <http://open.adas.ac.uk/adf22>`_.
    """

class TotalRadiatedPower:
    """The total radiated power rate in equilibrium conditions."""

    element: Element

    def __init__(self, element: Element) -> None: ...
    def __call__(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the total radiated power rate at the given plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the total radiated power rate at the given plasma conditions.

        :param float electron_density: Electron density in m^-3.
        :param float electron_temperature: Electron temperature in eV.

        :return: The total radiated power rate in W.m^3.
        """

class _RadiatedPower:
    """Base class for ionisation-resolved radiated powers."""

    element: Element
    charge: int

    def __init__(self, element: Element, charge: int) -> None: ...
    def __call__(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the radiated power rate at the given plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    @abstractmethod
    def evaluate(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the radiated power at the given plasma conditions.

        :param float density: Electron density in m^-3.
        :param float temperature: Electron temperature in eV.

        :return: The radiated power rate in W.m^3.
        """

class LineRadiationPower(_RadiatedPower):
    """
    The total line radiation power driven by excitation.

    Equivalent to the `ADF11 PLT <http://open.adas.ac.uk/adf11>`_ coefficient.
    """

class ContinuumPower(_RadiatedPower):
    """
    The power radiated from continuum, line power driven by recombination and Bremsstrahlung.

    Equivalent to the `ADF11 PRB <http://open.adas.ac.uk/adf11>`_ coefficient.
    """

class CXRadiationPower(_RadiatedPower):
    """
    Total line power radiated due to charge transfer from thermal neutral hydrogen.

    Equivalent to the `ADF11 PRC <http://open.adas.ac.uk/adf11>`_ coefficient.
    """

class FractionalAbundance:
    """
    Rate provider for fractional abundances in thermodynamic equilibrium.

    :param Element element: the radiating element.
    :param int charge: the integer charge state for this ionisation stage.
    :param str name: optional label identifying this rate.
    """

    name: str
    element: Element
    charge: int

    def __init__(self, element: Element, charge: int, name: str = "") -> None: ...
    @abstractmethod
    def evaluate(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the fractional abundance of this ionisation stage at the given plasma conditions.

        :param float electron_density: Electron density in m^-3.
        :param float electron_temperature: Electron temperature in eV.

        :return: Fractional abundance.
        """

    def __call__(self, electron_density: float, electron_temperature: float) -> float:
        """
        Evaluate the fractional abundance of this ionisation stage at the given plasma conditions.

        This function just wraps the cython evaluate() method.
        """

    def plot_temperature(
        self,
        temp_low: float = 1,
        temp_high: float = 1000,
        num_points: int = 100,
        dens: float = 1e19,
    ) -> None: ...
