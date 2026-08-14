from collections.abc import Mapping
from os import PathLike

from ....core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_beam_emission_rate(beam_species: Element, target_ion: Element, target_charge: int, transition: tuple[int, int], rate: Mapping[str, object], repository_path: _Path | None = None) -> None:
    """
    Adds a single beam emission rate to the repository.

    If adding multiple rate, consider using the update_beam_emission_rates()
    function instead. The update function avoid repeatedly opening and closing
    the rate files.

    :param beam_species: Beam neutral species (Element/Isotope).
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param transition: Tuple containing (initial level, final level).
    :param rate: Beam emission rate dictionary containing the following entries:

    |      'e': array-like of size (N) with interaction energy in eV/amu,
    |      'n' array-like of size (M) with target electron density in m^-3,
    |      't' array-like of size (K) with target electron temperature in eV,
    |      'sen' array-like of size (N, M) with beam emission rate energy component in photon.m^3.s^-1.
    |      'st' array-like of size (K) with beam emission rate temperature component in photon.m^3.s^-1.
    |      'eref': reference interaction energy in eV/amu,
    |      'nref': reference target electron density in m^-3,
    |      'tref': reference target electron temperature in eV,
    |      'sref': reference beam emission rate in photon.m^3.s^-1.
    |  The total beam emission rate: s = sen * st / sref.

    :param repository_path: Path to the atomic data repository.
    """

def update_beam_emission_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates the beam emission rate files:
    /beam/emission/<beam species>/<target ion>/<target_charge>.json
    in the atomic repository.

    File contains multiple rates, indexed by transition.

    :param rates: Dictionary in the form:

    |  { <beam_species>: { <target_ion>: { <target_charge>: {<transition>: <rate>} } } }, where
    |      <beam_species> is the beam neutral species (Element/Isotope)
    |      <target_ion> is the target species (Element/Isotope).
    |      <target_charge> is the charge of the target species.
    |      <transition> is the tuple containing (initial level, final level).
    |      <rate> Beam emission rate dictionary containing the following entries:
    |          'e': array-like of size (N) with interaction energy in eV/amu,
    |          'n' array-like of size (M) with target electron density in m^-3,
    |          't' array-like of size (K) with target electron temperature in eV,
    |          'sen' array-like of size (N, M) with beam emission rate energy component in photon.m^3.s^-1.
    |          'st' array-like of size (K) with beam emission rate temperature component in photon.m^3.s^-1.
    |          'eref': reference interaction energy in eV/amu,
    |          'nref': reference target electron density in m^-3,
    |          'tref': reference target electron temperature in eV,
    |          'sref': reference beam emission rate in photon.m^3.s^-1.
    |      The total beam emission rate: s = sen * st / sref.

    :param repository_path: Path to the atomic data repository.
    """

def get_beam_emission_rate(beam_species: Element, target_ion: Element, target_charge: int, transition: tuple[int, int], repository_path: _Path | None = None) -> _Rate:
    """
    Reads a single beam emission rate from the repository.

    :param beam_species: Beam neutral species (Element/Isotope).
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return rate: Beam emission rate dictionary containing the following entries:

    |      'e': 1D array of size (N) with interaction energy in eV/amu,
    |      'n' 1D array of size (M) with target electron density in m^-3,
    |      't' 1D array of size (K) with target electron temperature in eV,
    |      'sen' 2D array of size (N, M) with beam emission rate energy component in photon.m^3.s^-1.
    |      'st' 1D array of size (K) with beam emission rate temperature component in photon.m^3.s^-1.
    |      'eref': reference interaction energy in eV/amu,
    |      'nref': reference target electron density in m^-3,
    |      'tref': reference target electron temperature in eV,
    |      'sref': reference beam emission rate in photon.m^3.s^-1.
    |  The total beam emission rate: s = sen * st / sref.
    """
