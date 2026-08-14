from os import PathLike

from ...core.atomic.elements import *
from ...core.utility import RecursiveDict as RecursiveDict
from .. import repository as repository
from ..install import install_files as install_files

def populate(
    download: bool = True,
    repository_path: str | PathLike[str] | None = None,
    adas_path: str | PathLike[str] | None = None,
) -> None:
    """
    Populates the OpenADAS repository with a typical set of rates and wavelengths.

    If an ADAS file is not note found an attempt will be made to download the
    file from the OpenADAS website. This behaviour can be disabled by setting
    the download argument to False.

    :param download: Attempt to download the ADAS files if missing (default=True).
    :param repository_path: Alternate path for the OpenADAS repository (default=None).
    :param adas_path: Alternate path in which to search for ADAS files (default=None) .
    """
