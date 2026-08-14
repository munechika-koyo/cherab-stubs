from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Transition = tuple[int, int]

def add_wavelength(element: Element, charge: int, transition: _Transition, wavelength: float, repository_path: _Path | None = None) -> None:
    """
    Adds a single wavelength to the repository.

    If adding multiple wavelengths, consider using the update_wavelengths()
    function instead. The update function avoid repeatedly opening and closing
    the rate files.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param wavelength: Transition's wavelength in nm.
    :param repository_path: Path to the atomic data repository.
    """

def update_wavelengths(wavelengths: Mapping[object, object], repository_path: _Path | None = None) -> None:
    """
    Updates the wavelength files `/wavelength/<species>/<charge>.json`
    in atomic data repository.

    File contains multiple rates, indexed by the transitions.

    :param wavelengths: Dictionary in the form:

    |  { <species>: { <charge>: { <transition>: <wavelength> } } }, where
    |      <species> is the plasma species (Element/Isotope),
    |      <charge> is the charge of the plasma species,
    |      <transition> is the tuple containing (initial level, final level),
    |      <wavelength> is the transition's wavelength in nm.

    :param repository_path: Path to the atomic data repository.
    """

def get_wavelength(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> float:
    """
    Reads the wavelength for the given species, charge and transition from the repository.

    :param element: Plasma species (Element/Isotope).
    :param charge: Charge of the plasma species.
    :param transition: Tuple containing (initial level, final level).
    :param repository_path: Path to the atomic data repository.

    :return wavelength: Wavelength in nm.
    """
