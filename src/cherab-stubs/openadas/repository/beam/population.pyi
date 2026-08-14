from collections.abc import Mapping
from os import PathLike

from ....core.atomic import Element

_Path = str | PathLike[str]
_Rate = dict[str, object]

def add_beam_population_rate(beam_species: Element, beam_metastable: int, target_ion: Element, target_charge: int, rate: Mapping[str, object], repository_path: _Path | None = None) -> None: ...
def update_beam_population_rates(rates: Mapping[object, object], repository_path: _Path | None = None) -> None: ...
def get_beam_population_rate(beam_species: Element, beam_metastable: int, target_ion: Element, target_charge: int, repository_path: _Path | None = None) -> _Rate: ...
