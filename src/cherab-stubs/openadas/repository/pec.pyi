from collections.abc import Mapping
from os import PathLike

from ...core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]
_Transition = tuple[int, int]

def add_pec_excitation_rate(element: Element, charge: int, transition: _Transition, rate: Mapping[str, object], repository_path: _Path | None = None) -> None: ...
def add_pec_recombination_rate(element: Element, charge: int, transition: _Transition, rate: Mapping[str, object], repository_path: _Path | None = None) -> None: ...
def add_pec_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    receiver_charge: int,
    transition: _Transition,
    rate: Mapping[str, object],
    repository_path: _Path | None = None,
) -> None: ...
def update_pec_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None: ...
def update_pec_thermal_cx_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None: ...
def get_pec_excitation_rate(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> _Rate: ...
def get_pec_recombination_rate(element: Element, charge: int, transition: _Transition, repository_path: _Path | None = None) -> _Rate: ...
def get_pec_thermal_cx_rate(
    donor_element: Element,
    donor_charge: int,
    receiver_element: Element,
    receiver_charge: int,
    transition: _Transition,
    repository_path: _Path | None = None,
) -> _Rate: ...
