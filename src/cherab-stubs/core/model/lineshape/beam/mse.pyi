from collections.abc import Callable

from raysect.core.math import Point3D, Vector3D
from raysect.core.math.function.float import Function1D, Function2D
from raysect.optical import Spectrum

from ....atomic import AtomicData, Line
from ....beam import Beam
from .base import BeamLineShapeModel

class BeamEmissionMultiplet(BeamLineShapeModel):
    """
    Produces Beam Emission Multiplet line shape, also known as the Motional Stark Effect spectrum.
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        beam: Beam,
        atomic_data: AtomicData,
        sigma_to_pi: Callable[[float, float], float] | Function2D,
        sigma1_to_sigma0: Callable[[float], float] | Function1D,
        pi2_to_pi3: Callable[[float], float] | Function1D,
        pi4_to_pi3: Callable[[float], float] | Function1D,
    ) -> None: ...
    def add_line(
        self,
        radiance: float,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
