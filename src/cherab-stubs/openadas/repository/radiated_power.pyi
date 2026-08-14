from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_line_power_rate(species: Element, charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single line radiated power rate to the repository.

    If adding multiple rates, consider using the update_line_power_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param species: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param rate: Line radiated power rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with line radiated power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def update_line_power_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Update the files for the line radiated power rates:
    /radiated_power/line/<species>.json
    in the atomic data repository.

    File contains multiple rates, indexed by the ion's charge state.

    :param rates: Dictionary in the form {<species>: {<charge>: <rate>}}, where

    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <rate> is the line radiated rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with line radiated power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def add_continuum_power_rate(species: Element, charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single continuum power rate to the repository.

    If adding multiple rates, consider using the update_continuum_power_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param species: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param rate: Continuum power rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with continuum power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def update_continuum_power_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Update the files for the continuum power rates:
    /radiated_power/continuum/<species>.json
    in the atomic data repository.

    File contains multiple rates, indexed by ion's charge state.

    :param rates: Dictionary in the form {<species>: {<charge>: <rate>}}, where

    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <rate> is the continuum power rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with continuum power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def add_cx_power_rate(species: Element, charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single CX radiation power rate to the repository
    (charge exchange with neutral hydrogen).

    If adding multiple rates, consider using the update_cx_power_rates()
    function instead. The update function avoids repeatedly opening and closing
    the rate files.

    :param species: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param rate: CX power rate dictionary containing the following entries:

    |      'ne': array-like of size (N) with electron density in m^-3,
    |      'te': array-like of size (M) with electron temperature in eV,
    |      'rate': array-like of size (N, M) with CX power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def update_cx_power_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Update the files for the CX radiation power rates
    (charge exchange with neutral hydrogen):
    /radiated_power/cx/<species>.json
    in the atomic data repository.

    File contains multiple rates, indexed by ion's charge state.

    :param rates: Dictionary in the form {<species>: {<charge>: <rate>}}, where

    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <rate> is the thermal CX power rate dictionary containing the following entries:
    |          'ne': array-like of size (N) with electron density in m^-3,
    |          'te': array-like of size (M) with electron temperature in eV,
    |          'rate': array-like of size (N, M) with thermal CX power rate in W.m^3.

    :param repository_path: Path to the atomic data repository.
    """

def get_line_radiated_power_rate(element: Element, charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the line radiated power rate for the given species and charge
    from the atomic data repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param repository_path: Path to the atomic data repository.

    :return rate: Line radiated power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with line radiated power rate in W.m^3.
    """

def get_continuum_radiated_power_rate(element: Element, charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the continuum power rate for the given species and charge
    from the atomic data repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param repository_path: Path to the atomic data repository.

    :return rate: Continuum power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with continuum power rate in W.m^3.
    """

def get_cx_radiated_power_rate(element: Element, charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads the CX radiation power rate for the given species and charge
    from the atomic data repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param repository_path: Path to the atomic data repository.

    :return rate: CX radiation power rate dictionary containing the following entries:

    |      'ne': 1D array of size (N) with electron density in m^-3,
    |      'te': 1D array of size (M) with electron temperature in eV,
    |      'rate': 2D array of size (N, M) with CX radiation power rate in W.m^3.
    """
