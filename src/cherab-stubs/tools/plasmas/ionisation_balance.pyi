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

def _parameters_to_numpy(*parameters: object, free_variable: ArrayLike | None = None) -> list[NDArray[np.float64]]:
    """
    Check the consistency of parameters.

    Parameters can be scalar numbers, numpy arrays or dictionary of type {charge: rate}.

    :param parameters: List of parameters.
    :param free_variable: Free variable for the interpolating functions.
    :return: parameters formed into numpy array
    """

def _assign_donor_density(
    donor_density: _Profile | None,
    major_profile: NDArray[np.float64],
    free_variable: ArrayLike | None = None,
) -> NDArray[np.float64]:
    """
    If donor density is none, it should be assigned a zeros numpy array of the shape matching free_variable or
    major_profile if free_variable is None. It is populated if donor_density is an interpolating function.

    :param donor_density: donor density value or interpolator
    :param free_variable: free_variable value
    :param major_profile: major_profile value
    :return: numpy array
    """

def get_rates_ionisation(atomic_data: AtomicData, element: Element) -> dict[int, IonisationRate]:
    """
    Returns recombination rate interpolators for individual ion charges of the specified
    element from the specified data source.

    :param atomic_data: Any cherab Element
    :param element: Any cherab AtomicData source
    :return: dictionary of the form {charge: Interpolator}
    """

def get_rates_recombination(atomic_data: AtomicData, element: Element) -> dict[int, RecombinationRate]:
    """
    Returns recombination rate interpolators for individual ion charges of
    the specified element from the specified data source.

    :param atomic_data: Any cherab Element
    :param element: Any cherab AtomicData source
    :return: dictionary of the form {charge: Interpolator}
    """

def get_rates_tcx(atomic_data: AtomicData, donor: Element, donor_charge: int, receiver: Element) -> dict[int, ThermalCXRate]:
    """
    Returns thermal charge-exchange rate interpolators for individual ion charges of the
    specified element and donor from the specified data source.

    :param atomic_data: Any cherab AtomicData source
    :param donor: Element donating the electron in the CX collision.
    :param donor_charge: Charge of the donating element.
    :param receiver: Element receiving electron in the collision.
    :return: dictionary of the form {charge: Interpolator}
    """

def _fractional_abundance_point(
    element: Element,
    n_e: float,
    t_e: float,
    coef_ion: _Rates,
    coef_recom: _Rates,
    coef_tcx: _Rates | None = None,
    tcx_donor_density: float = 0,
) -> NDArray[np.float64]:
    """
    Calculate fractional abundance of charge states of the specified element, for the specified temperature and density using
    steady state ionization balance.

    If tcx_donor is specified, the balance equation will take into account effects
    of charge exchange with specified donor. The results are returned as fractional abundances i.e. ratio of the individual
    ionic charge state density to the overall element density.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab Element
    :param n_e: Electron density in m^-3 to calculate the balance for
    :param t_e: Electron temperature in eV to calculate the balance for
    :param coef_ion: Dictionary with ionization rates
    :param coef_recom: Dictionary with recombination rates
    :param coef_tcx: Optional, dictionary with thermal cx rates
    :param tcx_donor: Optional, any cherab element. Specifies donating species in tcx collisions.
    :param tcx_donor_density: Optional, mandatory if tcx_donor parameter passed. Specifies density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: array with fractional abundances of ionic charges. Array indexes correspond to ion charge state.
    """

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
) -> NDArray[np.float64]:
    """
    Calculate density of charge states of the specified element, for the specified electron temperature,
    electron density and absolute element density using steady state ionization balance.

    If tcx_donor is specified, the balance equation will take into account effects of charge exchange
    with the specified donor. The results are returned as density in m^-3.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab Element
    :param element_density: Density of the element in m^-3
    :param n_e: Electron density in m^-3 to calculate the balance for
    :param t_e: Electron temperature in eV to calculate the balance for
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. Specifies density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param coef_ion: Optional, ionization rates. If not passed rates will be loaded (slow).
    :param coef_recom: Optional, recombination rates. If not passed rates will be loaded (slow).
    :param coef_tcx: Optional, thermal cx rates. If not passed rates will be loaded (slow).
    :return: array with densities in m^-3 of ion charge states. Array indexes correspond to ion charge state.
    """

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
) -> NDArray[np.float64]:
    """
    Calculate density of charge states of the specified element, for the specified
    electron temperature and density.

    Ratio of densities of ionization stages of the element follows the steady state
    balance calculation for given electron properties. The absolute density of the
    element is determined to match the plasma neutrality (electron density) together
    with the other (provided) ion species densities. It is useful for example to fill
    in the bulk (e.g. hydrogen isotope or even helium) plasma element once rest of
    the impurities are known.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element to calculate matching density for
    :param n_species: list of arrays or dictionaries with ion densities of the rest of the plasma elements
    :param n_e: electron density in m^-3
    :param t_e: electron temperature in eV
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_density: Optional, mandatory if tcx_donor parameter passed. Specifies density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param coef_ion: Optional, ionization rates. If not passed rates will be loaded (slow).
    :param coef_recom: Optional, recombination rates. If not passed rates will be loaded (slow).
    :param coef_tcx: Optional, thermal cx rates. If not passed rates will be loaded (slow).
    :return: array with densities in m^-3 of ion charge states. Array indexes correspond to ion charge state.
    """

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
) -> NDArray[np.float64]:
    """
    Calculate Fractional abundance of the specified element for the specified
    electron density and temperature.

    Returns values of fractional abundances of the charge states of the element
    for given plasma parameters.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param n_e: numpy ndarray of values of electron density in m$^{-3}$
    :param t_e: numpy ndarray of values of electron temperature in [ev]
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. Numpy ndarray of values of electron density
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param coef_ion: Optional, ionization rates. If not passed rates will be loaded (slow).
    :param coef_recom: Optional, recombination rates. If not passed rates will be loaded (slow).
    :param coef_tcx: Optional, thermal cx rates. If not passed rates will be loaded (slow).
    :return: dim 0 corresponds to element charge state, dim > 0 correspond to dimensions of provided values.
    """

def fractional_abundance(
    atomic_data: AtomicData,
    element: Element,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
    free_variable: ArrayLike | None = None,
) -> dict[int, NDArray[np.float64]]:
    """
    Calculate Fractional abundance of the specified element for the specified electron density and temperature.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param n_e: Scalar, iterable or interpolating function of values of electron density in m$^{-3}$
    :param t_e: Scalar, iterable or interpolating function of values of electron temperature in [ev]
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. Scalar, iterable or interpolating function of values of electron density
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param free_variable: Mantadory if n_e, t_e or tcx_donor_n is an interpolating function. If 2D interpolator is passed
     free_variable has to be list or tuple of 1D arrays with coordinates
    :return: Dictionary with values of fractional abundances in the form {charge: values}
    """

def _from_elementdensity(
    atomic_data: AtomicData,
    element: Element,
    element_density: ArrayLike,
    n_e_profile: ArrayLike,
    t_e_profile: ArrayLike,
    tcx_donor: Element | None = None,
    tcx_donor_n_profile: ArrayLike | None = None,
    tcx_donor_charge: int = 0,
) -> NDArray[np.float64]:
    """
    For given plasma parameters the function calculates charge state densities of the element.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param element_density: Density profile of the element in m^-3
    :param n_e: numpy ndarray of values of electron density in m$^{-3}$
    :param t_e: numpy ndarray of values of electron temperature in [ev]
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. numpy ndarray of values of electron density
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: dim 0 corresponds to element charge state, dim > 0 correspond to dimensions of provided values.
    """

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
) -> dict[int, NDArray[np.float64]]:
    """
    For given plasma parameters the function calculates charge state densities of the element.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param element_density: Density profile of the element in m^-3
    :param n_e: Scalar or iterable of values of electron density in m$^{-3}$
    :param t_e: Scalar or iterable of values of electron temperature in [ev]
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. Scalar or iterable of values of donor density
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param free_variable: Mantadory if n_e, t_e or tcx_donor_n is an interpolating function.If 2D interpolator is passed
     free_variable has to be list or tuple of 1D arrays with coordinates
    :return: Dictionary with density profiles of charge states of the element in the form {charge: profile}
    """

def _match_plasma_neutrality(
    atomic_data: AtomicData,
    element: Element,
    n_species: ArrayLike,
    n_e_profile: ArrayLike,
    t_e_profile: ArrayLike,
    tcx_donor: Element | None = None,
    tcx_donor_n_profile: ArrayLike | None = None,
    tcx_donor_charge: int = 0,
) -> NDArray[np.float64]:
    """
    For given profiles of plasma parameters the function calculates density profiles of charge states of the element.

    The density is normalized using n_species_profiles and n_e_profiles to reach plasma neutrality condition.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param element_density_profile: Density profile of the element in m^-3
    :param n_e: Scalar or iterable of values of electron density in m$^{-3}$
    :param t_e: Scalar or iterable of values of electron temperature in [ev]
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. Scalar or iterable of values of donor density
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: Density profiles of charge states of the element. Dim 0 corresponds to charge of charge states.
    """

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
) -> dict[int, NDArray[np.float64]]:
    """
    For given profiles of plasma parameters the function calculates density profiles of charge states of the element.

    The density is normalized using n_species_profiles and n_e_profiles to reach plasme neutrality condition.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param element_density_profile: Density profile of the element in m^-3
    :param n_e: 1d profile giving values of electron density for free_variable
    :param t_e: 1d profile giving values of electron density for free_variable
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d profile giving density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :param free_variable: Mantadory if n_e, t_e or tcx_donor_n is an interpolating function. If 2D interpolator is passed
     free_variable has to be list or tuple of 1D arrays with coordinates
    :return: Dictionary with density profiles of charge states of the element in the form {charge: profile}
    """

def interpolators1d_fractional(
    atomic_data: AtomicData,
    element: Element,
    free_variable: ArrayLike,
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator1DArray]:
    """
    Creates 1d linear interpolators of fractional abundance of the specified element
    for the specified electron densities and temperatures.

    For more information see _fractional_abundance function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: Free variable (coordinate) to calculate the 1d fractional abundance interpolators from.If 2D interpolator is passed
     free_variable has to be list or tuple of 1D arrays with coordinates
    :param n_e_interpolator: 1d iterable or interpolator giving values of electron density for free_variable
    :param t_e_interpolator: 1d iterable or  interpolator giving values of electron density for free_variable
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n_interpolator: Optional, mandatory if tcx_donor parameter passed. 1d iterable interpolator giving
     density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: density}
    """

def interpolators2d_fractional(
    atomic_data: AtomicData,
    element: Element,
    free_variable: tuple[ArrayLike, ArrayLike],
    n_e: _Profile,
    t_e: _Profile,
    tcx_donor: Element | None = None,
    tcx_donor_n: _Profile | None = None,
    tcx_donor_charge: int = 0,
) -> dict[int, Interpolator2DArray]:
    """
    Creates 1d linear interpolators of fractional abundance of the specified element
    for the specified electron densities and temperatures.

    For more information see _fractional_abundance function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: Free variable (coordinate) to calculate the 1d fractional abundance interpolators from.If 2D interpolator is passed
     free_variable has to be list or tuple of 1D arrays with coordinates
    :param n_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param t_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n_interpolator: Optional, mandatory if tcx_donor parameter passed. 1d interpolator giving density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: density}
    """

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
) -> dict[int, Interpolator1DArray]:
    """
    Creates 1d linear interpolators of density profiles of the specified element for
    the specified electron densities and temperatures.

    For more information see _from_element_density function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: Free variable (coordinate) to calculate the 1d fractional abundance interpolators from.
    :param element_density: 1d iterable or an interpolator giving values of element density for free_variable in m^-3
    :param n_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param t_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n_interpolator: Optional, mandatory if tcx_donor parameter passed. 1d interpolator giving density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: interpolator}
    """

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
) -> dict[int, Interpolator1DArray]:
    """
    Creates 1d linear interpolators of density profiles of the specified
    element for the specified electron densities and temperatures.

    For more information see _match_element_density function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: Free variable (coordinate) to calculate the 1d fractional abundance interpolators from
    :param species_density: 1d interpolator giving values of the element density for free_variable
    :param n_e: 1d interpolator giving values of electron density for free_variable
    :param t_e: 1d interpolator giving values of electron density for free_variable
    :param tcx_donor: specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d interpolator giving density of donors in m^-3
    :param tcx_donor_charge:  Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: interpolator}
    """

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
) -> dict[int, Interpolator2DArray]:
    """
    Creates 1d linear interpolators of density profiles of the specified element
    for the specified electron densities and temperatures.

    For more information see _from_element_density function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: A tuple containing two 1D arrays of coordinate points
    :param element_density_interpolator: 1d interpolator giving values of element density for free_variable in m^-3
    :param n_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param t_e_interpolator: 1d interpolator giving values of electron density for free_variable
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n_interpolator: Optional, mandatory if tcx_donor parameter passed. 1d interpolator giving density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: interpolator}
    """

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
) -> dict[int, Interpolator2DArray]:
    """
    Creates 1d linear interpolators of density profiles of the specified element
    for the specified electron densities and temperatures.

    For more information see _match_element_density function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param free_variable: A tuple containing two 1D arrays of coordinate points
    :param species_density: 1d interpolator giving values of the element density for free_variable
    :param n_e: 1d interpolator giving values of electron density for free_variable
    :param t_e: 1d interpolator giving values of electron density for free_variable
    :param tcx_donor: specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d interpolator giving density of donors in m^-3
    :param tcx_donor_charge:  Optional, specifies the charge of the donor. Default is 0.
    :return: dictionary with 1d interpolators of fractional abundance of charge states of the element in the form {charge: interpolator}
    """

def abundance_axisymmetric_mapper(abundance: dict[int, Function2D]) -> dict[int, AxisymmetricMapper]:
    """
    Convert 2d abundance interpolators into AxisymmetricMapper.

    :param abundance: Dictionary with 2d Abundace/fractional abundance interpolators
    """

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
) -> dict[int, AxisymmetricMapper]:
    """
    Creates AxisymmetricMapper interpolator of fractional abundance of the specified
    element for the specified electron densities, temperatures and equilibrium by using
    the equilibrium.map3d function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param equilibrium: EFITEquilibrium object
    :param psin_1d:1D array with normalized poloidal flux coordinates
    :param n_e_profile: 1d iterable or interpolator giving values of electron density
    :param t_e_profile: 1d iterable or interpolator giving values of electron temperature
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d iterable interpolator giving
     density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    """

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
) -> dict[int, AxisymmetricMapper]:
    """
    Creates AxisymmetricMapper interpolator of fractional abundance of the
    specified element for the specified electron densities, temperatures,
    element densities and equilibrium by using the equilibrium.map3d function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param equilibrium: EFITEquilibrium object
    :param psin_1d:1D array with normalized poloidal flux coordinates
    :param element_density: 1d iterable or an interpolator giving values of element density for free_variable in m^-3
    :param n_e_profile: 1d iterable or interpolator giving values of electron density
    :param t_e_profile: 1d iterable or interpolator giving values of electron temperature
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d iterable interpolator giving
     density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    """

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
) -> dict[int, AxisymmetricMapper]:
    """
    Creates AxisymmetricMapper interpolator of fractional abundance of the specified
    element for the specified electron densities, temperatures
    and equilibrium by using the equilibrium.map3d function.

    :param atomic_data: Any cherab AtomicData source
    :param element: Any cherab element
    :param equilibrium: EFITEquilibrium object
    :param psin_1d:1D array with normalized poloidal flux coordinates
    :param species_density: list of 1d iterables interpolators giving values of element density for the values of psi in m^-3
    :param n_e_profile: 1d iterable or interpolator giving values of electron density
    :param t_e_profile: 1d iterable or interpolator giving values of electron temperature
    :param tcx_donor: Optional, specifies donating species in tcx collisions.
    :param tcx_donor_n: Optional, mandatory if tcx_donor parameter passed. 1d iterable interpolator giving
     density of donors in m^-3
    :param tcx_donor_charge: Optional, specifies the charge of the donor. Default is 0.
    """
