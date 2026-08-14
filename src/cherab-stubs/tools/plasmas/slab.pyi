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
) -> Plasma: ...
def build_constant_slab_plasma(
    length: float = 5,
    width: float = 1,
    height: float = 1,
    electron_density: float = 1e19,
    electron_temperature: float = 2.5e3,
    plasma_species: list[tuple[Element, int, float, float, Vector3D]] | None = None,
    b_field: Vector3D = ...,
    parent: Node | None = None,
) -> Plasma: ...
