from os import PathLike

from ...core.atomic import Element as Element
from ...core.utility import Cm3ToM3 as Cm3ToM3
from ...core.utility import PerCm3ToPerM3 as PerCm3ToPerM3
from ...core.utility import RecursiveDict as RecursiveDict

def parse_adf11(element: Element, adf_file_path: str | PathLike[str]) -> dict[str, object]:
    """
    Reads contents of open adas adf11 files

    :param element: Element described by ADF file.
    :param adf_file_path: Path to ADF11 file from ADAS root.
    :return: temperature, density, rates as numpy array
    """
