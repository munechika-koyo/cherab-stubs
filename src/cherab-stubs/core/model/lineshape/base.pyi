from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...math.integrators import Integrator1D
from ...plasma import Plasma
from ...species import Species

class LineShapeModel:
    """
    A base class for building line shapes.

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param Integrator1D integrator: Integrator1D instance to integrate the line shape
        over the spectral bin. Default is None.
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        integrator: Integrator1D | None = None,
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
