from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ....atomic import AtomicData, Line
from ....beam import Beam

class BeamLineShapeModel:
    """
    A base class for building beam emission line shapes.

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Beam beam: The beam class that is emitting.
    :param AtomicData atomic_data: The atomic data provider.
    """

    def __init__(self, line: Line, wavelength: float, beam: Beam, atomic_data: AtomicData) -> None: ...
    def add_line(
        self,
        radiance: float,
        beam_point: Point3D,
        plasma_point: Point3D,
        beam_direction: Vector3D,
        observation_direction: Vector3D,
        spectrum: Spectrum,
    ) -> Spectrum: ...
