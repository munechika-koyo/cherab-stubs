from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray
from raysect.core.math.function.float import Function1D, Function2D, Interpolator1DArray
from raysect.core.math.function.float.function2d import Interpolator2DArray

from ...core import AtomicData
from ...core.atomic import Element
from ...core.atomic.rates import IonisationRate, RecombinationRate, ThermalCXRate
from ...core.math import AxisymmetricMapper
from ..equilibrium import EFITEquilibrium

_Profile = ArrayLike | Function1D | Function2D | Callable[..., float]
_Rates = dict[int, IonisationRate | RecombinationRate | ThermalCXRate]

def _parameters_to_numpy(*parameters: object, free_variable: ArrayLike | None = None) -> list[NDArray[np.float64]]: ...
def _assign_donor_density(
    donor_density: _Profile | None,
    major_profile: NDArray[np.float64],
    free_variable: ArrayLike | None = None,
) -> NDArray[np.float64]: ...
def get_rates_ionisation(atomic_data: AtomicData, element: Element) -> dict[int, IonisationRate]: ...
def get_rates_recombination(atomic_data: AtomicData, element: Element) -> dict[int, RecombinationRate]: ...
def get_rates_tcx(atomic_data: AtomicData, donor: Element, donor_charge: int, receiver: Element) -> dict[int, ThermalCXRate]: ...
def _fractional_abundance_point(
    element: Element,
    n_e: float,
    t_e: float,
    coef_ion: _Rates,
    coef_recom: _Rates,
    coef_tcx: _Rates | None = None,
    tcx_donor_density: float = 0,
) -> NDArray[np.float64]: ...
def _from_element_density_point(
    atomic_data: AtomicData,
    element: Element,
    element_density: float,
    n_e: float,
    t_e: float,
    tcx_donor: Element | None = None,
    tcx_donor_n: float | None = None,
    tcx_donor_charge: int = 0,
    coef_ion: _Rates | None = None,
    coef_recom: _Rates | None = None,
    coef_tcx: _Rates | None = None,
) -> NDArray[np.float64]: ...
def _match_element_density_point(
    atomic_data: AtomicData,
    element: Element,
    n_species: float,
    n_e: float,
    t_e: float,
    tcx_donor: Element | None = None,
    tcx_donor_density: float | None = None,
    tcx_donor_charge: int = 0,
    coef_ion: _Rates | None = None,
    coef_recom: _Rates | None = None,
    coef_tcx: _Rates | None = None,
) -> NDArray[np.float64]: ...
def _fractional_abundance(
    atomic_data: AtomicData,
    element: Element,
    n_e: ArrayLike,
    t_e: ArrayLike,
    tcx_donor: Element | None = None,
    tcx_donor_n: ArrayLike | None = None,
    tcx_donor_charge: int = 0,
    coef_ion: _Rates | None = None,
    coef_recom: _Rates | None = None,
    coef_tcx: _Rates | None = None,
) -> NDArray[np.float64]: ...
def fractional_abundance(
    atomic_data: AtomicData,
    element: Element,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
    free_variable: ArrayLike | None = None,
) -> dict[int, NDArray[np.float64]]: ...
def _from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    element_density: ArrayLike,
    n_e_profile: ArrayLike,
    t_e_profile: ArrayLike,
    tcx_donor: Element | None = None,
    tcx_donor_n_profile: ArrayLike | None = None,
    tcx_donor_charge: int = 0,
) -> NDArray[np.float64]: ...
def from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    element_density: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
    free_variable: ArrayLike | None = None,
) -> dict[int, NDArray[np.float64]]: ...
def _match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    n_species: ArrayLike,
    n_e_profile: ArrayLike,
    t_e_profile: ArrayLike,
    tcx_donor: Element | None = None,
    tcx_donor_n_profile: ArrayLike | None = None,
    tcx_donor_charge: int = 0,
) -> NDArray[np.float64]: ...
def match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    n_species: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
    free_variable: ArrayLike | None = None,
) -> dict[int, NDArray[np.float64]]: ...
def interpolators1d_fractional(
    atomic_data: AtomicData,
    element: Element,
    free_variable: ArrayLike,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator1DArray]: ...
def interpolators2d_fractional(
    atomic_data: AtomicData,
    element: Element,
    free_variable: tuple[ArrayLike, ArrayLike],
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator2DArray]: ...
def interpolators1d_from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    free_variable: ArrayLike,
    element_density: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator1DArray]: ...
def interpolators1d_match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    free_variable: ArrayLike,
    species_density: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator1DArray]: ...
def interpolators2d_from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    free_variable: tuple[ArrayLike, ArrayLike],
    element_density: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator2DArray]: ...
def interpolators2d_match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    free_variable: tuple[ArrayLike, ArrayLike],
    species_density: _Profile,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator2DArray]: ...
def abundance_axisymmetric_mapper(abundance: dict[int, Function2D]) -> dict[int, AxisymmetricMapper]: ...
def equilibrium_map3d_fractional(
    atomic_data: AtomicData,
    element: Element,
    equilibrium: EFITEquilibrium,
    psin_1d: ArrayLike,
    n_e_profile: _Profile,
    t_e_profile: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, AxisymmetricMapper]: ...
def equilibrium_map3d_from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    equilibrium: EFITEquilibrium,
    psin_1d: ArrayLike,
    n_element: _Profile,
    n_e_profile: _Profile,
    t_e_profile: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, AxisymmetricMapper]: ...
def equilibrium_map3d_match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    equilibrium: EFITEquilibrium,
    psin_1d: ArrayLike,
    species_density: _Profile,
    n_e_profile: _Profile,
    t_e_profile: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, AxisymmetricMapper]: ...
