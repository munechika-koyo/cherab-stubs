from collections.abc import Callable, Mapping

from raysect.core import Node
from raysect.core.math.function.float import Function1D

from ...core import AtomicData, Maxwellian, Plasma
from ...tools.equilibrium import EFITEquilibrium

_ProfileTree = Mapping[str, object]
_ScalarFunction1D = Callable[[float], float] | Function1D

def load_edge_profiles() -> dict[str, object]:
    """
    Loads Generomak edge plasma profiles

    Return a single dictionary with available edge and plasma species temperature and
    density profiles. The profiles are saved on a 2D triangular mesh.

    :return: dictionary with mesh, electron and plasma composition profiles

    .. code-block:: pycon
       >>> # This example shows how to load data and create 2D edge interpolators
       >>>
       >>> from raysect.core.math.function.float.function2d.interpolate import Discrete2DMesh
       >>>
       >>>
       >>> data = load_edge_profiles()
       >>>
       >>> # create electron temperature 2D mesh interpolator
       >>> te = Discrete2DMesh(data["mesh"]["vertex_coords"],
                               data["mesh"]["triangles"],
                               data["electron"]["temperature"], limit=False)

       >>> # create hydrogen 0+ density 2D mesh interpolator
       >>> n_h0 = Discrete2DMesh.instance(te, data["composition"]["hydrogen"][0]["temperature"])
    """

def get_edge_interpolators() -> dict[str, object]:
    """
    Provides Generomak edge profiles 2d interpolator

    :return: dictionary holding instances of Discrete2DMesh density
             and temperature interpolators for plasma species
    """

def get_2d_distributions(profiles_2d: _ProfileTree | None = None) -> dict[str, object]:
    """
    Provides Generomak Maxwellian distribution of plasma species for 2d profiles

    :param profiles_2d: Dictionary with 2D profile interpolators in the shape
                        returned by the get_edge_interpolators() or get_full_profiles() functions.
                        If not specified, will use the value returned by get_edge_interpolators().
    :return: Dictionary holding instances of Maxwellian distributions for plasma species.
    """

def get_edge_plasma(
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak edge plasma",
) -> Plasma:
    """
    Provides Generomak default edge plasma.

    :param atomic_data: Instance of AtomicData, default is OpenADAS()
    :param parent: parent of the plasma node, defaults None
    :param name: name of the plasma node, defaults "Generomak edge plasma"
    :return: populated Plasma object
    """

def load_core_profiles() -> dict[str, object]:
    """
    Loads Generomak default core plasma profiles.

    Return a single dictionary with available core plasma species temperature and
    density profiles on a magnetic surface coordinate grid.

    :return: dictionary with electron and plasma composition profiles
    """

def get_core_interpolators() -> dict[str, object]:
    """
    Provides 1d interpolators for Generomak default core profiles.

    :return: dictionary holding 1D interpolators of density,
             temperature and velocity for plasma species
    """

def get_double_parabola(
    v_min: float,
    v_max: float,
    convexity: float,
    concavity: float,
    xmin: float = 0,
    xmax: float = 1,
) -> Function1D:
    """
    Returns a 1d double-quadratic Function1D

    The retuned Function1D is of the form

    .. math:: f(x) = ((v_{max} - v_{min}) * ((1 - ((1 - x_{norm}) ** convexity)) ** concavity) + v_min)

    where the :math: `x_norm` is calculated as

    .. math:: x_{norm} = (x - xmin) / (xmax - xmin).

    The returned function is decreasing and monotonous and its domain is [xmin, xmax].

    :param v_min: The minimum value of the profile at xmax.
    :param v_max: The maximum value of the profile at xmin.
    :param convexity: Controls the convexity of the profile in the lower values part of the profile.
    :param concavity: Controls the concavity of the profile in the higher values part of the profile.
    :param xmin: The lower edge of the function domain. Defaults to 0.
    :param xmax: The upper edge of the function domain Defaults to 1.
    :return: Function1D
    """

def get_exponential_growth(initial_value: float, growth_rate: float, initial_position: float = 1) -> Function1D:
    r"""
    returns exponentially growing Function1D

    The returned Function1D is of the form:

    ::math::
      v_0 \exp((x - x_0) * \lambda)

    where v_0 is the initial_value, x_0 is the initial_position and lambda is the growth_rate.

    :param initial_value: The value of the function at the initial position.
    :param growth_rate: Growth constant of the profile.
    :param initial_position: The initial position of the profile. Defaults to 1.
    :return: Function1D
    """

def get_maxwellian_distribution(
    equilibrium: EFITEquilibrium,
    f1d_density: _ScalarFunction1D,
    f1d_temperature: _ScalarFunction1D,
    f1d_vtor: _ScalarFunction1D,
    f1d_vpol: _ScalarFunction1D,
    f1d_vnorm: _ScalarFunction1D,
    rest_mass: float,
) -> Maxwellian:
    """
    Returns Maxwellian distribution for equilibrium mapped 1d profiles

    :param equilibrium: Instance of EFITEquilibrium
    :param f1d_density: Function1D describing density profile.
    :param f1d_temperature: Function1D describing temperature profile.
    :param f1d_vtor: Function1D describing bulk toroidal rotation velocity profile.
    :param f1d_vpol: Function1D describing bulk poloidal rotation velocity profile.
    :param f1d_vnorm: Function1D describing bulk velocity normal to magnetic surfaces.
    :rest_mass: Rest mass of the distribution species.
    :return: Maxwellian distribution
    """

def get_edge_profile_values(r: float, z: float, edge_interpolators: _ProfileTree | None = None) -> dict[str, object]:
    """
    Evaluate edge plasma profiles at the position [r, z]

    :param r: Radial distance in cylindrical coordinates in m.
    :param z: Elevation in cylindrical coordinates in m.
    :param edge_interpolators: Dictionary with edge interpolators in the shape
           returned by the get_edge_interpolators function.
    :return: Dictionary of edge values at [R, Z]
    """

def get_core_profiles_arguments(**kwargs: float) -> dict[str, object]:
    """
    Returns dictionary with core profile arguments

    The function compares the passed keyword arguments with the list of core profile arguments (listed below).
    If there is a match, the default value is overwritten by th passed value, the default value is kept
    otherwise.

    List of core parameters, their meaning and default values
        ne_core: (default 5e19) core electron density
        ne_convexity: (default 1.09) (default ) convexity of the electron density profile
        ne_concavity: (default 0.24) concavity of the electron density profile
        te_core core: (default 3e3) electron temperature
        te_convexity: (default 2.35) convexity of the electron temperature profile
        te_concavity: (default 1.26) concavity of the electron temperature profile
        th_core: (default 2.8e3) H1+ temperature
        th_convexity: (default 2) convexity of H1+ temperature profile
        th_concavity: (default 1.26) concavity of H1+ temperature profile
        th0_fraction: (default 0.8) H0 temperature factor
        timp_core: (default 2.8e3) core impurity temperature
        timp_convexity: (default 2) convexity of impurity temperature profile
        timp_concavity: (default 1.26) concavity of impurity temperature profile
        nimp_core: (default 5e17) impurity density
        nimp_convexity: (default 1.09) convexity of impurity density profile
        nimp_concavity: (default 0.24) concavity of impurity density profile
        vtor_core: (default 1e5) toroidal rotation velocity m/s
        vtor_edge: (default 1e4) toroidal rotation velocity at the edge m/s
        vtor_convexity: (default 2) convexity of the toroidal rotation profile
        vtor_concavity: (default 4) concavity of the toroidal rotation profile
        vpol_lcfs: (default 2e4) Bulk poloidal rotation velocity in m/s
        vpol_decay: (default 0.08) Decay rate of poloidal rotation velocity

    :return: dictionary of profile arguments
    """

def get_core_profiles_description(lcfs_values: _ProfileTree | None = None, core_args: _ProfileTree | None = None) -> dict[str, object]:
    """
    Returns dictionary of core profile functions and species descriptions

    :param lcfs_values: Dictionary of profile values at the separatrix on outer midplane.
                        The dictionary has to have the same format as the one returned by
                        the function get_edge_profile_values. The default value is the
                        dictionary returned by the call get_edge_profile_values for r, z
                        on last closed flux surface on outer midplane.
    :param core_args: Dictionary with arguments describing the core profiles. The dictionary
                      has to have the same shape as the one returned by the function
                      get_core_profiles_description. The default value is the dictionary
                      returned by the get_core_profiles() call.
    :return: dictionary of Function1D profiles
    """

def get_core_distributions(
    profiles: _ProfileTree | None = None,
    equilibrium: EFITEquilibrium | None = None,
) -> dict[str, object]:
    """
    Returns a dictionary of core plasma species Maxwellian distributions.

    :param profiles: Dictionary with core interpolators. The dictionary has to have
                     the same form as the one returned by the function
                     get_core_profiles_description or get_core_interpolators.
                     The default value is the value returned by the call
                     get_core_interpolators().
    :param equilibrium: an instance of EFITEquilibrium.
    :return:  dictionary of core plasma species with Maxwellian distribution
    """

def get_core_plasma(
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak core plasma",
) -> Plasma:
    """
    Provides Generomak default core plasma.

    :param atomic_data: Instance of AtomicData, default is OpenADAS()
    :param parent: parent of the plasma node, defaults None
    :param name: name of the plasma node, defaults "Generomak edge plasma"
    :return: populated Plasma object
    """

def get_full_profiles(
    equilibrium: EFITEquilibrium | None = None,
    core_profiles: _ProfileTree | None = None,
    edge_profiles: _ProfileTree | None = None,
    mask: object | None = None,
) -> dict[str, object]:
    """
    Blends core and edge profiles using the mask function as a modulator.

    :param equilibrium: an instance of EFITEquilibrium. The default value is the value returned by
                        load_equilibrium().
    :param core_profiles: Dictionary with core interpolators. The dictionary has to have
                          the same form as the one returned by the function
                          get_core_profiles_description or get_core_interpolators.
                          The default value is the value returned by the call
                          get_core_interpolators().
    :param edge_profiles: Dictionary with edge interpolators in the shape
                          returned by the get_edge_interpolators function.
                          If not specified, will use the value returned by
                          get_edge_interpolators().
    :param Function2D mask: Scalar 2D function returning a value in the range [0, 1].
                            If not specified, will use core profiles for psi_normal < 0.94,
                            the edge profiles for psi_normal > 1 and a weighted sum of core and
                            edge profiles for 0.94 < psi_normal < 1, with the edge profile weight
                            increasing from 0 to 1 linearly.

    :return: dictionary of blended plasma profiles with the structure identical to edge_profiles.
    """

def get_plasma(
    equilibrium: EFITEquilibrium | None = None,
    distributions: _ProfileTree | None = None,
    r_range: tuple[float, float] | None = None,
    z_range: tuple[float, float] | None = None,
    atomic_data: AtomicData | None = None,
    parent: Node | None = None,
    name: str = "Generomak plasma",
) -> Plasma:
    """
    Provides Generomak plasma. The full (core + edge) plasma is returned by default.

    :param equilibrium: an instance of EFITEquilibrium. The default value is the value returned by load_equilibrium().
    :param distributions: A dictionary of plasma distributions. Has to have the same format as the
                          dictionary returned by get_core_distributions or get_2d_distributions.
                          The default value is the value returned by the call:
                          get_2d_distributions(get_full_profiles(equilibrium)).
    :param r_range: Plasma domain range (min, max) in R direction in meters.
    :param z_range: Plasma domain range (min, max) in Z direction in meters.
    :param atomic_data: Instance of AtomicData, default is OpenADAS()
    :param parent: parent of the plasma node, defaults None
    :param name: name of the plasma node, defaults "Generomak plasma"
    :return: populated Plasma object
    """
