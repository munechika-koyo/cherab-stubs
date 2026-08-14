from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...plasma import Plasma
from ...species import Species
from .base import LineShapeModel

def add_gaussian_line(radiance: float, wavelength: float, sigma: float, spectrum: Spectrum) -> Spectrum: ...

class GaussianLine(LineShapeModel):
    """
    Produces Gaussian line shape.

    :param Line line: The emission line object for this line shape.
    :param float wavelength: The rest wavelength for this emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.

    .. code-block:: pycon

       >>> from cherab.core.atomic import Line, deuterium
       >>> from cherab.core.model import ExcitationLine, GaussianLine
       >>>
       >>> # Adding Gaussian line to the plasma model.
       >>> d_alpha = Line(deuterium, 0, (3, 2))
       >>> excit = ExcitationLine(d_alpha, lineshape=GaussianLine)
       >>> plasma.models.add(excit)
    """

    def __init__(self, line: Line, wavelength: float, target_species: Species, plasma: Plasma, atomic_data: AtomicData) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
