from raysect.core import Node, Vector3D
from raysect.core.math.function.float.function3d.base import Function3D

from ...core.atomic.elements import Element
from ...core.distribution import Maxwellian as Maxwellian
from ...core.plasma.node import Plasma as Plasma
from ...core.species import Species as Species

atomic_mass: float

electron_mass: float
hydrogen: Element

class NeutralFunction(Function3D):
    """A neutral profile that is constant outside the plasma, then exponentially decays
    inside the plasma boundary."""

    def __init__(self, peak_value: float, sigma: float, pedestal_top: float = 1) -> None: ...

class IonFunction(Function3D):
    """An approximate pedestal plasma profile that follows a double
    quadratic between the plasma boundary and the pedestal top."""

    def __init__(self, t_core: float, t_lcfs: float, p: float = 2, q: float = 2, pedestal_top: float = 1) -> None: ...

def build_slab_plasma(
    length: float = 5,
    width: float = 1,
    height: float = 1,
    peak_density: float = 1e19,
    peak_temperature: float = 2500,
    pedestal_top: float = 1,
    neutral_temperature: float = 0.5,
    impurities: list[tuple[Element, int, float]] | None = None,
    parent: Node | None = None,
) -> Plasma:
    """
    Constructs a simple slab of plasma.

    The plasma is defined for positive x starting at x = 0, symmetric in y-z. The plasma
    parameters such as electron density and temperature evolve in 1 dimension according
    to the input parameters specified. The slab includes an optional pedestal.

    Raysect cannot handle infinite geometry, so overall spatial dimensions of the slab need
    to be set, [length, width, height]. These can be set very large to make an effectively
    infinite slab of plasma, although the numerical performance will degrade accordingly.
    The dimensions should be set appropriately with valid assumptions for your scenario.

    Impurity species can be included as a list of tuples, where each tuple specifies an
    impurity. The specification format is (species, charge, concentration). For example:

        >>> impurities=[(carbon, 6, 0.005)]

    :param float length: the overall length of the slab along x.
    :param float width: the y width of the slab.
    :param float height: the z height of the slab.
    :param float peak_density: the peak electron density at the pedestal top.
    :param float peak_temperature: the peak electron temperature at the pedestal top.
    :param float pedestal_top: the length of the pedestal top.
    :param float neutral_temperature: the background neutral temperature.
    :param list impurities: an optional list of impurities to include.
    :param parent: the Raysect scene-graph parent node.
    :param atomic_data: the atomic data provider to use for subsequent spectroscopic calculations,
      defaults to atomic_data=OpenADAS(permit_extrapolation=True).

    .. code-block:: pycon

       >>> from raysect.optical import World
       >>> from cherab.core.atomic import carbon
       >>> from cherab.tools.plasmas.slab import build_slab_plasma
       >>>
       >>> plasma = build_slab_plasma(peak_density=5e19, impurities=[(carbon, 6, 0.005)])
       >>> plasma.parent = World()
    """

def build_constant_slab_plasma(
    length: float = 5,
    width: float = 1,
    height: float = 1,
    electron_density: float = 1e19,
    electron_temperature: float = 2.5e3,
    plasma_species: list[tuple[Element, int, float, float, Vector3D]] | None = None,
    b_field: Vector3D = ...,
    parent: Node | None = None,
) -> Plasma:
    """
    Constructs a simple slab of plasma with constant conditions.

    The plasma is defined for positive x starting at x = 0, symmetric in y-z. The plasma
    parameters such as electron density and temperature are constant over the plasma volume.

    Raysect cannot handle infinite geometry, so overall spatial dimensions of the slab need
    to be set, [length, width, height]. These can be set very large to make an effectively
    infinite slab of plasma, although the numerical performance will degrade accordingly.
    The dimensions should be set appropriately with valid assumptions for your scenario.

    Ion species can be included as a list of tuples, where each tuple specifies an
    impurity. The specification format is (species, charge, density, temperature, velocity). For example:

        >>> plasma_species = [(carbon, 6, 1e18, 3.4e3, Vector3D(1.0e3, 0, 0))]

    If omitted, hydrogen distribution with properties equal to electrons is used:
        >>> plasma_species = [(hydrogen, 1, electron_density, electron_temperature, Vector3D(0, 0, 0))]

    If an empty list is passed, plasma contains only electrons.

    :param float length: the overall length of the slab along x.
    :param float width: the y width of the slab.
    :param float height: the z height of the slab.
    :param float electron_density: the electron density in m^-3 .
    :param float electron_temperature: the electron temperature in eV.
    :param list plasma_species: an optional list of impurities to include.
    :param Vector3D b_field: vector giving the magnetic field
    :param parent: the Raysect scene-graph parent node.

    .. code-block:: pycon

       >>> from raysect.optical import World
       >>> from cherab.core.atomic import hydrogen, carbon
       >>> from cherab.tools.plasmas.slab import build_constant_slab_plasma
       >>>
       >>> plasma_species = [(hydrogen, 0, 1e19, 3.5e3, Vector3D(5e3, 0, 0)), (carbon, 5, 1e18, 3.4e3, Vector3D(1.0e3, 0, 0))]
       >>> plasma = build_constant_slab_plasma(0.2, 0.5, 0.5, electron_density = 1.19, electron_temperature=4e4, plasma_species=plasma_species, b_field=Vector3D(0, 5, 0))
       >>> plasma.parent = World()
    """
