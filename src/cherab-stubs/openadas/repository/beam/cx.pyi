from collections.abc import Mapping
from os import PathLike

from ....core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_beam_cx_rate(
    donor_ion: Element, donor_metastable: int, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int], rate: Mapping[str, object], repository_path: _Path | None = None
) -> None:
    """
    Adds a single beam CX PEC to the repository.

    If adding multiple rate, consider using the update_beam_cx_rates() function
    instead. The update function avoid repeatedly opening and closing the rate
    files.

    :param donor_ion: Beam neutral atom (Element/Isotope) donating the electron.
    :param donor_metastable: Metastable/excited level of beam neutral atom.
    :param receiver_ion: Element/Isotope receiving the electron.
    :param receiver_charge: Charge of the receiving atom/ion.
    :param transition: Tuple containing (initial level, final level).
    :param rate: Beam CX PEC dictionary containing the following entries:

    |      'eb': array-like of size (N) with beam energy in eV/amu,
    |      'ti': array-like of size (M) with receiver ion temperature in eV,
    |      'ni': array-like of size (K) with plasma ion density in m^-3,
    |      'z': array-like of size (L) with plasma Z-effective,
    |      'b': array-like of size (J) with magnetic field strength in Tesla,
    |      'qeb': array-like of size (N) with CX PEC energy component in photon.m^3.s-1,
    |      'qti': array-like of size (M) with CX PEC temperature component in photon.m^3.s-1,
    |      'qni': array-like of size (K) with CX PEC density component in photon.m^3.s-1,
    |      'qz': array-like of size (L) with CX PEC Zeff component in photon.m^3.s-1,
    |      'qb': array-like of size (J) with CX PEC B-field component in photon.m^3.s-1,
    |      'qref': reference CX PEC in photon.m^3.s-1.
    |  The total beam CX PEC: q = qeb * qti * qni * qz * qb / qref^4.

    :param repository_path: Path to the atomic data repository.
    """

def update_beam_cx_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates the beam CX PEC files
    beam/cx/<donor_ion>/<receiver_ion>/<receiver_charge>.json
    in the atomic data repository.

    File contains multiple metastable-resolved rates, indexed by transition.

    :param rates: Dictionary in the form:

    |  { <donor_ion>: { <receiver_ion>: { <receiver_charge>: { <transition>: {<donor_metastable>: <rate>} } } } }, where
    |      <donor_ion> is the beam neutral atom (Element/Isotope) donating the electron.
    |      <donor_metastable> is the metastable/excited level of beam neutral atom.
    |      <receiver_ion> is the Element/Isotope receiving the electron.
    |      <receiver_charge> is the charge of the receiving atom/ion.
    |      <transition> is the tuple containing (initial level, final level).
    |      <rate> is the beam CX PEC dictionary containing the following entries:
    |          'eb': array-like of size (N) with beam energy in eV/amu,
    |          'ti': array-like of size (M) with receiver ion temperature in eV,
    |          'ni': array-like of size (K) with plasma ion density in m^-3,
    |          'z': array-like of size (L) with plasma Z-effective,
    |          'b': array-like of size (J) with magnetic field strength in Tesla,
    |          'qeb': array-like of size (N) with CX PEC energy component in photon.m^3.s-1,
    |          'qti': array-like of size (M) with CX PEC temperature component in photon.m^3.s-1,
    |          'qni': array-like of size (K) with CX PEC density component in photon.m^3.s-1,
    |          'qz': array-like of size (L) with CX PEC Zeff component in photon.m^3.s-1,
    |          'qb': array-like of size (J) with CX PEC B-field component in photon.m^3.s-1,
    |          'qref': reference CX PEC in photon.m^3.s-1.
    |      The total beam CX PEC: q = qeb * qti * qni * qz * qb / qref^4.

    :param repository_path: Path to the atomic data repository.
    """

def get_beam_cx_rates(donor_ion: Element, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int], repository_path: _Path | None = None) -> list[_Rate]:
    """
    Reads a single beam CX PEC from the repository.

    :param donor_ion: Beam neutral atom (Element/Isotope) donating the electron.
    :param donor_metastable: Metastable/excited level of beam neutral atom.
    :param receiver_ion: Element/Isotope receiving the electron.
    :param receiver_charge: Charge of the receiving atom/ion.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return rate: Beam CX PEC dictionary containing the following entries:

    |      'eb': 1D array of size (N) with beam energy in eV/amu,
    |      'ti': 1D array of size (M) with receiver ion temperature in eV,
    |      'ni': 1D array of size (K) with plasma ion density in m^-3,
    |      'z': 1D array of size (L) with plasma Z-effective,
    |      'b': 1D array of size (J) with magnetic field strength in Tesla,
    |      'qeb': 1D array of size (N) with CX PEC energy component in photon.m^3.s-1,
    |      'qti': 1D array of size (M) with CX PEC temperature component in photon.m^3.s-1,
    |      'qni': 1D array of size (K) with CX PEC density component in photon.m^3.s-1,
    |      'qz': 1D array of size (L) with CX PEC Zeff component in photon.m^3.s-1,
    |      'qb': 1D array of size (J) with CX PEC B-field component in photon.m^3.s-1,
    |      'qref': reference CX PEC in photon.m^3.s-1.
    |  The total beam CX PEC: q = qeb * qti * qni * qz * qb / qref^4.
    """
