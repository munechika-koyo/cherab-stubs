from collections.abc import Callable

from raysect.core.math import Point3D, Vector3D
from raysect.core.math.function.float import Function1D, Function2D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...atomic.elements import Element
from ...atomic.elements import Isotope as Isotope
from ...beam import Beam
from ...beam.model import BeamModel
from ...plasma import Plasma

PI2_TO_PI3: float
PI4_TO_PI3: float
SIGMA1_TO_SIGMA0: float
SIGMA_TO_PI: float
hydrogen: Element

class BeamEmissionLine(BeamModel):
    """Calculates beam emission multiplets for a single beam component.

    :param Line line: the transition of interest.
    """
    def __init__(
        self,
        line: Line,
        beam: Beam | None = None,
        plasma: Plasma | None = None,
        atomic_data: AtomicData | None = None,
        sigma_to_pi: Callable[[float, float], float] | Function2D = ...,
        sigma1_to_sigma0: Callable[[float], float] | Function1D = ...,
        pi2_to_pi3: Callable[[float], float] | Function1D = ...,
        pi4_to_pi3: Callable[[float], float] | Function1D = ...,
    ) -> None: ...
    @property
    def line(self) -> Line: ...
    @line.setter
    def line(self, value: Line) -> None: ...
    def emission(
        self,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
    def _change(self) -> None: ...
