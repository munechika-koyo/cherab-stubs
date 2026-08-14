from os import PathLike
from typing import TextIO

from ...core.atomic import Element
from ...core.utility import RecursiveDict as RecursiveDict
from ...core.utility.conversion import Cm3ToM3 as Cm3ToM3
from ...core.utility.conversion import PerCm3ToPerM3 as PerCm3ToPerM3
from .utility import readvalues as readvalues

def parse_adf12(
    donor_ion: Element,
    donor_metastable: int,
    receiver_ion: Element,
    receiver_charge: int,
    adf_file_path: str | PathLike[str],
) -> dict[str, object]:
    """
    Opens and parses ADAS ADF12 data files.

    :param donor_ion: The donor ion element described by the rate file.
    :param donor_metastable: The donor ion metastable level.
    :param receiver_ion: The receiver ion element described by the rate file.
    :param receiver_charge: The receiver ion charge state described by the rate file.
    :param adf_file_path: Path to ADF15 file from ADAS root.
    :return: Dictionary containing rates.
    """

def _parse_block(file: TextIO) -> tuple[tuple[int, int], dict[str, object]]:
    """
    Reads and parses an ADF12 rate block from an IO stream.

    :param file: Text stream sought to the start of the block.
    :return: Tuple containing (transition tuple, rate data dictionary).
    """
