from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...plasma import Plasma
from ...species import Species
from .base import LineShapeModel

def add_gaussian_line(radiance: float, wavelength: float, sigma: float, spectrum: Spectrum) -> Spectrum:
    r"""
    Adds a Gaussian line to the given spectrum and returns the new spectrum.

    The formula used is based on the following definite integral:
    :math:`\frac{1}{\sigma \sqrt{2 \pi}} \int_{\lambda_0}^{\lambda_1} \exp(-\frac{(x-\mu)^2}{2\sigma^2}) dx = \frac{1}{2} \left[ -Erf(\frac{a-\mu}{\sqrt{2}\sigma}) +Erf(\frac{b-\mu}{\sqrt{2}\sigma}) \right]`

    :param float radiance: Intensity of the line in radiance.
    :param float wavelength: central wavelength of the line in nm.
    :param float sigma: width of the line in nm.
    :param Spectrum spectrum: the current spectrum to which the gaussian line is added.
    :return:
    """

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
