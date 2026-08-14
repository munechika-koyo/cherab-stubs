from collections.abc import Callable, Mapping

from raysect.core import Node
from raysect.core.math.function.float import Function1D

from ...core import AtomicData, Maxwellian, Plasma
from ...tools.equilibrium import EFITEquilibrium

_ProfileTree = Mapping[str, object]
_ScalarFunction1D = Callable[[float], float] | Function1D

def load_edge_profiles() -> dict[str, object]: ...
def get_edge_interpolators() -> dict[str, object]: ...
def get_2d_distributions(profiles_2d: _ProfileTree | None = None) -> dict[str, object]: ...
def get_edge_plasma(
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak edge plasma",
) -> Plasma: ...
def load_core_profiles() -> dict[str, object]: ...
def get_core_interpolators() -> dict[str, object]: ...
def get_double_parabola(
    v_min: float,
    v_max: float,
    convexity: float,
    concavity: float,
    xmin: float = 0,
    xmax: float = 1,
) -> Function1D: ...
def get_exponential_growth(initial_value: float, growth_rate: float, initial_position: float = 1) -> Function1D: ...
def get_maxwellian_distribution(
    equilibrium: EFITEquilibrium,
    f1d_density: _ScalarFunction1D,
    f1d_temperature: _ScalarFunction1D,
    f1d_vtor: _ScalarFunction1D,
    f1d_vpol: _ScalarFunction1D,
    f1d_vnorm: _ScalarFunction1D,
    rest_mass: float,
) -> Maxwellian: ...
def get_edge_profile_values(r: float, z: float, edge_interpolators: _ProfileTree | None = None) -> dict[str, object]: ...
def get_core_profiles_arguments(**kwargs: float) -> dict[str, object]: ...
def get_core_profiles_description(lcfs_values: _ProfileTree | None = None, core_args: _ProfileTree | None = None) -> dict[str, object]: ...
def get_core_distributions(
    profiles: _ProfileTree | None = None,
    equilibrium: EFITEquilibrium | None = None,
) -> dict[str, object]: ...
def get_core_plasma(
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak core plasma",
) -> Plasma: ...
def get_full_profiles(
    equilibrium: EFITEquilibrium | None = None,
    core_profiles: _ProfileTree | None = None,
    edge_profiles: _ProfileTree | None = None,
    mask: object | None = None,
) -> dict[str, object]: ...
def get_plasma(
    equilibrium: EFITEquilibrium | None = None,
    distributions: _ProfileTree | None = None,
    r_range: tuple[float, float] | None = None,
    z_range: tuple[float, float] | None = None,
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak plasma",
) -> Plasma: ...
