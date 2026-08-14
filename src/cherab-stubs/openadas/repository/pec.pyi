from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]
_Transition = tuple[int, int]

def add_pec_excitation_rate(element: Element, charge: int, transition: _Transition, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single PEC excitation rate to the repository.

    If adding multiple rate, consider using the update_pec_rates() function
    instead. The update function avoid repeatedly opening and closing the rate
    files.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param rate: Excitation PEC dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with excitation PEC in photon.m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def add_pec_recombination_rate(element: Element, charge: int, transition: _Transition, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single PEC recombination rate to the repository.

    If adding multiple rate, consider using the update_pec_rates() function
    instead. The update function avoid repeatedly opening and closing the rate
    files.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param rate: Recombination PEC dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with recombination PEC in photon.m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def add_pec_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    receiver_charge: int,
    transition: _Transition,
    rate: Mapping[str, object],
    repository_path: _Path | None = None,
) -> None:
    """
    Adds a single PEC thermal charge exchange rate to the repository.

    If adding multiple rate, consider using the update_pec_thermal_rates() function
    instead. The update function avoid repeatedly opening and closing the rate
    files.

    :param donor_element: Electron donor plasma species (Element/Isotope).
    :param donor_charge: Electron donor charge.
    :param receiver_element: Electron receiver plasma species (Element/Isotope).
    :param receiver_charge: Electron receiver charge.
    :param transition: Tuple containing (initial level, final level).
    :param rate: Thermal CX PEC dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'td': array-like of size (K) with donor temperature in eV,
    |      'rate': array-like of size (N, M, K) with thermal CX PEC in photon.m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def update_pec_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates excitation and recombination PEC files /pec/<class>/<element>/<charge>.json.
    in the atomic data repository.

    File contains multiple PECs, indexed by the transition.

    :param rates: Dictionary in the form:

    |  { <class>: { <element>: { <charge>: { <transition>: <pec> } } } }, where
    |      <class> is the one of the following PEC types: 'excitation', 'recombination'.
    |      <element> is the plasma species (Element/Isotope).
    |      <charge> is the charge of the plasma species.
    |      <transition> is the tuple containing (initial level, final level).
    |      <pec> is the PEC dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with PEC in photon.m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def update_pec_thermal_cx_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates thermal CX PEC files /pec/thermal_cx/<donor_element>/<donor_charge>/<receiver_element>/<receiver_charge>.json
    in the atomic data repository.

    File contains multiple PECs, indexed by the transition.

    :param rates: Dictionary in the form:

    |  { <donor_element>: { <donor_charge>: { <receiver_element>: { <receiver_charge>: { <transition>: <pec> } } } } }, where
    |      <donor_element> is the electron donor species (Element/Isotope).
    |      <donor_charge> is the electron donor charge.
    |      <receiver_element> is the electron receiver species (Element/Isotope).
    |      <receiver_charge> is the electron receiver charge.
    |      <transition> is the tuple containing (initial level, final level).
    |      <pec> is the PEC dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'td': array-like of size (K) with donor temperature in eV,
    |          'rate': array-like of size (N, M, K) with PEC in photon.m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def get_pec_excitation_rate(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the excitation PEC from the repository for the given
    element, charge and transition.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return rate: Excitation PEC dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with excitation PEC in photon.m^3.s^-1.
    """

def get_pec_recombination_rate(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the recombination PEC from the repository for the given
    element, charge and transition.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return rate: Recombination PEC dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with recombination PEC in photon.m^3.s^-1.
    """

def get_pec_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    receiver_charge: int,
    transition: _Transition,
    repository_path: _Path | None = None,
) -> _Rate:
    """
    Reads the thermal charge exchange PEC from the repository for the given
    donor element, donor charge, receiver element, receiver charge and transition.

    :param donor_element: Electron donor plasma species (Element/Isotope).
    :param donor_charge: Electron donor charge.
    :param receiver_element: Electron receiver plasma species (Element/Isotope).
    :param receiver_charge: Electron receiver charge.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return rate: Thermal CX PEC dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'td': 1D array of size (K) with donor temperature in eV,
    |      'rate': 2D array of size (N, M, K) with thermal CX PEC in photon.m^3.s^-1.
    """
