from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_ionisation_rate(species: Element, charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single ionisation rate to the repository.

    If adding multiple rates, consider using the update_ionisation_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param species: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param rate: Ionisation rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with ionisation rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def update_ionisation_rates(rates: Mapping[Element, Mapping[int, Mapping[str, object]]], repository_path: _Path | None = None) -> None:
    """
    Updates the ionisation rate files `/ionisation/<species>.json`
    in atomic data repository.

    File contains multiple rates, indexed by the ion charge state.

    :param rates: Dictionary in the form {<species>: {<charge>: <rate>}}, where

    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <rate> is the ionisation rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with ionisation rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def add_recombination_rate(species: Element, charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single recombination rate to the repository.

    If adding multiple rates, consider using the update_recombination_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param species: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param rate: Recombination rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with recombination rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def update_recombination_rates(rates: Mapping[Element, Mapping[int, Mapping[str, object]]], repository_path: _Path | None = None) -> None:
    """
    Updates the recombination rate files `/recombination/<species>.json`
    in the atomic data repository.

    File contains multiple rates, indexed by the ion charge state.

    :param rates: Dictionary in the form {<species>: {<charge>: <rate>}}, where

    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <rate> is the recombination rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with recombination rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def add_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    rate: Mapping[str, object],
    repository_path: _Path | None = None,
) -> None:
    """
    Adds a single thermal charge exchange rate to the repository.

    If adding multiple rates, consider using the update_recombination_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param donor_element: Element donating the electron.
    :param donor_charge: Charge of the donating atom/ion.
    :param receiver_element: Element receiving the electron.
    :param receiver_charge: Charge of the receiving atom/ion.
    :param rate: Thermal CX rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with thermal CX rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def update_thermal_cx_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates the thermal charge exchange rate files
    `/thermal_cx/<donor_element>/<donor_charge>/<receiver_element>.json`
    in the atomic data repository.

    File contains multiple rates, indexed by the ion charge state.

    :param rates: Dictionary in the form:

    |  { <donor_element>: { <donor_charge>: { <receiver_element>: { <donor_charge>: <rate> } } } }, where
    |      <donor_element> is the element donating the electron.
    |      <donor_charge> is the charge of the donating atom/ion.
    |      <receiver_element> is the element receiving the electron.
    |      <receiver_charge> is the charge of the receiving atom/ion.
    |      <rate> is the thermal CX rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with thermal CX rate in m^3.s^-1.

    :param repository_path: Path to the atomic data repository.
    """

def get_ionisation_rate(element: Element, charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the ionisation rate for the given species and charge
    from the atomic data repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param repository_path: Path to the atomic data repository.

    :return rate: Ionisation rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with ionisation rate in m^3.s^-1.
    """

def get_recombination_rate(element: Element, charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the recombination rate for the given species and charge
    from the atomic data repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param repository_path: Path to the atomic data repository.

    :return rate: Recombination rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with recombination rate in m^3.s^-1.
    """

def get_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    receiver_charge: int,
    repository_path: _Path | None = None,
) -> _Rate:
    """
    Reads the thermal charge exchange rate for the given species and charge
    from the atomic data repository.

    :param donor_element: Element donating the electron.
    :param donor_charge: Charge of the donating atom/ion.
    :param receiver_element: Element receiving the electron.
    :param receiver_charge: Charge of the receiving atom/ion.
    :param repository_path: Path to the atomic data repository.

    :return rate: Thermal CX rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with thermal CX rate in m^3.s^-1.
    """
