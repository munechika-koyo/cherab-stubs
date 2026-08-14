from collections.abc import Mapping
from os import PathLike
from typing import Literal

from ..core.atomic import Element
from ..core.atomic import hydrogen as hydrogen
from ..core.utility import Cm3ToM3 as Cm3ToM3
from ..core.utility import PerCm3ToPerM3 as PerCm3ToPerM3
from ..core.utility import RecursiveDict as RecursiveDict
from . import repository as repository
from .parse import *

OPENADAS_FILE_URL: str

_Path = str | PathLike[str]

def install_files(configuration: Mapping[str, object], download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None: ...
def install_adf11scd(element: Element, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None:
    """
    Adds the ionisation rate defined in an ADF11 file to the repository.

    :param element: The element described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf11acd(element: Element, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None:
    """
    Adds the recombination rate defined in an ADF11 file to the repository.

    :param element: The element described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf11ccd(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    file_path: _Path,
    download: bool = False,
    repository_path: _Path | None = None,
    adas_path: _Path | None = None,
) -> None:
    """
    Adds the thermal charge exchange rate defined in an ADF11 file to the repository.

    :param donor_element: Element donating the electron, for the case of ADF11 files it is
      neutral hydrogen.
    :param donor_charge: Charge of the donor atom/ion.
    :param receiver_element: Element receiving the electron.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf11plt(element: Element, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None:
    """
    Adds the line radiated power rates defined in an ADF11 file to the repository.

    :param element: The element described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf11prb(element: Element, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None:
    """
    Adds the continuum radiated power rates defined in an ADF11 file to the repository.

    :param element: The element described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf11prc(element: Element, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None) -> None:
    """
    Adds the CX radiated power rates defined in an ADF11 file to the repository.

    :param element: The element described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf12(
    donor_ion: Element,
    donor_metastable: int,
    receiver_ion: Element,
    receiver_charge: int,
    file_path: _Path,
    download: bool = False,
    repository_path: _Path | None = None,
    adas_path: _Path | None = None,
) -> None:
    """
    Adds the rates in the ADF12 file to the repository.

    :param donor_ion: The donor ion element described by the rate file.
    :param donor_metastable: The donor ion metastable level.
    :param receiver_ion: The receiver ion element described by the rate file.
    :param receiver_charge: The receiver ion ionisation level described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf15(
    element: Element,
    ionisation: int,
    file_path: _Path,
    download: bool = False,
    repository_path: _Path | None = None,
    adas_path: _Path | None = None,
    header_format: Literal["hydrogen", "hydrogen-like"] | None = None,
) -> None:
    """
    Adds the rates in the ADF15 file to the repository.

    :param element: The element described by the rate file.
    :param ionisation: The ionisation level described by the rate file.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf21(
    beam_species: Element, target_ion: Element, target_charge: int, file_path: _Path, download: bool = False, repository_path: _Path | None = None, adas_path: _Path | None = None
) -> None:
    """
    Adds the beam stopping rate defined in an ADF21 file to the repository.

    :param beam_species: Beam neutral atom (Element/Isotope).
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf22bmp(
    beam_species: Element,
    beam_metastable: int,
    target_ion: Element,
    target_charge: int,
    file_path: _Path,
    download: bool = False,
    repository_path: _Path | None = None,
    adas_path: _Path | None = None,
) -> None:
    """
    Adds the beam population rate defined in an ADF22 BMP file to the repository.

    :param beam_species: Beam neutral atom (Element/Isotope).
    :param beam_metastable: Metastable/excitation level of beam neutral atom.
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def install_adf22bme(
    beam_species: Element,
    target_ion: Element,
    target_charge: int,
    transition: tuple[int, int],
    file_path: _Path,
    download: bool = False,
    repository_path: _Path | None = None,
    adas_path: _Path | None = None,
) -> None:
    """
    Adds the beam emission rate defined in an ADF22 BME file to the repository.

    :param beam_species: Beam neutral atom (Element/Isotope).
    :param target_ion: Target species (Element/Isotope).
    :param target_charge: Charge of the target species.
    :param transition: Tuple containing (initial level, final level).
    :param file_path: Path relative to ADAS root.
    :param download: Attempt to download file if not present (Default=True).
    :param repository_path: Path to the repository in which to install the rates (optional).
    :param adas_path: Path to ADAS files repository (optional).
    """

def _locate_adas_file(file_path: _Path, download: bool = False, adas_path: _Path | None = None, repository_path: _Path | None = None) -> str: ...
def _notation_adf11_adas2cherab(rate_adas: Mapping[object, object], filetype: str) -> dict[object, object]:
    """
    Converts adas unit, charge and numeric notation to cherab notation

    :param rate_adas: Nested dictionary of shape rate_adas[element][charge][te, ne, rates]
    :param filetype: string denoting adas adf11 file type to decide whether charge conversion is to be applied.
      Will be applied for file types: "scd", "ccd", "plt", "pls"
    :return: nested dictionary with cherab rates and units notation
    """

def _thermalcx_adf15_2dto3d_converter(rates: Mapping[object, object]) -> dict[object, object]:
    """
    Converts thermal CX PEC rates parsed from a standard ADF 15 file
    to the format supported by the repository.

    In the standard ADF 15 file, it is assumed that the donor is H0 and Tdon = Trec.
    """
