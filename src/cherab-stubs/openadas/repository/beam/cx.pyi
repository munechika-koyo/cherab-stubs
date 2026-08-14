from collections.abc import Mapping
from os import PathLike

from ....core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_beam_cx_rate(
    donor_ion: Element, donor_metastable: int, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int], rate: Mapping[str, object], repository_path: _Path | None = None
) -> None: ...
def update_beam_cx_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None: ...
def get_beam_cx_rates(donor_ion: Element, receiver_ion: Element, receiver_charge: int, transition: tuple[int, int], repository_path: _Path | None = None) -> list[_Rate]: ...
