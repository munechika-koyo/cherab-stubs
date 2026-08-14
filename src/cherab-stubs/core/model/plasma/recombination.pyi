from collections.abc import Mapping, Sequence

from raysect.core.math import Point3D, Vector3D
from raysect.optical import Spectrum

from ...atomic import AtomicData, Line
from ...plasma import Plasma
from ...plasma.model import PlasmaModel
from ..lineshape import LineShapeModel

class RecombinationLine(PlasmaModel):
    r"""
    Emitter that calculates spectral line emission from a plasma object
    as a result of dielectronic recombination of the target species.

    .. math::
        \epsilon_{\mathrm{recomb}}(\lambda) = \frac{1}{4 \pi} n_{Z_\mathrm{i} + 1} n_\mathrm{e}
        \mathrm{PEC}_{\mathrm{recomb}}(n_\mathrm{e}, T_\mathrm{e}) f(\lambda),

    where :math:`n_{Z_\mathrm{i} + 1}` is the recombining species density,
    :math:`\mathrm{PEC}_{\mathrm{recomb}}` is the dielectronic recombination photon emission coefficient
    for the specified spectral line of the :math:`Z_\mathrm{i}` ion,
    :math:`f(\lambda)` is the normalised spectral line shape,

    :param Line line: Spectroscopic emission line object.
    :param Plasma plasma: The plasma to which this emission model is attached. Default is None.
    :param AtomicData atomic_data: The atomic data provider for this model. Default is None.
    :param object lineshape: Line shape model class. Default is None (GaussianLine).
    :param object lineshape_args: A list of line shape model arguments. Default is None.
    :param object lineshape_kwargs: A dictionary of line shape model keyword arguments. Default is None.

    :ivar Plasma plasma: The plasma to which this emission model is attached.
    :ivar AtomicData atomic_data: The atomic data provider for this model.
    """

    def __init__(
        self,
        line: Line,
        plasma: Plasma | None = None,
        atomic_data: AtomicData | None = None,
        lineshape: type[LineShapeModel] | None = None,
        lineshape_args: Sequence[object] | None = None,
        lineshape_kwargs: Mapping[str, object] | None = None,
    ) -> None: ...
    def emission(self, point: Point3D, direction: Vector3D, spectrum: Spectrum) -> Spectrum: ...
    def _change(self) -> None: ...
