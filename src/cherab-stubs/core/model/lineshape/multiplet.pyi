from numpy.typing import ArrayLike
from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...plasma import Plasma
from ...species import Species
from .base import LineShapeModel

class MultipletLineShape(LineShapeModel):
    """
    Produces Multiplet line shapes.

    The lineshape radiance is calculated from a base PEC rate that is unresolved. This
    radiance is then divided over a number of components as specified in the multiplet
    argument. The multiplet components are specified with an Nx2 array where N is the
    number of components in the multiplet. The first axis of the array contains the
    wavelengths of each component, the second contains the line ratio for each component.
    The component line ratios must sum to one. For example:

    :param Line line: The emission line object for the base rate radiance calculation.
    :param float wavelength: The rest wavelength of the base emission line.
    :param Species target_species: The target plasma species that is emitting.
    :param Plasma plasma: The emitting plasma object.
    :param AtomicData atomic_data: The atomic data provider.
    :param multiplet: An Nx2 array that specifies the multiplet wavelengths and line ratios.

    .. code-block:: pycon

       >>> from cherab.core.atomic import Line, nitrogen
       >>> from cherab.core.model import ExcitationLine, MultipletLineShape
       >>>
       >>> # multiplet specification in Nx2 array
       >>> multiplet = [[403.509, 404.132, 404.354, 404.479, 405.692], [0.205, 0.562, 0.175, 0.029, 0.029]]
       >>>
       >>> # Adding the multiplet to the plasma model.
       >>> nitrogen_II_404 = Line(nitrogen, 1, ("2s2 2p1 4f1 3G13.0", "2s2 2p1 3d1 3F10.0"))
       >>> excit = ExcitationLine(nitrogen_II_404, lineshape=MultipletLineShape, lineshape_args=[multiplet])
       >>> plasma.models.add(excit)
    """

    def __init__(
        self,
        line: Line,
        wavelength: float,
        target_species: Species,
        plasma: Plasma,
        atomic_data: AtomicData,
        multiplet: ArrayLike,
    ) -> None: ...
    def add_line(self, radiance: float, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
