from os import PathLike

from ...core.atomic import Element
from ...core.utility import RecursiveDict as RecursiveDict
from ...core.utility.conversion import Cm3ToM3 as Cm3ToM3
from .utility import parse_adas2x_rate as parse_adas2x_rate

def parse_adf21(beam_species: Element, target_ion: Element, target_charge: int, adf_file_path: str | PathLike[str]) -> dict[str, object]:
    """
    Opens and parses ADAS ADF21 data files.

    :param beam_species: Element object describing the beam species.
    :param target_ion: Element object describing the target ion species.
    :param target_charge: Ionisation level of the target species.
    :param adf_file_path: Path to ADF15 file from ADAS root.
    :return: Dictionary containing rates.
    """
