from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Transition = tuple[int, int]

def add_wavelength(element: Element, charge: int, transition: _Transition, wavelength: float, repository_path: _Path | None = None) -> None: ...
def update_wavelengths(wavelengths: Mapping[object, object], repository_path: _Path | None = None) -> None: ...
def get_wavelength(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> float: ...
