from collections.abc import Generator
from os import PathLike
from typing import Literal, TextIO

from ...core.atomic import Element as Element
from ...core.atomic import hydrogen as hydrogen
from ...core.utility import RecursiveDict as RecursiveDict
from ...core.utility.conversion import Cm3ToM3 as Cm3ToM3
from ...core.utility.conversion import PerCm3ToPerM3 as PerCm3ToPerM3

_L_LOOKUP: dict[int, str]

def parse_adf15(
    element: Element,
    charge: int,
    adf_file_path: str | PathLike[str],
    header_format: Literal["hydrogen", "hydrogen-like"] | None = None,
) -> tuple[dict[str, object], dict[object, object]]:
    """
    Opens and parses ADAS ADF15 data files.

    :param element: Element described by ADF file.
    :param charge: Charge state described by ADF file.
    :param adf_file_path: Path to ADF15 file from ADAS root.
    :return: Dictionary containing rates.
    """

def _scrape_metadata_hydrogen(file: TextIO, element: Element, charge: int) -> dict[str, object]:
    """
    Scrapes transition and block information from the comments.
    """

def _scrape_metadata_hydrogen_like(file: TextIO, element: Element, charge: int) -> dict[str, object]:
    """
    Scrapes transition and block information from the comments.
    """

def _scrape_metadata_full(file: TextIO, element: Element, charge: int) -> dict[str, object]:
    """
    Scrapes transition and block information from the comments.
    """

def _extract_rate(file: TextIO, block_num: int) -> dict[str, object]:
    """
    Reads and converts the rate data for the specified block.
    """

def _group_by_block(source_file: TextIO, match_string: str) -> Generator[list[str]]:
    """
    Generator the splits the ADF15 file into blocks.

    Groups lines of file into blocks based on precursor '  6561.9A   24...'

    Note: comment section not filtered out of last block, don't over-read!
    """
