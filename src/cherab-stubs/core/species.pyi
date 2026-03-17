from .atomic import Element
from .distribution import DistributionFunction

class Species:
    """
    A class representing a given plasma species.

    A plasma in Cherab will be composed of 1 or more Species objects. A species
    can be uniquely identified through its element and charge state.

    When instantiating a Species object a 6D distribution function (3 space, 3 velocity)
    must be defined. The DistributionFunction object provides the base interface for
    defining a distribution function, it could be a reduced analytic representation
    (such as a Maxwellian for example) or a fully numerically interpolated 6D function.

    :param Element element: The element object of this species.
    :param int charge: The charge state of the species.
    :param DistributionFunction distribution: A distribution function for this species.

    .. code-block:: pycon

       >>> # In this example we define a single plasma species with spatially homogeneous properties
       >>>
       >>> from scipy.constants import atomic_mass
       >>> from raysect.core.math import Vector3D
       >>> from cherab.core import Species, Maxwellian
       >>> from cherab.core.atomic import deuterium
       >>>
       >>> # Setup a distribution function for the species
       >>> density = 1e18
       >>> temperature = 10
       >>> bulk_velocity = Vector3D(-1e6, 0, 0)
       >>> d1_distribution = Maxwellian(
       ...     density, temperature, bulk_velocity, deuterium.atomic_weight * atomic_mass
       ... )
       >>>
       >>> # create the plasma Species object
       >>> d1_species = Species(deuterium, 1, d1_distribution)
       >>>
       >>> # Request some properties from the species' distribution function.
       >>> print(d1_species)
       <Species: element=deuterium, charge=1>
       >>> d1_species.distribution.density(1, -2.5, 7)
       1e+18
    """

    element: Element
    charge: int
    distribution: DistributionFunction

    def __init__(self, element: Element, charge: int, distribution: DistributionFunction) -> None: ...
    def __repr__(self) -> str: ...

class SpeciesNotFound(Exception): ...
