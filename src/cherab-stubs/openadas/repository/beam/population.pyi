from collections.abc import Mapping
from os import PathLike

from ....core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_beam_population_rate(beam_species: Element, beam_metastable: int, target_ion: Element, target_charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single beam population rate to the repository.

    :param beam_species: Beam neutral species (Element/Isotope).
    :param beam_metastable: Metastable level of beam neutral atom.
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param rate: Beam population rate dictionary containing the following entries:

    |      'e': array-like of size (N) with interaction energy in eV/amu,
    |      'n': array-like of size (M) with target electron density in m^-3,
    |      't': array-like of size (K) with target electron temperature in eV,
    |      'sen': array-like of size (N, M) with dimensionless beam population rate energy component.
    |      'st': array-like of size (K) with dimensionless beam population rate temperature component.
    |      'eref': reference interaction energy in eV/amu,
    |      'nref': reference target electron density in m^-3,
    |      'tref': reference target electron temperature in eV,
    |      'sref': reference dimensionless beam population rate.
    |  The total beam population rate: s = sen * st / sref.

    :param repository_path: Path to the atomic data repository.
    """

def update_beam_population_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates the beam population rate files
    /beam/population/<beam species>/<beam metastable>/<target ion>/<target_charge>.json
    in the atomic data repository.

    Each json file contains a single rate, so it can simply be replaced.

    :param rates: Dictionary in the form:

    |  { <beam_species>: { <beam_metastable>: { <target_ion>: {<target_charge>: <rate>} } } }, where
    |      <beam_species> is the beam neutral species (Element/Isotope)
    |      <beam_metastable> is the metastable level of beam neutral atom.
    |      <target_ion> is the target species (Element/Isotope).
    |      <target_charge> is the charge of the target species.
    |      <rate> is the beam population rate dictionary containing the following fields:
    |          'e': array-like of size (N) with interaction energy in eV/amu,
    |          'n': array-like of size (M) with target electron density in m^-3,
    |          't': array-like of size (K) with target electron temperature in eV,
    |          'sen': array-like of size (N, M) with dimensionless beam population rate energy component.
    |          'st': array-like of size (K) with dimensionless beam population rate temperature component.
    |          'eref': reference interaction energy in eV/amu,
    |          'nref': reference target electron density in m^-3,
    |          'tref': reference target electron temperature in eV,
    |          'sref': reference dimensionless beam population rate.
    |      The total beam population rate: s = sen * st / sref.

    :param repository_path: Path to the atomic data repository.
    """

def get_beam_population_rate(beam_species: Element, beam_metastable: int, target_ion: Element, target_charge: int, repository_path: _Path | None = None) -> _Rate:
    """
    Reads a single beam population rate from the repository.

    :param beam_species: Beam neutral species (Element/Isotope).
    :param beam_metastable: Metastable level of beam neutral atom.
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param repository_path: Path to the atomic data repository.

    :return rate: Beam population rate dictionary containing the following entries:

    |      'e': 1D array of size (N) with interaction energy in eV/amu,
    |      'n': 1D array of size (M) with target electron density in m^-3,
    |      't': 1D array of size (K) with target electron temperature in eV,
    |      'sen': 2D array of size (N, M) with dimensionless beam population rate energy component.
    |      'st': 1D array of size (K) with dimensionless beam population rate temperature component.
    |      'eref': reference interaction energy in eV/amu,
    |      'nref': reference target electron density in m^-3,
    |      'tref': reference target electron temperature in eV,
    |      'sref': reference dimensionless beam population rate.
    |  The total beam population rate: s = sen * st / sref.
    """
